# admin.py

from django.contrib import admin
from .models import Service,Presentation,Baniere,BaniereDestination,Activity,Destination, LegalDocument

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('pays', 'prix', 'date')
    search_fields = ('pays',)


class PresentationAdmin(admin.ModelAdmin):
    # Liste des champs à afficher dans la vue principale de l'admin
    list_display = ('intitule', 'titre', 'date', 'short_description','image')
    list_filter = ('date',)  # Ajout d'un filtre par date
    search_fields = ('intitule', 'titre')  # Ajout de champs de recherche
    ordering = ('-date',)  # Trier par date décroissante
    # Champs à afficher lors de l'édition ou de l'ajout d'un enregistrement
    fields = ('intitule', 'titre', 'date', 'description','image')

    def short_description(self, obj):
        """Méthode pour afficher une version tronquée de la description."""
        return obj.description[:75] + '...' if len(obj.description) > 75 else obj.description
    short_description.short_description = "Description courte"
    

admin.site.register(Presentation, PresentationAdmin)


from django.contrib import admin
from .models import Article, Comment

# Class d'administration pour l'article
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')  # Colonnes à afficher dans la liste
    list_filter = ('created_at', 'author')  # Filtres sur les articles
    search_fields = ('title', 'content', 'author')  # Recherche par titre, contenu et auteur
    ordering = ('-created_at',)  # Tri par date de création, du plus récent au plus ancien
    prepopulated_fields = {'slug': ('title',)}  # Générer automatiquement un slug à partir du titre

# Class d'administration pour les commentaires
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'article', 'parent', 'created_at')  # Colonnes à afficher dans la liste
    list_filter = ('created_at', 'author')  # Filtres sur les commentaires
    search_fields = ('author', 'content')  # Recherche par auteur et contenu
    ordering = ('-created_at',)  # Tri par date de création, du plus récent au plus ancien
    raw_id_fields = ('parent',)  # Utiliser un champ "recherche" pour les commentaires parents

# Enregistrer les modèles et leurs classes d'administration
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)


#class d'administration pour la baniere
@admin.register(Baniere)
class BaniereAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image', 'date')


#class d'administration des destinations
@admin.register(BaniereDestination)
class BaniereDestinationAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image', 'date')


@admin.register(Activity)
class AtivityAdmin(admin.ModelAdmin):
    lsit_display = ('name', 'description', 'image', 'date')


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'description', 'image', 'date')
    
@admin.register(LegalDocument)
class LegalDocumentAdmin(admin.ModelAdmin):
    list_display = ('get_title_display', 'date', 'content_snippet')
    list_filter = ('title', 'date')
    search_fields = ('title', 'content')
    ordering = ('date',)

    def get_title_display(self, obj):
        return dict(LegalDocument.DOCUMENT_TYPES).get(obj.title, obj.title)
    get_title_display.short_description = "Type de document"

    def content_snippet(self, obj):
        return obj.content[:50] + "..." if obj.content else "Pas de contenu"
    content_snippet.short_description = "Aperçu du contenu"
