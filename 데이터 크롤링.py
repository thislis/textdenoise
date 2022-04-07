import pandas as pd
import requests
import time


def get_html(code: str, page: int) -> str:
    url = "https://finance.naver.com/item/sise_day.nhn?"
    querystring = {"code": code, "page": page}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
    response = requests.get(url, params=querystring, headers=headers)
    try:
        response.raise_for_status()
    except Exception as exc:
        print(exc)
        exit(0)

    return response.text


def get_last_page(code: str) -> int:
    page = 9999
    dfs = pd.read_html(get_html(code, page))
    df = dfs[1]
    return df[df.shape[1] - 1].iloc[0]


def scrap_data(code: str, sleep_time: int = 2) -> pd.DataFrame:
    df = pd.DataFrame()
    for page in range(1, get_last_page(code) + 1):
        date_converter = lambda d: d.replace('.', '-')
        dfs = pd.read_html(io=get_html(code, page), converters={0: date_converter})
        df = df.append(dfs[0].dropna().astype(dtype='int64', errors='ignore'), ignore_index=True)
        print(df.tail(1))
        time.sleep(sleep_time)
    return df


def store_data(df: pd.DataFrame, code: int) -> None:
    df.to_csv(f"{code}.csv", index=False)


code = '005930'
store_data(scrap_data(code), code)