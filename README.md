# Daangn Market Nintendo Switch 거래 분석

강남·분당·부산 “닌텐도 스위치” 매물 데이터를 분석하여  
지역별 가격 동향, 모델·상태별 가격 패턴, 거래 상태 분포를 시각화합니다.

## Goal

* 지역별 평균 거래가 비교  
* 모델(예: OLED, Lite)·상태(미개봉·중고)별 가격 분포 분석  
* 거래 상태(on_sale·reserved·sold)별 비율 및 평균가 도출  
* 시각화 대시보드 제작

## 프로젝트 구조

폴더명            | 설명  
-----------------|--------------------------------  
`data/`          | 원본 스크래핑 데이터 (`daangn_nintendo.csv`), 당근마켓 데이터 크롤링을 위한 당근마켓 지역코드 데이터(`daangn_regions_full.csv`)
`notebooks/`     | 0EDA 및 감성분석, 시각화 노트북 
`visuals/`       | 결과로 생성된 차트 및 이미지
`report/`        | 분석 결과 요약 및 인사이트 정리  
`requirements.txt` | 필요한 패키지 리스트  

## 사용 기술

* Python (pandas, matplotlib, seaborn)  
* Jupyter Notebook  
* Git / GitHub  

## 주요 분석 항목

* EDA: 전체 매물 가격 분포, 거래 상태별(count & avg price) 
* 제품별(OLED, Lite) 별 가격 차이 
* 지역별 평균가격 비교 (강남 vs 분당 vs 부산)   
* 지역별 거래 완료율

## 결론


## 확장 가능성


## 레포트

1. 전처리 보고서 
2. EDA 보고서 
3. 키워드 분석 보고서 
4. 최종 보고서 

