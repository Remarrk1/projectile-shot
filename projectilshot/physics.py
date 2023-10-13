import math

# Глобальные переменные, представляющие значения свободного падения и начальные координаты.
g = 9.81
x0, y0 = 10, 10
V = 0
angle = 0
time_step = 0.1

def calculate_velocity(V0, angle_deg):
    """
    Рассчитывает горизонтальную и вертикальную составляющие скорости Vx и Vy.

    Args:
        V0 (float): Начальная скорость.
        angle_deg (float): Угол в градусах.

    Returns:
        float: Горизонтальная составляющая скорости (Vx).
        float: Вертикальная составляющая скорости (Vy).
    """
    global V
    V = V0
    angle = math.radians(angle_deg)  # Переводим угол из градусов в радианы.
    Vx = V * math.cos(angle)
    Vy = V * math.sin(angle)
    return Vx, Vy

def calculate_coordinates(Vx, Vy):
    """
    Рассчитывает новые координаты точки движения на плоскости.

    Args:
        Vx (float): Горизонтальная составляющая скорости.
        Vy (float): Вертикальная составляющая скорости.

    Returns:
        float: Новая горизонтальная координата (x0).
        float: Новая вертикальная координата (y0).
    """
    global x0, y0
    x0 += Vx * time_step
    y0 += Vy * time_step - 0.5 * g * time_step**2
    return x0, y0
