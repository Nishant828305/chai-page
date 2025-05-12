from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class chaivariety(models.Model):
    chai_type_choices =  [
    ('ml', "Masala Chai"),
    ('sp', "Spiced Chai"),
    ('ch', "Chai Latte"),
    ('g',  "Ginger Chai"),
    ('l',  "Lemon Chai"),
    ('m',  "Mint Chai"),
    ('t',  "Chai Tea"),
    ('p',  "Peppermint Chai"),
    ('h',  "Honey Chai"),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField(default='')
    # date_added =models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/')
    chai_type = models.CharField(max_length=20, choices=chai_type_choices) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name_plural ='Chai Varieties'
    
    def __str__(self):
        return self.name

    
# one to many

class chaiReview(models.Model):
    chai = models.ForeignKey(chaivariety,on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment =models.TextField()
    date_added =models.DateTimeField(default=timezone.now)
    
    def __str__(self):
      return f'{self.user.username}review for {self.chai.name}'

# Many to Many

class store(models.Model):
    name =models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    chai_varieties =models.ManyToManyField(chaivariety,related_name='stores')
    def __str__(self):
       return self.name
    
    
    
# one to one   

class chaiCertificate (models.Model):
    chai = models.OneToOneField(chaivariety,on_delete=models.CASCADE,related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date =models.DateTimeField(default=timezone.now)
    valid_date =models.DateTimeField()
    
    
    def __str__(self):
        return f'Certificate for {self.name.chai}'