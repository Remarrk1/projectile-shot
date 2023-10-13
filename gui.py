import tkinter as tk

def create_interface(root, shoot_callback):
    """
    Создает графический интерфейс для ввода параметров выстрела.

    Args:
        root (tk.Tk): Корневой объект приложения tkinter.
        shoot_callback (function): Функция обратного вызова для обработки выстрела.

    Returns:
        tk.Canvas: Объект холста для рисования.
        tk.Entry: Поле для ввода скорости снаряда.
        tk.Entry: Поле для ввода угла выстрела.
    """
    root.title("Движение снаряда")

    # Создаем холст для рисования
    canvas = tk.Canvas(root, width=800, height=400)
    canvas.pack(side=tk.RIGHT)

    # Рисуем координатные оси
    canvas.create_line(10, 390, 790, 390, arrow=tk.LAST)
    canvas.create_line(10, 390, 10, 10, arrow=tk.LAST)

    # Создаем поля для ввода скорости и угла выстрела
    entry_speed = tk.Entry(root, width=10)
    entry_angle = tk.Entry(root, width=10)

    # Создаем кнопку для выполнения выстрела
    button_shoot = tk.Button(root, text="Выстрел", command=shoot_callback)

    # Создаем метки для полей ввода
    label_speed = tk.Label(root, text="Скорость (м/с):")
    label_angle = tk.Label(root, text="Угол (градусы):")

    # Упаковываем виджеты в интерфейс
    label_speed.pack()
    entry_speed.pack()
    label_angle.pack()
    entry_angle.pack()
    button_shoot.pack()

    return canvas, entry_speed, entry_angle
