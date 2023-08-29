from django.db import models


# Create your models here.
class ProcessMaster(models.Model):
    processmaster_id = models.BigAutoField(primary_key=True)
    processmaster_name = models.CharField(max_length=500)
    processmaster_description = models.TextField()
    processmaster_type = models.CharField(max_length=50)
    processmaster_dependencytype = models.CharField(max_length=50)
    processmaster_dependentprocessname = models.CharField(max_length=500)
    processmaster_seqno = models.IntegerField()
    processmaster_parentid = models.BigIntegerField()
    processmaster_starttime = models.DateTimeField()
    processmaster_endtime = models.DateTimeField()
    processmaster_slabreach = models.DateTimeField()
    processmaster_alertme = models.TextField()

    class Meta:
        managed = False
        db_table = 'processmaster'
