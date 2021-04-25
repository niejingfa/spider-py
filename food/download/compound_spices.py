import requests
import codecs

file_path = 'writable/food/compound_spices.html'

def get_html(url):
  user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
  headers = {'User-Agent': user_agent}
  html = requests.get(url, headers = headers)
  html.encoding = 'utf-8'
  file = codecs.open(file_path, 'w', encoding='utf-8')
  file.write(html.text)
  file.close()

if __name__ == '__main__':
  url = "http://db.foodmate.net/2760-2014//index.php?m=spices&a=search&b=3"
  get_html(url)