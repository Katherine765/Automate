import bs4
import os
import requests
url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    result = requests.get(url)
    result.raise_for_status()
    soup = bs4.BeautifulSoup(result.text) # result.text is html
    element = soup.select('#comic img')[0]
    if element:
        imgUrl = 'http:' + element.get('src')
        result = requests.get(imgUrl)
        result.raise_for_status()
        with open(os.path.join('xkcd', os.path.basename(imgUrl)), 'wb') as imgFile: # imgUrl ex. '...comics/artificial_gravity.png and basename works on that
            for chunk in result.iter_content(100000):
                imgFile.write(chunk)
        
    url = 'http://xkcd.com' +  soup.select('a[rel="prev"]')[0].get('href') #href="/3110/"


print('done')