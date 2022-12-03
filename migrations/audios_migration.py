from pymongo import MongoClient
from werkzeug.security import generate_password_hash
import os
import configparser
from datetime import datetime
from bson.objectid import ObjectId

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

# DB_URI = config['PROD']['PIALARA_DB_URI']
# DB_NAME = config['PROD']['PIALARA_DB_NAME']
DB_URI = config['LOCAL']['PIALARA_DB_URI']
DB_NAME = config['LOCAL']['PIALARA_DB_NAME']

db = MongoClient(DB_URI)[DB_NAME]

audios = [
    {
        "_id": ObjectId("6379ff018659dd172e6afadc"),
        "aws_object_id": "https://audio.com/",
        "duracion": 60,
        "notas": "en esta sesion a lo mejor ha habido mucho ruido",
        "valoracion": 4,
        "fecha": datetime(2022, 12, 1),
        "texto": {
            "id":ObjectId("638348e9b3ba0b56509dfa1b"),
            "texto": "Esto es una prueba 2",
            "creador": {
                "id": ObjectId("637fb70f9297829bcac1be50"),
                "rol": "admin",
                "nombre": "Sebas"
            },
            "tags": [
                "dislalia",
                "paralisis facial",
                "futbol",
                "madrid"
            ]
        },
        "usuario": {
            "id": ObjectId("637a02b38659dd172e6afae4"),
            "sexo": "H",
            "provincia": "alicante",
            "edad": 42,
            "nombre": "Jesús",
            "enfermedad": [
                "paralisis"
            ],
            "dis": [
                "dislalia"
            ]
        }
    }
]

audiosValidator = {
    "$jsonSchema": {
        "required": [
            'aws_object_id',
            'texto',
            'usuario'
        ],

    }
}

try:
    db.drop_collection("audio")
    db.drop_collection("audios")
    db.create_collection("audios", validator=audiosValidator)
    db.audios.insert_many(audios)
except Exception as e:
    print(e)
