from django.db import models
from .type_of_game import TypeOfGame

class GameMode(models.Model):
    
    game_mode_id = models.AutoField(primary_key=True, db_column='game_mode_id')
    game_mode_name = models.CharField(max_length=255, null=True, blank=True)  
    type_of_game_id = models.ForeignKey(TypeOfGame, on_delete=models.CASCADE, null=True, blank=True, db_column='type_of_game_id')

    def __str__(self):
        return f"{self.name}: {self.description}"
    
    class Meta:
        managed = False
        db_table = 'game_modes'