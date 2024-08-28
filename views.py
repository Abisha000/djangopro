from django.shortcuts import render,redirect
from app.forms import Imageform
from app.models import Image
# Create your views here.
def index (request,*args,**kwargs):
    if request.method=='POST':
        form =Imageform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=Imageform()
    return render(request,'index.html',{'form':form})
def home(request):
    return render(request,"home.html")
# from django.shortcuts import render
# from .models import Files  # Assuming Files is a Django model you've defined

# def myfile(request):
#     new_urls = []

#     if request.method == "POST":
#         files = request.FILES.getlist('files')

#         for file in files:
#             new_file = Files(file=file)
#             new_file.save()
#             new_urls.append(new_file.file.url)  # Assuming 'file' is the FileField in Files model

#     return render(request, 'file.html', {'new_urls': new_urls})

