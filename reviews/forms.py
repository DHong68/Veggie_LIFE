from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['store_name', 'title', 'body', 'file']
        labels = {
            'store_name': '식당명',
            'title': '제목',
            'body': '내용',
            'file':'파일'
        }
        