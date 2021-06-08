from django.http.response import Http404
from django.shortcuts import render

from django.template.response import TemplateResponse
from shopping.models import Product   #モデルをインポート

#インポートしたモデルからデータを取得して返す、product_listというview関数
def product_list(request):
    products = Product.objects.order_by('name')
    return TemplateResponse(request, 'shopping/product_list.html', {'products': products})

def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)        
    except Product.DoesNotExist:
        raise Http404
    return TemplateResponse(request, 'shopping/product_detail.html', {'product': product})

