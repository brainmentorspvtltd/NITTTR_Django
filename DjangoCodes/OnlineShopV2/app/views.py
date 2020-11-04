from django.shortcuts import render
import json
import urllib.request as url

path = "https://raw.githubusercontent.com/brainmentorspvtltd/NITTTR_Django/main/data.json"
res = url.urlopen(path)
data = json.load(res)
products = data['products']

def index(req):
    return render(req, 'index.html', context={'products':products})

def product(req,pk):
    data = []
    for i in range(len(products)):
        if pk == 1:
            if products[i]['p_category'] == 'laptop':
                data.append(products[i])
        elif pk == 2:
            if products[i]['p_category'] == 'mobile':
                data.append(products[i])
    return render(req, 'products.html', {'products':data})