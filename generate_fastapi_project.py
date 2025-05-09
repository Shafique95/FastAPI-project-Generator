import os

BASE_DIR = "my_fastapi_project"
import os
import argparse

structure = {
    "app": {
        "__init__.py": "",
        "main.py": '''from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# Include feature routers here
from app.modules.punch.router import router as punch_router
app.include_router(punch_router, prefix="/punch", tags=["Punch"])
''',
        "database.py": '''from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
''',
        "core": {
            "__init__.py": "",
            "config.py": '''from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Feature-First App"

    class Config:
        env_file = ".env"

settings = Settings()
'''
        },
        "shared": {
            "__init__.py": "",
            "dependencies.py": '''from app.database import SessionLocal
from fastapi import Depends

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
'''
        },
        "modules": {
            "__init__.py": "",
            "punch": {
                "__init__.py": "",
                "models.py": '''from sqlalchemy import Column, Integer, DateTime
from app.database import Base
from datetime import datetime

class Punch(Base):
    __tablename__ = "punches"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, index=True)
    punch_in_time = Column(DateTime, default=datetime.utcnow)
    punch_out_time = Column(DateTime, nullable=True)
''',
                "schemas.py": '''from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PunchBase(BaseModel):
    employee_id: int
    punch_in_time: datetime

class PunchCreate(PunchBase):
    punch_out_time: Optional[datetime] = None

class PunchOut(PunchCreate):
    punch_in_time: datetime

    class Config:
        orm_mode = True
''',
                "router.py": '''from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.shared.dependencies import get_db
from app.modules.punch import models, schemas
from app.modules.punch.models import Punch

router = APIRouter()

@router.post("/", response_model=schemas.PunchOut)
def punch_in_out(punch: schemas.PunchCreate, db: Session = Depends(get_db)):
    db_punch = models.Punch(employee_id=punch.employee_id, punch_in_time=punch.punch_in_time, punch_out_time=punch.punch_out_time)
    db.add(db_punch)
    db.commit()
    db.refresh(db_punch)
    return db_punch
'''
            },
            "user": {
                "__init__.py": "",
                "models": {
                    "__init__.py": "",
                    "user.py": "",
                    "address.py": "",
                    "profile.py": ""
                },
                "schemas": {
                    "__init__.py": "",
                    "user.py": "",
                    "address.py": ""
                },
                "crud": {
                    "__init__.py": "",
                    "user.py": ""
                },
                "services": {
                    "__init__.py": "",
                    "user_service.py": ""
                },
                "routes": {
                    "__init__.py": "",
                    "user_routes.py": ""
                },
                "utils": {
                    "__init__.py": "",
                    "helpers.py": ""
                },
                "auth": {
                    "__init__.py": "",
                    "auth.py": ""
                },
                "config": {
                    "__init__.py": "",
                    "settings.py": ""
                }
            }
        }
    }
}

def create_structure(base_path, struct):
    for name, content in struct.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, "w") as f:
                f.write(content)

def main():
    parser = argparse.ArgumentParser(description="Create a FastAPI project with feature-based structure.")
    parser.add_argument("project_name", help="Name of the FastAPI project directory to create")
    args = parser.parse_args()

    project_name = args.project_name

    if os.path.exists(project_name):
        print(f"❌ Directory '{project_name}' already exists.")
        return

    create_structure(".", {project_name: structure})
    print(f"✅ Project '{project_name}' has been created with initial structure.")

    os.chdir(project_name)
    os.system("git init")
    os.system("git add .")
    os.system('git commit -m "Initial commit with project structure and punch/user features"')
    print("✅ Git repository initialized and initial commit made.")

if __name__ == "__main__":
    main()

structure = {
    "app": {
        "__init__.py": "",
        "main.py": '''from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# Include feature routers here
from app.modules.punch.router import router as punch_router
app.include_router(punch_router, prefix="/punch", tags=["Punch"])
''',
        "database.py": '''from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
''',
        "core": {
            "__init__.py": "",
            "config.py": '''from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Feature-First App"

    class Config:
        env_file = ".env"

settings = Settings()
'''
        },
        "shared": {
            "__init__.py": "",
            "dependencies.py": '''from app.database import SessionLocal
from fastapi import Depends

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
'''
        },
        "modules": {
            "__init__.py": "",
            "punch": {
                "__init__.py": "",
                "models.py": '''from sqlalchemy import Column, Integer, DateTime
from app.database import Base
from datetime import datetime

class Punch(Base):
    __tablename__ = "punches"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, index=True)
    punch_in_time = Column(DateTime, default=datetime.utcnow)
    punch_out_time = Column(DateTime, nullable=True)
''',
                "schemas.py": '''from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PunchBase(BaseModel):
    employee_id: int
    punch_in_time: datetime

class PunchCreate(PunchBase):
    punch_out_time: Optional[datetime] = None

class PunchOut(PunchCreate):
    punch_in_time: datetime

    class Config:
        orm_mode = True
''',
                "router.py": '''from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.shared.dependencies import get_db
from app.modules.punch import models, schemas
from app.modules.punch.models import Punch

router = APIRouter()

@router.post("/", response_model=schemas.PunchOut)
def punch_in_out(punch: schemas.PunchCreate, db: Session = Depends(get_db)):
    db_punch = models.Punch(employee_id=punch.employee_id, punch_in_time=punch.punch_in_time, punch_out_time=punch.punch_out_time)
    db.add(db_punch)
    db.commit()
    db.refresh(db_punch)
    return db_punch
'''
            },
            "user": {
                "__init__.py": "",
                "models": {
                    "__init__.py": "",
                    "user.py": "",
                    "address.py": "",
                    "profile.py": ""
                },
                "schemas": {
                    "__init__.py": "",
                    "user.py": "",
                    "address.py": ""
                },
                "crud": {
                    "__init__.py": "",
                    "user.py": ""
                },
                "services": {
                    "__init__.py": "",
                    "user_service.py": ""
                },
                "routes": {
                    "__init__.py": "",
                    "user_routes.py": ""
                },
                "utils": {
                    "__init__.py": "",
                    "helpers.py": ""
                },
                "auth": {
                    "__init__.py": "",
                    "auth.py": ""
                },
                "config": {
                    "__init__.py": "",
                    "settings.py": ""
                }
            }
        }
    }
}

def create_structure(base_path, struct):
    for name, content in struct.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, "w") as f:
                f.write(content)

def main():
    if os.path.exists(BASE_DIR):
        print(f"❌ Directory '{BASE_DIR}' already exists.")
        return

    create_structure(".", {BASE_DIR: structure})
    print(f"✅ Project '{BASE_DIR}' has been created with initial structure.")

    os.chdir(BASE_DIR)
    os.system("git init")
    os.system("git add .")
    os.system('git commit -m "Initial commit with project structure and punch/user features"')
    print("✅ Git repository initialized and initial commit made.")

if __name__ == "__main__":
    main()
