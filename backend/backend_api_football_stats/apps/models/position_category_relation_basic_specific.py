


from django.db import models
from ..models import BasicPositionCategory
from ..models import SpecificsPositionsByCategory

class PositionCategoryRelationBasicSpecific(models.Model):
    
    position_id = models.ForeignKey(
        SpecificsPositionsByCategory,
        on_delete=models.CASCADE,
        db_column='position_id',
        related_name='specifics_positions_by_category'
    )
    
    category_id = models.ForeignKey(
        BasicPositionCategory,
        on_delete=models.CASCADE,
        db_column='category_id',
        related_name='basic_position_category'
    )
    
    
    class Meta:
        managed = False
        db_table = 'position_category_relation'
        
        
