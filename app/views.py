from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':10000,'b':4000,'c':600}
    return render(request,'condition.html',context=d)