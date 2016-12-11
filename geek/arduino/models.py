from django.db import models

# Create your models here.
class Card(models.Model):
    board_model = models.CharField(max_length=50)
    discription = models.CharField(max_length=100)
    img = models.CharField(blank=False,max_length=200)
    level = models.CharField(choices=(('entry', 'Entry'), ('enhanced', 'Enhanced')
    ,('internet_of_things','Internet Of Things'),('wearable','Wearable'),('3D_printing','3D Printing')),max_length=25)

    def __str__(self):
        return self.board_model

class Detail(models.Model):
    card = models.ForeignKey('Card')
    documents = models.CharField(max_length=50000);
