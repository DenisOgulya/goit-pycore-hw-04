from pathlib import Path

path_way = path_way = Path(__file__).parent / "path.txt"


def total_salary(path_way):
    
    total = 0
    users_amount = 0
    
    try:
        with open (path_way, "r", encoding="utf-8") as file:
            users = file.readlines()
            for user in users:
                users_amount+=1
                _, salary = user.strip().split(',')
                total += int(salary)
        return (total,total/users_amount)
    except FileNotFoundError: 
        return 'Не вдалося знайти файл'

total, average = total_salary(path_way)

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
