import argparse

from . import databasehandler
from . import display


class TodoList:
    def __init__(self):

        self.parser = argparse.ArgumentParser(description='')

        self.databasehandler = databasehandler.databasehandler()

        self.display = display.Display()

        self.parser.add_argument('-add', help="To add a new item", type=str, nargs="+")

        self.parser.add_argument('-remove', help="Remove item", type=int)
        self.parser.add_argument('-done', help="Mark item as done", type=int)
        self.parser.add_argument('-undone', help="Mark item as not done", type=int)  # Revert done
        # should be 0 or 1 arg here
        self.parser.add_argument('-view', help="View list or view item", type=int, nargs='*')

        self.parser.add_argument('-description', help="Add description to item", nargs="*")
        self.parser.add_argument('-due', help="Add due date to item", nargs="*")

        self.parser.add_argument('-welcome', help="Display welcome message", action="store_true")

        self.parser.add_argument('-vacuum', help="Vacuum database ids", action="store_true")
        self.parser.add_argument('-debug', help="Dump database to screen", action="store_true")

        args = self.parser.parse_args()
        if self.check_arguments(args):
            self.handle_arguments(args)
        else:
            self.display_list()

        self.databasehandler.close_connection()
        return

    @staticmethod
    def check_arguments(self, args):
        any_arg_set = False
        for arg in vars(args):
            if getattr(args, arg):
                any_arg_set = True
                break
        return any_arg_set

    def handle_arguments(self, args):
        display_list = False
        if args.add:
            self.databasehandler.add_to_todo_list(args.add, args.due, args.description)
            display_list = True
        elif args.description:
            # Split the args into the id and description
            self.databasehandler.add_description(args.description[0], args.description[1::])
        elif args.due:
            self.databasehandler.add_due_date(args.due[0], args.due[1])

        if args.remove:
            self.databasehandler.remove_by_id(args.remove)
            display_list = True

        if args.done:
            self.databasehandler.mark_as_done(args.done)
            display_list = True
        if args.undone:
            self.databasehandler.mark_as_undone(args.undone)
            display_list = True

        if args.debug:
            self.databasehandler.dump_database()
        if args.vacuum:
            self.databasehandler.vacuum_id()
            display_list = True

        if args.welcome:
            self.display.display_welcome()

        if args.view:
            self.display_details(args.view[0])
        if display_list:
            self.display_list()

    def display_details(self, item_id):
        self.display.display_details(self.databasehandler.get_item_description(item_id))

    def display_list(self):
        todo_list = self.databasehandler.get_todo_list()
        self.display.show_list(todo_list)


def run_todo():
    TodoList()