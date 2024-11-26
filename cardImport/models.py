from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

status_options = [('NEW', 'new'), ('IN PROCESS', 'In Process'), ("DONE", "Done"), ("ERROR", "Error")]
type_options = [('CARD', 'Card'), ('DECK', 'deck')]
class ImportRequest(models.Model):
    request_date = models.DateTimeField()
    csv_file = models.FileField()
    status = models.CharField(max_length= 10, choices=status_options)
    error_msg = models.CharField(max_length=10000)
    type = models.CharField(max_length=10, choices=type_options)

    
@receiver(post_save, sender=ImportRequest) #listens for when a import request is created
def model_instance_created(sender, instance, created, **kwargs): 
    if created:  #if created
        reqeustRecord = ImportRequest.objects.get(pk=instance.pk)
        reqeustRecord.status = 'DONE' #set the status to done
        reqeustRecord.save() #actually save the record
    else:
        print("something went wrong")
