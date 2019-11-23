from django.shortcuts import get_object_or_404, render, redirect

from shelter.models import Shelter, Building, Room, Cage
from shelter.forms import ShelterForm, BuildingForm, RoomForm, CageForm

OBJ_TYPE_DICT = {
    'building': (Building, 'shelter:shelter_detail'),
    'room': (Room, 'shelter:building_detail'),
    'cage': (Cage, 'shelter:room_detail'),
}

# Create your views here.
def shelter_landing(request):
    return render(request, 'shelter_landing.html')

def shelter_list(request):
    shelter_list = Shelter.objects.all()
    return render(request, 'shelter_list.html', {'shelter_list':shelter_list})

def shelter_detail(request, pk):
    shelter = get_object_or_404(Shelter, pk=pk)
    return render(request, 'shelter_details.html', {'shelter':shelter})

def shelter(request, pk=None):
    instance = Shelter.objects.get(pk=pk) if pk else None
    form = ShelterForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('shelter:shelter_list')
    return render(request, 'shelter.html', {'form':form})

def building_detail(request, pk):
    building = get_object_or_404(Building, pk=pk)
    return render(request, 'building_details.html', {'building':building})

def building(request, shelter_pk, pk=None):
    instance = Building.objects.get(pk=pk) if pk else None
    shelter = Shelter.objects.get(pk=shelter_pk)
    form = BuildingForm(shelter, request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('shelter:shelter_detail', shelter_pk)
    return render(request, 'building.html', {'form':form})

def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'room_details.html', {'room':room})

def room(request, building_pk, pk=None):
    instance = Room.objects.get(pk=pk) if pk else None
    building = Building.objects.get(pk=building_pk)
    form = RoomForm(building, request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('shelter:building_detail', building_pk)
    return render(request, 'room.html', {'form':form})

def cage_detail(request, pk):
    cage = get_object_or_404(Cage, pk=pk)
    return render(request, 'cage_details.html', {'cage':cage})

def cage(request, room_pk, pk=None):
    instance = Cage.objects.get(pk=pk) if pk else None
    room = Room.objects.get(pk=room_pk)
    form = CageForm(room, request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('shelter:room_detail', room_pk)
    return render(request, 'cage.html', {'form':form})

def shelter_object_delete(request, obj_type, pk):
    obj = OBJ_TYPE_DICT[obj_type][0].objects.get(pk=pk)
    parent = obj.parent
    obj.delete()
    return redirect(OBJ_TYPE_DICT[obj_type][1], parent.pk)
