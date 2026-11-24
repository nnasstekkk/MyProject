# app/app.py
import streamlit as st
import pandas as pd
import json
from database import get_session, Matrix, Result
from logic import process_matrix

# Настройка страницы
st.set_page_config(page_title="Обработка матриц", layout="centered")
st.title("Система обработки матриц")
st.write("Введите матрицу построчно, а система выведет её по столбцам и сохранит в БД.")

# --- Боковая панель (Интеллектуальный интерфейс) ---
st.sidebar.header("Размерность матрицы")
rows = st.sidebar.number_input("Строки:", min_value=1, max_value=10, value=2)
cols = st.sidebar.number_input("Столбцы:", min_value=1, max_value=10, value=3)

# Инициализация состояния для хранения данных ввода
if 'matrix_input' not in st.session_state or st.session_state.matrix_input.shape != (rows, cols):
    st.session_state.matrix_input = pd.DataFrame(0.0, index=range(rows), columns=range(cols))

st.subheader("Ввод данных")
# Используем data_editor для красивого ввода матрицы
edited_df = st.data_editor(st.session_state.matrix_input, use_container_width=True)

if st.button("Обработать и сохранить в БД", type="primary"):
    matrix_list = edited_df.values.tolist()
    result_list = process_matrix(matrix_list)
    
    session = get_session()
    try:
        # 1. Сохраняем исходную матрицу
        new_matrix = Matrix(rows=rows, cols=cols, data=json.dumps(matrix_list))
        session.add(new_matrix)
        session.commit() # Сохраняем, чтобы получить ID
        
        # 2. Сохраняем результат
        new_result = Result(matrix_id=new_matrix.id, result_data=json.dumps(result_list))
        session.add(new_result)
        session.commit()
        
        st.success("Успешно сохранено в БД!")
        st.write("**Результат (по столбцам):**")
        st.write(result_list)
    except Exception as e:
        session.rollback()
        st.error(f"Ошибка БД: {e}")
    finally:
        session.close()

st.divider()
st.subheader("История из БД")

# --- ИСПРАВЛЕННЫЙ БЛОК ЧТЕНИЯ ИСТОРИИ ---
session = get_session()
matrices_data = []

# Вытаскиваем все данные из БД в обычные словари Python, пока сессия открыта
for m in session.query(Matrix).order_by(Matrix.id.desc()).all():
    matrices_data.append({
        "id": m.id,
        "rows": m.rows,
        "cols": m.cols,
        "created_at": m.created_at,
        "data": json.loads(m.data),
        # Проверка на случай, если результата вдруг нет
        "result_data": json.loads(m.result.result_data) if m.result else "Нет данных" 
    })

session.close() # Закрываем сессию только после того, как всё сохранили в список

if not matrices_data:
    st.info("БД пуста.")
else:
    for m in matrices_data:
        # Выводим данные из нашего словаря, а не из базы
        with st.expander(f"ID: {m['id']} | Размер: {m['rows']}x{m['cols']} | Дата: {m['created_at'].strftime('%Y-%m-%d %H:%M')}"):
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Исходная матрица:**")
                st.write(m['data'])
            with col2:
                st.write("**Результат по столбцам:**")
                st.write(m['result_data'])