# one doc
# ST 23 name your function, pass and argument(doc), bring all your format in your square from your model
def DecodeBlog(blog):
    # Ensure blog is a dict; otherwise, raise an error
    if not isinstance(blog, dict):
        print(f"Received data type: {type(blog)} - Data: {blog}")
    return {
        "_id": str(blog["_id"]),
        "title": blog.get("title", ""),
        "subtitle": blog.get("subtitle", ""),
        "content": blog.get("content", ""),
        "author": blog.get("author", ""),
        "tags": blog.get("tags", ""),
        "date": blog.get("date", ""),
        "comments": [DecodedComment(comment) for comment in blog.get("comments", [])]
    }
# Decoding function for comments


def DecodedComment(comment):
    # Ensure comment is a dict; otherwise, raise an error
    if not isinstance(comment, dict):
        print(f"Received comment type: {type(comment)} - Data: {comment}")
        raise TypeError("Expected 'comment' to be a dictionary.")
    return {
        "comment_id": str(comment.get("comment_id", "")),
        "content": comment.get("content", ""),
        "author": comment.get("author", ""),
        "date": comment.get("date", ""),
    }
# ST 24 all blogs


def DecodeBlogs(docs) -> list:
    return [
        DecodeBlog(doc) for doc in docs
    ]
