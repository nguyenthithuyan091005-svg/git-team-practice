tasks = []

def show_tasks():
    print("Danh sach cong viec:")
    for task in tasks:
        print(task)

def add_task(task):
    tasks.append(task)
    print("Da them cong viec:", task)

add_task("Hoc Git")
show_tasks()