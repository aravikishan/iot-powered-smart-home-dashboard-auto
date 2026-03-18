# app.py

from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from passlib.context import CryptContext
from datetime import datetime
import uvicorn

# Database setup
DATABASE_URL = "sqlite:///./smart_home.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Models
class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    device_type = Column(String)
    status = Column(String)
    last_updated = Column(DateTime, default=datetime.utcnow)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    role = Column(String)

# Create tables
Base.metadata.create_all(bind=engine)

# Seed data
def seed_data(db: Session):
    if not db.query(Device).first():
        device1 = Device(name="Living Room Light", device_type="light", status="off")
        device2 = Device(name="Thermostat", device_type="thermostat", status="on")
        db.add(device1)
        db.add(device2)
        db.commit()
    if not db.query(User).first():
        user = User(username="admin", password_hash=pwd_context.hash("admin"), role="admin")
        db.add(user)
        db.commit()

# FastAPI app
app = FastAPI()

# Dependency
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Routes
@app.get("/", response_class=HTMLResponse)
async def read_dashboard():
    with open("templates/dashboard.html") as f:
        return f.read()

@app.get("/devices", response_class=HTMLResponse)
async def read_devices():
    with open("templates/devices.html") as f:
        return f.read()

@app.get("/settings", response_class=HTMLResponse)
async def read_settings():
    with open("templates/settings.html") as f:
        return f.read()

@app.get("/login", response_class=HTMLResponse)
async def read_login():
    with open("templates/login.html") as f:
        return f.read()

@app.get("/api/devices")
async def get_devices(db: Session = Depends(get_db)):
    devices = db.query(Device).all()
    return devices

@app.post("/api/devices")
async def add_device(device: Device, db: Session = Depends(get_db)):
    db.add(device)
    db.commit()
    db.refresh(device)
    return device

@app.put("/api/devices/{id}")
async def update_device(id: int, device: Device, db: Session = Depends(get_db)):
    db_device = db.query(Device).filter(Device.id == id).first()
    if db_device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    db_device.name = device.name
    db_device.device_type = device.device_type
    db_device.status = device.status
    db_device.last_updated = datetime.utcnow()
    db.commit()
    db.refresh(db_device)
    return db_device

@app.delete("/api/devices/{id}")
async def delete_device(id: int, db: Session = Depends(get_db)):
    db_device = db.query(Device).filter(Device.id == id).first()
    if db_device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    db.delete(db_device)
    db.commit()
    return {"detail": "Device deleted"}

@app.get("/api/devices/{id}/status")
async def get_device_status(id: int, db: Session = Depends(get_db)):
    db_device = db.query(Device).filter(Device.id == id).first()
    if db_device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    return {"status": db_device.status}

if __name__ == "__main__":
    db = SessionLocal()
    seed_data(db)
    db.close()
    uvicorn.run(app, host="0.0.0.0", port=8000)
