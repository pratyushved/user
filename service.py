from sqlalchemy.orm import Session

from Project.sql_app.user import models, schemas
from Project.sql_app.user.crud import create_user, get_user


def get_user_service(db: Session):
    return get_user(db)


def create_user_service(db: Session, user: str):
    org = models.User(name = user)
    return create_user(db, org)
