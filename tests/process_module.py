import json

def process_matrix():
    """Модуль обработки: выводит матрицу по столбцам."""
    try:
        # Читаем данные из JSON-файла
        with open("data_input.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        n = data["n"]
        m = data["m"]
        matrix = data["matrix"]
        
        # Обработка: выводим по столбцам
        result = []
        for j in range(m):
            column = []
            for i in range(n):
                column.append(matrix[i][j])
            result.append(column)
        
        # Сохраняем результат в JSON
        output_data = {"n": n, "m": m, "result_matrix": result}
        with open("data_output.json", "w", encoding="utf-8") as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)
        
        print("[process_module] Результат сохранён в data_output.json")
        return output_data

    except FileNotFoundError:
        print("[ОШИБКА] Файл data_input.json не найден. Сначала запустите модуль ввода.")
    except KeyError as e:
        print(f"[ОШИБКА] В JSON-файле отсутствует ключ: {e}")
    except Exception as e:
        print(f"[ОШИБКА] Непредвиденная ошибка: {e}")