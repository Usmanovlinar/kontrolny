from django.db import models
class Calc_History(models.Model):
    val1 = models.IntegerField()
    val2 = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=100, blank= True)
    operator = models.CharField(max_length=100)
# Create your models here.
