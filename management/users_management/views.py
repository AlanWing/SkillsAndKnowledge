import json

from django.db.models import Count
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from users_management.models import UserInfo, Access
import pandas as pd


# 登录
def auth_login(request):
    username = request.GET.get("username", "")
    password = request.GET.get("password", "")
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        access = Access.objects.get(account=username)
        return JsonResponse({"code": 0, "data": access.access})
    else:
        return JsonResponse({"code": 1, "data": "登录失败"})


# 登出
def auth_logout(request):
    logout(request)
    return JsonResponse({
        "code": 0,
        "data": "登出成功"
    })


def auth_register(request):
    username = request.GET.get("username")
    password = request.GET.get("password")
    try:
        User.objects.create_user(username=username, password=password)
    except:
        return JsonResponse({
            "code": 1,
            "data": "用户已存在"
        })
    return JsonResponse({
        "code": 0,
        "data": "注册成功"
    })


def group_by_inspection(request):
    if not request.user.is_active:
        return JsonResponse({
            "code": 1,
            "data": "未登录"
        })
    before = UserInfo.objects.filter(annual_survey_date__lt="2020-01-01")
    after = UserInfo.objects.filter(annual_survey_date__gte="2020-01-01")
    response = {
        "code": 0,
        "data": {
            "before": before.__len__(),
            "after": after.__len__()
        }
    }
    return JsonResponse(response)


def group_by_district(request):
    username = request.user.username
    access = Access.objects.get(account=username).access
    if access == "省级":
        data = list(UserInfo.objects.values("city").annotate(count=Count("id")))
    elif access == "市级":
        city = Access.objects.get(account=username).city
        data = list(UserInfo.objects.values("district").filter(city=city).annotate(count=Count("id")))
    else:
        return JsonResponse({"code": 0, "data": "当前权限无法显示"})
    return JsonResponse({"code": 0, "data": data})


def group_by_class(request):
    username = request.user.username
    access = Access.objects.get(account=username)
    if access.access == "省级":
        data = list(UserInfo.objects.values("instructor_class").annotate(count=Count("id")))
    elif access.access == "市级":
        city = access.city
        data = list(UserInfo.objects.values("instructor_class").filter(city=city).annotate(count=Count("id")))
    else:
        district = access.province
        data = list(UserInfo.objects.values("instructor_class").filter(village=district).annotate(count=Count("id")))
    return JsonResponse({"code": 0, "data": data})


def group_by_verification(request):
    username = request.user.username
    access = Access.objects.get(account=username)
    if access.access == "省级":
        data = list(UserInfo.objects.values("ver_status").annotate(count=Count("id")))
    elif access.access == "市级":
        city = access.city
        data = list(UserInfo.objects.values("ver_status").filter(city=city).annotate(count=Count("id")))
    else:
        district = access.province
        data = list(UserInfo.objects.values("ver_status").filter(village=district).annotate(count=Count("id")))
    return JsonResponse({"code": 0, "data": data})


def group_by_gender(request):
    username = request.user.username
    access = Access.objects.get(account=username)
    if access.access == "省级":
        data = list(UserInfo.objects.values("sex").annotate(count=Count("id")))
    elif access.access == "市级":
        city = access.city
        data = list(UserInfo.objects.values("sex").filter(city=city).annotate(count=Count("id")))
    else:
        district = access.province
        data = list(UserInfo.objects.values("sex").filter(village=district).annotate(count=Count("id")))
    return JsonResponse({"code": 0, "data": data})


def group_by_type(request):
    username = request.user.username
    access = Access.objects.get(account=username)
    if access.access == "省级":
        data = list(UserInfo.objects.values("instructor_type").annotate(count=Count("id")))
    elif access.access == "市级":
        city = access.city
        data = list(UserInfo.objects.values("instructor_type").filter(city=city).annotate(count=Count("id")))
    else:
        district = access.province
        data = list(UserInfo.objects.values("instructor_type").filter(village=district).annotate(count=Count("id")))
    return JsonResponse({"code": 0, "data": data})


