# Todo-using-CLI

**Overview**

Todo-CLI is a simple command-line interface (CLI) application for managing your to-do list. With this tool, you can easily add, delete, and list your to-do items with different priority levels.


**Features**

**Hello Command:** 

A friendly command to greet the user by name.

todo hello --name <your_name>

**Add Todo Command:** 

Add a new to-do item with a specified name, description, and priority level.

todo add_todo -n "Task Name" -d "Task Description" -p <priority>

**Delete Todo Command:**

Remove a to-do item by its index.

todo delete_todo <index>

**List Todos Command:** 

Display the to-do list with an optional filter by priority.

todo list_todos -p <priority>

**Priorities**
Todo items can have the following priority levels:

o: Optional

l: Low

m: Medium

h: High

c: Crucial


**Clone the repository:**

git clone https://github.com/dheepaks33/todo-cli.git


**Run the application:**

python main.py <command>

Explore the different commands and options to efficiently manage your to-do list from the command line.

Feel free to contribute, report issues, or suggest enhancements. Happy organizing!

