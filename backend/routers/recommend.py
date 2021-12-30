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
from schemas import recommend as RecommendSchema

router = APIRouter()
#-------------------------------------------------------------------------------------------------------#
# user functions --


#-------------------------------------------------------------------------------------------------------#
# API
@router.post(
    "/main",
    summary="[Recommed-001] 홈 화면 정보를 불러온다.",
    description="로그인 후에 진입하는 홈 화면에 필요한 정보(대문 사진, 선호도 별 추천 이미지)를 전달한다.",
    response_model=RecommendSchema.MainSchema,
)
def return_main_info(): 
 
    results = {
        "main_image_path": "S3://../ABC.jpg",
        "categories": {
            "category_name": "modern art",
            "image_list": [
                {
                    "image_path": "S3://../ABC1.jpg",
                    "image_idx": 1
                },
                {
                    "image_path": "S3://../ABC2.jpg",
                    "image_idx": 2
                }
           ]
        }
    }

    return results

@router.post(
    "/images",
    summary="[Recommed-002] 추천 결과 이미지를 받아온다.",
    description="사용자에게 전달받은 이미지로 추천 알고리즘 결과를 반환한다.",
    response_model=RecommendSchema.RecommendImagesSchema,
)
def return_recommend_images(
        input_path: str = Query(
        "S3://../../ABC.jpg",
        example="S3://../../ABC.jpg",
        description="사용자가 촬영 or 업로드한 이미지를 S3애 저장한 경로",
        title="입력 이미지 경로",
    )
): 
    results = {
        "background_description" : "The photographed image is judged to be a warm and cozy house with an overall white tone.",
        "categories": {
            "category_name": "modern art",
            "image_list": [
                {
                    "image_path": "S3://../ABC1.jpg",
                    "image_idx": 1
                },
                {
                    "image_path": "S3://../ABC2.jpg",
                    "image_idx": 2
                }
           ]
        }
    }

    return results

@router.post(
    "/results",
    summary="[Recommed-003] 추천 결과 메타정보를 받아온다.",
    description="사용자가 시뮬레이터 완료 한 이미지로 메타정보(구매링크, 추천설명)을 반환한다.",
    response_model=RecommendSchema.RecommendResultsSchema,
)
def return_recommend_results(
        image_idx: int = Query(
        123,
        example=123,
        description="사용자가 선택한 이미지의 고유 인덱스",
        title="이미지 인덱스",
    )
): 

    results = {
        "recommend_description" : "In general, it is judged that a modern picture would suit the cozy living room in white tones.",
        "image_info" : {
            "image_path" : "S3://../ABC.jpg",
            "image_idx" : 12345,
            "purchase_link" : "http://.../ABC.com",
            "price" : "10000",
            "mall_name" : "네이버",
        }
    }

    return results