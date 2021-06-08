from django.http.response import Http404, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse

from shopping.models import Product  # モデルをインポート

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

def product_cart(request):
    cart = request.session.get('cart')
    if cart:
        products = []
        for product_id in cart:
            try:
                products.append(Product.objects.get(id=product_id))
            except Product.DoesNotExist:
                pass
    else:
        products = []

    total_price = 0
    for product in products:
        total_price += product.price

    return TemplateResponse(request, 'shopping/product_cart.html', {'products': products, 'total_price': total_price})

def cart_add(request, product_id):
    if not Product.objects.filter(id=product_id).exists():
        raise Http404
    cart = request.session.get('cart')
    if cart:
        cart.append(product_id)
        request.session['cart'] = cart
    else:
        request.session['cart'] = [product_id]
    return HttpResponseRedirect(reverse('product_list'))

def cart_delete(request, product_id):
    if not Product.objects.filter(id=product_id).exists():
        raise Http404
    cart = request.session.get('cart')
    if cart:
        filtered = []
        for p in cart:
            if p != product_id:
                filtered.append(p)
        request.session['cart'] = filtered
    return HttpResponseRedirect(reverse('product_cart'))