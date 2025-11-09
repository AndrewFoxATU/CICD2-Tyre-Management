# backend/tyres_service/main.py
from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from schemas import Tyre, TyreCreate
from models import TyreModel

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tyres Service API")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get all tyres
@app.get("/api/tyres")
def get_tyres(db: Session = Depends(get_db)):
    return db.query(TyreModel).all()

# Get a single tyre by ID
@app.get("/api/tyres/{tyre_id}")
def get_tyre(tyre_id: int, db: Session = Depends(get_db)):
    tyre = db.query(TyreModel).filter(TyreModel.id == tyre_id).first()
    if not tyre:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tyre not found")
    return tyre

# Add a new tyre
@app.post("/api/tyres", status_code=status.HTTP_201_CREATED)
def add_tyre(tyre: TyreCreate, db: Session = Depends(get_db)):
    new_tyre = TyreModel(**tyre.dict())
    db.add(new_tyre)
    db.commit()
    db.refresh(new_tyre)
    return new_tyre

# Update a tyre
@app.put("/api/tyres/{tyre_id}")
def update_tyre(tyre_id: int, updated_tyre: TyreCreate, db: Session = Depends(get_db)):
    tyre = db.query(TyreModel).filter(TyreModel.id == tyre_id).first()
    if not tyre:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tyre not found")

    for key, value in updated_tyre.dict().items():
        setattr(tyre, key, value)

    db.commit()
    db.refresh(tyre)
    return tyre

# Delete a tyre
@app.delete("/api/tyres/{tyre_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tyre(tyre_id: int, db: Session = Depends(get_db)):
    tyre = db.query(TyreModel).filter(TyreModel.id == tyre_id).first()
    if not tyre:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tyre not found")

    db.delete(tyre)
    db.commit()
    return

@app.get("/health")
def health_check():
    return {"status": "ok"}
