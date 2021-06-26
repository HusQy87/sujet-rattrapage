# -*- coding: utf-8 -*-
import bottle
import string
import mysql.connector

conn = mysql.connector.connect(host="galcera.ovh", user='lesRattrapeurs', password="OnDitMerciQuiPourLeZéro", database="Base_sujet_test")
c = conn.cursor()

@bottle.route('/', method='GET')
@bottle.route('/<SahTuMetCeQueTuVeux>', method='GET')
def index(SahTuMetCeQueTuVeux=None):
    if SahTuMetCeQueTuVeux is None:
        return {'errror': False, "message": f"Écris un truc dans l'url wsh"}
    return {"error": False, "message": f"Ta daronne la grosse {SahTuMetCeQueTuVeux}"}


@bottle.route('/cookie/set' , method='GET')
def setCookie():
    bottle.response.set_cookie('connard', 'caca')
    return {"error": False, "message": "le cookie a bien été set"}


@bottle.route('/cookie/read', method='GET')
def getCookie():
    print(bottle.request.get_cookie('connard'))



bottle.run(host='127.0.0.1', port=6969, reloader=True)
