from django.shortcuts import render
from MyConvertisseur.forms import ConvertDevise
from MyConvertisseur.Convertisseur import Convertisseur

def showForm(request):
    form_convert = ConvertDevise()
    new_amount = 0.0
    unitee1 = ''
    unitee2 = ''
    
    if request.method == "POST":
        form_convert = ConvertDevise(request.POST)
        if form_convert.is_valid():
            amount1 = form_convert.cleaned_data['amount_to_convert']
            unitee1 = form_convert.cleaned_data['initial_unitee']
            unitee2 = form_convert.cleaned_data['unitee_of_conversion']
            convertisseur1 = Convertisseur(amount1, unitee1, unitee2)
            new_amount = convertisseur1.convertir_devise()
            message = "amount converted succefully !"
        else:
            message = "form is not valid !"
            
    else:
        message = "method is not post !"
        

    return render(request,
                  'MyConvertisseur/form_convert.html',
                  {'form_convert':form_convert,
                   'message':message,
                   'new_amount':new_amount,
                   'unitee1':unitee1,
                   'unitee2':unitee2})

