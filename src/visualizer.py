'''Github仓库数据可视化模块'''

import matplotlib
matplotlib.use("Agg")

from src.config import FIGSIZE_DEFAULT, SAVE_KW
import matplotlib.pyplot as plt

def plot_stars_top(df, top_n: int, output: str)->None:
    '''
    stars排名图
    
    Parameters
    ----------
    df: pandas.DataFrame
        包含'name'和'stars'列，可按stars降序排列
    top_n: int
        展示前n名
    output: str
        输出文件路径
    '''
    # 取前n名并反转使最高星在上面(barh从下往上画)
    top_df = df.head(top_n).iloc[::-1]

    fig, ax = plt.subplots(figsize = FIGSIZE_DEFAULT)
    ax.barh(top_df['name'], top_df['stars'])
    ax.set_title(f'Stars Top{top_n}排名图')
    ax.set_xlabel("stars数")
    ax.set_ylabel("仓库名")
    ax.grid(axis='x', alpha = 0.3)

    plt.savefig(f'{output}.png',**SAVE_KW)
    plt.close(fig)

def plot_language_distribution(language_counts: list[tuple[str, int]], output: str)->None:
    '''
    语言分布柱状图
    
    Parameters
    ----------
    language_counts : list[tuple[str, int]]
        [(语言名, 仓库数), ...] 格式的数据
    output : str
        输出文件路径
    '''
    names = [item[0] for item in language_counts]
    counts = [item[1] for item in language_counts]

    fig, ax = plt.subplots(figsize = FIGSIZE_DEFAULT)
    ax.bar(names, counts, linewidth = 0.5)
    ax.set_title("语言分布柱状图")
    ax.set_xlabel("语言")
    ax.set_ylabel("仓库数")
    ax.grid(axis='y', alpha = 0.3)

    ax.set_xticklabels(names, rotation = 45, ha = 'right')
    plt.savefig(f'{output}.png', dpi = 150, bbox_inches = "tight")
    plt.close(fig)