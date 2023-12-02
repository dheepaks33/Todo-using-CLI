import click

@click.group()
def mycommands():
    pass

@click.command
@click.option("--name",prompt = "Enter your name: ",help="The name of the User")
def hello(name):
    click.echo(f"Hello {name}")
PRIORITIES = {
    "o" : "Optional",
    "l":"Low",
    "m":"Medium",
    "h":"High",
    "c":"Crucial"
}


@click.command
@click.argument("priority",type=click.Choice(PRIORITIES.keys(), default="m"))
@click.argument("todofile", type=click.Path(exits=False), required=0)
@click.option("-n","--name", prompt="Enter the ToDo name", help="The name of the ToDo Item")
@click.option("-d","--desc", prompt="Describe the ToDo", help="The description of the ToDo Item")
def add_todo(name, description, prioritory, todifile):
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename,"a+") as f:
        f.write(f"{name}: {description} [Priority:{PRIORITIES[priority]}]")

@click.command
@click.argument("idx",type=int,required=1)
def delete_todo(idx):
    with open("mytodos.txt","r") as f:
        l = f.read().splitlines()
        l.pop(idx)
    with open("mytodos.txt","w") as f:
        f.write("\n".join(l))
        f.write("\n")


@click.command
@click.option("-p","--priority",type=click.Choice(PRIORITIES.keys()))
@click.argument("todofile",type=click.Path(exits=True), required=0)
def list_todos(priority, todofile):
    filename = todofile if todofile is not None else "mytodos.txt" 
    with open(filename,"r") as f:
        l = f.read().splitlines()
    if priority is None:
        for i,todo in enumerate(l):
            print(f"({i} - {todo})")
    else:
        for i,todo in enumerate(l):
            if f"[Priority: {PRIORITIES[priority]}]" in todo:
                print(f"({i} - {todo})")

mycommands.add_command(hello)
mycommands.add_command(add_todo)
mycommands.add_command(delete_todo)
mycommands.add_command(list_todos)

if __name__=="__main__":
    mycommands()

