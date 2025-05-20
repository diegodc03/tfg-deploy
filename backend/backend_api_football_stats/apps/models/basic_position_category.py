
from django.db import models

class BasicPositionCategory(models.Model):
    
    category_id = models.AutoField(primary_key=True, db_column='category_id')
    category_name = models.CharField(max_length=255, null=True, blank=True) 
    
    class Meta:
        managed = False
        db_table = 'position_category'