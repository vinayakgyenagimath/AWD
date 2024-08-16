from django.core.management.base import BaseCommand
import csv
from dataentry.models import Student
import datetime
from django.apps import apps



class Command(BaseCommand):
  help ="export the data form db table to csv"
  print("okkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
  
  def add_arguments(self,parser):
    parser.add_argument("model_name" ,type=str,help="model name")
  
  print("KKKKKKKKKKKKKKKKKKKKKKKKkkkkkkkkkkkkkkkkkdddddddddddd")
  
  def handle(self,*args,**kwargs):
    
    model_name = kwargs['model_name']
    model= None
    for i in apps.get_app_configs():
      try:
        model =apps.get_model(i.label,model_name)
        break
      except:
        pass
      
    if not model:
      self.stderr.write(f'model {model_name} is not found')
      return
      
    data = model.objects.all()
    timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    filepath = f'exported {model_name}_data_{timestamp}.csv'
    
    with open(filepath ,"w",newline='') as file:
      writer = csv.writer(file)
      writer.writerow([field.name for field in model._meta.fields])
      for dt1 in data:
        writer.writerow([getattr(dt1,f.name) for f in model._meta.fields])
        # print(dt1)
      self.stdout.write(self.style.SUCCESS("Exported to csv succesfully"))
      
    
    
  # 
    
    # data = model.objects.all()
    
    
    
    # timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    # file_path = f"exported_{model_name}_data_{timestamp}.csv"
    
    # with open(file_path ,"w",newline="") as file :
    #   writer =csv.writer(file)
    #   writer.writerow([field.name for field in model._meta.fields])
      
    #   for dt in data:
    #     writer.writerow([dt])
    
    
    
    
    
    