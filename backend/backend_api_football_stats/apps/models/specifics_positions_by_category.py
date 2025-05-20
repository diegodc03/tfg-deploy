

from django.db import models

class SpecificsPositionsByCategory(models.Model):
    
    specific_position_id = models.AutoField(primary_key=True, db_column='specific_position_id')  # ID de la posición específica
    specific_position_name = models.CharField(max_length=255, null=True, blank=True)  # Nombre de la posición específica
    
    class Meta:
        managed = False
        db_table = 'positions_specifics_by_category'