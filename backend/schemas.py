from pydantic import BaseModel

class CityResponse(BaseModel):
    id: int
    city_name: str
    state: str
    latitude: float
    longitude: float

    model_config = {
        "from_attributes": True
    }