def group_by_age(request):
    username = request.user.username
    access = Access.objects.get(account=username)
    if access.access == "省级":
        first = UserInfo.objects.filter(age__lt=20).__len__()
        second = UserInfo.objects.filter(age__gte=20, age__lte=50).__len__()
        third = UserInfo.objects.filter(age__gt=50).__len__()
    elif access.access == "市级":
        city = access.city
        first = UserInfo.objects.filter(city=city, age__lt=20).__len__()
        second = UserInfo.objects.filter(city=city, age__gte=20, age__lte=50).__len__()
        third = UserInfo.objects.filter(city=city, age__gt=50).__len__()
    else:
        district = access.province
        first = UserInfo.objects.filter(village=district, age__lt=20).__len__()
        second = UserInfo.objects.filter(village=district, age__gte=20, age__lte=50).__len__()
        third = UserInfo.objects.filter(village=district, age__gt=50).__len__()
    data = {"<20": first, "20-50": second, "<50": third}
    return JsonResponse({"code": 0, "data": data})


# 获取权限下的所有用户
# def all_users(request):
#     username = request.user.username
#     access = Access.objects.get(account=username)
#     res = {"code": 0, "data": []}
#     if access.access == "省级":
#         cities = UserInfo.objects.values("city").annotate(count=Count("id"))
#         for i in cities:
#             data = {i["city"]: []}
#             districts = UserInfo.objects.values("village").filter(city=i["city"]).annotate(count=Count("id"))
#             for j in districts:
#                 dis = []
#                 users = UserInfo.objects.filter(village=j["village"])
#                 for u in users:
#                     dis[j["village"]].append([{"name":u.name,"age": u.age}])
#                 data[i["city"]].append({j["village"]:dis})
#             res["data"].append(data)
#         return JsonResponse(res)
# elif access.access == "市级":

# def user_information(request):
#     username = request.user.objects.get("username")
#     access = Access.objects.get(account=username).access
#     if access == "省级":
#         # users = UserInfo.objects.all().order_by("province")
#         pass
# 获取
def regions(request):
    username = request.user.username
    access = Access.objects.get(account=username)
    res = {"code": 0, "data": {}}
    if access.access == "省级":
        cities = UserInfo.objects.values("city").annotate(count=Count("id"))
        for i in cities:
            districts = UserInfo.objects.values("village").filter(city=i["city"]).annotate(count=Count("id"))
            district_list = []
            for j in districts:
                district_list.append(j["village"])
            res["data"][i["city"]] = district_list
    elif access.access == "市级":
        city = access.city
        districts = [i["village"] for i in
                     UserInfo.objects.values("village").filter(city=city).annotate(count=Count("id"))]
        res["data"][city] = districts
    else:
        city = access.city
        district = access.district
        res["data"][city] = district
    return JsonResponse(res)


# 返回指定区域用户
def users(request):
    city = request.GET.get("city", "")
    district = request.GET.get("district", "")
    if city and district:
        users = UserInfo.objects.filter(city=city, village=district)
        users_dic = {}
        for u in users:
            users_dic.setdefault(u.id,
                                 {"name": u.name, "sex": u.sex, "age": u.age, "height": u.height, "weight": u.weight,
                                  "address": u.address, "id_number": u.id_number, "tel": u.tel, "edu":u.edu_background,
                                  "is_ins": "是" if u.is_instructor else "否","class": u.instructor_class,"city": u.city,
                                  "type": u.instructor_type,"ver_status": u.ver_status, "province": u.province,
                                  "village": u.village, "certi_num": u.certificate_num, "certi_date":u.certificate_date,
                                  "gym": u.gym, "assessment": u.assessment,"upload_time": u.upload_time,
                                  "annual_survey_date": str(u.annual_survey_date)})
    else:
        access = Access.objects.get(account=request.user.username).access
        if access == "省级":
            pass

        # 返回
