import os
from flask import Flask,abort,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()
username=os.getenv('user')
mdp=os.getenv('pswd')
host=os.getenv('host')
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://{}:{}@:5432/bdlivre'.format(username,mdp,host)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Categorie(db.Model):
    __tablename__='categories'
    id=db.Column(db.Integer,primary_key=True)
    libelle_categorie=db.Column(db.String(128),nullable=False)
    livres=db.relationship('Livre',backref='categories',lazy=True)
    def __init__(self,libelle_categorie):
        self.libelle_categorie=libelle_categorie

    def inserer_categorie(self):
        db.session.add(self)
        db.session.commit()

    def modifier_categorie(self):
        db.session.commit()
    def supprimer_categorie(self):
        db.session.delete(self)
        db.session.commit()
    def categorie_format(self):
        return({
        'id':self.id,
        'categorie':self.libelle_categorie
        })




class Livre(db.Model):
    __tablename__='livres'
    id=db.Column(db.Integer,primary_key=True)
    isbn=db.Column(db.String(20),unique=True)
    titre=db.Column(db.String(60),nullable=False)
    date_publication=db.Column(db.DateTime)
    auteur=db.Column(db.String(100),nullable=False)
    editeur=db.Column(db.String(100),nullable=False)
    categorie_id=db.Column(db.Integer,db.ForeignKey('categories.id'),nullable=False)
    def  __init__(self,isbn,titre,date_publication,auteur,editeur,categorie_id):
        self.isbn=isbn
        self.titre=titre
        self.date_publication=date_publication
        self.auteur=auteur
        self.editeur=editeur
        self.categorie_id=categorie_id
    def inserer_livre(self):
        db.session.add(self)
        db.session.commit()
    def modifier_livre(self):
        db.session.commit()
    def  supprimer_livre(self):
        db.session.delete(self)
        db.session.commit()

    def livre_format(self):
        return({
        'id':self.id,
        'isbn':self.isbn,
        'titre':self.titre,
        'date': self.date_publication,
        'auteur':self.auteur,
        'editeur':self.editeur,
        'categorie':self.categorie_id
        })


db.create_all()
###Lister tous les livres
@app.route('/livres',methods=['GET'])
def get_all_books():
    livres=Livre.query.all()
    liv_format=[l.livre_format() for l in livres]
    return jsonify({
    'succes':True,
    'livres':liv_format,
    'total':Livre.query.count()
    })
    ###Chrcher un livre avec son id
@app.route('/livres/<int:id>',methods=['GET'])
def get_one_book(id):
    try:
        livre=Livre.query.get(id)
        if livre is None:
            abort(404)
        else:
            return jsonify({
            'success':True,
            'livre demandé ':livre.livre_format()
            })
    except :
        abort(400)


###La liste des livres d'une categorie
@app.route('/categories/<int:id>/livres',methods=['GET'])
def one_category_books(id):
    try:
        livres_cat=Livre.query.filter_by(categorie_id=id)
        if livres_cat is None:
            abort(404)
        else:
            livres_cat_format=[l.livre_format() for l in livres_cat]
            nom_cat=Categorie.query.get(id).libelle_categorie
            return jsonify({
            'Categorie_id':id,
            'Nom categorie':nom_cat,
            'Livres':livres_cat_format,
            'Total_livre_categorie':livres_cat.count()
            })

    except :
        abort(400)


##Lister une categorie
@app.route('/categories/<int:id>',methods=['GET'])
def get_one_category(id):
    try:
        categorie=Categorie.query.get(id)
        if categorie is None:
            abort(404)
        else:
            return jsonify({
            'Success':True,
            'Categorie':categorie.categorie_format(),

            })
    except :
        abort(400)

