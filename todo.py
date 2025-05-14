from db import get_connection

def add_task(title):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (title) VALUES (%s);", (title,))
    conn.commit()
    cur.close()
    conn.close()

def list_tasks():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, done FROM tasks;")
    tasks = cur.fetchall()
    cur.close()
    conn.close()
    return tasks

def mark_done(task_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET done = TRUE WHERE id = %s;", (task_id,))
    conn.commit()
    cur.close()
    conn.close()

def delete_task(task_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id = %s;", (task_id,))
    conn.commit()
    cur.close()
    conn.close()
