from django.shortcuts import render


# Create your views here.
def home_page(request):
    if request.method=='POST':
        return render(request, 'home.html', context={'list_item': request.POST['new_item']})
    else:
        return render(request, 'home.html')
