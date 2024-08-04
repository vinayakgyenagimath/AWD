from typing import Any
from django.core.management.base import BaseCommand


class Command(BaseCommand):
  help = "prints hello world"
  
  # write main logic hea
  def handle(self,*args, **kwargs):
    self.stdout.write("hello world veenayak")
    self.stdout.write("have a good day")
    print("this is print statement")