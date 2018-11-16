from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# from .forms import NewIdForm


from django import forms


def index(request):

    f = open('ids.txt', 'w')
    if request.method == "POST":
        message = request.POST["addnewid"]
        f.write(message)
    f.close()
    return render(request, "upload/main.html")


def addnewid(request):
    f = open('ids.txt', 'w')
    x = "123"
    form = NewIdForm(request.POST or None)
    if request.method == "POST":
        print("213adguqhegluqhuiqhtio32ito2i3to2;ty23tihy38yt34ty38434yt8qhio8yhgoiy84")
    """
    if 'addnewid' in request.POST:
        message = 'You searched for: %r' % request.POST['addnewid']
        f.write(x)
    else:
        message = 'You submitted an empty form.'
    """
    f.close()
    return HttpResponse(message)
