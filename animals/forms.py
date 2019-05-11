from django import forms
from animals.models import Animal

class DogForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DogForm, self).__init__(*args, **kwargs)
        self.initial['species'] = 'dog'

    class Meta:
        model = Animal
        labels = {
            "pcolor" : "Dog Primary Color",
            "scolor" : "Dog Secondary Color",
            "markings" : "Dog Markings",
        }

        exclude = ('latitude', 'longitude', 'request', 'owner')

class CatForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CatForm, self).__init__(*args, **kwargs)
        self.initial['species'] = 'cat'

    class Meta:
        model = Animal
        labels = {
            "pcolor" : "Cat Primary Color",
            "scolor" : "Cat Secondary Color",
            "markings" : "Cat Markings",
        }

        exclude = ('latitude', 'longitude', 'request', 'owner')

class OtherForm(forms.ModelForm):

    class Meta:
        model = Animal
        labels = {
            "pcolor" : "Primary Color",
            "scolor" : "Secondary Color",
            "markings" : "Markings",
        }

        exclude = ('latitude', 'longitude', 'request', 'owner')