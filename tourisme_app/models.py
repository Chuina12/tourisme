from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)  # auto_now_add remplit automatiquement la date lors de l'insertion

    def __str__(self):
        return self.nom_categorie


class Service(models.Model):
    pays = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    description = RichTextField()  # Utilisation de CKEditor pour le champ de description
    date = models.DateField()
    image_couverture = models.ImageField(upload_to='couverture_image',blank=True, null=True)

    def __str__(self):
        return f"{self.pays} - {self.prix} €"
    
    
class Presentation(models.Model):
    # Définition des champs du modèle
    intitule = models.CharField(max_length=100)
    titre = models.CharField(max_length=200)
    date = models.DateField()
    description = RichTextField()
    image = models.ImageField(upload_to='presentations_images/',blank=True, null=True)  # Nouveau champ image


    def __str__(self):
        return self.intitule

    class Meta:
        verbose_name = "Présentation"
        verbose_name_plural = "Présentations"
        
from django.db import models
from django.utils import timezone

from django.utils.text import slugify

class Article(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(max_length=200)
    content = RichTextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='articles_images/', blank=True, null=True)  # Nouveau champ image

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Génère un slug à partir du titre
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="replies")

    def __str__(self):
        return f"Comment by {self.author} on {self.article.title}"


from django.contrib import admin
from .models import Categorie

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom_categorie', 'date')  # Affiche les colonnes nom_categorie et date dans la liste d'admin
    search_fields = ('nom_categorie',)        # Permet la recherche par nom de catégorie
    list_filter = ('date',)                   # Ajoute un filtre pour la date

    # Vous pouvez aussi ajouter d'autres options selon vos besoins, par exemple :
    ordering = ('-date',)                     # Trie par date décroissante


# class pour l'administration de la baniere de l'accueil
class Baniere(models.Model):
    title=models.CharField(max_length=1000)
    content=RichTextField()
    image=models.ImageField(upload_to="baniere")
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


#class pour l'administration des destinations
class Activity(models.Model):
    name=models.CharField(max_length=250)
    description=RichTextField()
    image=models.ImageField(upload_to="activity")
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class BaniereDestination(models.Model):
    title=models.CharField(max_length=500)
    content=RichTextField()
    image=models.ImageField(upload_to="banieredestination")
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Destination(models.Model):
    title=models.CharField(max_length=250)
    price=models.IntegerField()
    description=RichTextField()
    image=models.ImageField(upload_to="destination")
    date=models.DateTimeField(default=timezone.now)

    activities=models.ManyToManyField(Activity, related_name="destinations")
    baniereDestination=models.ManyToManyField(BaniereDestination, related_name="destinations")
    
    def __str__(self):
        return self.title
    
    
class LegalDocument(models.Model):
    DOCUMENT_TYPES = [
        ('privacy_policy', 'Politique de confidentialité'),
        ('terms_of_use', 'Conditions d\'utilisation'),
        ('legal_notice', 'Mentions légales'),
    ]

    title = models.CharField(max_length=255, choices=DOCUMENT_TYPES, unique=True)
    date = models.DateField(null=True, blank=True)  # Optionnel pour les documents autres que Politique de confidentialité
    content = RichTextField()

    def __str__(self):
        return dict(self.DOCUMENT_TYPES).get(self.title, self.title)

    class Meta:
        verbose_name = "Document juridique"
        verbose_name_plural = "Documents juridiques"