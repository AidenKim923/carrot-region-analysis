import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import os

def collect_article_contents(df_links, backup_interval=50, backup_path="data/backup_partial.csv"):
    print(f"[본문 + 시간 수집 시작] 전체 {len(df_links)}건")

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1280,1000")

    driver = webdriver.Chrome(options=options)
    contents = []
    posted_times = []

    for idx, url in enumerate(df_links['link']):
        try:
            driver.get(url)
            time.sleep(0.5)

            soup = BeautifulSoup(driver.page_source, "html.parser")

            content_tag = soup.select_one("p[class*=fontWeight_regular]")
            content = content_tag.get_text(separator=' ', strip=True) if content_tag else ""
            content = content.replace('\r', ' ').replace('\n', ' ').replace('"', "'")

            time_tag = soup.select_one("time[datetime]")
            raw_time = time_tag['datetime'] if time_tag else ""
            parsed_time = pd.to_datetime(raw_time, errors='coerce')
            posted_time = parsed_time.strftime("%Y-%m-%d") if pd.notnull(parsed_time) else ""

            contents.append(content)
            posted_times.append(posted_time)

            if (idx + 1) % backup_interval == 0:
                print(f"[{idx+1}]건 완료 -> 백업 저장")
                # 중간 백업
                backup_df = df_links.iloc[:idx+1].copy()
                backup_df['content'] = contents
                backup_df['posted_time'] = posted_times
                backup_df.to_csv(backup_path, index=False, encoding="utf-8-sig", quoting=1)

        except Exception as e:
            print(f"[{idx+1}] 오류: {e}")
            contents.append("")
            posted_times.append("")

    driver.quit()

    return contents, posted_times


if __name__ == "__main__":
    df = pd.read_csv("data/daangn_nintendo_cleaned.csv")

    df['content'], df['posted_time'] = collect_article_contents(
        df_links=df,
        backup_interval=50,
        backup_path="data/backup_partial.csv"
    )

    df.to_csv("data/daangn_nintendo_full.csv", index=False, encoding="utf-8-sig", quoting=1)
    print("전체 크롤링 및 저장 완료: daangn_nintendo_full.csv")
