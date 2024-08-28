
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://sam:sam@atlascluster.1a5w0.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# create your database(db) + the name of the MongoClient variable created up(client) + name of you wanna chose as your database(Blogging)
db = client.Blogging
# create a collection = name of your collection (blogs)
blogs_collection = db["blogs"]
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)





#.\venv\scripts\activate
# uvicorn main:app --reload

#GET REQUEST is used to retrieve data from the server
#POST REQUEST is used to post/creating/save a new blog to our server/database
#PATCH REQUEST is used to update an existing request on the database
#DELETE REQEUST is used to delete data from our database
# create a folder "python blogging backend", open with cmd prompt, install "pip install virtualenv" then press enter. To create a virtual environment type"virtualenv venv(name your virtual environment) then press enter
# Activate to be able to use ".\venv(name you give your environment)\scripts\activate" then pres enter
# Install some dependencies "pip install fastapi uvicorn" . Later install "pip install pymongo"
# create your structure FOLDER : "config > config.py" "routes" "models" "serializers" 
# on your MONGODb acct create a cluster, name it and user password also. Go to driver set  your driver & version . Paste number 2 on your cmd prompt . Copy number 3 on your config.py file , chaange the pasword to the pasword you set on the mongoDB auth user you created
#RUN YOUR CONFIG FILE WITH EXTENSION code runner, check your terminal
# if you close you and reopen and activate with ".\venv(name you give your environment)\scripts\activate"
# create your entry point(main.py) before you run your server 
# create entry.py . After ST7 comd promt (uvicorn main:app --reload)
# ST8 post new blog to our database. create blog in MODEL folder
# ST9 create blog.py in ROUTES folder
#
#
#
#