from django.shortcuts import render
from .models import Agent
def agents(request):
    all_agents = Agent.objects.all()
    return render(request, 'agents/agents.html', {'all_agents':all_agents})
