from fastapi import APIRouter
# ST1 using api router to wrap all api endpoint.i nameit (entry_root). initialise your file(entry.py)with apirouter
entry_root = APIRouter()
#ST2
# first get request endpoint. (/)means the main route
@entry_root.get("/")
#ST3 name a your function (apiRunning)
def apiRunning():
#ST4 create a response dictionary(res)
    res ={
        "status" :"ok",
        "message" : "API is runnning"
    }
    return res