from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session):
    return db.query(models.User).all()


def create_user(db: Session, user: schemas.ItemBase):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
