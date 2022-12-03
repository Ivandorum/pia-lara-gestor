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

syllabus = [
    {
      "_id": ObjectId("637a078e8659dd172e6afaf5") ,
      "texto": "Esto es una prueba",
      "creador": {
        "id": ObjectId("6379fc6871880707a2c89537"),
        "nombre": "Rocio",
        "rol": "admin"
      },
      "tags": [
        "dislalia",
        "paralisis facial",
        "futbol",
        "madrid"
      ],
      "audios": [
        {
          "$oid": ObjectId("637a08118659dd172e6afafa")
        },
        {
          "$oid": ObjectId("637a08208659dd172e6afafb")
        },
        {
          "$oid": ObjectId("637a08388659dd172e6afafc")
        }
      ],
      "fecha_creacion": datetime(2022, 11, 21)
    },
    {
      "_id": ObjectId("638348e9b3ba0b56509dfa1b"),
      "texto": "Esto es una prueba 2",
      "creador": {
        "id": ObjectId("637fd98b2950843403bd5d8a"),
        "nombre": "Mario",
        "rol": "cliente"
      },
      "tags": [
        "dislalia",
        "paralisis facial",
        "futbol",
        "madrid"
      ],
      "audios": [
        {
          "$oid": ObjectId("6379ff018659dd172e6afadc")
        },
        {
          "$oid": ObjectId("638ab4684b8c5b1f2090ee6d")
        },
        {
          "$oid": ObjectId("638ab46e4b8c5b1f2090ee6e")
        }
      ],
      "fecha_creacion": datetime(2022, 11, 29)
    }
]

syllabusValidator = {
    "$jsonSchema": {
        "required": [
          'texto',
          'creador',
          'fecha_creacion'
        ],
        "properties": {
            "texto": {
                "bsonType": 'string'
            },
            "creador": {
                "bsonType": 'object'
            },
            "tags": {
                "bsonType": 'array'
            },
            "fecha_creacion": {
                "bsonType": 'date'
            }
        }
    }
}

try:
    db.drop_collection("sylabus")
    db.drop_collection("syllabus")
    print("drop")
    db.create_collection("syllabus", validator=syllabusValidator)
    print("create")
    db.syllabus.insert_many(syllabus)
    print("insert")
except Exception as e:
    print(e)
