from modules.input_module import input_matrix
from modules.process_module import process_matrix
from modules.output_module import output_matrix

def main():
    print("=== ЗАПУСК ИНТЕГРИРОВАННОЙ СИСТЕМЫ ===")
    input_matrix()
    process_matrix()
    output_matrix()
    print("\n=== РАБОТА ЗАВЕРШЕНА ===")

if __name__ == "__main__":
    main()