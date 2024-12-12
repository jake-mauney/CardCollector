from django.db import models
from django.contrib.auth.models import User

#the picklist options referencd below. Not sure why it is in the format of SOMETHING, something
status_options = [('NEW', 'new'), ('IN PROCESS', 'In Process'), ("DONE", "Done"), ("ERROR", "Error")]
request_type_options = [('CARD', 'Card'), ('DECK', 'Deck')]

class ImportRequest(models.Model):
    request_date = models.DateTimeField(auto_now_add=True) #Just to keep track of when these are created and how long to process
    csv_file = models.FileField() #the actual csv file. No validation 
    status = models.CharField(max_length= 10, choices=status_options, blank=True, null=True) #used in case error handling is implemented
    error_msg = models.CharField(max_length=10000, blank=True, null=True) 
    type = models.CharField(max_length=10, choices=request_type_options) #Importing in deck format or just a raw collection?
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    

