import random
from django.shortcuts import render,redirect,get_object_or_404 
from .models import User , Cart_de_credit,Article,user_profil,mon_panier,Commande,Transaction
from django.core.exceptions import ValidationError
from django.core.validators import  validate_email
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate,login,logout
from django.core.validators import EmailValidator
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.contrib.auth import password_validation
from decimal import Decimal



# Create your views here.

def page404(request, exception):
    return render(request,'page404.html',{},status=404)

def sup_user(request):
    if not request.user.is_authenticated:
        return redirect('loginn')
    
    if not request.user.is_superuser:
        user=request.user
        user.delete()
        redirect('singup')








def action_sur_commande(request, id_commande):
     
    if Commande.objects.filter(statut1=True, statut2=True).exists():
        
        Commande.objects.filter(id_commande=id_commande).delete()
       
        return redirect('commande')
    
    else:
         
        if request.user.is_superuser:
            commande = get_object_or_404(Commande, id_commande=id_commande)
            commande.statut2 = True
            commande.save()  
            return redirect('commande')
        
        
        elif not request.user.is_superuser:
            commande = get_object_or_404(Commande, id_commande=id_commande)
            commande.statut1 = True
            commande.save()  
            return redirect('commande')

        
    
    

def passer_commande(request):
    if not request.user.is_authenticated:
        return redirect('loginn')

    if request.method == 'POST':
        ville = request.POST.get('ville')

        if not ville:
            return render(request, "eboutique/confimation_command.html", {'error': 'Veuillez indiquer la ville de destination.'})

        carte_de_credit = Cart_de_credit.objects.filter(user_mail=request.user.email).first()
        if not carte_de_credit:
            return redirect('carte_de_credit')

        eboutique_admin = get_object_or_404(User, username='@EboutiqueSuperAdim@', is_superuser=True)

        carte_eboutique = Cart_de_credit.objects.filter(user_mail=eboutique_admin.email).first()
        if not carte_eboutique:
            return redirect('index')

        total_commande = request.session.get('total_commande')
        article_ids = request.session.get('article_ids')

        if not article_ids or not total_commande:
            return redirect('mon_panier')

       
        if carte_de_credit.montant < Decimal(total_commande):
            return render(request, "eboutique/confimation_command.html", {'error': 'Le solde de votre carte de crédit est insuffisant.'})

      
        nouvelle_transaction = Transaction.objects.create(
            user_env=request.user,
            user_rec="@EboutiqueSuperAdim@",
            Cart_de_credit=carte_de_credit,
            amount=total_commande,
            description=str(article_ids),
        )

      
        nouvelle_commande = Commande.objects.create(
            id_env=request.user,
            id_article=article_ids,
            prix_total=total_commande,
            id_transaction=nouvelle_transaction,
            destination=ville,
        )

         
        carte_de_credit.montant -= Decimal(total_commande)
        carte_de_credit.save()

        carte_eboutique.montant += Decimal(total_commande)
        carte_eboutique.save()

        
        request.session['panier'] = {}

        return redirect('commande')

    else:
        panier = request.session.get('panier', {})
        if not panier:
            return redirect('mon_panier')

        total_commande = Decimal(0)
        article_ids = []

        for article_id, details in panier.items():
            article = get_object_or_404(Article, article_id=article_id)

            if isinstance(details, dict):
                quantite = details.get('quantite', 1)
            else:
                quantite = details

            prix_total = article.article_price * quantite
            article_ids.append(article_id)
            total_commande += prix_total

        request.session['total_commande'] = float(total_commande)
        request.session['article_ids'] = article_ids

        return render(request, 'eboutique/confimation_command.html', {
            'total_commande': total_commande,
            'article_ids': article_ids
        })

 



















def vider_panier(request):
    if not request.user.is_authenticated:
        return redirect('loginn')
    
    del request.session['panier']
    del request.session['total_articles']
    return redirect('mon_panier')


def ajt_panier(request,article_id):
    if not request.user.is_authenticated:
        return redirect('loginn')
    
    if  request.user.is_superuser:
        return redirect('index')
    
    article=Article.objects.get(article_id=article_id)
    
    if 'panier' not in request.session:
        request.session['panier']={}
    
    panier=request.session['panier']
    
    if str(article_id) in panier:
        panier[str(article_id)]+=1
    else:
        panier[str(article_id)]=1
        
    request.session['panier']= panier
    
    total_articles = sum(panier.values())
    
    request.session['total_articles']= total_articles
    
    return redirect('mon_panier')


