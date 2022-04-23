from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.hashers import make_password

from faker import Faker

from django.contrib.auth.models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('num', nargs='+', type=int)

    def handle(self, *args, **options):
        number = options.get('num')[0]
        if number is None:
            number = 5
        password = make_password('123456')
        faker = Faker(locale="zh_CN")
        for _ in range(int(number)):
            data = {
                'username': faker.name_male(),
                'password': password,
                'is_superuser': False,
            }
            try:
                User.objects.create(
                    **data
                )
                User.save()
            except:
                CommandError('创建失败！')
            self.stdout.write(self.style.SUCCESS('Successfully create user "%s"' % faker.name_male()))
