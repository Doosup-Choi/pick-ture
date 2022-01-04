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
root_save_dir = "./data"
root_croped_dir = "./data_croped"
root_meta_dir = "./meta"
num_query = 10

for idx, cur_main_category in enumerate(main_category_list):
    
    # Step1) 카테고리 별 메타 정보를 생성한다.
    category_info = {
        "category_idx" : idx+1,
        "main_category" : cur_main_category,
        "query" : f"인테리어 {cur_main_category}",
        "others" : {},
        "time" : str(datetime.now()),
        "items" : [],
    }

    # Step2) 카테고리 별 이미지 저장 폴더를 생성한다.
    folder_dir = os.path.join(root_save_dir, f"{str(cur_main_category)}")
    os.makedirs(folder_dir, exist_ok=True)    

    croped_dir = os.path.join(root_croped_dir, f"{str(cur_main_category)}")
    os.makedirs(croped_dir, exist_ok=True)    

    meta_dir = os.path.join(root_meta_dir, f"{str(cur_main_category)}")
    os.makedirs(meta_dir, exist_ok=True)   

    # Step3) 카테고리 별 num_query 수 만큼 네이버 API를 호출한다. 
    for n in range(num_query):
        # Query Parameters
        display = "100"
        start = str(n*int(display)+1) #최소1 최대1000
        sort = "sim" #정렬 옵션 : sim(유사도), date(날짜순), asc(가격오름차순), dsc(가격내림차순)
        query = category_info["query"] 

        query = urllib.parse.quote(query)
        url = "https://openapi.naver.com/v1/search/shop?query=" + query + "&display=" + display+ "&start=" + start + "&sort=" + sort 

        client_id = "ns_lsVeiLXPoagHNyqXD"
        client_secret = "tKVxt4TFYp"

        request = urllib.request.Request(url)
        request.add_header('X-Naver-Client-Id', client_id)
        request.add_header('X-Naver-Client-Secret', client_secret)

        response = urllib.request.urlopen(request)
        results = response.read().decode('utf-8')
        results_json = json.loads(results)

        # Step4) 쿼리 결과를 json파일에 Extend 한다.
        for row in results_json["items"]:
            category_info["items"].append(row)
        
    # Step5) 카테고리 별 메타 정보를 저장한다.
    save_time = time.strftime('%y%m%d-%H%M%S')
    with open(f'./meta/{cur_main_category}/art_json_category {cur_main_category} {str(save_time)}.json', 'w', encoding='UTF-8') as f: 
        json.dump(category_info, f, indent=4, ensure_ascii=False)
    
    # Step6) 이미지를 저장한다.
    for idx, cur_picture in enumerate(category_info["items"]):

        url = cur_picture["image"]
        root, extension = os.path.splitext(url)
        save_name = os.path.join(root_save_dir, f"{str(cur_main_category)}", url.split('/')[-1])
        urllib.request.urlretrieve(url, save_name)
        print(f"{str(idx+1)}")
        print(f"{str(idx+1)} Root Image : {root}{extension}")
        print(f"{str(idx+1)} Saved Image : {url.split('/')[-1]}")
        
        # time.sleep(0.1)