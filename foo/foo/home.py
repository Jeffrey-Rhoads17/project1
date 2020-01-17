from django.shortcuts import get_object_or_404, render

def homeView(request):
    return render(request, "foo/home.html")
