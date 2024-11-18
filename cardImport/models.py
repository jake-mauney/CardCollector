from django.db import models
status_options = [('NEW', 'new'), ('IN PROCESS', 'In Process'), ("DONE", "Done"), ("ERROR", "Error")]
type_options = [('CARD', 'Card'), ('DECK', 'deck')]
class ImportRequest(models.Model):
    request_date = models.DateTimeField()
    csv_file = models.FileField()
    status = models.CharField(max_length= 10, choices=status_options)
    error_msg = models.CharField(max_length=10000)
    type = models.CharField(max_length=10, choices=type_options)