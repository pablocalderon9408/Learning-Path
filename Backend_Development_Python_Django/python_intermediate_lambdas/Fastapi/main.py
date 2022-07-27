# Python
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI, Body, Path, Query

app = FastAPI()

# Models
class Location(BaseModel):
    city: str
    state: str
    country: str



class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None

@app.get("/")
def home():
    return {"Hello": "World"}

# Los tres puntos de Body me dice que el body es obligatorio.
@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person


# Los query parameters son aquellos que son opcionales, vienen después del ? en la url.
@app.get("/person/detail")
def show_person(
    # Name es opcional y es un Query parameter. En caso tal de que lo envíen, debe cumplir la longitud.
    name: Optional[str] = Query(
        None, min_length=1, 
        max_length=50,
        title="Person Name",
        description="This is the person name. 1 to 50 characters."
        ),
    # El query parameter en este caso es obligatorio, pero no es una buena práctica.
    # Si es obligatorio, debería ser un path parameter.
    age: str = Query(
        ...,
        title="Person age",
        description="This is the person age. Required."
        )
):
    return {name:age}


@app.get("/person/detail/{person_id}")
def show_person(
    # Los path parameters son obligatorios.
    person_id: int = Path(..., gt=0)

):
    return {person_id: "It exists!"}


# Validaciones de Request Body.

@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person id",
        description="This is the person id.",
        gt=0
    ),
    person: Person = Body(
        ...
        ),
    location: Location = Body(
        ...
    )
):
    results = person.dict()
    results.update(location.dict())  
    return results
