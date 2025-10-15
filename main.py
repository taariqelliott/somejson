from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from faker import Faker

faker = Faker()

app = FastAPI()

keys = ["phrase", "message", ""]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    key = faker.word()
    value = faker.text()
    print(key, value)
    return {"phrase": value}
