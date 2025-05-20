
from django.db import models


class Player(models.Model):
    
    
    player_id = models.AutoField(primary_key=True, db_column='player_id')
    player_name = models.CharField(max_length=255, null=True, blank=True, db_column='player')
    shirt_number = models.IntegerField(null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    nacionality = models.CharField(max_length=255, null=True, blank=True)
    
    class Meta:
        db_table = 'jugador'
        managed = False