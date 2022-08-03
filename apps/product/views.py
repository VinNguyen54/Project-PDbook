import random
from django.contrib import messages
from django.shortcuts import redirect, render,get_object_or_404
from django.db.models import Q

from .forms import AddToCartForm
from .models import Category, Product, Review

from apps.cart.cart import Cart

def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'product/search.html', {'products': products, 'query': query})
# Create your views here.
def product(request, category_slug, product_slug):
    cart =  Cart(request)

    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    
    if request.method == 'POST':
        form = AddToCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']

            cart.add(product_id=product.id, quantity=quantity, update_quantity=False)

            messages.success(request, 'The product was added to the cart')

            return redirect('product', category_slug=category_slug, product_slug=product_slug)
    else:
        form = AddToCartForm()

    similar_products = list(product.category.products.exclude(id=product.id))
    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)

    if request.method == 'POST':
        rating  = request.POST.get('rating', 3)
        content = request.POST.get('content', '')

        if content:
            reviews = Review.objects.filter(created_by = request.user, product = product)

            if reviews.count() >0:
                review = reviews.first()
                review.rating = rating
                review.content = content
                review.save()
            else:
                review = Review.objects.create(product = product, rating = rating,content = content, created_by = request.user)

            return redirect('product', category_slug=category_slug, product_slug=product_slug)

    context = {
        'form':form,
        'product': product,
        'similar_products': similar_products,
    }

    return render(request, 'product/product.html', context)

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    return render(request, 'product/category.html', {'category': category})
