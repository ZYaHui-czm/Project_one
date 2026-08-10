import pandas as pd
import logging
from collections import Counter


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    filename="log.log",
    filemode="w"
)

def analyze_repos(items: list[dict])->dict:
    logging.info("analyze_repo开始")

    if not items:
        logging.warning("items参数为空")
        return {
            "avg_stars": 0.0,
            "max_stars_name": '',
            "top_language": ''
        }

    rows = []
    for item in items:
        rows.append({
            "name": item["name"],
            "stars": item["stars"],
            "forks": item["forks"],
            "language": item["language"] or "N/A",
            "created_at": item["created_at"]
        })

    languages = [r["language"] for r in rows]
    count_languages = Counter(languages)

    df = pd.DataFrame(rows)
    avg_star = round(df["stars"].mean(), 1)
    max_stars_name = max(rows, key=lambda x: x["stars"])["name"]
    top_language = count_languages.most_common(1)[0][0]

    analyze_dict = {
        "avg_stars": avg_star,
        "max_stars_name": max_stars_name,
        "top_language": top_language
    }

    logging.info("analyze_repo完成")

    return analyze_dict