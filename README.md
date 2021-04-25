# spider

## 环境
- 语言：`python(3.9)`
- 解析器包： `requests-html

  安装命令：`pip install requests-html`

- 本地网页代理包： `requests_file`

  安装命令：`pip install requests_file`

- 导出 `Excel` 包： `xlwt`

  安装命令：`pip install xlwt`

## 目录
#### 1. writable 暂时保存网页的文件夹
#### 2. output 输出 `.xlsx` 的文件夹

---
## 一些网页相关的爬虫脚本

- 食品添加剂：http://db.foodmate.net/2760-2014//index.php?m=additives&a=index。（中文名称、英文名称、功能、食品名称、最大使用量(g/kg)）

- 加工助剂：http://db.foodmate.net/2760-2014//index.php?m=processing_aids&a=index（中文名称、英文名称、功能、使用范围）

- 酶制剂：http://db.foodmate.net/2760-2014//index.php?m=enzyme&a=index（中文名称、英文名称、来源、供体）

- 天然香精香料：http://db.foodmate.net/2760-2014//index.php?m=spices&a=search&b=2（中文名称、英文名称）

- 合成香料：http://db.foodmate.net/2760-2014//index.php?m=spices&a=search&b=3（中文名称、英文名称）