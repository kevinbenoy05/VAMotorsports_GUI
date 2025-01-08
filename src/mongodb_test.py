from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import urllib
uri = "mongodb+srv://kevinbenoy:" + urllib.parse.quote("VAMS@1644")+"@cluster.simtg.mongodb.net/?retryWrites=true&w=majority&appName=cluster"

# Send a ping to confirm a successful connection
client = MongoClient(uri, server_api=ServerApi(version='1', strict=True, deprecation_errors=True))
try:
    # Connect the client to the server (optional starting in v4.7)
    client._connect()
    # Send a ping to confirm a successful connection
    client.admin.command({'ping': 1})
    print("Pinged your deployment. You successfully connected to MongoDB!")
finally:
    # Ensures that the client will close when you finish/error
    client.close()