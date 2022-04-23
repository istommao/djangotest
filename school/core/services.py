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

    return qs
