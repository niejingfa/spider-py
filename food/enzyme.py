import codecs
import xlwt #导入模块
from requests_html import HTMLSession
from requests_file import FileAdapter

# 读取本地的网页
file_path = 'writable/food/enzyme.html'
# file 代理的路径
pwd = 'Users/niejingfa/Documents/spider/'
# 输出的文件
output = 'output/food/enzyme.xlsx'

def parsing_html(url):
  session = HTMLSession()
  session.mount('file://', FileAdapter())
  r = session.get(url)
  sel = 'table#scroll_bar >tr > td'
  items = r.html.find(sel)

  wb = xlwt.Workbook()
  ws = wb.add_sheet('sheet1')
  ws.write(0, 0, '中文名称')
  ws.write(0, 1, '英文名称')
  ws.write(0, 2, '来源')
  ws.write(0, 3, '供体')
  for i in range(int(len(items) / 5)):
    ws.write(i + 1, 0, items[i * 5].text)
    ws.write(i + 1, 1, items[i * 5 + 1].text)
    ws.write(i + 1, 2, items[i * 5 + 2].text)
    ws.write(i + 1, 3, items[i * 5 + 3].text)

  wb.save(output)

if __name__ == '__main__':
  url = 'file:///' + pwd + file_path
  parsing_html(url)