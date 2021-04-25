import codecs
from requests_html import HTMLSession
from requests_file import FileAdapter

# 读取本地的网页
file_path = 'writable/food/enzyme.html'
# file 代理的路径
pwd = 'Users/niejingfa/Documents/spider/'
# 输出的文件
output = 'output/food/enzyme.csv'

def parsing_html(url):
  session = HTMLSession()
  session.mount('file://', FileAdapter())
  r = session.get(url)
  sel = 'table#scroll_bar >tr > td'
  items = r.html.find(sel)

  f = codecs.open(output, 'w', encoding='utf-8')
  f.write('中文名称,英文名称,来源,供体\n')
  for i in range(int(len(items) / 5)):
    item_group = items[i * 5 : i * 5 + 4]
    text_arr = []
    for _item in item_group:
      text_arr.append(_item.text)

    f.write(','.join(text_arr))
    f.write('\n')

  f.close()

if __name__ == '__main__':
  url = 'file:///' + pwd + file_path
  parsing_html(url)