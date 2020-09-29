from django.test import TestCase
# Create your tests here.
import os, django
os.environ['DJANGO_SETTINGS_MODULE'] = 'management.settings'
django.setup()
from users_management.models import UserInfo, Access
from django.db.models import Sum, Count

users = UserInfo.objects.all()
# for i in users:
#     print(i.)
# print(UserInfo.objects.filter(age__lt=30))


# city = "太原市"
# first = UserInfo.objects.filter(city=city,age__lt=20).__len__()
# second = UserInfo.objects.filter(city=city,age__lt=50,age__gt=20).__len__()
# third = UserInfo.objects.filter(city=city,age__gt=50).__len__()
# data = {"<20": first, "20-50": second, "<50": third}

# district = "小店区"
# first = UserInfo.objects.filter(village=district, age__lt=20).__len__()
# second = UserInfo.objects.filter(village=district, age__gte=20,age__lte=50).__len__()
# third = UserInfo.objects.filter(village=district, age__gt=50).__len__()
# data = {"<20": first, "20-50": second, "<50": third}
# print(data)

# print(list(UserInfo.objects.values("instructor_type").filter(city="太原市").annotate(count=Count("id"))))
# from django.db import connection
# cursor = connection.cursor()
# cursor.execute("select city from userinfo group by city")
# print(cursor.fetchall())UserInfo.objects.values("city").filter(city=i["city"]).annotate(count=Count("id"))

# print(UserInfo.objects.values("city").annotate(count=Count("id")))

# res = {
#     "code":0,
#     "data":[]
# }
# users = UserInfo.objects.filter(city="太原市", village="小店区")
# users_dic = {}
# for u in users:
#     users_dic.setdefault(u.id,
#                          {"name": u.name, "sex": u.sex, "age": u.age, "height": u.height, "weight": u.weight,
#                           "address": u.address, "id_number": u.id_number, "tel": u.tel, "edu": u.edu_background,
#                           "is_ins": "是" if u.is_instructor else "否", "class": u.instructor_class, "city": u.city,
#                           "type": u.instructor_type, "ver_status": u.ver_status, "province": u.province,
#                           "village": u.village, "certi_num": u.certificate_num, "certi_date": u.certificate_date,
#                           "gym": u.gym, "assessment": u.assessment, "upload_time": u.upload_time,
#                           "annual_survey_date": str(u.annual_survey_date)})
# print(users_dic)
user = UserInfo.objects.get(id=1)
user.annual_survey_date = "2020-09-08"
user.save()


