from django.shortcuts import redirect, render, HttpResponse
from .utils import get_all_customs
from upload.models import Upload
from django.conf import settings
from django.contrib import messages

from django.core.management import call_command
# Create your views here.
def import_data(request):
  if request.method =="POST":
    file_path = request.FILES.get('filepath')
    model_name = request.POST.get('modelname')
    print(file_path ,"filepath")
    print(model_name ,"model name")
    Upload_obj = Upload.objects.create(file = file_path , model_name = model_name)
    relative_path =str(Upload_obj.file.url)
    base_url = str(settings.BASE_DIR)
    absolute_path = base_url+relative_path
    print("Absolute path =>",absolute_path)
    try:
      call_command('importdata',absolute_path,model_name)
      messages.success(request,"Data imported Successfully")
    except Exception as e:
      messages.error(request,str(e))
    return redirect('import_data')
    
  else:
    all_models=get_all_customs()
    context ={
      "all_models":all_models,
    }

  return render(request,'dataentry/import.html',context)
