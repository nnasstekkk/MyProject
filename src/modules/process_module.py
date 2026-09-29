import json

def process_matrix():
    """Модуль обработки: выводит матрицу по столбцам."""
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
    
    print("[process_module] Результат сохранён в data_output.json")
    return output_data