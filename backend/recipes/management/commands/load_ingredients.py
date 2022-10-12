import json
import os

from django.core.management.base import BaseCommand, CommandError

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Загружает данные об ингредиентах в бд'

    def add_arguments(self, parser):
        parser.add_argument('filename', default='ingredients.json', type=str)

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']
        try:
            with open(
                os.path.join('data/', filename), encoding='utf-8'
            ) as file:
                data = json.load(file)

            if filename.split('.')[0] == 'ingredients':
                for item in data:
                    Ingredient.objects.get_or_create(
                        name=item.get('name'),
                        measurement_unit=item.get('measurement_unit')
                    )
        except FileNotFoundError:
            raise CommandError(f'Файл {filename} отсутствует в каталоге data')
