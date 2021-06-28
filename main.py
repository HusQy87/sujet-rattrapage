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


bottle.run(host='127.0.0.1', port=6969, reloader=True)
