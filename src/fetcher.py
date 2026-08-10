'''
写 fetcher.py 完整模块，要求：

定义函数 fetch_top_repos(top: int) -> list[dict]
从环境变量读 token(用 os.getenv)
用 requests.get 请求 GitHub 搜索 API(q=language:python&sort=stars)
timeout=10,超时/网络错误抛自定义 ApiError
非 2xx 状态码抛 ApiError(带状态码信息)
返回 data["items"] 列表
'''

import requests
import os
from src.exceptions import ApiError


def fetch_top_repos(top: int)->list[dict]:
    GITHUB_API = "https://api.github.com/search/repositories"
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    params = {"q": "language:python", "sort": "stars", "per_page": top}
    headers = {"Authorization": f'token {GITHUB_TOKEN}'}

    # 空TOKEN检查
    if not GITHUB_TOKEN:
        raise ApiError(0, '缺少GITHUB_TOKEN')
    
    try:
        resp = requests.get(GITHUB_API, params=params, headers=headers, timeout=10)
        if not(200 <= resp.status_code < 300):
            raise ApiError(resp.status_code, resp.text)
        
    except requests.exceptions.Timeout:
        raise ApiError(0, "请求超时")
    except requests.exceptions.ConnectionError:
        raise ApiError(0, "网络连接失败")

    data = resp.json() 
    return data["items"]
