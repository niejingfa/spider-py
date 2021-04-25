import time
import codecs
from requests_html import HTMLSession
from requests_file import FileAdapter

# 读取本地的网页
file_path = 'writable/food/additive.html'
# file 代理的路径
pwd = 'Users/niejingfa/Documents/spider/'
# 输出的文件
output = 'output/food/additive.csv'

def parsing_html(url):
  session = HTMLSession()
  session.mount('file://', FileAdapter())
  r = session.get(url)
  sel1 = 'table#scroll_bar >tr.py2 > td > a'
  items = r.html.find(sel1)

  sel2 = 'table#scroll_bar >tr.py2 > td'
  arr = r.html.find(sel2)

  f = codecs.open(output, 'w', encoding='utf-8')
  f.write('中文名称,英文名称,功能,食品名称,最大使用量(g/kg)\n')
  for i, item in enumerate(items):
    _href = item.attrs['href']
    item_arr = get_html(_href)

    for item_a in item_arr:
      f.write(','.join([item.text, arr[i * 5 + 1].text, arr[i * 5 + 4].text, item_a['name'], item_a['max']]))
      f.write('\n')

    time.sleep(1)

  f.close()

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