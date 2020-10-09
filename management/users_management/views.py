import time

from django.db.models import Count
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from users_management.models import UserInfo, Access, Moment, FeedBack
from django.core.paginator import Paginator


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

# 用户注册
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


# 根据年检日期分类
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


# 根据地区汇总人口
def group_by_district(request):
    username = request.user.username
    access = Access.objects.get(account=username).access
    if access == "省级":
        data = list(UserInfo.objects.values("city").filter(city__isnull=False).annotate(count=Count("id")))
    elif access == "市级":
        city = Access.objects.get(account=username).city
        data = UserInfo.objects.values("village").filter(city=city,village__isnull=False).annotate(count=Count("id"))
        data = [{"city":i["village"],"count":i["count"]} for i in data]
    else:
        return JsonResponse({"code": 0, "data": "当前权限无法显示"})
    return JsonResponse({"code": 0, "data": data})


# 根据等级分类
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


# 根据审核状态分类
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


# 根据性别分类
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


# 根据指导类型汇总
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


# 根据年龄汇总
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

# 获取市区
def regions(request):
    username = request.user.username
    access = Access.objects.get(account=username)
    res = {"code": 0, "data": {}}
    if access.access == "省级":
        cities = Access.objects.values("city").filter(city__isnull=False).annotate(count=Count("id"))
        for i in cities:
            districts = Access.objects.values("district").filter(city=i["city"],district__isnull=False).annotate(count=Count("id"))
            district_list = []
            for j in districts:
                district_list.append(j["district"])
            res["data"][i["city"]] = district_list
    elif access.access == "市级":
        city = access.city
        districts = [i["district"] for i in
                     Access.objects.values("district").filter(city=city,district__isnull=False).annotate(count=Count("id"))]
        res["data"][city] = districts
    else:
        city = access.city
        district = access.district
        res["data"][city] = [district,]
    return JsonResponse(res)


# 返回指定区域用户
def users(request):
    city = request.GET.get("city", "")
    district = request.GET.get("district", "")
    page = request.GET.get("page", "")
    limit = request.GET.get("limit", "")
    if city and district:
        users = UserInfo.objects.filter(city=city, village=district)
    else:
        access = Access.objects.get(account=request.user.username)
        if access.access == "省级":  # 返回所有市的用户
            users = UserInfo.objects.filter(is_active=True)
        elif access.access == "市级":  # 返回所有区用户
            users = UserInfo.objects.filter(city=access.city, is_active=True)
        else:
            users = UserInfo.objects.filter(village=access.district, is_active=True)
    if not users:
        return JsonResponse({"code": 0, "data": []})
    users_list = []
    for u in users:
        users_list.append(
            {"id": u.id, "name": u.name, "sex": u.sex, "age": u.age, "height": u.height, "weight": u.weight,
             "address": u.address, "id_number": u.id_number, "tel": u.tel, "edu": u.edu_background,
             "is_ins": "是" if u.is_instructor else "否", "instructor_class": u.instructor_class, "village": u.village,
             "city": u.city, "instructor_type": u.instructor_type, "ver_status": u.ver_status, "province": u.province,
             "certi_num": u.certificate_num, "certi_date": u.certificate_date, "gym": u.gym,
             "assessment": u.assessment, "upload_time": u.upload_time,
             "annual_survey_date": str(u.annual_survey_date)})
    paginator = Paginator(object_list=users_list, per_page=limit, )
    page_obj = paginator.get_page(page).object_list
    return JsonResponse({"code": 0, "count": users_list.__len__(), "data": page_obj})


def users_update(request):
    try:
        id = int(request.GET.get("id", ""))
        name = request.GET.get("name", "")
        sex = request.GET.get("sex", "")
        age = request.GET.get("age", "")
        height = request.GET.get("height", "")
        weight = request.GET.get("weight", "")
        address = request.GET.get("address", "")
        id_number = request.GET.get("id_number", "")
        tel = request.GET.get("tel", "")
        edu = request.GET.get("edu", "")
        is_ins = request.GET.get("is_ins", "")
        instructor_class = request.GET.get("instructor_class", "")
        instructor_type = request.GET.get("instructor_type", "")
        ver_status = request.GET.get("ver_status", "")
        certi_num = request.GET.get("certi_num", "")
        certi_date = request.GET.get("certi_date", "")
        gym = request.GET.get("gym", "")
        assessment = request.GET.get("assessment", "")
        upload_time = time.strftime("%Y%m%d")
        annual_survey_date = request.GET.get("annual_survey_date", "")
        user = UserInfo.objects.get(id=id)
        user.name = name
        user.sex = sex
        user.age = age
        user.height = height
        user.weight = weight
        user.address = address
        user.id_number = id_number
        user.tel = tel
        user.edu_background = edu
        user.is_instructor = True if is_ins == "true" else False
        user.instructor_class = instructor_class
        user.instructor_type = instructor_type
        user.ver_status = ver_status
        user.certificate_num = certi_num
        user.certificate_date = certi_date
        user.gym = gym
        user.assessment = assessment
        user.upload_time = upload_time
        user.annual_survey_date = annual_survey_date
        user.is_active = True
        user.save()
    except Exception as error:
        print(error)
    return JsonResponse({"code": 0, "data": "修改成功"})


