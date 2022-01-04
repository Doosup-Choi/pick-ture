import requests
import urllib
import json
import os
import pathlib
import time

from datetime import datetime

# 작가 그림

main_category_list = ["추상화"]
# main_category_list = ["유명화가","추상화", "모던아트"]
root_meta_dir = "./meta"
root_croped_dir = "./data_croped"

for cur_category in main_category_list:

    cur_category_merge_dict = {"main_category": cur_category, "items":[]}
    cur_json_dir = os.path.join(root_meta_dir, f"{cur_category}.json")
    cur_croped_list = os.listdir(os.path.join(root_croped_dir, cur_category))

    with open(cur_json_dir, "r", encoding = "utf-8") as f:      
        json_data = json.load(f)  

    for idx, cur_item in enumerate(json_data["items"]):

        image_name = cur_item["image"].split("/")[-1]
        if image_name in cur_croped_list:
            cur_category_merge_dict["items"].append(cur_item)

    save_json_name = os.path.join(root_meta_dir,f"{cur_category}_croped.json") 
    with open(save_json_name, 'w', encoding = "utf-8") as f:
        json.dump(cur_category_merge_dict, f, indent=4, ensure_ascii=False)