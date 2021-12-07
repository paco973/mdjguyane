from django.shortcuts import render, redirect
from lxml import etree

# Create your views here.
from base.models import Study


def formation(request):
    tree = etree.parse("./Onisep_Ideo_Fiches_Formations_18102021.xml")
    for user in tree.xpath("formation/libelle_complet"):
        try:
            Study.objects.get(name=user.text)
        except:
            study = Study.objects.create(name=user.text)
            study.save()

    return redirect('home')
