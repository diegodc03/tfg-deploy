from django.db import models

class TypeOfGame(models.Model):
    
    type_of_game_id = models.AutoField(primary_key=True, db_column='type_of_game_id')  # ID del tipo de juego
    type_of_game_name = models.CharField(max_length=255, null=True, blank=True)  # Nombre del tipo de juego
    
    
    def __str__(self):
        return f"{self.name}: {self.description}"
    
    class Meta:
        managed = False
        db_table = 'type_of_game'