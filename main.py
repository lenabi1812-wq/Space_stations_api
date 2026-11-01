from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List

app = FastAPI(title="API каталога космических станций")

class StationCreate(BaseModel):
    name: str
    orbit: str
    crew: int

class Station(BaseModel):
    id: int
    name: str
    orbit: str
    crew: int

stations_db = [
    {"id": 1, "name": "МКС", "orbit": "Земля", "crew": 7},
    {"id": 2, "name": "Тяньгун", "orbit": "Земля", "crew": 3}
]

@app.get("/stations", response_model=List[Station])
def get_stations():
    return stations_db

@app.post("/stations", response_model=Station, status_code=status.HTTP_201_CREATED)
def create_station(station: StationCreate):
    new_id = max([s["id"] for s in stations_db], default=0) + 1

    new_station_dict = {
        "id": new_id,
        "name": station.name,
        "orbit": station.orbit,
        "crew": station.crew
    }

    stations_db.append(new_station_dict)

    return new_station_dict