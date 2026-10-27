import sys
import os

# Эта строчка добавляет папку src в пути поиска Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
import json
from modules.process_module import process_matrix

def test_process_matrix():
    input_data = {"n": 2, "m": 2, "matrix": [[1.0, 2.0], [3.0, 4.0]]}
    with open('data_input.json', 'w', encoding='utf-8') as f:
        json.dump(input_data, f)
    
    result = process_matrix()
    
    assert result['result_matrix'] == [[1.0, 3.0], [2.0, 4.0]]
    assert os.path.exists('data_output.json')