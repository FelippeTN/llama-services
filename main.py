import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", reload=False)