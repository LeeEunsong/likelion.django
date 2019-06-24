from django import forms
from .models import Blog

class BlogForm(forms.ModelForm): # 모델기반으로 한 공간
    class Meta:
        model = Blog #어떤 모델인지
        fields = '__all__' #모델에서 어떤 필드를 쓸지