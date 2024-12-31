from typing import Any
from django.core.management.base import BaseCommand
from blog.models import Category

class Command(BaseCommand):
    help = "this command helps to feed data to database"

    def handle(self,*args: Any, **options: Any):
        # to delete the existing data before populating again
        Category.objects.all().delete()

        categories = ['sports', 'Technology' , 'Science' , 'Art', 'Food']

        for category in categories:
            Category.objects.create(name = category)
        
        self.stdout.write(self.style.SUCCESS("Categories are successfully added to the categories table"))