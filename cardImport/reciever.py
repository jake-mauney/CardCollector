from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ImportRequest
import csv


@receiver(post_save, sender=ImportRequest) #listens for when a import request is created
def model_instance_created(sender, instance, created, **kwargs): 
    if created:  #if created process the rows within the file
        reqeustRecord = ImportRequest.objects.get(pk=instance.pk)
        filename = 'userimport/'+str(reqeustRecord.csv_file)
        csv_file = csv.DictReader(open(filename))
        result = {}
        i=1
        for row in csv_file:
            result[i]=row
            i+=1
            import_name = row['name']
            import_set_code = row['set_code']
            import_set_num = row['set_num']
            import_foil = row['foil']
        print(result)
        
    else:
        print("something went wrong")
        