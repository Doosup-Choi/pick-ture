import requests
import urllib
import json
import os
import pathlib
import time

from datetime import datetime

# 작가 그림

# main_category_list = ["추상화"]
main_category_list = ["유명화가","추상화", "모던아트"]
root_meta_dir = "./meta"
root_data_dir = "./data"

for cur_category in main_category_list:
    cur_category_merge_dict = {"main_category": cur_category, "items":[]}
    cur_category_query_list = os.listdir(os.path.join(root_meta_dir,cur_category))
    cur_category_query_list = [i for i in cur_category_query_list if cur_category in i]
    print(cur_category_query_list)

    for cur_query in cur_category_query_list:
        cur_query_file =  os.path.join(root_meta_dir, cur_category, cur_query)
        # print(cur_query_file)
        with open(cur_query_file, "r", encoding = "utf-8") as f:      
            json_data = json.load(f)  

        cur_category_merge_dict["items"].extend(json_data["items"])

    # print(cur_category_merge_dict)

    save_json_name = os.path.join(root_meta_dir,f"{cur_category}.json") 
    with open(save_json_name, 'w', encoding = "utf-8") as f:
        json.dump(cur_category_merge_dict, f, indent=4, ensure_ascii=False)

