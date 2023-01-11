from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'streams.html')

def quiz(request):
    return render(request, 'room.html')