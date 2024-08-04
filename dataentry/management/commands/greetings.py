from django.core.management.base import BaseCommand, CommandParser


# prposed command = python manage.py greetings name
# proposed output = "hello name , good morning"

class Command(BaseCommand):
  
  def add_arguments(self, parser):
    parser.add_argument("name",type=str,help="specify the user")
    
    
  help ="greetings of the day"
  
  def handle(self,*args,**kwargs):
    name=kwargs['name']
    greeting =f'hello {name} , howwzz you'
    self.stdout.write(self.style.ERROR(greeting))