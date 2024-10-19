import tkinter as tk
from tkinter import ttk

# Функция для добавления задачи
def add_task():
    task = task_entry.get()  # Получаем текст из поля ввода
    priority = priority_combobox.get()  # Получаем выбранный приоритет
    if task:
        task_with_priority = f"{task} [{priority}]"  # Формируем строку задачи с приоритетом
        task_listBox.insert(tk.END, task_with_priority)  # Вставляем в конец списка
        task_entry.delete(0, tk.END)  # Очищаем поле ввода

# Функция для удаления задачи
def delete_task():
    selected_task = task_listBox.curselection()  # Получаем индекс выбранной задачи
    if selected_task:
        task_listBox.delete(selected_task)  # Удаляем выбранную задачу

# Функция для отметки задачи как выполненной
def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.itemconfig(selected_task, bg="slate blue")  # Изменяем цвет фона выполненной задачи

# Создание окна
root = tk.Tk()
root.title("Task list")
root.configure(background="HotPink")

# Метка для ввода задачи
text1 = tk.Label(root, text="Введите вашу задачу:", bg="HotPink")
text1.pack(pady=5)

# Поле для ввода задачи
task_entry = tk.Entry(root, width=30, bg="DeepPink1")
task_entry.pack(pady=10)

# Метка для выбора приоритета
priority_label = tk.Label(root, text="Выберите приоритет:", bg="HotPink")
priority_label.pack(pady=5)

# Выпадающий список для выбора приоритета
priority_combobox = ttk.Combobox(root, values=["Высокий", "Средний", "Низкий"])
priority_combobox.current(1)  # Устанавливаем "Средний" как значение по умолчанию
priority_combobox.pack(pady=5)

# Кнопка для добавления задачи
add_task_button = tk.Button(root, text="Добавить задачу", command=add_task)
add_task_button.pack(pady=5)

# Кнопка для удаления задачи
delete_button = tk.Button(root, text="Удалить задачу", command=delete_task)
delete_button.pack(pady=5)

# Кнопка для отметки задачи как выполненной
mark_button = tk.Button(root, text="Отметить выполненную задачу", command=mark_task)
mark_button.pack(pady=5)

# Метка для списка задач
text2 = tk.Label(root, text="Список задач:", bg="HotPink")
text2.pack(pady=5)

# Список для задач
task_listBox = tk.Listbox(root, height=10, width=50, bg="LightPink1")
task_listBox.pack(pady=10)

# Запуск основного цикла
root.mainloop()