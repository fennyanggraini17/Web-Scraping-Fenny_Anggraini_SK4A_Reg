import requests
import csv

key = input('masukkan keyword :')
write = csv.writer(open('hasil/{}.csv'.format(key), 'w', newline=''))
header = ['Nama', 'Harga', 'Stok']
write.writerow(header)

url ='https://api.bukalapak.com/multistrategy-products'

count =0
for page in range(1,11):
    parameter = {
    'keywords': key,
    'limit': 50,
    'offset': 0,
    'facet': True,
    'page': page,
    'shouldUseSeoMultistrategy': False,
    'access_token': 'jzCqLX8aWcaCpO9pVz6UdThQgbKGrSAg8-UnQG8wGD8sLg'
    }

    r = requests.get(url, params=parameter).json()

    products = r['data']
    for p in products:
        nama = p['name']
        harga = p['price']
        stok = p['stock']
        count+=1
        print('No :',count, 'nama :',nama, 'harga:',harga, 'stok :',stok)
        write = csv.writer(open('hasil/{}.csv'.format(key), 'a', newline=''))
        data = [nama, harga, stok]
        write.writerow(data)