def retirer_panier(request,article_id):
    if not request.user.is_authenticated:
        return redirect('loginn')
    
    panier=request.session.get('panier',{})
    if str(article_id) in panier:
        
        del panier[str(article_id)]
            
        request.session['panier']=panier
        
    else:
        
        print("erreur")
        
    return redirect('mon_panier')

 




def commande(request):
    if not request.user.is_authenticated:
        return redirect('loginn')
    
    if request.user.is_superuser:
        
        commandes=Commande.objects.all()
    else:
        commandes=Commande.objects.filter(id_env=request.user)
    
    
    return render(request,"eboutique/commande.html",{'commande':commandes})




 


def mon_panier(request):
    if not request.user.is_authenticated:
        return redirect('loginn')
    
    if  request.user.is_superuser:
        return redirect('index')
    
    panier= request.session.get('panier', {} )
    
    articles=[]
    
    total_prix=0
    
    for article_id , quantite in panier.items():
        article=Article.objects.get(article_id=article_id)
        articles.append({
            'article':article,
            'quantite':quantite,
            'prix_total':article.article_price*quantite
                        })
        total_prix+=article.article_price*quantite
        
    return render(request,'eboutique/mon_panier.html',{
        'articles':articles,
        'total_prix':total_prix
    })
        

        

def sup_pro(request, author):
    if not request.user.is_authenticated:
        return redirect('loginn')
    pro=get_object_or_404(user_profil,author__username=author)
    pro.delete()
    return redirect('parametre')


def sup_cart(request, card_number):
    if not request.user.is_authenticated:
        return redirect('loginn')
    cart=get_object_or_404(Cart_de_credit,card_number=card_number)
    cart.user_mail=None
    cart.save()
    return redirect('profil')


def a_propos(request):
    if not request.user.is_authenticated:
        return redirect('loginn')
    return render(request,"eboutique/a_propos.html")


def ajt_article(request):
    errors = []
    
    
    if not request.user.is_authenticated:
        return redirect('loginn')
    
    
    if request.method == 'POST':
        
        article_title = request.POST.get('nom')
        article_type = request.POST.get('type')
        article_price = request.POST.get('prix')
        article_disp = request.POST.get('stock')
        article_img = request.FILES.get('article_img')
        article_content = request.POST.get('desc')
        
         
        if not article_title or not article_type or not article_price or not article_disp   or not article_content or not article_img:
            errors.append("Tous les champs sont obligatoires.")
            
            
        else:
            try:
                
                article = Article(
                    article_title=article_title,
                    article_content=article_content,
                    article_type=article_type,
                    article_price=article_price,
                    article_autor=request.user,  
                    article_img=article_img,
                    user_delete=False,
                    article_disp=article_disp
                )
                
                
                article.save()
                
                return redirect('mes_article')
            except Exception as e:
                
                errors.append(f"Erreur lors de l'enregistrement : {str(e)}")
    
    
    return render(request, "eboutique/ajt_article.html", {'errors': errors})


def categorie(request):
    if not request.user.is_authenticated:
        return redirect('loginn')
    else:
        article_liste=Article.objects.filter(user_delete=False).order_by('-article_created')
        
        paginator = Paginator(article_liste,8)
        
        page_number= request.GET.get('page')
        
        article=paginator.get_page(page_number)
        
        return render(request,"eboutique/index.html",{'article':article})

def det_article(request,article_id):
    if not request.user.is_authenticated:
        return redirect('loginn')
    article=get_object_or_404(Article,article_id=article_id)
    return render(request,"eboutique/det_article.html",{'article':article})


def index(request):

        if not request.user.is_authenticated:
            return redirect('loginn')
    
        article_liste=Article.objects.filter(user_delete=False).order_by('-article_created')
        
        paginator = Paginator(article_liste,8)
        
        page_number= request.GET.get('page')
        
        article=paginator.get_page(page_number)
        
        return render(request,"eboutique/index.html",{'article':article})





def loginn(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    errors = []
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)

            try:
                user_profile = user_profil.objects.get(author=user)  # Get the user profile based on the logged-in user
                
                # Store the user's profile photo in the session if it exists
                request.session['photo'] = user_profile.user_profil.url if user_profile.user_profil else None
            
            except user_profil.DoesNotExist:
                request.session['photo'] = None
            
            return redirect('index')  
        else:
            errors.append("Nom d'utilisateur ou mot de passe incorrect.")

    return render(request, 'eboutique/login.html', {'errors': errors})









 

