from typing import Optional

from fastapi import FastAPI

from db import connect

app = FastAPI()

conn = connect()
curs = conn.cursor()

@app.get('/')
def read_root():
    return {'hello': 'world'}

@app.post('/numbers/')
def create_number(num_id: int, num_val: str):
    q = f"INSERT INTO numbers VALUES ({num_id}, '{num_val}')"
    curs.execute(q)
    conn.commit()
    return 'record created' 

@app.get('/numbers/')
def read_numbers():
    q = "SELECT * FROM numbers"
    curs.execute(q)
    res = curs.fetchall()
    return res

@app.get('/numbers/{num_id}')
def read_number(num_id: int):
    q = f"SELECT * FROM numbers WHERE id = {num_id}"
    curs.execute(q)
    res = curs.fetchone()
    return res

@app.put('/numbers/{num_id}')
def update_number_value(num_id: int, num_val: str):
    q = f"UPDATE numbers SET value = '{num_val}' WHERE id = {num_id}"
    curs.execute(q)
    conn.commit()
    return 'record updated'

@app.delete('/numbers/{num_id}')
def delete_number(num_id: int):
    q = f"DELETE FROM numbers WHERE id = {num_id}"
    curs.execute(q)
    conn.commit()
    return 'record deleted'

