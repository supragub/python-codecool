# codecool-python / 006-Todo

This application in Python keeps your to-dos in one place. It should support the following features:

- listing tasks;

- adding a new task;

- marking a task as completed;

- archive (deleting all complete tasks).

Expected Console Output:

user@computer:~$ python todo.py

Please specify a command [list, add, mark, archive]: x

user@computer:~$ python todo.py

Please specify a command [list, add, mark, archive]: add

Add an item: Buy some milk

Item added.

user@computer:~$ python todo.py

Please specify a command [list, add, mark, archive]: list

You saved the following to-do items:

    1. [ ] Buy some milk

user@computer:~$ python todo.py

Please specify a command [list, add, mark, archive]: add

Add an item: Learn Python

Item added.

user@computer:~$ python todo.py

Please specify a command [list, add, mark, archive]: add

Add an item: Learn Git

Item added.

user@computer:~$ python todo.py

Please specify a command [list, add, mark, archive]: list

You saved the following to-do items:

    1. [ ] Buy some milk

    2. [ ] Learn Python

    3. [ ] Learn Git

user@computer:~$ python todo.py

Please specify a command [list, add, mark, archive]: mark

You saved the following to-do items:

    1. [ ] Buy some milk

    2. [ ] Learn Python

    3. [ ] Learn Git

Which one you want to mark as completed: 2

Learn Python is completed

user@computer:~$ python todo.py

Please specify a command [list, add, mark, archive]: list

You saved the following to-do items:

    1. [ ] Buy some milk

    2. [x] Learn Python

    3. [ ] Learn Git

user@computer:~$ python todo.py

Please specify a command [list, add, mark, archive]: archive

All completed tasks got deleted.

user@computer:~$ python todo.py

Please specify a command [list, add, mark, archive]: list

You saved the following to-do items:

    1. [ ] Buy some milk

    2. [ ] Learn Git