def mdp_oub(request):
    errors = []

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            errors.append('Aucun compte trouvé à cette adresse email.')
            return render(request, "eboutique/mdp_oub.html", {'errors': errors})

         
        username = user.username

        
        recovery_code = random.randint(100000, 999999)
        
        
        request.session['recovery_code'] = recovery_code
        request.session['email'] = email

        
        send_mail(
            'Eboutique : Code de récupération', 
            f'Bonjour utilisateur:  {username},\n\nVotre code de récupération est : {recovery_code}.', 
            'az9245054@gmail.com', 
            [email], 
            fail_silently=False
        )

        
        return redirect('mdp_oub2')

    return render(request, "eboutique/mdp_oub.html")





def mdp_oub2(request):
    if request.user.is_authenticated:
        return redirect('index')

    errors = []
    if request.method == 'POST':
        code = request.POST.get('code')
        if code and int(code) == request.session.get('recovery_code'):
            return redirect('reset_password')   
        else:
            errors.append('Le code de récupération est incorrect.')

    return render(request, "eboutique/mdp_oub2.html", {'errors': errors})

def mes_article(request):
    if not request.user.is_authenticated:
        return redirect('loginn')
    elif request.user.is_authenticated:
        article=Article.objects.filter(article_autor=request.user).order_by('-article_created')
    else:
        article=Article.objects.none()
    nbr=Article.objects.filter(article_autor=request.user).count()
    return render(request,"eboutique/mes_article.html",{'article':article,'nbr':nbr})


 


def reset_password(request):
    
    if request.user.is_authenticated:
        return redirect('index')

    errors = []
    
    if request.method == 'POST':
        
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        email = request.session.get('email')
        
        if email:
            try:
                validate_email(email)   
            except ValidationError:
                errors.append("L'adresse e-mail fournie est invalide.")
                email = None 
        else:
            errors.append("Aucune adresse e-mail trouvée.")
        
        if email:
            if new_password != confirm_password:
                errors.append("Les mots de passe ne correspondent pas.")
            else:
                try:
                    user = User.objects.get(email=email)

                    # Validation du mot de passe
                    try:
                        validate_password(new_password, user)
                    except ValidationError as e:
                        errors.append(f"Mot de passe invalide : {', '.join(e.messages)}")
                    
                    if not errors:
                        user.set_password(new_password)
                        user.save()

                        # Nettoyage des sessions
                        del request.session['recovery_code']
                        del request.session['email']
                    
                        return redirect('loginn')
                
                except User.DoesNotExist:
                    errors.append("Erreur lors de la réinitialisation du mot de passe.")
                    
    return render(request, "eboutique/reset_password.html", {'errors': errors})





def modifier_article(request,article_id):
    if not request.user.is_authenticated:
        return redirect('loginn')
    article=get_object_or_404(Article,article_id=article_id)
    
    if request.method == 'POST':
        
        article_title = request.POST.get('nom')
        article_type = request.POST.get('type')
        article_price = request.POST.get('prix')
        article_disp = request.POST.get('stock')
        article_img = request.FILES.get('article_img')
        article_content = request.POST.get('desc')

        if article_img is not None:
            article.article_img=article_img
            
        article.article_title=article_title
        article.article_type=article_type
        article.article_price=article_price
        article.article_disp=article_disp
        article.article_content=article_content
        
        article.save()
        
        return redirect('mes_article')
        
    
    return render(request,"eboutique/modifier_article.html",{'article':article})


def modifier_mdp(request):
    errors = []
    if not request.user.is_authenticated:
        return redirect('loginn')
    
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        user = request.user
        
        
        if check_password(current_password, user.password):
             
            try:
                validate_password(new_password, user)   
            except ValidationError as e:
                errors.extend(e.messages)   
            
            if new_password == confirm_password:
                if not errors:
                    user.set_password(new_password)
                    user.save()
                    login(request, user)
                    return redirect('index')
                else:
                    return render(request, "eboutique/modifier_mdp.html", {'errors': errors})
            else:
                errors.append("Les nouveaux mots de passe ne correspondent pas")
        else:
            errors.append("L'ancien mot de passe ne correspond pas")
            
        return render(request, "eboutique/modifier_mdp.html", {'errors': errors})
    
    return render(request, "eboutique/modifier_mdp.html")



 

def parametre(request):
    errors = []
    user_info = None   
    
    if not request.user.is_authenticated:
        return redirect('loginn')

    
    try:
        u_profil = user_profil.objects.get(author=request.user)
    except user_profil.DoesNotExist:
       
        u_profil = user_profil(author=request.user)  
        u_profil.save()

    if request.method == 'POST':
        user_profil_image = request.FILES.get('image')

        if user_profil_image is None:
            errors.append('Veuillez sélectionner une image.')
        else:
            u_profil.user_profil = user_profil_image
            u_profil.save()
            return redirect('parametre')

     
    profil_image = None
    if u_profil.user_profil and u_profil.user_profil.name:   
        profil_image = u_profil.user_profil.url  

    user_info = request.user

    return render(request, "eboutique/parametre.html", {
        'profil': u_profil,
        'profil_image': profil_image,  
        'errors': errors,
        'user_info': user_info 
    })





