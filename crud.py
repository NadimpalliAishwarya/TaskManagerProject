from db import get_connection

def add_task():
    name = input("Task name: ")
    description = input("Description: ")
    deadline = input("Deadline (YYYY-MM-DD): ")
    priority = input("Priority (High/Medium/Low): ")
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (name, description, deadline, priority)
        VALUES (?, ?, ?, ?)
    ''', (name, description, deadline, priority))
    conn.commit()
    conn.close()
    print(" Task added successfully.\n")

def view_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    rows = cursor.fetchall()
    conn.close()

    print("\n All Tasks:")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Deadline: {row[3]}, Priority: {row[4]}, Status: {row[5]}")
    print()

def update_task():
    task_id = input("Enter Task ID to update: ")
    new_status = input("Enter new status (Pending/Completed): ")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE tasks SET status = ? WHERE id = ?
    ''', (new_status, task_id))
    conn.commit()
    conn.close()
    print("Task updated successfully.\n")

def delete_task():
    task_id = input("Enter Task ID to delete: ")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    print("Task deleted successfully.\n")
