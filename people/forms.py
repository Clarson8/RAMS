import re
from django import forms
from people.models import Owner, TeamMember
from django.core.validators import RegexValidator

NAME_REGEX = re.compile(r'[A-Za-z ]+')
NAME_ERROR = "Invalid Input: Non-Letter Characters Found"

PHONE_REGEX = re.compile(r'\(?\d{3}\)?\-?\d{3}\-?\d{4})')
PHONE_FORM_ERROR = "Invalid Input: Use Following Formats (xxx)-xxx-xxxx OR xxxxxxxxxx "



class OwnerForm(forms.ModelForm):
    
    class Meta:
    model = Owner
    fields = [ 'first_name', 'last_name', 'home_phone', \
        'work_phone', 'cell_phone', 'best_contact', \
        'drivers_license', 'address', 'apartment', 'city', \
        'state', 'zip_code', ]

  
    def clean_first_name(self):
        fname = self.cleaned_data['first_name']
        if not re.match(NAME_REGEX, fname):
            raise validation_error(NAME_ERROR)
        return fname
    
    def clean_last_name(self):
        lname = self.cleaned_data['last_name']
        if not re.match(NAME_ERROR, lname):
            raise validation_error(NAME_ERROR)
        return lname
    
    def clean_home_phone(self):
        hphone = self.cleaned_data['home_phone']
        if not re.match(PHONE_REGEX, hphone):
            raise validation_error(PHONE_FORM_ERROR)
        return hphone
    
    def clean_work_phone(self):
        wphone = self.cleaned_data['work_phone']
        if not re.match(PHONE_REGEX, wphone):
            raise validation error(PHONE_FORM_ERROR)
        return wphone
    
    def clean_cell_phone(self):
        cphone = self.cleaned_data['cell_phone']
        if not re.match(PHONE_REGEX, cphone):
            raise validation_error(PHONE_FORM_ERROR)
        return cphone
    
    def clean_city(self):
        city = self.cleaned_data['city']
        if not re.match(NAME_REGEX, city):
            raise validation_error(NAME_ERROR)

    def clean_zip(zip):
        zip = self.cleaned_data['zip_code']
        if not zip.isdigit():
            raise validation_error("Invalid Input: Non-Numerical Characters Found")

class ReporterForm(forms.ModelForm):

    class Meta:
        model = Owner
        fields = [ 'first_name', 'last_name', 'home_phone', \
            'work_phone', 'cell_phone', 'best_contact', \
            'drivers_license', 'address', 'apartment', 'city', \
            'state', 'zip_code', ]


class TeamMemberForm(forms.ModelForm):

    class Meta:
        model = TeamMember
        fields = ['first_name', 'last_name', 'cell_phone', 'agency_id']