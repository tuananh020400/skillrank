from django.shortcuts import render

# Create your views here.
def create_challenge(request):
    return render(request, 'challenges/create_challenge.html')