##Chrcher une categorie par son id
"""
@app.route('/categories/<int:id>',methods=['GET'])
def search_one_categories(id):
    try:
        categorie=Categorie.query.get(id)
        if categorie is None:
            resultat=jsonify({
            'Success':False,
            'Resultat':'categorie inexistante!!'
            })
        else:
            resultat= jsonify({
        'Success':"True la catégorie existe",
        'Categorie':categorie.categorie_format,

        })
        return resultat

    except:
        abort(400)
"""
#Lister toutes les catégories
@app.route('/categories',methods=['GET'])
def get_all_categories():
    categories=Categorie.query.all()
    if categories is None:
        abort(404)
    else:
        categories_format=[c.categorie_format() for c in categories]
        return jsonify({
        'Success':True,
        'Categories':categories_format,
        'Total':Categorie.query.count()
        })

##Supprimer un livre
@app.route('/livres/<int:id>',methods=['DELETE'])
def delete_one_book(id):
    try:
        livre_a_supprimer=Livre.query.get(id)
        if livre_a_supprimer is None:
            abort(404)
        else:
            livre_a_supprimer.supprimer_livre()
            return jsonify({'Success':True,
            'Livre supprimé': livre_a_supprimer.livre_format(),
            'Total livres':Livre.query.count()
            })

    except :
        abort(422)
#Supprimer une categorie
@app.route('/categories/<int:id>',methods=['DELETE'])
def delete_one_categories(id):
    try:
        categorie=Categorie.query.get(id)
        if categorie is None:
            abort(404)
        else:
            categorie.supprimer_categorie()
            return jsonify({
            'Success':True,
            'Categorie supprimé':categorie.categorie_format(),
            'Total':Categorie.query.count()

            })

    except :
        abort(400)
#Modifier les informations d'un livre
@app.route('/livres/<int:id>',methods=['PATCH'])
def update_one_book(id):
    donnee=request.get_json()
    livre=Livre.query.get(id)
    livre.isbn=donnee.get("isbn",None)
    livre.titre=donnee.get("titre",None)
    livre.auteur=donnee.get("auteur",None)
    livre.editeur=donnee.get("editeur",None)
    livre.date_publication=donnee.get("date",None)
    livre.categorie_id=donnee.get("categorie",None)
    if livre.isbn is None or livre.titre is None or livre.auteur is None or livre.editeur is None or livre.date_publication is None or livre.categorie_id is None :
        abort(400)
    else:
        livre.modifier_livre()
        return jsonify({
        "success":True,
        "Livre modifie":livre.livre_format()

        })
@app.route('/categories/<int:id>',methods=['PATCH'])
def update_one_category(id):
    donnee=request.get_json()
    categorie=Categorie.query.get(id)
    categorie.libelle_categorie=donnee.get("categorie",None)
    if categorie.libelle_categorie is None:
        abort(400)
    else:
        categorie.modifier_categorie()
        return jsonify({"success":True,
        "Categorie modifie":categorie.categorie_format()
        })


@app.route('/livres',methods=['POST'])
def create_book():
    donnees=request.get_json()
    isbn=donnees.get("isbn",None)
    titre=donnees.get("titre",None)
    date=donnees.get("date",None)
    auteur=donnees.get('auteur',None)
    editeur=donnees.get("editeur",None)
    cat=donnees.get("categorie",None)
    livre=Livre(isbn=isbn,titre=titre,date_publication=date,auteur=auteur,editeur=editeur,categorie_id=cat)
    livre.inserer_livre()
    return jsonify({
    "success": True,
    "Nouveau livre " :livre.livre_format(),
    "Total":Livre.query.count()
    })

@app.route('/categories',methods=['POST'])
def add_categories():
    donnees=request.get_json()
    lib=donnees.get("libelle_categorie",None)
    if lib is None:
        abort(404)
    else:
        cat=Categorie(libelle_categorie=lib)
        cat.inserer_categorie()
        return jsonify({
        "success": True,
        "Categorie cree": cat.categorie_format()
        })

@app.errorhandler(404)
def not_found(error):
    return jsonify({'success':False,'error': 404,'message': 'not found'}),404

@app.errorhandler(400)
def server_error(error):
    return jsonify({'success':False,'error': 400,'message': 'bad request'}),400

if __name__=='__main__':
    app.run(debug=True)
