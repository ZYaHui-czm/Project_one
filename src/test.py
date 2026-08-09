"""
Matplotlib 多子图绑制完整示例
=================================
涵盖：创建子图、绑定数据、样式设置、中文支持、
      布局调整、保存图片、显示窗口
"""

# ============================================================
# 第一部分：导入库 & 全局配置
# ============================================================
import matplotlib.pyplot as plt
import numpy as np

# --- 中文显示配置（必须在绑图之前设置）---
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'PingFang SC', 'Noto Sans CJK SC']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号 '-' 显示为方块的问题

# ============================================================
# 第二部分：准备模拟数据
# ============================================================
np.random.seed(42)  # 固定随机种子，保证每次运行结果一致

x = np.linspace(0, 2 * np.pi, 200)       # 200个等距点，用于三角函数
y1 = np.sin(x)                            # 正弦波
y2 = np.cos(x)                            # 余弦波

bar_labels = ['产品A', '产品B', '产品C', '产品D', '产品E']
bar_values = [23, 45, 56, 12, 38]         # 柱状图数据

scatter_x = np.random.randn(150)          # 散点图 x（正态分布）
scatter_y = scatter_x * 1.5 + np.random.randn(150) * 0.5  # 散点图 y（线性相关+噪声）

hist_data = np.random.normal(loc=50, scale=15, size=1000)  # 直方图数据

# ============================================================
# 第三部分：创建画布和子图结构（核心！）
# ============================================================
# plt.subplots(2, 3) 创建一个 2行×3列 的子图网格
# figsize=(14, 9) 设置画布尺寸为 14英寸×9英寸
# dpi=100 设置默认分辨率
fig, axes = plt.subplots(2, 3, figsize=(14, 9), dpi=100)

# 此时 axes 是一个 shape=(2,3) 的 numpy 数组
# axes[0,0] 是第1行第1列的子图
# axes[1,2] 是第2行第3列的子图

# ============================================================
# 第四部分：逐个绑定数据到各子图
# ============================================================

# --- 子图1：折线图（左上角 axes[0,0]）---
axes[0, 0].plot(x, y1, color='#E74C3C', linewidth=2, label='sin(x)')
axes[0, 0].plot(x, y2, color='#3498DB', linewidth=2, linestyle='--', label='cos(x)')
axes[0, 0].set_title('三角函数曲线', fontsize=13, fontweight='bold')
axes[0, 0].set_xlabel('x（弧度）')
axes[0, 0].set_ylabel('y')
axes[0, 0].legend(loc='upper right')   # 添加图例
axes[0, 0].grid(True, alpha=0.3)       # 添加半透明网格

# --- 子图2：柱状图（中上 axes[0,1]）---
colors = ['#2ECC71', '#E67E22', '#9B59B6', '#1ABC9C', '#E74C3C']
axes[0, 1].bar(bar_labels, bar_values, color=colors, edgecolor='black', linewidth=0.5)
axes[0, 1].set_title('产品销量统计', fontsize=13, fontweight='bold')
axes[0, 1].set_xlabel('产品类别')
axes[0, 1].set_ylabel('销量（万件）')
# 在柱子顶部添加数值标签
for i, v in enumerate(bar_values):
    axes[0, 1].text(i, v + 1, str(v), ha='center', fontsize=11)

# --- 子图3：散点图（右上 axes[0,2]）---
axes[0, 2].scatter(scatter_x, scatter_y, alpha=0.6, s=30, color='#8E44AD', edgecolors='white', linewidth=0.3)
axes[0, 2].set_title('散点分布图', fontsize=13, fontweight='bold')
axes[0, 2].set_xlabel('特征 X')
axes[0, 2].set_ylabel('特征 Y')

# --- 子图4：直方图（左下 axes[1,0]）---
axes[1, 0].hist(hist_data, bins=30, color='#F39C12', edgecolor='white', density=True)
axes[1, 0].set_title('正态分布直方图', fontsize=13, fontweight='bold')
axes[1, 0].set_xlabel('数值')
axes[1, 0].set_ylabel('概率密度')

# --- 子图5：面积图/填充图（中下 axes[1,1]）---
axes[1, 1].fill_between(x, y1, alpha=0.4, color='#1ABC9C', label='sin区域')
axes[1, 1].plot(x, y1, color='#16A085', linewidth=1.5)
axes[1, 1].axhline(y=0, color='black', linewidth=0.8, linestyle='-')  # 添加y=0参考线
axes[1, 1].set_title('面积填充图', fontsize=13, fontweight='bold')
axes[1, 1].set_xlabel('x')
axes[1, 1].set_ylabel('sin(x)')
axes[1, 1].legend()

# --- 子图6：多条折线+标注（右下 axes[1,2]）---
axes[1, 2].plot(x, np.sin(x) * np.exp(-0.1 * x), 'r-', linewidth=2, label='衰减正弦')
axes[1, 2].plot(x, np.cos(x) * np.exp(-0.1 * x), 'b--', linewidth=2, label='衰减余弦')
axes[1, 2].annotate('峰值', xy=(0, 1), xytext=(1, 0.8),
                    fontsize=11, color='red',
                    arrowprops=dict(arrowstyle='->', color='red'))
axes[1, 2].set_title('阻尼振荡', fontsize=13, fontweight='bold')
axes[1, 2].set_xlabel('时间 t')
axes[1, 2].set_ylabel('振幅')
axes[1, 2].legend(loc='upper right')
axes[1, 2].grid(True, alpha=0.2)

# ============================================================
# 第五部分：全局修饰（作用于整个 Figure）
# ============================================================
fig.suptitle('数据分析可视化报告（2026年8月）', fontsize=16, fontweight='bold', y=0.98)
# suptitle 是整个画布的总标题，区别于每个子图的 set_title

# 自动调整子图间距，防止标题/标签重叠
fig.tight_layout(rect=[0, 0, 1, 0.95])
# rect=[0,0,1,0.95] 表示子图区域占画布下方95%，上方5%留给 suptitle

# ============================================================
# 第六部分：保存文件（必须在 plt.show() 之前！）
# ============================================================
# 保存为 PNG（位图，适合PPT/网页）
fig.savefig('multi_subplot_report.png', dpi=300, bbox_inches='tight', facecolor='white')

# 保存为 SVG（矢量图，适合论文/无损缩放）
fig.savefig('multi_subplot_report.svg', bbox_inches='tight', facecolor='white')

# 保存为 PDF（矢量图，适合打印/学术投稿）
fig.savefig('multi_subplot_report.pdf', bbox_inches='tight', facecolor='white')

print("✅ 图片已保存：multi_subplot_report.png / .svg / .pdf")

# ============================================================
# 第七部分：显示窗口（放在最后！）
# ============================================================
plt.show()

# ============================================================
# 第八部分：释放资源（批量绘图时必须）
# ============================================================
plt.close(fig)  # 关闭该 Figure，释放内存