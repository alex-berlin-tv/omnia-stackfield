from .stackfield import Stackfield

from fastapi import FastAPI, Request


app = FastAPI()


@app.post("/on-omnia-updates")
async def webhook(request: Request):
    # with open("dump.json", "a") as f:
    #     data = await request.json()
    #     print(data)
    #     f.write(str(data))
    data = await request.json()
    if "trigger" not in data:
        return
    if "event" not in data["trigger"]:
        return
    if data["trigger"]["event"] != "encoded":
        return
    if data["item"]["streamtype"] != "video":
        return
    
    id = data["item"]["ID"]
    title = data["data"]["general"]["title"]
    uploaded = data["data"]["general"]["uploaded"]

    print(f"id: {id}, title: {title}, uploaded: {uploaded}")
    stackfield = Stackfield()
    stackfield.task(f"{id}: {title}", f"Ein neues Video wurde am {uploaded} hochgeladen. Bitte die Aufgabe einer Contentperson zuordnen.")
    
    return