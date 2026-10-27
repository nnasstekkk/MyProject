import sys
import os

# Эта строчка добавляет папку src в пути поиска Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
import json
from modules.input_module import input_matrix

def test_input_matrix(monkeypatch):
    # Имитируем ввод пользователя: 2 строки, 2 столбца, числа 1, 2, 3, 4
    inputs = iter(['2', '2', '1', '2', '3', '4'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    data = input_matrix()
    
    assert data['n'] == 2
    assert data['m'] == 2
    assert data['matrix'] == [[1.0, 2.0], [3.0, 4.0]]
    assert os.path.exists('data_input.json')