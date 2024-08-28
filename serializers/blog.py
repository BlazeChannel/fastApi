# one doc
#ST 23 name your function, pass and argument(doc), bring all your format in your square from your model
def DecodeBlog(doc) -> dict:
    return{
        "_id": str(doc["_id"]),
        "title": doc["title"],
        "subtitle": doc["subtitle"],
        "content": doc["content"],
        "author": doc["author"],
        "date": doc["date"]
    }

#ST 24 all blogs

def DecodeBlogs(docs) -> list:
    return[
        DecodeBlog(doc) for doc in docs
    ]