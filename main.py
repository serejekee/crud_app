from db import init_db
from todo import add_task, list_tasks, mark_done, delete_task

init_db()

add_task("Купить молоко")
add_task("Сделать домашку")

print("Список задач:")
for task in list_tasks():
    print(task)

mark_done(1)
delete_task(2)

print("\nПосле обновлений:")
for task in list_tasks():
    print(task)
