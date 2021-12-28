import os
import random
import json
from typing import List, Dict, Optional
from datetime import date, datetime, time
from pathlib import Path
import shutil
import random
import requests

from pydantic import BaseModel 
from fastapi import APIRouter, HTTPException, status, Query
from fastapi.responses import JSONResponse, Response

router = APIRouter()
#-------------------------------------------------------------------------------------------------------#
# user functions --


#-------------------------------------------------------------------------------------------------------#
# API
@router.get('/health_check')
def health_check(): 

    return Response(status_code=status.HTTP_204_NO_CONTENT)