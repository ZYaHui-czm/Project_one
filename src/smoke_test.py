import os
import pandas as pd
from collections import Counter

# 导入被测函数
from analyzer import analyze_repos
from visualizer import plot_language_distribution, plot_stars_top

# 模拟数据
repos = [
    {
        "name": "fastapi",
        "stars": 81000,
        "forks": 6200,
        "language": "Python",
        "created_at": "2018-12-08T00:00:00Z"
    },
    {
        "name": "vue",
        "stars": 208000,
        "forks": 34000,
        "language": "JavaScript",
        "created_at": "2014-07-29T00:00:00Z"
    },
    {
        "name": "rust",
        "stars": 98000,
        "forks": 12500,
        "language": "Python",
        "created_at": "2010-06-16T00:00:00Z"
    },
]

if __name__ == "__main__":
    # 测试analyzer
    result = analyze_repos(repos)
    print(f'analyze测试结束，结果：{result}')

    # 测试visualizer
    df = pd.DataFrame([{'name': r["name"], 'stars': r["stars"]} for r in repos]).sort_values("stars",ascending=False).reset_index(drop=True)
    count_language = Counter(r['language'] or 'N/A' for r in repos).most_common()

    plot_stars_top(df, top_n=3, output='test_1')
    plot_language_distribution(language_counts=count_language, output='test_2')

    # 检验文件是否存在
    for f in ['test_1.png', 'test_2.png']:
        assert os.path.isfile(f), f'错误：文件不存在'

    print(f'测试通过')