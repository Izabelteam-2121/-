from fastapi import FastAPI, Request
from fastapi_users import fastapi_users, FastAPIUsers
from pages.router import router as router_pages
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="Investment App"
)

fake_users = [
    {"id": 1, "role": "admin", "name": "Anita"},
    {"id": 2, "role": "investor", "name": "Izabel"},
    {"id": 3, "role": "trader", "name": "Bob"},
]


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]


fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12},
]


@app.get("/trades")
def get_trades(limit: int = 1, offset: int = 0):
    return fake_trades[offset:][:limit]


fake_users2 = [
    {"id": 1, "role": "admin", "name": "Anita"},
    {"id": 2, "role": "investor", "name": "Izabel"},
    {"id": 3, "role": "trader", "name": "Bob"},
]


@app.post("/users/{user_id}")
def change_user(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, fake_users2))[0]
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}


app.include_router(router_pages)
