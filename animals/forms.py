from django import forms
from animals.models import Animal
from animals.choices import ANIMAL_LOOKUP_DICT
from location.forms import LocationForm

class AnimalForm(LocationForm):

    collar_info = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}))
    behavior_notes = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}))
    chip_info = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}))
    diet_notes =forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}))
    med_notes = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}))
    image = forms.ImageField(required=False)

    def __init__(self, species, owner=None, *args, **kwargs):
        super(AnimalForm, self).__init__(owner, *args, **kwargs)
        self.fields['species'].initial = species
        self.fields['pcolor'].choices = ANIMAL_LOOKUP_DICT[species]['pcolor']
        self.fields['scolor'].choices = ANIMAL_LOOKUP_DICT[species]['scolor']
        self.fields['markings'].choices = ANIMAL_LOOKUP_DICT[species]['markings']
        self.fields['owner'].initial = owner
        if owner:
            self.set_initial_location(owner)

    class Meta:
        model = Animal
        exclude = ('latitude', 'longitude', 'request')
        widgets = {'owner': forms.HiddenInput()}
        