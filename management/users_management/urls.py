from django.urls import path

from users_management.views import auth_login, auth_logout, auth_register, group_by_inspection, \
    group_by_district, group_by_class, group_by_verification, group_by_gender, group_by_type, group_by_age, \
    regions, users, users_update, users_add, users_delete, moment, feedback

urlpatterns = [
    path("login/",auth_login),# Login path
    path("logout/",auth_logout), # logout path
    path("register/",auth_register), # register path
    path("inspection/",group_by_inspection), # 按照年检分类
    path("district/",group_by_district),# 按照地区分类
    path("class/",group_by_class), # 按照指导员等级分类
    path("verification/",group_by_verification), # 按照审核状态划分
    path("gender/",group_by_gender),# 按照性别分类
    path("type/",group_by_type),# 按照指导类型划分
    path("age/",group_by_age),# 按照年龄分类
    path("regions/",regions), # 返回所有市区
    path("users/all/", users),  # 所有用户
    path("users/update/",users_update), # 用户信息修改
    path("users/add/",users_add), # 增加用户
    path("users/delete/",users_delete), # 删除用户
    path("moment/",moment),# 所有动态
    path("feedback/",feedback),# 所有评论
]

