from pymongo import MongoClient
from werkzeug.security import generate_password_hash
import os
import configparser
from datetime import datetime

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

# DB_URI = config['PROD']['PIALARA_DB_URI']
# DB_NAME = config['PROD']['PIALARA_DB_NAME']
DB_URI = config['LOCAL']['PIALARA_DB_URI']
DB_NAME = config['LOCAL']['PIALARA_DB_NAME']

db = MongoClient(DB_URI)[DB_NAME]

users = [
    {
        "fecha_nacimiento": datetime(1998, 5, 17),
        "email": "rococo@gmail.com",
        "password": generate_password_hash("admin", method='sha256'),
        "rol": "admin",
        "nombre": "Rocío",
        "sexo": "M",
        "ultima_conexion": datetime.today()
    },
    {
        "fecha_nacimiento": datetime(1989, 5, 17),
        "email": "mario@gmail.com",
        "password": generate_password_hash("admin", method='sha256'),
        "rol": "cliente",
        "nombre": "Mario",
        "sexo": "H",
        "provincia": "Alicante",
        "ultima_conexion": datetime.today(),
        "enfermedades": [
            "paralisis facial"
        ],
        "dis": [
            "disfemia"
        ]
    },
    {
        "fecha_nacimiento": datetime(1957, 4, 21),
        "email": "ines@gmail.com",
        "password": generate_password_hash("admin", method='sha256'),
        "rol": "tecnico",
        "nombre": "Inés",
        "sexo": "M",
        "ultima_conexion": datetime.today()

    },
    {
        "fecha_nacimiento": datetime(1997, 2, 4),
        "email": "pedro@gmail.com",
        "password": generate_password_hash("admin", method='sha256'),
        "rol": "cliente",
        "nombre": "Pedro",
        "sexo": "H",
        "provincia": "Alicante",
        "ultima_conexion": datetime.today(),
        "enfermedades": [
            "paralisis facial"
        ],
        "dis": [
            "disfemia"
        ]
    },
    {
        "fecha_nacimiento": datetime(1996, 3, 1),
        "email": "pedro@gmail.com",
        "password": generate_password_hash("admin", method='sha256'),
        "rol": "cliente",
        "nombre": "Pedro",
        "sexo": "H",
        "provincia": "Alicante",
        "ultima_conexion": datetime.today(),
        "enfermedades": [
            "paralisis facial"
        ],
        "dis": [
            "disfemia"
        ]
    },

    {
        "fecha_nacimiento": datetime(1945, 2, 12),
        "email": "pedro@gmail.com",
        "password": generate_password_hash("admin", method='sha256'),
        "rol": "cliente",
        "nombre": "Hector",
        "sexo": "H",
        "provincia": "Madrid",
        "ultima_conexion": datetime.today(),
        "enfermedades": [
            "iptus"
        ],
        "dis": [
            "dislexia"
        ]
    }

]

userValidator = {
    "$jsonSchema": {
        "required": [
            'password',
            'email',
            'nombre',
            'rol',
            'fecha_nacimiento',
            'ultima_conexion'
        ],
        "properties": {
            "email": {
                "bsonType": 'string'
            },
            "password": {
                "bsonType": 'string'
            },
            "id": {
                "bsonType": 'objectId'
            },
            "fecha_nacimiento": {
                "bsonType": 'date'
            },
            "ultima_conexion": {
                "bsonType": 'date'
            },
            "nombre": {
                "bsonType": 'string'
            },
            "rol": {
                "bsonType": 'string',
                'enum': [
                    "admin",
                    "tecnico",
                    "cliente"
                ]
            },
            "provincia": {
                "bsonType": 'string',
                'enum': [
                    'A Coruña',
                    'Álava',
                    'Albacete',
                    'Alicante',
                    'Almería',
                    'Asturias',
                    'Ávila',
                    'Badajoz',
                    'Baleares',
                    'Barcelona',
                    'Burgos',
                    'Cáceres',
                    'Cádiz',
                    'Cantabria',
                    'Castellón',
                    'Ciudad Real',
                    'Córdoba',
                    'Cuenca',
                    'Girona',
                    'Granada',
                    'Guadalajara',
                    'Gipuzkoa',
                    'Huelva',
                    'Huesca',
                    'Jaén',
                    'La Rioja',
                    'Las Palmas',
                    'León',
                    'Lérida',
                    'Lugo',
                    'Madrid',
                    'Málaga',
                    'Murcia',
                    'Navarra',
                    'Ourense',
                    'Palencia',
                    'Pontevedra',
                    'Salamanca',
                    'Segovia',
                    'Sevilla',
                    'Soria',
                    'Tarragona',
                    'Santa Cruz de Tenerife',
                    'Teruel',
                    'Toledo',
                    'Valencia',
                    'Valladolid',
                    'Vizcaya',
                    'Zamora',
                    'Zaragoza',
                    'Ceuta',
                    'Melilla'
                ]
            },
            "sexo": {
                "bsonType": 'string',
                'enum': [
                    'M',
                    'H'
                ]
            }
        }
    }
}

try:
    db.drop_collection("usuarios")
    db.drop_collection("users")
    db.create_collection("users", validator=userValidator)
    db.users.insert_many(users)
except Exception as e:
    print(e)
