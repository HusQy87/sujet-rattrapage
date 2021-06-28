# Étape 1 - prérequis

- Python d'installer min 3.x
- Bottle
  `pip install bottle` ou `python -m pip install --upgrade pip`
- Postman
- Sql-connector puour python `python -m pip install mysql-connector-python`



# Exo 1 GET et paramètres

Écriver une fonction qui prend un mot en paramètre et renvoie une erreur si le mot fait plus de 10 caractère `/testlongueur/<leMotATester>`
  - Astuce : on récupere la longeur d'une chaine de caractère `len(chaineATester)` 


# Exo 2 Définition et lecture de cookie

Une fonction qui écrit crée un cookie "connard" vous utiliserer une route qui prendra le nom du cookie connard a définir la route sera `/cookie/set/`
- Astuce : on attribut un cookie de cette facon `bottle.response.set_cookie("leNomDuCookie", "LaValeurDuCookie")`

Puis une fonction qui affichera ce cookie a l'utilisateur avec la route `/cookie/read/<nomDuCookie>`
- Astuce : `bottle.request.get('leNomDuCookie)` Récupère le cookie



# Exo 3 POST et base de données

  Envoyer une requête post qui prend un nom d'utilisateur et un mot de passe en paramètres
  puis elle devra vous retourner l'adresse email lié à cette utilisateur
