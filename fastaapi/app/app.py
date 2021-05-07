from fastapi import FastAPI 

app = FastAPI()


# minimal app - get request

@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return{"ping": "pong"}


# Get --> Read Todo
@app.get('/todo', tags=['todos'])
async def get_todo() -> dict:
    return{"data": todos}


# post ---> Create todo
@app.post("/todo", tags=["todos"])
async def add_todo(todo:dict) -> dict:
    todos.append(todo)
    return {
        "data": "A todo has been entered"
    }


@app.put("/todo/{id}", tags=["todos"])
async def update_todo(id: int, body: dict) -> dict:
    for todo in todos:
        if int(todo['id']) == id:
            todo['Activity'] = body['Activity']
            return {
                "data":f"Todo with id {id} has been updated"
            }
            return {
                "data":f"Todo with this id number {id} was not found"
            }


# delete post
@app.delete("/todo/{id}", tags=["todos"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int((todo["id"])) == id:
            todo.remove(todo)
            return {
                "data":f"todo with id {id} has been deleted"
            }
    return {
        "data":f"this todo with {id} wasn't found."

    }
todos = [
    {
        "id": "1",
        "Activity": "walking and praying at my street for 45 minutes at 7:00 AM."
    },
    {
        "id": "2",
        "Activity": "checked and reply all my emails 2:00 PM."
    },
    {
        "id": "3",
        "Activity": "Wrote down my day's target and achievement plans."
    },
    {
        "id": "4",
        "Activity": "Start taking my course on Data Science with some reading inbetween"
    }
]