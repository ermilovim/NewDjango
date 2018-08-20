from django.shortcuts import render, render_to_response
from django.http import HttpResponse

from .forms import NameForm

import sqlite3
# Create your views here.

def index(request):
    # логика работы с данными
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    data = cur.execute('SELECT * FROM users')
    # упаковываешь контекст
    context = {'table_in_html': data}
    return render_to_response("mywebpage2/main.html", context)


def addnewid(request):
    f = open('ids.txt', 'a')
    if 'add_new_id' in request.GET:
        message = 'You searched for: %r' % request.GET['add_new_id']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
