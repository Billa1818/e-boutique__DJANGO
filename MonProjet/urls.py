"""
URL configuration for MonProjet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from eboutique.views import index,a_propos,ajt_article,categorie,det_article
from eboutique import views
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('a_propos/',views.a_propos,name='a_propos'),
    
    path('ajt_article/',views.ajt_article,name='ajt_article'),
    
    path('categorie/',views.categorie,name='categorie'),
    
    path('commande/',views.commande,name='commande'),

    path('det_article/<int:article_id>/',views.det_article,name='det_article'),
    
    path('index/',views.index,name='index'),
    
    path('',views.index,name='index'),
    
    path('loginn/',views.loginn,name='loginn'),
    
    path('mdp_oub/',views.mdp_oub,name='mdp_oub'),

    path('mdp_oub2/',views.mdp_oub2,name='mdp_oub2'),
    
    path('mes_article/',views.mes_article,name='mes_article'),
    

    path('modifier_article/<int:article_id>/',views.modifier_article,name='modifier_article'),
    
    path('modifier_mdp/',views.modifier_mdp,name='modifier_mdp'),
    
    path('mon_panier/',views.mon_panier,name='mon_panier'),
    
    path('nous_contacter/',views.nous_contacter,name='nous_contacter'),
    
    path('parametre/',views.parametre,name='parametre'),
    
    path('profil/',views.profil,name='profil'),
    
    path('recherche/',views.recherche,name='recherche'),

    path('singup/',views.singup,name='singup'),

    path('sup_art/<int:article_id>/',views.sup_art,name='sup_art'),
    
    path('action_sur_commande/<int:id_commande>/',views.action_sur_commande,name='action_sur_commande'),
    
    path('sup_user/',views.sup_user,name='sup_user'),
    
    path('carte_de_credit/',views.carte_de_credit,name='carte_de_credit'),
    
    path('det_carte/',views.det_carte,name='det_carte'),
    
    path('logoutt/',views.logoutt,name='logoutt'),
    
     path('sup_cart/<str:card_number>/',views.sup_cart,name='sup_cart'),
    
    path('reset_password/',views.reset_password,name='reset_password'),
    
    path('sup_pro/<str:author>/',views.sup_pro,name='sup_pro'),
    
    path('conf_sup/<str:article_id>/',views.conf_sup,name='conf_sup'),
    
    path('statut_art/<int:article_id>/',views.statut_art,name='statut_art'),
    
    path('ajt_panier/<int:article_id>/',views.ajt_panier,name='ajt_panier'),
    
    path('vider_panier/',views.vider_panier,name='vider_panier'),

    path('retirer_panier/<int:article_id>/',views.retirer_panier,name='retirer_panier'),
    
    path('passer_commande/',views.passer_commande,name='passer_commande'),
    
    
    
    
    
    
    
    
    
    
    
     
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
