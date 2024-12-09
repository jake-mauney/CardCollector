from django.db import models
#the picklist options referencd below. Not sure why it is in the format of SOMETHING, something
status_options = [('NEW', 'new'), ('IN PROCESS', 'In Process'), ("DONE", "Done"), ("ERROR", "Error")]
type_options = [('CARD', 'Card'), ('DECK', 'deck')]

class ImportRequest(models.Model):
    request_date = models.DateTimeField() #Just to keep track of when these are created and how long to process
    csv_file = models.FileField() #the actual csv file. No validation 
    status = models.CharField(max_length= 10, choices=status_options) #used in case error handling is implemented
    error_msg = models.CharField(max_length=10000) 
    type = models.CharField(max_length=10, choices=type_options) #Importing in deck format or just a raw collection?

    

