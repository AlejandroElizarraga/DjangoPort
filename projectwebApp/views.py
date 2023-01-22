from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,'portfolio/index.html')

def contacto(request):

    if request.method=='POST':
        
        return render(request, 'portfolio/contacto.html')
    
    return render(request,'portfolio/index.html')