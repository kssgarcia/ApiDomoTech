from django.shortcuts import render

# Create your views here.

def Lobby(request):
    print(request)
    return render(request, 'chat/lobby.html')
