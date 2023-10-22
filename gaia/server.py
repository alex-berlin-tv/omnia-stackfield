from fastapi import FastAPI, Request


app = FastAPI()


@app.post("/on-omnia-updates")
async def webhook(request: Request):
    with open("dump.json", "w") as f:
        data = await request.json()
        print(data)
        f.write(str(data))