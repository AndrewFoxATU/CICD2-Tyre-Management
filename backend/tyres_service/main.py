# backend/tyres_service/main.py
from fastapi import FastAPI, HTTPException, status
from schemas import Tyre

app = FastAPI(title="Tyres Service API")

tyres: list[Tyre] = []

#Get all tyres
@app.get("/api/tyres")
def get_tyres():

    return tyres

#Get a single tyre by ID
@app.get("/api/tyres/{tyre_id}")
def get_tyre(tyre_id: int):
    for t in tyres:
        if t.id == tyre_id:
            return t
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tyre not found")

#Add a new tyre
@app.post("/api/tyres", status_code=status.HTTP_201_CREATED)
def add_tyre(tyre: Tyre):
    if any(t.id == tyre.id for t in tyres):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Tyre ID already exists")
    tyres.append(tyre)
    return tyre


#Update a tyre
@app.put("/api/tyres/{tyre_id}")
def update_tyre(tyre_id: int, updated_tyre: Tyre):
    for index, t in enumerate(tyres):
        if t.id == tyre_id:
            tyres[index] = updated_tyre
            return updated_tyre
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tyre not found")

#Delete a tyre
@app.delete("/api/tyres/{tyre_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tyre(tyre_id: int):
    for index, t in enumerate(tyres):
        if t.id == tyre_id:
            tyres.pop(index)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tyre not found")


@app.get("/health")
def health_check():
    return {"status": "ok"}
