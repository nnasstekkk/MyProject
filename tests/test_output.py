import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
import json
from modules.output_module import output_matrix

def test_output_matrix(capsys):
    # Создаем файл с результатом
    output_data = {"n": 2, "m": 2, "result_matrix": [[1.0, 3.0], [2.0, 4.0]]}
    with open('data_output.json', 'w', encoding='utf-8') as f:
        json.dump(output_data, f)
    
    # Запускаем функцию вывода
    output_matrix()
    
    # Перехватываем то, что программа напечатала на экран
    captured = capsys.readouterr()
    
    # Проверяем, что нужные числа появились в выводе
    assert "1.0 3.0" in captured.out
    assert "2.0 4.0" in captured.out