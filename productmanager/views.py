from django.shortcuts import render
from .models import Product, Review
from .forms import ProductForm

# Create your views here.
def browse(request):
    q = request.GET.get('q')
    if q:
        products = Product.objects.filter(name__icontains=q)
        print(products)
    else:
        products = Product.objects.all()
    context = {'products': products}
    return render(request, 'productmanager/browse.html', context)

def details(request, id):
    # print(id)
    productData = Product.objects.get(id=id)
    reviews = Review.objects.filter(product=id)
    context = {'productData' : productData, 'reviews' : reviews}
    return render(request, 'productmanager/details.html', context)

def addProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        print(request.POST)
    context = {'form' : form}
    return render(request, 'productmanager/add-product.html', context)

def submitReview(request):
    if request.method == 'POST':
        review = Review()
        # id = request.for
        review.product = Product.objects.get(id=id)
        review.rating = request.POST['rating']
        review.save()
        return details(request, id)
    
    return details(request, id)