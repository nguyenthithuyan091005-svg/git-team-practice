tasks = ["Hoc Git", "Hoc Python"]

def show_tasks():
    print("Danh sach cong viec:")
    for task in tasks:
        print(task)

def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Da xoa cong viec:", task)
    else:
        print("Khong tim thay cong viec")

delete_task("Hoc Git")
show_tasks()