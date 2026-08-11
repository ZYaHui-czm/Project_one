from src.fetcher import fetch_top_repos
from src.analyzer import analyze_repos
from src.visualizer import plot_language_distribution, plot_stars_top
from collections import Counter

if __name__ == "__main__":
    top = int(input("请输入需要获取的仓库数:"))
    top_n = int(input("请输入需要展示的仓库数："))

    fetch_data = fetch_top_repos(top)

    analyze_data = analyze_repos(fetch_data)
    df = analyze_data.sort_values("stars", ascending=False).reset_index(drop=True)
    language_count = Counter(analyze_data['language']).most_common()

    plot_stars_top(df, top_n, output=(input("请输入要输出的stars排名图的文件名:")))
    plot_language_distribution(language_count, output=(input("请输入要输出的语言分布柱状图文件名：")))

    avg_stars = round(df['stars'].mean(), 1)
    max_stars_name = df.loc[df["stars"].idxmax(), 'name']

    print(f'avg_stars:{avg_stars}')
    print(f'max_stars_name:{max_stars_name}')