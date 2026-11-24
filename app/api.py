# app/api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import json
from database import get_session, Matrix, Result
from logic import process_matrix

app = FastAPI(title="Matrix API")

class MatrixInput(BaseModel):
    data: List[List[float]]

"/api/matrices/"
def create_matrix(payload: MatrixInput):
    session = get_session()
    matrix_list = payload.data
    result_list = process_matrix(matrix_list)
    
    try:
        new_matrix = Matrix(rows=len(matrix_list), cols=len(matrix_list[0]), data=json.dumps(matrix_list))
        session.add(new_matrix)
        session.commit()
        
        new_result = Result(matrix_id=new_matrix.id, result_data=json.dumps(result_list))
        session.add(new_result)
        session.commit()
        return {"id": new_matrix.id, "result": result_list, "status": "saved"}
    finally:
        session.close()

@app.get("/api/matrices/")
def get_all_matrices():
    session = get_session()
    matrices = session.query(Matrix).all()
    session.close()
    return [{"id": m.id, "rows": m.rows, "cols": m.cols, "data": json.loads(m.data)} for m in matrices]

@app.delete("/api/matrices/{matrix_id}")
def delete_matrix(matrix_id: int):
    session = get_session()
    matrix = session.query(Matrix).filter(Matrix.id == matrix_id).first()
    if not matrix:
        session.close()
        raise HTTPException(status_code=404, detail="Matrix not found")
    
    session.delete(matrix)
    session.commit()
    session.close()
    return {"message": "Deleted successfully"}