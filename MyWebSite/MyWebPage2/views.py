from django.shortcuts import render, render_to_response
import sqlite3
# Create your views here.

def index(request):
    # логика работы с данными
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    data = cur.execute('SELECT * FROM user')
    # упаковываешь контекст
    context = {'table_in_html': data}
    return render_to_response("mywebpage2/main.html", context)
