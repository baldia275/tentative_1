from django.shortcuts import render
from ajoutProduitCatalogue.models import *


# Create your views here.
def index(request):
    return render(request, "index.html")


def listeProduits(request):
    tous_les_produits = Produit.objects.all()

    contenu = {"Produits": tous_les_produits}

    return render(request, "listeProduits.html", contenu)

def ajoutProduit(request):

    return render(request,"ajoutProduit.html")
