def get_cats_info(path):
    cats_info = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
              for line in file:
                   cat_data = line.strip().split(',')
                   cat_dict = {
                        "id": cat_data[0],
                        "name": cat_data[1],
                        "age": cat_data[2]
                   }
                   cats_info.append(cat_dict)
        return cats_info

    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях до файлу")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []

path_to_file = "/Users/innafinchenko/Desktop/web/goit-pycore-hw-04/goit-pycore-hw-04/cats_file.txt"
cats_info = get_cats_info(path_to_file)

print(cats_info)
