from django.db import models

class OutcomeStats(models.Model):
    
    id = models.AutoField(primary_key=True, db_column='id')
    outcome_name = models.CharField(max_length=255, null=True, blank=True)
    

    class Meta:
        managed = False
        db_table = 'outcome_stats'
