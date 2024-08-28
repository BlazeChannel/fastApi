from fastapi import  APIRouter
#  ST13 name of FOLDER.name of file then WHAT ypu want to IMPORT
from models.blog import BlogModel,  UpdateBlogModel
#   ST17 to post the data(blogs_collection) gottten from the user to our database
from config.config import blogs_collection
from serializers.blog import DecodeBlogs, DecodeBlog
#
from bson import ObjectId
# ST18 import date from library
import datetime
#  ST10 initialise your apirouter with the name of the file(blog.py) in the route folder
blog_root = APIRouter()



#ST11 post request . Name your url(/new/blog)
@blog_root.post("/new/blog")
#ST12 create your function (NewBlog). pass an argumment(doc)[it holds the data the user is sending], then pass the (BlogModel)
def NewBlog(doc:BlogModel):
#ST14 name your variable(doc)then pass the argument of your function(NewBlog)
    doc = dict(doc)
# ST19 name a variable
    current_date = datetime.date.today()
# ST 20
    doc["date"] = str(current_date)
#ST 21 to post the data in our database. pass our data (doc) to a variable (res)
    res = blogs_collection.insert_one(doc)
# ST 22 for generating id name a variable (doc_id)
    doc_id = str(res.inserted_id)
    return {
        "status": "ok",
        "message" : "Blog posted successfuly",
        "id" : doc_id 
    }



#ST 25 getting all blogs

@blog_root.get("/all/blogs")
def AllBlogs():
    res = blogs_collection.find()
    decoded_data = DecodeBlogs(res)

    return{
        "status":"ok",
        "data": decoded_data ,
    }

#ST 26 /blog/ GET a particular id
@blog_root.get("/blog/{_id}")
def Getblog(_id:str) : 
    res = blogs_collection.find_one({"_id" : ObjectId(_id) } )
    decoded_blog = DecodeBlog(res)
    return {
        "status" : "ok",
        "data" : decoded_blog 
    }

#update blog
@blog_root.patch("/update/{_id}")
def UpdateBlog(_id: str, doc:UpdateBlogModel):
    req = dict(doc.model_dump(exclude_unset=True))
    blogs_collection.find_one_and_update({"_id" : ObjectId(_id) },
            {"$set": req }          
              ) 
    return {
        "status": "ok",
        "message" : "blog uupdated"
    }

#delete blog
@blog_root.delete("/delete/{_id}")
def DeleteBlog(_id : str):
        blogs_collection.find_one_and_delete(
             {"_id" : ObjectId(_id) }
        )
        return {
             "status" : "ok",
             "message" : "blog deleted"
        }