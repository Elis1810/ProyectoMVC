from app import app, db   #,ma
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship

# defino las tablas
class Producto(db.Model):   # la clase Producto hereda de db.Model de SQLAlquemy   
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombre=db.Column(db.String(100))
    precio=db.Column(db.Integer)
    stock=db.Column(db.Integer)    
    tipo=db.Column(db.String(40))    
    caracteristicas=db.Column(db.String(100))
    peso=db.Column(db.Integer)
    altura=db.Column(db.Integer)
    imagen=db.Column(db.String(200))
    def __init__(self,nombre,precio,stock,tipo,caracteristicas,peso,altura,imagen): #crea el  constructor de la clase
        self.nombre=nombre # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.precio=precio
        self.stock=stock        
        self.tipo=tipo        
        self.caracteristicas=caracteristicas
        self.peso=peso
        self.altura=altura
        self.imagen=imagen
    #  si hay que crear mas tablas , se hace aqui

with app.app_context():
    db.create_all()  # aqui crea todas las tablas si es que no estan creadas