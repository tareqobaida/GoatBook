from django.shortcuts import render
from .models import Item


# Create your views here.
def home_page(request):
    if request.method == 'POST':
        item = Item()
        item.text = request.POST['item_text']
        item.save()
        return render(request, 'home.html', context={'new_item_text': request.POST['item_text']})
    else:
        return render(request, 'home.html')
