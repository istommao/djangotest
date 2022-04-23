from django.db.models import F

from core.models import Student


def get_students_by_sex(sex: int):
    qs = Student.objects.filter(
        sex=sex
    ).select_related(
        'user', 'owner_class'
    ).values(
        student_name=F('user__username'),
        class_name=F('owner_class__name')
    )
    print(qs.query)

    return qs


def calc_fibonacci(n):
    l, v = 0, 1
    for i in range(1, n ,2):
        l += v
        v += l
    if n & 1:
        return v
    return l


def fib_generator(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
        yield a


def calc_fibonacci_use_generator(n):
    item = 0
    for i in fib_generator(n):
        item = i
    return item
