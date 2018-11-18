from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewIdForm
import browser_cookie3
import facebook
import requests
import sqlite3
# Create your views here.


from django import forms


def index(request):
    return render(request, "upload/main.html")


def addnewid(request):
    print("ADDNEWID РАБОТАЕТ!")
    f = open('ids.txt', 'a')
    if request.method == "POST":
        message = request.POST["addnewid"]
        f.write(message)
    f.write("\n")
    f.close()
    return render(request, "upload/main.html")


def check_exist_user_by_id(request):
    print("Я ТУТ РАБОТАЮ ТАК ТО!!!!!!!!")
    sess = requests.Session()
    sess.cookies = browser_cookie3.chrome()
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (id VARCHAR(100), existence VARCHAR(15))')
    con.commit()
    newIds = open("ids.txt", 'r').readlines()
    for id in newIds:
        id = id.strip()
        cur.execute("insert into users values (?, null)", [id])
    con.commit()

    # with open("ids", 'w') as f:
    #     f.write('')

    ids = cur.execute('SELECT id FROM users').fetchall()

    graph = facebook.GraphAPI('1938851329475559|9N7KF0F4LokFujG_oTibHwz3YwM')

    for id in ids:
        id = id[0].strip()
        existence = False
        if id.isdigit():
            try:
                graph.get_object(id)
                existence = True
            except Exception as e:
                existence = False
        else:
            resp = sess.get('https://www.facebook.com/{}'.format(id))
            # open(f'{time.time()}.html', 'w', encoding='UTF-8').write(resp.text)
            if ('Sorry, this content' in resp.text) or ('not found' in resp.text) or ("не найдена" in resp.text):
                existence = False
            else:
                existence = True
        existence = 'Exists' if existence else 'Not exists'
        cur.execute('update users set existence = "{}" where id == "{}"'.format(existence, id))
    con.commit()
    return render(request, "upload/main.html")
