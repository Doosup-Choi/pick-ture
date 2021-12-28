from pydantic import BaseModel  # pylint: disable=no-name-in-module
from fastapi import APIRouter, HTTPException, status, Query
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse, Response

from routers import preprocessing  
from routers import recommend  

import uvicorn 

#-------------------------------------------------------------------------------------------------------#
# creating FastAPI app --
def create_app() -> FastAPI:
    app = FastAPI(
        title="Pick-ture Backend API",
        )
    return app


app = create_app()   
    
#-------------------------------------------------------------------------------------------------------#
# Routers
app.include_router(
    preprocessing.router, prefix=f"/api_v1/preprocessing", tags=["Preprocessing"]
)
app.include_router(
    recommend.router, prefix=f"/api_v1/recommend", tags=["Recommend"]
)

#-------------------------------------------------------------------------------------------------------#
if __name__ == '__main__':
    print("start API Service")
    
    uvicorn.run(app, host="0.0.0.0")
    
