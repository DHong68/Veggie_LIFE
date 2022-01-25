from django import forms
from .models import User
from django.contrib.auth.models import User as Users
from argon2 import PasswordHasher


class SignupForm(forms.ModelForm):
    pass
    class Meta:
        model = User
        # fields = ['user_id', 'password', 're_password', 'email', 'name', 'veg_type']
        fields = ['user_id', 'password', 'email', 'name', 'veg_type']
        
        def clean(self):
                cleaned_data = super().clean()

                password = cleaned_data.get('password', '')
                re_password = cleaned_data.get('re_password', '')


                if len(password) < 8:
                        raise forms.ValidationError('비밀번호는 8자 이상으로 설정해주세요.')
                        # return self.add_error('password', '비밀번호는 8자 이상으로 설정해주세요.')
           


        widgets = { 
                'user_id': forms.TextInput(attrs={'required': True, 'size': 30}),
                'password': forms.PasswordInput(attrs={'required': True, 'size': 50}),
                're_password': forms.PasswordInput(attrs={'required': True, 'size': 50}),
                'email': forms.TextInput(attrs={'required': True, 'size': 50}),
                'name': forms.TextInput(attrs={'required': True, 'size': 50}),
                'veg_type': forms.TextInput(attrs={'required': True, 'size': 30})
        }
        labels = {
                'user_id': '아이디',
                'password': '비밀번호',
                # 're_password': '비밀번호 확인',
                'email': '이메일',
                'name': '이름',
                'veg_type': '채식 단계'
        }
