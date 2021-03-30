from django.shortcuts import render
from django.http.response import StreamingHttpResponse,HttpResponse
from stream.camara import VideoCamera
from django.views.decorators import gzip

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@gzip.gzip_page
def livecam_feed(request):
    try:
        cam = VideoCamera()
        if cam.disponible:
            return StreamingHttpResponse(gen(cam),content_type="multipart/x-mixed-replace;boundary=frame")
        else:
            return HttpResponse("Camara se encuentra ocupada")
    except:
        pass


def principal(request):
    return render(request,"stream/VistaPrincipal.html",{})