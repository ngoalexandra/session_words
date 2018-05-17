from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, strptime, localtime
from datetime import datetime

def index(request):
    if 'words' not in request.session:
        request.session['words'] = []
    return render(request, 'first_app/index.html')
    
def process(request):
    # this is saying, if the checkbox is checked, meaning if it's posted, then you set it to true, otherwise you have it to false
    if 'bigfont' in request.POST:
        checkbox = True
    else:
        checkbox = False

    # the reason why we set sessions within a variable is because django doesn't let you append to session.
    temp_list = request.session['words']
    temp_list.append({
        'new_word': request.POST['new_word'],
        'color': request.POST['color'],
        "bigfont" : checkbox,
        'date': strftime("%B %d, %Y %H:%M %p", gmtime()),
    })

    request.session['words'] = temp_list
    return redirect('/')

def clear(request):
    request.session.flush()
    return redirect('/')
    # if request.method == 'POST':
    #     request.session['name'] = request.POST['name']
    #     request.session['color'] = request.POST['color']
    #     request.session['bigfont'] = request.POST['bigfont']

# Create your views here.