def profil(request):
    if not request.user.is_authenticated:
        return redirect('loginn')
    
    user=request.user
    
    if user:
        
        cart_de_credit=Cart_de_credit.objects.filter(user_mail=user.email).first()
        
        if cart_de_credit is not None:
            return render(request,"eboutique/profil.html",{'user':user,'cart_de_credit':cart_de_credit})
    
    return render(request,"eboutique/profil.html",{'user':user})

def recherche(request):
    if not request.user.is_authenticated:
        return redirect('loginn')
    else:
        articles=[]
        query=" "
        
        if request.method == "POST":
            query=request.POST.get("rec")
            if query:
                  articles=Article.objects.filter(article_title__icontains=query)
        
        return render(request,"eboutique/recherche.html",{'article':articles,'query':query})
                

def singup(request):
    if request.user.is_authenticated:
        return redirect('index')

    errors = []

    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        name = request.POST.get('nom')
        firstname = request.POST.get('prenom')
        password = request.POST.get('mdp1')
        confirmpassword = request.POST.get('mdp2')

         
        if password != confirmpassword:
            errors.append('Les deux mots de passe ne correspondent pas.')

         
        try:
            validate_email(email)
        except ValidationError:
            errors.append('L\'email est invalide.')

         
        try:
            validate_password(password)
        except ValidationError as e:
            errors.append(str(e))   

         
        if User.objects.filter(username=username).exists():
            errors.append('Le nom d\'utilisateur existe déjà.')

        
        if User.objects.filter(email=email).exists():
            errors.append('L\'email existe déjà.')

        
        if not errors:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=name,
                last_name=firstname
            )
            errors.append('Inscription réussie.')
            return redirect('loginn')

    return render(request, "eboutique/singup.html", {'errors': errors})


def sup_art(request,article_id):
    if not request.user.is_authenticated:
        return redirect('loginn')
    article=Article.objects.get(article_id=article_id)
    return render(request,"eboutique/sup_art.html",{'article':article})



def carte_de_credit(request):
    
    if not request.user.is_authenticated:
        return redirect('loginn')
    if request.method  == 'POST':
        errors=[]
        
        number = request.POST.get('number')
        name = request.POST.get('name')
        date = request.POST.get('date')
        cvv = request.POST.get('cvv')
        
        
        try:
            cart=Cart_de_credit.objects.get(card_number=number,card_name=name,expiration=date,cvv=cvv)
            if  cart.user_mail:
                errors.append(' la carte  est deja utiliser ')
                return render(request,"eboutique/carte_de_credit.html",{'errors':errors})
            else:
                cart.user_mail=request.user.email
            cart.save()
            return redirect('profil')
        
        except Cart_de_credit.DoesNotExist:
            
            errors.append('les information de la carte ne correspond pas   ')
            
            return render(request,"eboutique/carte_de_credit.html",{'errors':errors})
    return render(request,"eboutique/carte_de_credit.html")
            


def det_carte(request):
    if not request.user.is_authenticated:
        return redirect('loginn')

    user = request.user

    
    if user:
         
        cart_de_credit = Cart_de_credit.objects.filter(user_mail=user.email).first()

        if cart_de_credit:
             
            transaction = Transaction.objects.filter(Cart_de_credit=cart_de_credit)

            
            context = {
                'user': user,
                'cart_de_credit': cart_de_credit,
                'transaction': transaction if transaction.exists() else None
            }
        

        return render(request, "eboutique/det_carte.html", context)

    
    return render(request, "eboutique/det_carte.html", {'user': user})
        




def logoutt(request):
    logout(request)
    return redirect('loginn')




def conf_sup(request,article_id):
    if not request.user.is_authenticated:
        return redirect('loginn')
    Article.objects.filter(article_id=article_id).delete()
    return redirect( 'mes_article' )
    



def statut_art(request,article_id):
    if not request.user.is_authenticated:
        return redirect('loginn')
    try:
        article=Article.objects.get(article_id=article_id)
    except Article.DoesNotExist:
        return redirect('mes_article')
    
    if not article.user_delete:
        article.user_delete=True
        article.save()
        return redirect('mes_article')
    else :
        article.user_delete=False
        article.save()
        return redirect('mes_article')
    
    
    

def nous_contacter(request):
    
    return render(request,"eboutique/nous_contacter.html")




def pageerreur(request, exception=None):
     
     
    return render(request, 'eboutique/pageerreur.html', status=500)