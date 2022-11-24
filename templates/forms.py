from django.forms import ModelForm

from ajoutProduitCatalogue.models import *


class frmAjoutProduit(ModelForm):
    class Meta:  # créer une classe dans une classe$
        model = Produit
        fields = ['nom', 'prix', 'description']
        labels = {
            'nom': 'Nom',
            'description': 'Description',
            'prix': 'Prix '
        }
