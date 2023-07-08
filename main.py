from fastapi import FastAPI
import uvicorn

import authentication
import offers



app = FastAPI()

app.include_router(authentication.router)
app.include_router(offers.router)

if __name__=="__main__":
    uvicorn.run(app)