import sqlite3
import argparse
import redis
import json

def parse_args():
    desc = 'Todo manager for storing and removing tasks'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-a", "--add", "-add", help="To add a new item to the list",
                        type=str, nargs="+")
    parser.add_argument("-r", "-remove", "--remove", help="To remove an item from the list",
                        type=int)
    parser.add_argument("-l", "-list", "--list", help="displays the tasks or task in the list",
                        nargs="*")
    args = parser.parse_args()
    return args


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_todo_list():
    database_connection.row_factory = dict_factory
    cursor = database_connection.cursor()
    cursor.execute("select * FROM todo_list")
    # The 2 lines below joins the string together and returns in the format "1 Do the chores on Sunday"
    for item in cursor.fetchall():
        print(" ".join(str(x) for x in item.values()))


def add_to_todo_list(task):
    task = " ".join(task)
    cursor = database_connection.cursor()
    cursor.execute("INSERT INTO todo_list VALUES (?, ?)", (None, task))
    database_connection.commit()


def redis_add():
    database_connection.row_factory = dict_factory
    cursor = database_connection.cursor()
    cursor.execute("select * FROM todo_list")
    for idx, item in enumerate(cursor.fetchall()):
        rval = json.dumps(item)id
        redis_connection.set(idx, rval)


def remove_from_todo_list(rowid):
    cursor = database_connection.cursor()
    cursor.execute("DELETE FROM todo_list WHERE rowid = ?", (rowid,))
    database_connection.commit()


if __name__ == '__main__':
    commands = parse_args()
    redis_connection = redis.StrictRedis(host='localhost',
                                         port=6379,
                                         db=0)
    # Creating table for database using sqlite
    database_connection = sqlite3.connect('todo_list.db')
    cursor = database_connection.cursor()
    cursor.execute('''CREATE TABLE if not exists todo_list(
                  id INTEGER PRIMARY KEY,
                  description TEXT);''')
    database_connection.commit()

    if commands.add:
        add_to_todo_list(commands.add)
        redis_add()
    elif commands.remove:
        remove_from_todo_list(commands.remove)
    elif commands.list is not None:
        get_todo_list()