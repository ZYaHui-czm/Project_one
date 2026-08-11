import pandas as pd
import logging



logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    filename="log.log",
    filemode="w"
)

def analyze_repos(items: list[dict]):
    logging.info("analyze_repo start")

    # 空值检查
    if not items:
        logging.warning("items为空")
        return pd.DataFrame(columns=['name', 'stars','forks', 'language', 'created_at'])
    rows = []
    for item in items:
        rows.append({
            "name": item["name"],
            "stars": item["stars"],
            "forks": item["forks"],
            "language": item["language"] or "N/A",
            "created_at": item["created_at"]
        })

    df = pd.DataFrame(rows)


    logging.info("analyze_repo completed")

    return df