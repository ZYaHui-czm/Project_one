import matplotlib.pyplot as plt

# 中文 & 符号
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 画布大小
FIGSIZE_DEFAULT = (10, 6)

# 保存参数
SAVE_KW = dict(dpi = 150,
               bbox_inches = 'tight',
               facecolor = 'white')