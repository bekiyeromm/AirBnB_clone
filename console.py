#!/usr/bin/python3
"""
Module console
Defines class HBNBCommand
command line interface
"""


from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    public class attribute:
        class_dic: class dictionary
    methods:
        do_quit(self)
        do_EOF(self, line)
        emptyline(self)
        do_create(self, line)
    """
    class_dic = {"BaseModel": BaseModel, "User": User, "State": State,
                 "City": City, "Amenity": Amenity,
                 "Place": Place, "Review": Review}
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        quit()

    def do_EOF(self, line):
        """Exit the console => ctr+D"""
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """
        create a new instance
        Usage create classname
        """
        try:
            classname = line
            if classname == '':
                raise KeyError("** class name missing **")
            elif classname not in self.class_dic.keys():
                raise NameError("** class doesn't exist **")
            inst = self.class_dic[classname]()
            inst.save()
            print(inst.id)

        except NameError as e:
            print(e)
        except KeyError as e:
            print(e)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        Usage show classname classid
        """
        try:
            if len(line) == 0:
                raise Exception("** class name missing **")
            if " " not in line:
                if line in self.class_dic.keys():
                    raise Exception("** instance id missing **")
                else:
                    raise Exception("** class doesn't exist **")
            cls_name, cls_id = line.split(" ")
            key = "{}.{}".format(cls_name, cls_id)
            if key not in storage.all().keys():
                raise Exception("** no instance found **")
            print(storage.all()[key])
        except Exception as e:
            print(e)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        Usage destroy classname classid
        """
        try:
            if len(line) == 0:
                raise Exception("** class name missing **")
            if " " not in line:
                if line in self.class_dic.keys():
                    raise Exception("** instance id missing **")
                else:
                    raise Exception("** class doesn't exist **")
            cls_name, cls_id = line.split(" ")
            key = "{}.{}".format(cls_name, cls_id)
            if key not in storage.all().keys():
                raise Exception("** no instance found **")
            del storage.all()[key]
        except Exception as e:
            print(e)

    def do_all(self, line):
        """
        create a new instance
        Usage all or all class name
        """
        try:
            classname = line
            all_objs = storage.all()
            list_t = []
            spec_list = []
            for obj_id in all_objs.keys():
                list_t.append(str(all_objs[obj_id]))
            if len(line) > 0:
                if classname not in self.class_dic.keys():
                    raise Exception("** class doesn't exist **")
                else:
                    for i in list_t:
                        if line in i:
                            spec_list.append(i)
                    print(spec_list)
            else:
                print(list_t)

        except Exception as e:
            print(e)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        Usage update <class name> <id> <attribute name> "<attribute value>"
        """
        try:
            if len(line) == 0:
                raise Exception("** class name missing **")
            if " " not in line:
                if line in self.class_dic.keys():
                    raise Exception("** instance id missing **")
                else:
                    raise Exception("** class doesn't exist **")
            list_t = line.split(" ")
            key = "{}.{}".format(list_t[0], list_t[1])
            if key not in storage.all().keys():
                raise Exception("** no instance found **")
            if len(list_t) == 2:
                raise Exception("** attribute name missing **")
            elif len(list_t) == 3:
                raise Exception("** value missing **")
            inst = storage.all()[key]
            list_t[3] = list_t[3].strip('"')
            if hasattr(inst, list_t[2]):
                if type(getattr(inst, list_t[2])) is int:
                    val = int(list_t[3])
                elif type(getattr(inst, list_t[2])) is float:
                    val = float(list_t[3])
                else:
                    val = list_t[3]
            else:
                val = list_t[3]
            setattr(inst, list_t[2], val)
            inst.save()

        except Exception as e:
            print(e)

    def do_count(self, line):
        """Display count of instances specified"""
        if line in self.class_dic:
            count = 0
            for key, objs in storage.all().items():
                if line in key:
                    count += 1
            print(count)
        else:
            print("**class doesn't exist**")

    def default(self, line):
        """Accepts class name followed by arguement"""
        args = line.split('.')
        class_name = args[0]
        if len(args) == 1:
            print("*** Unknown syntax: {}".format(line))
            return
        try:
            args = args[1].split('(')
            command = args[0]
            if command == 'all':
                HBNBCommand.do_all(self, class_name)
            elif command == 'count':
                HBNBCommand.do_count(self, class_name)
            elif command == 'show':
                args = args[1].split(')')
                id_ = args[0]
                id_ = id_.strip("'")
                id_ = id_.strip('"')
                arg = class_name + ' ' + id_
                HBNBCommand.do_show(self, arg)
            elif command == 'destroy':
                args = args[1].split(')')
                id_ = args[0]
                id_ = id_.strip("'")
                id_ = id_.strip('"')
                arg = class_name + ' ' + id_
                HBNBCommand.do_destroy(self, arg)
            elif command == 'update':
                args = args[1].split(',')
                id_ = args[0]
                id_ = id_.strip("'")
                id_ = id_.strip('"')
                name_arg = args[1].strip(',')
                val_arg = args[2]
                name_arg = name_arg.strip(' ')
                name_arg = name_arg.strip("'")
                name_arg = name_arg.strip('"')
                val_arg = val_arg.strip(' ')
                val_arg = val_arg.strip(')')
                arg = class_name + ' ' + id_ + ' ' + name_arg + ' ' + val_arg
                HBNBCommand.do_update(self, arg)
            else:
                print("*** Unknown syntax: {}".format(line))
        except IndexError:
            print("*** Unknown syntax: {}".format(line))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
