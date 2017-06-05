from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.conf import settings
from django.shortcuts import render_to_response, render , redirect
import qrcode


def index(request):
    student_list = Student.objects.all()
    return render(request, 'index.html', {'student_list': student_list})

def detail(request, id):
    student_list = Student.objects.all().filter(id=id)
    print student_list

    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=2,
    )

    qr.add_data(student_list)                                      ## Add data
    qr.make(fit=True)
    qr.format = "PNG"                                              ## format
    qr_image = qr.make_image()                                     ## make image

    # qr_image.show();                                             ## show image
    qr_image.save(settings.MEDIA_ROOT+"/qrcode_image/"+id+".png")  ## save in media
    # qr_image.save(id+".png")                                     ## save in src


    return render(request, 'detail.html', {'id': id,'student_list': student_list})
