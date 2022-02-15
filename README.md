# api_livres_categories_iai
API GESTION DE BIBLIOTHEQUES
Pour commencer
Installation des Dépendances
Python 3.10.0
pip 22.0.2 from C:\Users\azerty\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)

Suivez les instructions suivantes pour installer la dernière version de python sur la plateforme python docs
Dépendances de PIP

Pour installer les dépendances exécuter la commande suivante:

pip install -r requirements.txt
or
pip3 install -r requirements.txt

Ceci va entrainer  l'installation de tous les packages se trouvant dans le fichier requirements.txt.
clé de Dépendances

    Flask est un petit framework web Python léger, qui fournit des outils et des fonctionnalités utiles qui facilitent la création d’applications web en Python.

    SQLAlchemy est un toolkit open source SQL et un mapping objet-relationnel écrit en Python et publié sous licence MIT. SQLAlchemy a opté pour l'utilisation du pattern Data Mapper plutôt que l'active record utilisés par de nombreux autres ORM

   
Démarrer le serveur

Pour démarrer le serveur sur Linux ou Mac, executez:

export FLASK_APP=app.py
export FLASK_ENV=development
flask run

Pour le démarrer sur Windows, executez:

set FLASK_APP=app.py
set FLASK_ENV=development
flask run

API REFERENCE

Pour commencer

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://localhost:5000; which is set as a proxy in frontend configuration.
Type d'erreur

Les erreurs sont renvoyées sou forme d'objet au format Json: { "success":False "error": 404 "message":"not found" }

L'API vous renvoie 2 types d'erreur: . 400: Bad request ou ressource non disponible . 404: Not found
Endpoints

. ## GET/livres

GENERAL:
    Cet endpoint retourne la liste des objets livres, la valeur du succès et le total des livres. 

    
EXEMPLE: curl http://localhost:5000/livres

      {
    "livres": [
        {
            "auteur": "Wole Soyinka",
            "categorie": 9,
            "date": "Wed, 09 Jun 2021 00:00:00 GMT",
            "editeur": "Flammarion",
            "id": 19,
            "isbn": "123",
            "titre": "les années d'enfance"
        },
        {
            "auteur": "Mariama Bâ",
            "categorie": 8,
            "date": "Tue, 09 Oct 2001 00:00:00 GMT",
            "editeur": "Rocher serpent à plumes",
            "id": 20,
            "isbn": "124",
            "titre": "Une si longue lettre"
        },
        {
            "auteur": "Cheikh Hamidou Kane",
            "categorie": 8,
            "date": "Mon, 01 Oct 1979 00:00:00 GMT",
            "editeur": "Vincent Monteil",
            "id": 21,
            "isbn": "125",
            "titre": "L'aventure ambigue"
        },
        {
            "auteur": "Djibril Tamsir Niane",
            "categorie": 12,
            "date": "Fri, 20 Apr 2001 00:00:00 GMT",
            "editeur": "Présence africaine",
            "id": 22,
            "isbn": "126",
            "titre": "L'épopée madingue"
        }
    ],
    "succes": true,
    "total": 4
}


.##GET/livres(livre_id) 
GENERAL: Cet endpoint permet de récupérer les informations d'un livre particulier s'il existe par le biais de l'ID.

EXEMPLE: curl  http://localhost:5000/livres/19


{
    "id demandé": 19,
    "livre demandé ": {
        "auteur": "Wole Soyinka",
        "categorie": 9,
        "date": "Wed, 09 Jun 2021 00:00:00 GMT",
        "editeur": "Flammarion",
        "id": 19,
        "isbn": "123",
        "titre": "les années d'enfance"
    },
    "success": true
}

    

. ## DELETE/livres (livre_id)

GENERAL:
    Supprimer un element si l'ID existe. Retourne l'ID du livre supprimé, la valeur du succès et le nouveau total.

    EXEMPLE: curl -X DELETE http://localhost:5000/livres/22
    {
    "Livre supprimé": {
        "auteur": "Djibril Tamsir Niane",
        "categorie": 12,
        "date": "Fri, 20 Apr 2001 00:00:00 GMT",
        "editeur": "Présence africaine",
        "id": 22,
        "isbn": "126",
        "titre": "L'épopée madingue"
    },
    "Success": true,
    "Total livres": 3
}

   

. ##PATCH/livres(livre_id) GENERAL: Cet endpoint permet de mettre à jour, le titre, l'auteur, et l'éditeur du livre. Il retourne un livre mis à jour.

EXEMPLE  curl -X PATCH http://localhost:5000/livres/21

  {
    "Livre modifie": {
        "auteur": "Cheikh Hamidou Kane",
        "categorie": 9,
        "date": "Mon, 01 Oct 1979 00:00:00 GMT",
        "editeur": "Vincent Monteil",
        "id": 21,
        "isbn": "125",
        "titre": "L'aventure ambigue"
    },
    "success": true
}
  ```

. ## GET/categories

  GENERAL:
      Cet endpoint retourne la liste des categories de livres, la valeur du succès et le total des categories disponibles. 
  
      
  EXEMPLE: curl http://localhost:5000/categories
{
    "Categories": [
        {
            "categorie": "Amour",
            "id": 8
        },
        {
            "categorie": "Aventure",
            "id": 9
        },
        {
            "categorie": "Policier",
            "id": 10
        },
        {
            "categorie": "Drame",
            "id": 11
        },
        {
            "categorie": "Fiction",
            "id": 12
        }
    ],
    "Success": true,
    "Total catégories": 5
}


.##GET/categories(categorie_id) GENERAL: Cet endpoint permet de récupérer les informations d'une categorie si elle existe par le biais de l'ID.

EXEMPLE: http://localhost:5000/categories/12

    {
    "Categorie": {
        "categorie": "Fiction",
        "id": 12
    },
    "Id de la catégorie listée": 12,
    "Success": true
}
. ## DELETE/categories (categories_id)

GENERAL:
    Supprimer un element si l'ID existe. Retourne l'ID da la catégorie supprimé, la valeur du succès et le nouveau total.

    EXEMPLE: curl -X DELETE http://localhost:5000/categories/11
{
    "Categorie supprimé": {
        "categorie": "Epique",
        "id": 13
    },
    "Success": true,
    "Total catégorie ": 5
}

. ##PATCH/categories(categorie_id) GENERAL: Cet endpoint permet de mettre à jour le libelle ou le nom de la categorie. Il retourne une nouvelle categorie avec la nouvelle valeur.

EXEMPLE.....Avec Patch
{
    "Categorie modifie": {
        "categorie": "POLICIER",
        "id": 10
    },
    "success": true
}

 

.##GET/categories(categorie_id)/livres
GENERAL:
Cet endpoint permet de lister les livres appartenant à une categorie donnée.
Il renvoie la classe de la categorie et les livres l'appartenant.

  EXEMPLE: http://localhost:5000/categories/12/livres
  {
    "Categorie_id": 12,
    "Livres de la catégorie": [
        {
            "auteur": "Djibril Tamsir Niane",
            "categorie": 12,
            "date": "Fri, 20 Apr 2001 00:00:00 GMT",
            "editeur": "Présence africaine",
            "id": 23,
            "isbn": "126",
            "titre": "L'épopée madingue"
        }
    ],
    "Nom categorie": "Fiction",
    "Total_livre_categorie": 1
}

