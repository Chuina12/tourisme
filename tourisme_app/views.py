from django.shortcuts import render,redirect
from .models import Service,Presentation,Article, Comment,Categorie,Baniere,Activity,BaniereDestination,Destination,LegalDocument
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def index(request):
    service = Service.objects.all()
    presentations = Presentation.objects.all().order_by('-date')
    baniere = Baniere.objects.all()
    activity = Activity.objects.all()
    baniereDestination = BaniereDestination.objects.all()
    destination=Destination.objects.all()
    legal = LegalDocument.objects.all()
    return render(request,'index.html',
    {'service':service,
    'presentations': presentations,
    'baniere':baniere,
    'destination':destination,
    'legal':legal
    })

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contacts.html')

def destination_details(request, pk):
    activity = Activity.objects.all()
    baniereDestination = BaniereDestination.objects.all()
    destination=get_object_or_404(Destination, pk=pk)
    return render(request,'destination_details.html', {'destination':destination})

def shop(request):
    return render(request,'shop.html')

def egypte_destination(request):
    return render(request,'egypte_destination.html')

def dubai_destination(request):
    return render(request,'dubai_destination.html')

def maldives_destination(request):
    return render(request,'maldives_destination.html')

def zanzibar_destination(request):
    return render(request,'zanzibar_destination.html')

def zanzi(request):
    return render(request, 'zanzi.html')

def uganda_safari(request):
    return render(request,'uganda_safari.html')

def kenya_safari(request):
    return render(request,'kenya_safari.html')

def tanzania_safari(request):
    return render(request,'tanzania_safari.html')


# def service_detail(request, pk):
#     service = get_object_or_404(Service, pk=pk)
#     service_detail = Presentation.objects.all()
#     return render(request, 'service_detail.html', {'service': service,'service_detail':service_detail})


def presesentation_detail(request, pk):
    detail_pres = get_object_or_404(Presentation, pk=pk)
    return render(request, 'presesentation_detail.html', {'detail_pres': detail_pres})


def request_devis(request):
    devis = Service.objects.all()

    if request.method == "POST":
        # Récupérer les données du formulaire
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        destination = request.POST.get('destination')
        prix = request.POST.get('prix')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        num_adults = request.POST.get('num_adults')
        num_minors = request.POST.get('num_minors')
        num_babies = request.POST.get('num_babies')
        details = request.POST.get('details')

        # Email pour l'administrateur
        subject_admin = f"New Quote Request from {name}"
        message_admin = f"""
        You have received a new quote request with the following details:

        Full Name: {name}
        Email: {email}
        Phone: {phone}
        Country: {country}
        Destination: {destination}
        Price: {prix}
        Start Date: {start_date}
        End Date: {end_date}
        Number of Adults: {num_adults}
        Number of Minors: {num_minors}
        Number of Babies: {num_babies}

        Additional Details:
        {details}
        """
        send_mail(
            subject_admin,
            message_admin,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        # Préparer l'email HTML pour le client
        subject_client = "Confirmation of Your Quote Request"
        html_content = render_to_string('emails/email_template_client.html', {
            'name': name,
            'email': email,
            'phone': phone,
            'country': country,
            'destination': destination,
            'prix': prix,
            'start_date': start_date,
            'end_date': end_date,
            'num_adults': num_adults,
            'num_minors': num_minors,
            'num_babies': num_babies,
            'details': details,
        })
        text_content = strip_tags(html_content)  # Contenu en texte brut

        # Email HTML avec pièce jointe
        email_client = EmailMultiAlternatives(subject_client, text_content, settings.DEFAULT_FROM_EMAIL, [email,'thierry.devp@gmail.com'])
        email_client.attach_alternative(html_content, "text/html")
        email_client.send()
        from django.contrib import messages
        messages.success(request,'Thank you for your reservation. We will contact you as soon as possible.')
        return redirect('request_devis')

    return render(request, 'request_devis.html', {'devis': devis})

def booking(request,pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request,'booking.html', {'service': service})




def payment_success(request):
    return render(request, 'payment_success.html')

def payment_failed(request):
    return render(request, 'payment_failed.html')

# def blog(request):
#     return render(request, 'blog.html')


def detail(request):
    return render(request, 'detail.html')


def blog(request):
    articles = Article.objects.all().order_by('-created_at')
    categorie = Categorie.objects.all()
    return render(request, 'blog.html', {'articles': articles,'categorie':categorie})

def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    articles = Article.objects.all().order_by('-created_at')
    categorie = Categorie.objects.all()
    comments = article.comments.filter(parent=None).order_by('-created_at')  # commentaires sans parent
    return render(request, 'detail.html', {'article': article, 'articles': articles,'categorie':categorie})


def articles_par_categorie(request, category_id):
    categories = get_object_or_404(Categorie, id=category_id)
    articles = Article.objects.filter(categorie=categories)  # Filtre les articles de la catégorie
    categorie = Categorie.objects.all()  # Récupère toutes les catégories pour le menu latéral
    return render(request, 'articles_par_categorie.html', {'articles': articles, 'categorie': categorie, 'selected_category': categories})


def legaldocument(request, document_type):
    # Récupérer le document en fonction de son type
    document = get_object_or_404(LegalDocument, title=document_type)
    
    # Passer les données au modèle
    return render(request, 'legaldocument.html', {'document': document})

def test(request):
    return render(request,'test.html')