from django.db import models

# Create your models here.
class Book(models.Model):
    b_name = models.CharField(max_length=32)
    b_price = models.FloatField(default=1)

    def to_dict(self):
        return {'id':self.id,'name':self.b_price,'price':self.b_name}
