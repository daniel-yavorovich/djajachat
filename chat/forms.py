# -*- coding: utf-8 -*-
from django import forms

class LoginForm(forms.Form):
    first_name  = forms.CharField(max_length=100)
    last_name   = forms.CharField(max_length=100)