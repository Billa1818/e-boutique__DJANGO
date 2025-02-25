from django.contrib import admin
from .models import Article, Message,Cart_de_credit,Transaction,mon_panier,Commande,user_profil





# Register your models here.

admin.site.register(Article)

admin.site.register(Message)

admin.site.register(Cart_de_credit)

admin.site.register(Transaction)

admin.site.register(mon_panier)

admin.site.register(Commande)

admin.site.register(user_profil)

