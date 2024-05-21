from django.shortcuts import render
from django.http import FileResponse, Http404
from django.conf import settings
import os


from .models import Esrog



# Create your views here.



def index(request):
    esrogim = Esrog.objects.all()
    return render(request, 'index.html', {'esrogim': esrogim})


def serve_image(request, image_name):
    file_path = os.path.join("esrogim_images", f"{image_name}.png")
    print(f"{file_path = }")
    return FileResponse(open(file_path, 'rb'), as_attachment=True)