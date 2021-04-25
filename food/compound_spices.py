import codecs
from requests_html import HTMLSession
from requests_file import FileAdapter

# 读取本地的网页
file_path = 'writable/food/compound_spices.html'
# file 代理的路径
pwd = 'Users/niejingfa/Documents/spider/'
# 输出的文件
output = 'output/food/compound_spices.csv'

def parsing_html(url):
  session = HTMLSession()
  session.mount('file://', FileAdapter())
  r = session.get(url)
  sel = 'table.layer_big > tr > td'
  items = r.html.find(sel)

  f = codecs.open(output, 'w', encoding='utf-8')
  f.write('中文名称,英文名称\n')
  for i in range(int(len(items) / 7)):
    f.write(','.join([items[i * 7 + 1].text, items[i * 7 + 2].text]))
    f.write('\n')

  f.close()

if __name__ == '__main__':
  url = 'file:///' + pwd + file_path
  parsing_html(url)
