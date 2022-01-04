This is a Pick-ture project.
=============

### * 네이버 쇼핑 API 크롤링 절차(네이버 오픈 API 활용, 샘플 예시)
1. 네이버 개발자 어플리케이션 등록
    * https://developers.naver.com/docs/search/shopping/ 에서 자세한 가이드 제공

2. crawling 폴더 내 crawling.ipynb 실행
    * query / display / start / sort 를 활용하여 크롤링 조건 변경
    * 이미지 다운로드



### * 데이터 확보 절차
1. Step1 : 네이버 쇼핑 오픈 API를 통한 크롤링
    * python Step1_data_collection.py

2. Step2 : 크롤링 정보 Merge
    * python Step2_merge_meta.py

3. Step3 : Croped 된 이미지로 Meta 정보 최종 생성
    * python Step3_filter_meta_by_croped_image.py


### * 데이터 및 메타 정보 폴더 구조
```bash
├── data
│   ├── 모던아트
│   ├── 추상화
│   ├── 유명작가
├── data_croped
│   ├── 모던아트
│   ├── 추상화
│   ├── 유명작가
├── meta
│   ├── 모던아트.json
│   ├── 추상화.json
│   ├── 유명작가.json
│   ├── 모던아트_croped.json
│   ├── 추상화_croped.json
│   ├── 유명작가_croped.json
└── crawling.ipynb
└── Step1_data_collection.py
└── Step2_merge_meta.py
└── Step3_filter_meta_by_croped_image.py
``` 