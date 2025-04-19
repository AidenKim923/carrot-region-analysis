# Daangn Market Nintendo Switch 거래 분석

강남·분당·부산 “닌텐도 스위치” 매물 데이터를 분석하여  
지역별 가격 동향, 모델·상태별 가격 패턴, 거래 상태 분포를 분석합니다. 


## 프로젝트 구조

폴더명            | 설명  
-----------------|--------------------------------  
`data/`          | 원본 스크래핑 데이터 (`daangn_nintendo.csv`), 당근마켓 데이터 크롤링을 위한 당근마켓 지역코드 데이터(`daangn_regions_full.csv`)
`notebooks/`     | EDA 및 감성분석, 시각화 노트북 
`visuals/`       | 결과로 생성된 차트 및 이미지
`report/`        | 분석 결과 요약 및 인사이트 정리  
`requirements.txt` | 필요한 패키지 리스트  

## 사용 기술

* Python (pandas, matplotlib)  
* Jupyter Notebook  
* Git / GitHub  

## 주요 분석 항목

* 제품별 (OLED, Lite, Edition)별 가격 차이
* 지역별 평균가격 비교
* 요일별 평균 가격

## 결론
[최종 보고서](reports/final_report.md)

## 느낀점 
* 데이터 전처리를 하는데 생각보다 많은 시간이 걸렸음
* 세트와 단품에 대한 명확한 기준이 없어서 가격처리하는부분에서 꽤나 애를먹음
* 조금 더 공부를 많이 해야겠다고 느낌