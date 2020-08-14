from sqlalchemy.orm import Session
from . import models, schemas


def get_smartphone(db: Session, smartphone_id: int):
    return db.query(models.Smartphone).filter(
        models.Smartphone.id == smartphone_id).first()


def get_smartphones(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Smartphone).offset(skip).limit(limit).all()


def create_smartphone(db: Session,
                      smartphone: schemas.SmartphoneCreate,
                      smartphone_id: int):
    db_smartphone = models.Smartphone(**smartphone.dict(),
                                      id=smartphone_id)
    db.add(db_smartphone)
    db.commit()
    db.refresh(db_smartphone)
    return db_smartphone


def update_smartphone(db: Session,
                      smartphone: schemas.SmartphoneCreate,
                      smartphone_id: int):
    db_smartphone = models.Smartphone(id=smartphone_id, **smartphone.dict())
    upd_smartphone = smartphone.dict()
    upd_smartphone['id'] = smartphone_id
    db.query(models.Smartphone).filter(
        models.Smartphone.id == smartphone_id).update(upd_smartphone)
    db.commit()
    return db_smartphone
