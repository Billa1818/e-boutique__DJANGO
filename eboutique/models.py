from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Article(models.Model):
    
    article_id=models.AutoField(primary_key=True)
    
    article_title = models.CharField(max_length=255)
    
    article_autor =models.ForeignKey(User,on_delete=models.CASCADE)
    
    article_img=models.ImageField( upload_to='user_article/')
    
    article_content = models.TextField()
    
    article_type = models.TextField()
    
    article_created = models.DateTimeField(auto_now_add=True)
    
    article_updated = models.DateTimeField(auto_now=True)
    
    article_disp = models.DecimalField(max_digits=10, decimal_places=0, default=1)
    
    article_price=models.DecimalField(max_digits=10, decimal_places=0, default=1)
    
    user_delete=models.BooleanField( default=False )
    
    
    
class Message(models.Model):
    
    message_id=models.AutoField(primary_key=True)
    
    sujet =  models.CharField(max_length=255)
    
    contenu = models.TextField()
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    destinataire= models.CharField(max_length=255)
    
    date_publication = models.DateTimeField(default=timezone.now)
    
    


class Cart_de_credit(models.Model):
    
    card_number = models.CharField(max_length=16, unique=True,primary_key=True)
    
    card_name = models.CharField(max_length=255)
    
    user_mail=models.EmailField( null=True ,blank=True)
    
    expiration = models.DateField()
    
    cvv = models.CharField(max_length=3)
    
    montant = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

  
class Transaction(models.Model):
    
    user_env=models.TextField()
    
    user_rec=models.TextField()
    
    Cart_de_credit = models.ForeignKey(Cart_de_credit, on_delete=models.CASCADE )
    
    transaction_date = models.DateTimeField(auto_now_add=True)
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
     
    description = models.TextField(blank=True, null=True)
    
    

class mon_panier(models.Model):
    
    panier_id=models.ForeignKey(User, on_delete=models.CASCADE )
    
    panier_article=models.TextField(blank=True, null=True) 
    

class Commande(models.Model):
    
    id_commande=models.AutoField(primary_key=True)
    
    id_article=models.JSONField(default=list)
    
    id_transaction=models.TextField()
    
    id_env=models.ForeignKey(User, on_delete=models.CASCADE )
    
    prix_total= models.DecimalField(max_digits=10, decimal_places=2)
    
    statut1=models.BooleanField( default=False,blank=True  )
    
    statut2=models.BooleanField( default=False,blank=True  )
    
    destination=models.TextField( blank=True )

    
class user_profil(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    user_profil=models.ImageField(upload_to='user_profil/' , null=True , blank=True)
    
    