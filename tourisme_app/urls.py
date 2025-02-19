from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contacts',views.contact,name='contacts'),
    path('destination_details/<int:pk>/', views.destination_details, name='destination_details'),
    # path('service/<int:pk>/', views.service_detail, name='service_detail'),
    path('presesentation_detail/<int:pk>/', views.presesentation_detail, name='presesentation_detail'),
    path('request_devis',views.request_devis,name='request_devis'),
    path('booking/<int:pk>',views.booking,name='booking'),
    path('egypte_destination',views.egypte_destination,name='egypte_destination'),
    path('dubai_destination',views.dubai_destination,name='dubai_destination'),
    path('maldives_destination',views.maldives_destination,name='maldives_destination'),
    path('zanzibar_destination',views.zanzibar_destination,name='zanzibar_destination'),
    path('zanzi', views.zanzi, name='zanzi'),
    path('uganda_safari',views.uganda_safari,name='uganda_safari'),
    path('kenya_safari',views.kenya_safari,name='kenya_safari'),
    path('tanzania_safari',views.tanzania_safari,name='tanzania_safari'),
    path('shop',views.shop,name='shop'),
    path('paiement/succes/', views.payment_success, name='payment_success'),
    path('paiement/echec/', views.payment_failed, name='payment_failed'),
    path('blog', views.blog, name='blog'),
    path('detail/<int:article_id>', views.detail, name='detail'),
    path('categorie/<int:category_id>/', views.articles_par_categorie, name='articles_par_categorie'),
    path('legaldocument/<str:document_type>/', views.legaldocument, name='legaldocument'),
    path('test',views.test)
]
