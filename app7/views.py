from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage

# Create your views here.
def img_upld(request):
    file_url=False
    if request.method=="POST" and request.FILES:
        image=request.FILES['sam']
        fs=FileSystemStorage()
        file=fs.save(image.name,image)
        file_url=fs.url(file)
    return render(request,"img_upload.html",context={'file_url':file_url})
