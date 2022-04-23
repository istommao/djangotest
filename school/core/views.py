from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from core.services import get_students_by_sex


def student_view(request, sex):
    if sex not in(1, 2):
        return JsonResponse({'errmsg': '请输入正确的性别参数'})

    qs = list(get_students_by_sex(sex))

    retdata = {'data': qs}

    return JsonResponse(retdata)



def fib_generator(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
        yield a


def calc_fibonacci(n):
    item = 0
    for i in fib_generator(n):
        item = i
    return item


@login_required
def fibnacci_view(request, number):
    result = calc_fibonacci(number)

    retdata = {'calc_result': result}

    return JsonResponse(retdata)
