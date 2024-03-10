from django.shortcuts import render
import os
import joblib
#from . personalityclassifier import *

# Create your views here.
def home(request):

    return render(request, "index.html", {})

def predict(request):
    if request.method == 'POST':
        my_writing = request.POST.get('textual')

       # my_posts = my_writing[0].split('|||')
       # len(my_posts)

       # trait=tellmemyMBTI(my_posts, 'Divy')

        context = {
            'predicted_text': trait,
        }


    return render(request, "index.html", context)