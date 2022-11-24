from django.db import models


# Creation de la table "produits"
class Produit(models.Model):
    nom = models.CharField(max_length=100, null=False)
    prix = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    description = models.TextField(max_length=1000, null=False)
