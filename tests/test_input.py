import os
import json

# Мы просто копируем логику модуля ввода прямо сюда
def input_matrix():
    n = int(input("Введите количество строк(n): "))
    m = int(input("Введите количество столбцов(m): "))
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            value = float(input(f"Введите элемент [{i+1}][{j+1}]: "))
            row.append(value)
        matrix.append(row)
    data = {"n": n, "m": m, "matrix": matrix}
    with open("data_input.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return data

def test_input_matrix(monkeypatch):
    # Имитируем ввод пользователя: 2 строки, 2 столбца, числа 1, 2, 3, 4
    inputs = iter(['2', '2', '1', '2', '3', '4'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    # Запускаем функцию
    data = input_matrix()
    
    # Проверяем результат
    assert data['n'] == 2
    assert data['m'] == 2
    assert data['matrix'] == [[1.0, 2.0], [3.0, 4.0]]
    assert os.path.exists('data_input.json')