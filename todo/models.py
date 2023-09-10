from django.db import models

# 앱의 모델에서는 그 앱의 필요한 데이터들을 데이터베이스에 입력받아 옮겨놓게 한다
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100) # todo의 제목
    description = models.TextField(blank=True) # todo에 대한 설명 # 건너뛰어도 OK
    created = models.DateTimeField(auto_now_add=True) # todo생성 일자
    complete = models.BooleanField(default=False) # todo완성 여부 # False값을 기본으로 시작해라
    important = models.BooleanField(default=False) # Todo중요 여부

    def __str__(self): # admin에 보이는게 달라짐
        return self.title