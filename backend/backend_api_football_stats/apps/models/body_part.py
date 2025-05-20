

from django.db import models

class BodyPart(models.Model):
    
    id = models.AutoField(primary_key=True, db_column='id')
    body_part_name = models.CharField(null=True, blank=True)
    

    class Meta:
        managed = False
        db_table = 'body_part'
