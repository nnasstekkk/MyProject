import json

def input_matrix():
    """Модуль ввода: считывает матрицу от пользователя."""
    n = int(input("Введите количество строк(n): "))
    m = int(input("Введите количество столбцов(m): "))
    
    matrix = []
    print("Введите элементы матрицы построчно:")
    for i in range(n):
        row = []
        for j in range(m):
            value = float(input(f"Введите элемент [{i+1}][{j+1}]: "))
            row.append(value)
        matrix.append(row)
    
    data = {"n": n, "m": m, "matrix": matrix}
    with open("data_input.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("[input_module] Данные сохранены в data_input.json")
    return data