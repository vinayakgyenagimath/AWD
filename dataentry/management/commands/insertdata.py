from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
  help = "insert the data to database"
  
  
  def handle(self,*args,**kwargs):
    
    dataset = [
      {"roll_no":2,"name":"blinkitti" , "age":28},
      {"roll_no":5,"name":"laxmi" , "age":55},
      {"roll_no":4,"name":"gurubasayya" , "age":60},
    ]
    
    for data in dataset:
      existing_record = Student.objects.filter(roll_no = data['roll_no']).exists()
      if not existing_record:
        db_inserted = Student.objects.create(roll_no = data['roll_no'] ,name=data['name'], age=data['age'])
        print(db_inserted)
        self.stdout.write(self.style.SUCCESS("Inserted data successfully"))
      else:
        self.stdout.write(self.style.WARNING(f"student with roll no {data['roll_no']} is already exists in database"))
        
      