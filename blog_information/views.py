from django.shortcuts import render


# Create your views here.
def about_me(request):
    return render(request, 'pages/about_me.html')
