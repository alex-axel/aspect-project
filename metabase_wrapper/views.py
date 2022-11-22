from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse, JsonResponse
from .models import SOFile

# Create your views here.

class MainView(TemplateView):
    template_name = 'metabase_wrapper/main.html'


class UploadStartView(ListView):
    model = SOFile
    template_name = 'metabase_wrapper/upload_start.html'



def file_upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')
        SOFile.objects.create(filename=uploaded_file.name, upload=uploaded_file)
        return HttpResponse('upload')
    
    return JsonResponse({'error': 'only post method available for this url'})
