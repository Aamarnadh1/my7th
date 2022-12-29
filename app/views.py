from django.shortcuts import render

# Create your views here.
d={'name':'amar','age':21}
def jinja_html(request):
    return render(request,'jinja_html.html',context=d)
