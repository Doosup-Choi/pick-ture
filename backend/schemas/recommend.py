from typing import List, Dict, Optional
from datetime import datetime

from pydantic import BaseModel, Field
from starlette import background


class ImageSchema(BaseModel):

    image_path:str = "S3://../ABC.jpg"
    image_idx:int = 12345
    purchase_link:str = "http://.../ABC.com"
    price:str = "10000"
    mall_name:str = "네이버"

    class Config:
        orm_mode = True

class CategorySchema(BaseModel):

    category_name:str = "modern art"
    image_list: List[ImageSchema]
    class Config:
        orm_mode = True

class MainSchema(BaseModel):
    
    main_image_path:str = "S3://../ABC.jpg"
    categories: CategorySchema
    
    class Config:
        orm_mode = True

class RecommendImagesSchema(BaseModel):

    background_description:str="The photographed image is judged to be a warm and cozy house with an overall white tone."
    categories: CategorySchema

    class Config:
        orm_mode = True

class RecommendResultsSchema(BaseModel):

    recommend_description:str="In general, it is judged that a modern picture would suit the cozy living room in white tones."
    image_info: ImageSchema

    class Config:
        orm_mode = True