from fastapi import APIRouter, HTTPException
#  ST13 name of FOLDER.name of file then WHAT ypu want to IMPORT
from models.blog import BlogModel,  UpdateBlogModel, CommentModel
#   ST17 to post the data(blogs_collection) gottten from the user to our database
from config.config import blogs_collection
from config.config import comments_collection
from serializers.blog import DecodeBlogs, DecodeBlog, DecodedComment
from datetime import datetime
#
from bson import ObjectId
# ST18 import date from library

#  ST10 initialise your apirouter with the name of the file(blog.py) in the route folder
blog_root = APIRouter()

# ST11 post request . Name your url(/new/blog)


# @blog_root.post("/new/blog")
# # ST12 create your function (NewBlog). pass an argumment(doc)[it holds the data the user is sending], then pass the (BlogModel)
# def NewBlog(blog: BlogModel):
#     try:
#         blog_dict = dict()  # Convert the BlogModel to a dictionary
#         # Generate a new unique ID for the blog
#         blog_dict["_id"] = str(ObjectId())
#         result = blogs_collection.insert_one(
#             blog_dict)  # Insert into the database
#         new_blog = blogs_collection.find_one(
#             {"_id": result.inserted_id})  # Fetch the newly inserted blog
#         return DecodeBlog(new_blog)  # Decode and return the new blog
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))




@blog_root.post("/new/blog")
def NewBlog(blog: BlogModel):
    # Properly convert BlogModel to a dictionary
    blog_dict = blog.dict()

    # Generate the current date correctly
    current_date = datetime.now().isoformat()
    blog_dict["date"] = current_date

    # Insert blog into the database
    res = blogs_collection.insert_one(blog_dict)
    doc_id = str(res.inserted_id)

    # Fetch the newly inserted blog
    new_blog = blogs_collection.find_one({"_id": ObjectId(doc_id)})

    # Correctly decode the full blog document for response
    return {
        "status": "ok",
        "message": "Blog posted successfully",
        "data": DecodeBlog(new_blog)  # Correct: Pass the actual blog document
    }


#     # ST14 name your variable(doc)then pass the argument of your function(NewBlog)
#     doc = dict(doc)
# # ST19 name a variable
#     current_date = datetime.date.today()
# # ST 20
#     doc["date"] = str(current_date)
# # ST 21 to post the data in our database. pass our data (doc) to a variable (res)
#     res = blogs_collection.insert_one(doc)
# # ST 22 for generating id name a variable (doc_id)
#     doc_id = str(res.inserted_id)
#     return {
#         "status": "ok",
#         "message": "Blog posted successfuly",
#         "data": DecodeBlog(doc_id)
#     }

# to add a comment to a blog


@blog_root.post("/blog/{blog_id}/comment")
async def add_comment(blog_id: str, comment: CommentModel):
    print(f"Received blog ID: {blog_id}")
    # Check if blog_id is a valid ObjectId
    if not ObjectId.is_valid(blog_id):
        raise HTTPException(status_code=400, detail="Invalid blog ID format")
    comment_dict = comment.dict()
    # Generating a unique ID for each comment
    comment_dict["comment_id"] = str(ObjectId())
    update_result = blogs_collection.update_one(
        {"_id": ObjectId(blog_id)},
        {"$push": {"comments": comment_dict}}
    )
    if update_result.modified_count == 0:
        print(f"Blog post not found for ID: {blog_id}")
        raise HTTPException(
            status_code=404, detail="Blog post not found")

    # Fetch the updated blog post
    updated_blog = blogs_collection.find_one(
        {"_id": ObjectId(blog_id)})
    return {"message": "Comment added successfully",
            "data": DecodeBlog(updated_blog)
            }

    #     # Find the blog by ID
    #     result = blogs_collection.find_one({"_id": ObjectId(blog_id)})
    #     if not result:
    #         raise HTTPException(status_code=404, detail="Blog post not found")

    #     # Update the blog with the new comment
    #     blogs_collection.update_one(
    #         {"_id": ObjectId(blog_id)},
    #         {"$push": {"comments": comment.dict()}}
    #     )
    #     return {"message": "Comment added successfully"}
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=str(e))


@blog_root.get("/comments/{blog_id}")
async def list_comments(blog_id: str):
    if not ObjectId.is_valid(blog_id):
        raise HTTPException(status_code=400, detail="Invalid blog ID format.")
    comments = blogs_collection.find({"_id": ObjectId(blog_id)}, {
                                     "comments": 1})  # Find comments for the blog ID
    if not comments:
        # No comments found error
        raise HTTPException(
            status_code=404, detail="No comments found for this blog post.")
    comment_list = list(comments.get("comments", [])
                        )  # Extract comments list
    return [{"_id": str(comment.get("comment_id")), "content": comment.get("content", ""),
             "author": comment.get("author", ""), "date": comment.get("date", "")}
            for comment in comment_list]  # Format the response


# ST 25 getting all blogs
@blog_root.get("/all/blogs")
def AllBlogs():
    res = blogs_collection.find()
    decoded_data = DecodeBlogs(res)
    return {
        "status": "ok",
        "data": decoded_data
    }

# ST 26 /blog/ GET a particular id , including comments


@blog_root.get("/blog/{blog_id}")
async def Getblog(blog_id: str):
    blog = blogs_collection.find_one({"_id": ObjectId(blog_id)})
    if not blog:
        raise HTTPException(status_code=404, detail="Blog post not found")
    return {
        "status": "ok",
        "data":  DecodeBlog(blog)}

# update/patch blog


@blog_root.patch("/update/{blog_id}")
def UpdateBlog(blog_id: str, doc: UpdateBlogModel):
    req = dict(doc.model_dump(exclude_unset=True))
    blogs_collection.find_one_and_update({"_id": ObjectId(blog_id)},
                                         {"$set": req}
                                         )
    return {
        "status": "ok",
        "message": "blog uupdated"
    }

# delete blog


@blog_root.delete("/delete/{blog_id}")
def DeleteBlog(blog_id: str):
    blogs_collection.find_one_and_delete(
        {"_id": ObjectId(blog_id)}
    )
    return {
        "status": "ok",
        "message": "blog deleted"
    }
