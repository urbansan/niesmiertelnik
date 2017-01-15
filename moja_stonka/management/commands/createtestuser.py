from django.core.management.base import BaseCommand, CommandError
import os

class Command(BaseCommand):
    help = "My test command"

    # def add_arguments(self, parser):
    #     parser.add_argument('number_of_users', type=int, 
    #             help = 'give the number of random users you want to generate (max 5000)'
    #     )

    def handle(self, *args, **options):
        os.system("./manage.py createsuperuser --username=test --email=test@test.com")
