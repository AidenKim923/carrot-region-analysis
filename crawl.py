import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time

def collect_all_articles(gu, dong, region_id, keyword="닌텐도 스위치", max_count=100):
    print(f"[{dong}] 시작")

    url = f"https://www.daangn.com/kr/buy-sell/?in={dong}-{region_id}&search={keyword.replace(' ', '+')}"
    
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1280,1000")
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(3)

    collected_links = set()
    results = []

    while True:
        items = driver.find_elements(By.XPATH, '//a[@data-gtm="search_article"]')

        for tag in items:
            try:
                lines = tag.text.splitlines()
                lines = [line.strip() for line in lines if line.strip()]
                if not lines:
                    continue

                # 상태 확인
                status_keywords = ["판매완료", "예약중", "나눔"]
                status = "판매중"
                if lines[0] in status_keywords:
                    status = lines[0]
                    lines = lines[1:]

                title, region_and_time, price_text = "", "", ""

                for line in lines:
                    if "·" in line:
                        region_and_time = line
                    elif "전" in line and not region_and_time:
                        region_and_time = line
                    elif "원" in line:
                        price_text = line
                    elif not title:
                        title = line

                if "·" in region_and_time:
                    time_text = region_and_time.split("·")[-1].strip()
                else:
                    time_text = region_and_time.strip()

                price_digits = re.sub(r"[^\d]", "", price_text)
                price = int(price_digits) if price_digits else None

                href = tag.get_attribute("href")
                link = href if href.startswith("http") else "https://www.daangn.com" + href

                if link in collected_links:
                    continue

                results.append({
                    "gu": gu,
                    "dong": dong,
                    "title": title,
                    "price": price,
                    "time": time_text,
                    "link": link,
                    "status": status
                })

                collected_links.add(link)

                if len(results) >= max_count:
                    driver.quit()
                    return pd.DataFrame(results)

            except Exception:
                continue

        try:
            more_btn = driver.find_element(By.XPATH, "//button[contains(text(), '더보기')]")
            driver.execute_script("arguments[0].click();", more_btn)
            time.sleep(2)
        except:
            break

    driver.quit()
    return pd.DataFrame(results)


if __name__ == "__main__":
    df_regions = pd.read_csv("daangn_regions_full.csv")
    all_results = []

    for _, row in df_regions.iterrows():
        gu = row["gu_name"]
        dong = row["display_name"]
        region_id = str(row["region_id"])

        try:
            df = collect_all_articles(gu, dong, region_id, max_count=100)
            all_results.append(df)
        except Exception as e:
            print(f"[{dong}] 수집 실패: {e}")
            continue

    final_df = pd.concat(all_results, ignore_index=True)
    final_df.to_csv("당근_닌텐도_스위치_전체_크롤링.csv", index=False)
    print("모든 지역 크롤링 완료")
