from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/smartphones/", response_model=schemas.Smartphone)
def create_smartphone(smartphone_id: int,
                      smartphone: schemas.SmartphoneCreate,
                      db: Session = Depends(get_db)):
    return crud.create_smartphone(
        db=db, smartphone=smartphone, smartphone_id=smartphone_id)


@app.get("/smartphones/", response_model=List[schemas.Smartphone])
def read_smartphones(skip: int = 0,
                     limit: int = 100,
                     db: Session = Depends(get_db)):
    smartphones = crud.get_smartphones(db, skip=skip, limit=limit)
    return smartphones


@app.get("/smartphones/{smartphone_id}", response_model=schemas.Smartphone)
def read_smartphone(smartphone_id: int, db: Session = Depends(get_db)):
    db_smartphone = crud.get_smartphone(db, smartphone_id=smartphone_id)
    if db_smartphone is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_smartphone


@app.put("/smartphones/{smartphone_id}", response_model=schemas.Smartphone)
def update_smartphone(smartphone_id: int,
                      smartphone: schemas.SmartphoneCreate,
                      db: Session = Depends(get_db)):
    return crud.update_smartphone(
        db=db, smartphone=smartphone, smartphone_id=smartphone_id)
