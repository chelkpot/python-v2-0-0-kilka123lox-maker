# tasks/task3.py

def solve():
# Ниже пишите решение задачи
 n = int(input())
 print(n // 100 + n % 100 // 20 + n % 20 // 10 + n % 10 // 5 + n % 5)


# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()