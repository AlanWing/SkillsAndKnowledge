from django.db import models

# Create your models here.
from django.db.models import Model, IntegerField, CharField, FloatField, BooleanField, ForeignKey, CASCADE, TextField, \
    ManyToManyField, AutoField, SET_NULL, SET, DateField


class Access(Model):
    id = AutoField(primary_key = True)
    account = CharField(max_length=30,null=False)
    password = CharField(max_length=30,null=False)
    province = CharField(max_length=30,null=False)
    city = CharField(max_length=30,null=True)
    district = CharField(max_length=30,null=True)
    access = CharField(max_length=30,null=False)
    class Meta:
        db_table = "access"



class UserInfo(Model):
    id = AutoField(primary_key=True, verbose_name="用户ID")
    name = CharField(max_length=20, verbose_name="用户名称", null=True)
    sex = CharField(max_length=20, verbose_name="性别", null=True)
    age = IntegerField(verbose_name="年龄", null=True)
    height = CharField(max_length=20, verbose_name="身高/cm", null=True)
    weight = CharField(max_length=20, verbose_name="体重", null=True)
    address = CharField(max_length=50, verbose_name="住址", null=True)
    id_number = CharField(max_length=30, verbose_name="身份证号", null=True)
    tel = CharField(max_length=20, verbose_name="电话号码", null=True)
    edu_background = CharField(max_length=20, verbose_name="文化程度", null=True)
    is_instructor = BooleanField(verbose_name="是否指导员", null=True)
    instructor_class = CharField(max_length=20, verbose_name="指导员等级", null=True)
    instructor_type = CharField(max_length=40, verbose_name="指导类型", null=True)
    ver_status = CharField(max_length=20, verbose_name="审核状态", null=True)
    province = CharField(max_length=20, verbose_name="省级区划", null=True)
    city = CharField(max_length=20, verbose_name="市级区划", null=True)
    village = CharField(max_length=20, verbose_name="乡镇", null=True)
    certificate_num = CharField(max_length=50, verbose_name="证书编号", null=True)
    certificate_date = CharField(max_length=20, verbose_name="发证日期", null=True)
    gym = CharField(max_length=50, verbose_name="健身地点", null=True)
    assessment = CharField(max_length=30, verbose_name="评定成绩", null=True)
    upload_time = CharField(max_length=30, verbose_name="上传日期", null=True)
    annual_survey_date = DateField(max_length=30, verbose_name="年检日期", null=True)

    class Meta:
        db_table = "userinfo"


class Moment(Model):
    id = AutoField(primary_key=True, verbose_name="ID")
    user_id = ForeignKey(UserInfo, on_delete=CASCADE, verbose_name="用户ID")
    content = CharField(max_length=128, verbose_name="发布内容", null=True)
    post_time = CharField(max_length=30, verbose_name="发布时间", null=True)
    picture_path = CharField(max_length=128, verbose_name="图片路径", null=True)
    location = CharField(max_length=128, verbose_name="定位", null=True)
    title = CharField(max_length=50, verbose_name="话题/标签", null=True)

    class Meta:
        db_table = "moment"


class Like(Model):
    id = IntegerField(primary_key=True)
    like = ManyToManyField(UserInfo, verbose_name="点赞者")
    moment_id = ForeignKey(Moment, on_delete=CASCADE, verbose_name="点赞动态ID")
    time = CharField(max_length=30, verbose_name="点赞时间", null=True)

    class Meta:
        db_table = "like"


class Follow(Model):
    id = IntegerField(primary_key=True)
    follow = ManyToManyField(UserInfo, verbose_name="关注者")
    moment = ForeignKey(Moment, on_delete=CASCADE, verbose_name="动态ID")
    time = CharField(max_length=30, verbose_name="关注时间", null=True)

    class Meta:
        db_table = "follow"


class Favorite(Model):
    id = IntegerField(primary_key=True)
    moment_id = ForeignKey(Moment, on_delete=CASCADE, verbose_name="点赞动态ID")
    colletcor = ManyToManyField(UserInfo, verbose_name="收藏者")

    class Meta:
        db_table = "favorite"


class Comment(Model):
    id = IntegerField(primary_key=True)
    moment_id = ForeignKey(Moment, on_delete=CASCADE, verbose_name="动态ID")
    user = ManyToManyField(UserInfo, verbose_name="评论者ID")
    comment = TextField(max_length=800, verbose_name="评论内容")
    time = CharField(max_length=30, verbose_name="评论时间", null=True)

    class Meta:
        db_table = "comment"


class FeedBack(Model):
    id = IntegerField(primary_key=True)
    user = ForeignKey(UserInfo, on_delete=CASCADE, verbose_name="反馈者")
    content = TextField(max_length=800, verbose_name="反馈内容")
    time = CharField(max_length=30, verbose_name="反馈时间", null=True)

    class Meta:
        db_table = "feedback"

