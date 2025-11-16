# tasks/task2.py

def solve():
# Ниже пишите решение задачи

# Читаем входные данные в одной строке
    X, Y, Z = map(int, input().split())

# Известные цены
    price_pencil = 3  # цена карандаша
    price_pen = price_pencil + 2  # цена ручки (на 2 рубля больше карандаша)
    price_marker = price_pen + 7  # цена фломастера (на 7 рублей больше ручки)

# Вычисляем общую стоимость
    total_cost = (X * price_pencil) + (Y * price_pen) + (Z * price_marker)

    print(total_cost)
   

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()