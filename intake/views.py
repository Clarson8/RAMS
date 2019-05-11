from django.shortcuts import render, redirect
from people.forms import OwnerForm
from people.views import owner_detail

# Create your views here.
def intake_landing(request):
    return render(request, 'intake_landing.html')

def intake_owned(request, reporter_pk=None):
    if request.POST:
        form = OwnerForm(request.POST)
        owner = form.save()
        return redirect('people:owner_detail', owner.pk)
    form = OwnerForm()
    return render(request, 'owner_edit.html', {'form':form})

