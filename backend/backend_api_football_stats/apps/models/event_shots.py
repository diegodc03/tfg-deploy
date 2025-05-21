from django.db import models

class EventShots(models.Model):
    
    id = models.AutoField(primary_key=True, db_column='id')
    event_shots_name = models.CharField(max_length=255, null=True, blank=True)
    

    class Meta:
        managed = False
        db_table = 'event_shots'
