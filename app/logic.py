# app/logic.py
def process_matrix(matrix_data):
    """
    Принимает двумерный список (строки).
    Возвращает двумерный список, транспонированный (по столбцам).
    """
    if not matrix_data or not matrix_data[0]:
        return []
    
    rows = len(matrix_data)
    cols = len(matrix_data[0])
    
    result = []
    for j in range(cols):
        col_data = [matrix_data[i][j] for i in range(rows)]
        result.append(col_data)
        
    return result