import time
import xlwt #导入模块
import codecs
from requests_html import HTMLSession
from requests_file import FileAdapter

# 读取本地的网页
file_path = 'writable/food/additive.html'
# file 代理的路径
pwd = 'Users/niejingfa/Documents/spider/'
# 输出的文件
output = 'output/food/additive.xlsx'

def parsing_html(url):
  session = HTMLSession()
  session.mount('file://', FileAdapter())
  r = session.get(url)
  sel1 = 'table#scroll_bar >tr.py2 > td > a'
  items = r.html.find(sel1)

  sel2 = 'table#scroll_bar >tr.py2 > td'
  arr = r.html.find(sel2)

  wb = xlwt.Workbook()
  ws = wb.add_sheet('sheet1')
  ws.write(0, 0, '中文名称')
  ws.write(0, 1, '英文名称')
  ws.write(0, 2, '功能')
  ws.write(0, 3, '食品名称')
  ws.write(0, 4, '最大使用量(g/kg)')
  count = 1
  for i, item in enumerate(items):
    _href = item.attrs['href']
    item_arr = get_html(_href)

    for j in range(len(item_arr)):
      ws.write(count, 0, item.text)
      ws.write(count, 1, arr[i * 5 + 1].text)
      ws.write(count, 2, arr[i * 5 + 4].text)
      ws.write(count, 3, item_arr[j]['name'])
      ws.write(count, 4, item_arr[j]['max'])
      count += 1

    time.sleep(1)

  wb.save(output)

def get_html(url):
  session = HTMLSession()
  r = session.get(url)
  r.encoding = 'utf-8'
  sel = 'table#scroll_bar > tr > td'
  items = r.html.find(sel)

  arr = []
  for i in range(int(len(items) / 4)):
    arr.append({'name': items[i * 4 + 1].text, 'max': items[i * 4 + 2].text})

  return arr


if __name__ == '__main__':
  url = 'file:///' + pwd + file_path
  parsing_html(url)