import json

def output_matrix():
    """Модуль вывода: читает результат и выводит его на экран."""
    with open("data_output.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    print("\n=== РЕЗУЛЬТАТ (вывод по столбцам) ===")
    for column in data["result_matrix"]:
        for value in column:
            print(value, end=" ")
        print()
    print("=" * 35)