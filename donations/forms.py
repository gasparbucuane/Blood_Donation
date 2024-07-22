from django import forms
from .models import Donor, Donation, ChoicesBloodType

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ('name','identification', 'blood_type', 'birth_day')
        
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['blood_type'].widget.attrs.update({'placeholder': 'Escolha o seu tipo sanguineo'})
        self.fields['birth_day'].widget.attrs.update({'placeholder': 'Insira a sua data de nascimento'})
        self.fields['identification'].widget.attrs.update({'placeholder': 'Insira o numero de BI'})


            

   