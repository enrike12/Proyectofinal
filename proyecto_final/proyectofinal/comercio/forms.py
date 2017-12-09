from django import forms

from .models import Burritos

class BurritosModelForm(forms.ModelForm):
    tamano = forms.CharField(label='',
                              widget=forms.Textarea(
                                        attrs={'placeholder':"Burritos",
                                               'class': "textarea"}
                              ))
    class Meta:
        model = Burritos
        fields = [
            "tamano", "descripcion", "ingredientes", "precio"
]
