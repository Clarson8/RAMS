from django.shortcuts import render, redirect
from evac.models import EvacTeam
from evac.forms import EvacTeamForm
from people.models import TeamMember
from people.forms import TeamMemberForm
# Create your views here.
def evac_landing(request):
    return render(request, 'evac_landing.html', {})

def evac_team(request, pk=None):
    evac_team = EvacTeam.objects.get(pk=pk) if pk else None
    form = EvacTeamForm(request.POST or None, instance=evac_team)
    if request.POST and form.is_valid():
        form.save()
        return redirect('evac:evac_landing')
    return render(request, 'evac_team.html', {'form':form})

def team_member(request, pk=None):
    team_member = TeamMember.objects.get(pk=pk) if pk else None
    form = TeamMemberForm(request.POST or None, instance=team_member)
    if request.POST and form.is_valid():
        form.save()
        return redirect('evac:evac_landing')
    return render(request, 'team_member.html', {'form':form})
