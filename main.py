import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from Project.sql_app.user import crud, models, schemas
from Project.sql_app.user.database import  SessionLocal, engine, get_db
from Project.sql_app.user.schemas import ItemCreate
from Project.sql_app.user.service import create_user_service, get_user_service

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# Dependency


@app.post("/user/")
def create_user(comp : ItemCreate, db: Session = Depends(get_db)):
    return create_user_service(db, comp.name)


@app.get("/users/")
def read_user(db: Session = Depends(get_db)):
    return get_user_service(db)


if __name__ == '__main__':
    uvicorn.run(app)
