from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from core.services import get_students_by_sex, calc_fibonacci


def student_delete_action(request, student_id):
    stu = None
    try:
        stu = Student.objects.get(id=student_id)
    except Student.DoesNotExists:
        return JsonResponse({'errmsg': '不存在的记录'})

    try:
        stu.user.delete()
    except Exception as err:
        # 记录log 收集到 sentry等告警平台
        return JsonResponse({'errmsg': '删除失败，服务器异常'})
    else:
        return JsonResponse({'errmsg': '删除成功'})


def student_detail_view(request, student_id):
    if request.method == 'DELETE':
        return student_delete_action(request, student_id)
    else:
        return JsonResponse({'errmsg': 'request method not allowed'})


def student_view(request, sex):
    if sex not in(1, 2):
        return JsonResponse({'errmsg': '请输入正确的性别参数'})

    qs = list(get_students_by_sex(sex))

    retdata = {'data': qs}

    return JsonResponse(retdata)


@login_required
def fibnacci_view(request, number):
    result = calc_fibonacci(number)

    retdata = {'calc_result': result}

    return JsonResponse(retdata)