def users_add(request):
    try:
        name = request.GET.get("name", "")
        sex = request.GET.get("sex", "")
        age = int(request.GET.get("age", ""))
        height = request.GET.get("height", "")
        weight = request.GET.get("weight", "")
        address = request.GET.get("address", "")
        id_number = request.GET.get("id_number", "")
        tel = request.GET.get("tel", "")
        edu_background = request.GET.get("edu_background", "")
        is_instructor = True if request.GET.get("is_instructor", "") == "true" else False
        instructor_class = request.GET.get("instructor_class", "")
        instructor_type = request.GET.get("instructor_type", "")
        ver_status = request.GET.get("ver_status", "")
        certificate_num = request.GET.get("certi_num", "")
        certificate_date = request.GET.get("certi_date", "")
        gym = request.GET.get("gym", "")
        assessment = request.GET.get("assessment", "")
        upload_time = time.strftime("%Y%m%d")
        annual_survey_date = request.GET.get("annual_survey_date", "")
        city = request.GET.get("city", "")
        village = request.GET.get("village", "")
        UserInfo(name=name, sex=sex, age=age, height=height, weight=weight, address=address, id_number=id_number,
                 tel=tel, edu_background=edu_background,
                 is_instructor=is_instructor, instructor_class=instructor_class, instructor_type=instructor_type,
                 ver_status=ver_status, certificate_num=certificate_num, certificate_date=certificate_date,
                 gym=gym, assessment=assessment, upload_time=upload_time, annual_survey_date=annual_survey_date,
                 city=city,
                 village=village, is_active=True).save()
        return JsonResponse({"code": 0, "data": "保存成功"})
    except Exception as error:
        print(error)
        return JsonResponse({"code": 1, "data": "入库出错"})


# 删除用户
def users_delete(request):
    id = request.GET.get("id", "")
    user = UserInfo.objects.get(id=id)
    user.is_active = False
    user.save()
    return JsonResponse({"code": 0, "data": "删除成功"})

# 动态
def moment(request):
    access = Access.objects.get(account=request.user.username)
    page = request.GET.get("page", "")
    limit = request.GET.get("limit", "")
    if access.access == "省级":  # 返回所有市的用户
        moments = Moment.objects.all()
    elif access.access == "市级":  # 返回所有区用户
        moments = Moment.objects.filter(user__city=access.city)
    else:
        moments = Moment.objects.filter(user__village=access.district)
    moments_list = []
    for m in moments:
        moments_list.append(
            {"id": m.id, "user": UserInfo.objects.get(id=m.user_id,is_active=True).name, "content": m.content, "post_time": m.post_time,
             "picture_path": m.picture_path, "location": m.location, "title": m.title})
    paginator = Paginator(object_list=moments_list, per_page=limit)
    page_obj = paginator.get_page(page).object_list
    return JsonResponse({"code":0,"count":moments_list.__len__(),"data":page_obj})



# 反馈
def feedback(request):
    access = Access.objects.get(account=request.user.username)
    page = request.GET.get("page", "")
    limit = request.GET.get("limit", "")
    if access.access == "省级":  # 返回所有市的用户
        feedbacks = FeedBack.objects.all()
    elif access.access == "市级":  # 返回所有区用户
        feedbacks = FeedBack.objects.filter(user__city=access.city)
    else:
        feedbacks = FeedBack.objects.filter(user__village=access.district)
    feed_list = []
    for f in feedbacks:
        feed_list.append(
            {"id": f.id, "user": UserInfo.objects.get(id=f.user).name, "content": f.content,
             "time": f.time})
    paginator = Paginator(object_list=feed_list, per_page=limit)
    page_obj = paginator.get_page(page).object_list

    return JsonResponse({"code": 0, "count": feed_list.__len__(), "data": page_obj})
