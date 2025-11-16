
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://g00419630_db_user:<Sagheer123>@cluster0.a0vb9r4.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, tls=True, tlsAllowInvalidCertificates=True, server_api=ServerApi('1'))

db = client.UserDatabase
collection = db["TTA"]