#django form을 저장할 수 있는 파이썬 파일
from django import forms
from .models import Blog

class BlogForm(forms.Form):
    #입력받고자 하는 값들
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea) # 좀더 넓은 공간에 입력받음(본문)

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog # 어떤 모델을 기반으로 자동 form을 생성할 것인가?
        # fields = '__all__' #어떤 입력값(필드)을 입력받을 지 => form에 있는 필드 전부
        fields = ['title', 'body'] #특정 필드 값만 입력받는 경우
