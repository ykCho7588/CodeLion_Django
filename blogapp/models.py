from pyexpat import model
from django.db import models

# Create your models here.
class Blog(models.Model): #이미 구현되어있는 장고의 모델기능을 사용 => 상속
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True) #자동으로 현재 시간을 추가

    def __str__(self):
        return self.title # 제목에 title을 표시하는 방법


