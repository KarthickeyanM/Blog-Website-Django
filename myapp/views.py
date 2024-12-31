from django.shortcuts import render

def custom_page_not_found(request,exception):

    return render(request,'404.html',status=404)

def error_500(request):
    return render(request,'500.html',status=500)