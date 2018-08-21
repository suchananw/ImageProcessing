import requests
import searchList
import information
import urllib.request
import os

URL = information.URL
API_KEY = information.API_KEY
CX = information.CX
params = 'filter=1&imgType=photo&searchType=image'
search_list = searchList.search100


def saveImage(items, start, name):
  count = start
  dir_name = 'ImageCollection/' + name
  for item in items:
    url = item['link']
    print(url)
    if os.path.exists(dir_name) is False:
      os.mkdir(dir_name)
    try:
      urllib.request.urlretrieve(url, '{}/{}.jpg'.format(dir_name ,count))
      count += 1
    except IOError:
      pass

def getImage(query, start):
  req = requests.get(URL, params={
      'q'   :query,
      'key' :API_KEY,
      'cx'  :CX,
      'filter'  :'1',
      'imgType' :'photo',
      'searchType'  :'image',
      'start'   :start
    })
  res = req.json()
  print (res)
  saveImage(res['items'], start, query)
  return res['queries']['request'][0]['totalResults']

def main():
  for item in search_list[6:]:
    query = item
    start = 1
    totalResult = int(getImage(query, start))
    nextStart = start
    while nextStart+10 < start+100:
      nextStart += 10
      getImage(query, nextStart)

if __name__ == '__main__':
  main()