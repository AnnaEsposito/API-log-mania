# Importamos Flask, que es un marco para desarrollar aplicaciones web
from flask import Flask
from logging_rutas import configuracion_rutas_logging
from database import crear_db


def crear_app():
    app = Flask(__name__)
   
    # Configuraciones generales (incluye SECRET_KEY)
    app.config.from_object('config.Config')
    
    crear_db()

    configuracion_rutas_logging(app)
    
    return  app


