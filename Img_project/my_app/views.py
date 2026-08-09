from django.shortcuts import render
from PIL import Image
from rembg import remove
import os
import random
from django.conf import settings
# Create your views here.
def home(request):
    return render(request,'my_app/home.html')
def contact(request):
    return render(request,'my_app/contact.html')
def gallery(request):
    return render(request,'my_app/gallery.html')
def bgremove(request):
    data=None
    if request.method == "POST" and request.FILES:
        file=request.FILES['file']
        open_img=Image.open(file)
        op=remove(open_img)
        filename=f'rem_{random.randint(1,9999)}.png'
        os.makedirs(os.path.join(settings.MEDIA_ROOT,'removebg'),exist_ok=True)
        img_path=os.path.join(settings.MEDIA_ROOT,'removebg',filename)
        op.save(img_path)

        data=settings.MEDIA_URL + 'removebg/'+ filename


    return render(request,'my_app/bgremove.html',{'data':data})
def about(request):
    return render(request,'my_app/about.html')