import codecs
import xlwt #导入模块
from requests_html import HTMLSession
from requests_file import FileAdapter

# 读取本地的网页
file_path = 'writable/food/natural_spices.html'
# file 代理的路径
pwd = 'Users/niejingfa/Documents/spider/'
# 输出的文件
output = 'output/food/natural_spices.xlsx'

def parsing_html(url):
  session = HTMLSession()
  session.mount('file://', FileAdapter())
  r = session.get(url)
  sel = 'table.layer_big > tr > td'
  items = r.html.find(sel)

  wb = xlwt.Workbook()
  ws = wb.add_sheet('sheet1')
  ws.write(0, 0, '中文名称')
  ws.write(0, 1, '英文名称')
  for i in range(int(len(items) / 7)):
    ws.write(i + 1, 0, items[i * 7 + 1].text)
    ws.write(i + 1, 1, items[i * 7 + 2].text)

  wb.save(output)

if __name__ == '__main__':
  url = 'file:///' + pwd + file_path
  parsing_html(url)