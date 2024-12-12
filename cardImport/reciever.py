from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ImportRequest
import csv
from cards.models import Card
from decks.models import Deck, DeckEntry


@receiver(post_save, sender=ImportRequest) #listens for when a import request is created
def model_instance_created(sender, instance, created, **kwargs): 
    print("we hit the reciever")
    if created:  #if created process the rows within the file
        reqeustRecord = ImportRequest.objects.get(pk=instance.pk)
        filename = 'userimport/'+str(reqeustRecord.csv_file)
        csv_file = csv.DictReader(open(filename))

        if reqeustRecord.type == 'CARD':
            for row in csv_file:
                import_name = row['name']
                import_set_code = row['set_code']
                import_set_num = row['set_num']
                import_foil = row['foil']
                import_owner = reqeustRecord.owner
                newCard = Card.objects.create(name = import_name, set_code= import_set_code, set_num = import_set_num, foil=import_foil, owner = import_owner)
        else:
            print("we hit the right else")
            
            newDeck = Deck.objects.create(name = 'new imported deck', owner=reqeustRecord.owner)
            for row in csv_file:
                quantityCounter = 1
                if isinstance(row['quantity'], int):
                    quantity = row['quantity']
                else: 
                    quantity = int(row['quantity'])
                while quantityCounter <= quantity:
                    import_name = row['name']
                    import_set_code = row['set_code']
                    import_set_num = row['set_num']
                    import_foil = row['foil']
                    import_owner = reqeustRecord.owner
                    newCard = Card.objects.create(name = import_name, set_code= import_set_code, set_num = import_set_num, foil=import_foil, owner = import_owner)
                    newDeckEntry = DeckEntry.objects.create(rel_card = newCard, rel_deck = newDeck, location=row['location'].upper())
                    quantityCounter +=1
                       
        
        
    else:
        print("something went wrong")
        