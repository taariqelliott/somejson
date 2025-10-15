from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from faker import Faker

app = FastAPI()
faker = Faker()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    value = faker.text()
    return {"phrase": value}
