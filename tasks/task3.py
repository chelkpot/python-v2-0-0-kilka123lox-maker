# tasks/task3.py

def solve():
# Ниже пишите решение задачи
    a, b = map(int, input().split())
# Общее количество банок = (a + b - 1)
# Потому что последняя банка была прострелена обоими
    total = a + b - 1
# Не прострелянные банки для каждого:
# Для Гарри: total - a
# Для Ларри: total - b
    garry_remaining = total - a
    larry_remaining = total - b

    print(garry_remaining, larry_remaining)

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()