
from django.core.management.base import BaseCommand, CommandError
# from dataentry.models import Student
import csv
from django.apps import apps
from django.db.utils import DataError

class Command(BaseCommand):
  help = "import csv file and write it to the database"
  
  def add_arguments(self, parser):
    parser.add_argument("file_path" , type=str ,help = "csv file path" )
    parser.add_argument("model_name" ,type=str,help="database table name")
    
  
  
  def handle(self,*args,**kwargs):
    
    filepath = kwargs['file_path']
    model_name=kwargs['model_name'].capitalize()
    print("model name is printing "+model_name)
    # will get the metadata of the apps
    model = None
    for i in apps.get_app_configs():
      try:
        
        model = apps.get_model(i.label,model_name)
        break
      except LookupError:
        continue
      
    if not model:
      raise CommandError(f'Model {model_name} not found in any app')
    
    model_fields = [f.name for f in model._meta.get_fields() if f.name != 'id']
    print(model_fields,"model_fields")
    with open(filepath,'r') as file:
      reader = csv.DictReader(file)
      csv_fields= reader.fieldnames
      print(csv_fields,"csv_fileds")
      if model_fields != csv_fields:
        raise DataError(f'csv file fields doesnot match with {model_name} fields')
      for row in reader:
         model.objects.create(**row)
    self.stdout.write(self.style.SUCCESS("imported and inserted sucessfully"))
  
  
