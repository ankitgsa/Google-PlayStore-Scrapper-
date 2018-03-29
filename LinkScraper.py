import requests
import time
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
category = "EDUCATION"
targetURL = 'https://play.google.com/store/apps/category/'+category+'/collection/topselling_new_free'
head = 'https://play.google.com'


def getAppLink(url, num):
    app_item = []
    rs = requests.session()
    formdata = {
        'start': num,
        'num': 120
    }
    res = rs.post(url, data=formdata, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    item_head = category
    for data in soup.select('.id-card-list .card'):
        app_data = head + data.find('a')['href']
        app_item.append(app_data)
    return app_item

def writeURL(urls):
    thefile = open('education.txt', 'w')
    for item in urls:
        thefile.write("%s\n" % item)




if __name__ == '__main__':
    tStart = time.time()
    print('Gathering ' + category + ' app links')
    app_data_list = []
    for num in range(0, 600, 120):
        app_data_list += getAppLink(targetURL, num)
        print(num)
    tEnd = time.time()
    print('Feteched'+str(len(app_data_list))+'   in'.format(round(tEnd - tStart, 2)))
    print('Writing to Text File')
    writeURL(app_data_list)
    print('DONE')