# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Customer(models.Model):
    '''客户信息'''
    pass
class CustomerFollowUp(models.Model):
    '''客户跟进表'''
    pass
class Course(models.Model):
    '''课程表'''
    pass
class ClassList(models.Model):
    '''班级列表'''
    pass
class UserProfile(models.Model):
    '''帐号表'''
    pass

class Role(models.Model):
    '''角色表'''
    pass
