import os
import json

# Копируем логику модуля обработки прямо сюда
def process_matrix():
    with open("data_input.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    n = data["n"]
    m = data["m"]
    matrix = data["matrix"]
    
    result = []
    for j in range(m):
        column = []
        for i in range(n):
            column.append(matrix[i][j])
        result.append(column)
    
    output_data = {"n": n, "m": m, "result_matrix": result}
    with open("data_output.json", "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    return output_data

def test_process_matrix():
    # Создаем тестовый файл
    input_data = {"n": 2, "m": 2, "matrix": [[1.0, 2.0], [3.0, 4.0]]}
    with open('data_input.json', 'w', encoding='utf-8') as f:
        json.dump(input_data, f)
    
    # Запускаем функцию
    result = process_matrix()
    
    # Проверяем результат
    assert result['result_matrix'] == [[1.0, 3.0], [2.0, 4.0]]
    assert os.path.exists('data_output.json')