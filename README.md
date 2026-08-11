# GitHub 热门 Python 仓库分析工具
>拉取Github数据，使用pandas分析，matplotlib出图，logging记入日志

## 功能列表
```
fetcher     获取数据
analyzer    分析数据
visualizer  数据可视化
```

## 快速开始

### 本地部署

#### 克隆仓库
```

git clone https://github.com/ZYaHui-czm/Project_one.git

```

#### 安装依赖
```
pip install -r requirements.txt
```

#### 配置变量（可选）
```
cp .env.example .env
```
编辑'.env'
```env
GITHUB_TOKEN = xxx

#### 运行项目
```
python -m main