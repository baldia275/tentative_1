from django.shortcuts import render,redirect
from ajoutProduitCatalogue.models import *
from templates.forms import *



# Create your views here.
def index(request):
    return render(request, "index.html")


def listeProduits(request):
    tous_les_produits = Produit.objects.all()

    contenu = {"Produits": tous_les_produits}

    return render(request, "listeProduits.html", contenu)

def ajoutProduit(request):

    if request.method == "POST":
        form = frmAjoutProduit(request.POST)
        if form.is_valid():
            nv_produit = Produit()
            nv_produit.nom = form.cleaned_data['nom']
            nv_produit.description = form.cleaned_data['description']
            nv_produit.prix = form.cleaned_data['prix']
            nv_produit.save()
            return redirect("afficher_produit")
        else:
            print("Erreur, le formulaire n'est pas valide")

    else:
        form = frmAjoutProduit()
    contenu ={"formulaire" : form}

    return render(request,"ajoutProduit.html", contenu)
