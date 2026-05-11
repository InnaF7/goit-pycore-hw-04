def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')

                total += int(salary)
                count += 1

        average = total / count if count > 0 else 0

        return (total, average)
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях до файлу")
        return None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None
    
path_to_file = "/Users/innafinchenko/Desktop/web/goit-pycore-hw-04/goit-pycore-hw-04/salary_file.txt"
result = total_salary(path_to_file)

if result:
    total, average = result
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")