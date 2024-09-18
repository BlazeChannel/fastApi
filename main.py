from fastapi import FastAPI
#ST6 name of folder.name of file AND what you wanna import
from routes.entry import entry_root
#ST15
from routes.blog import blog_root
from fastapi.middleware.cors import CORSMiddleware


#ST5 initalise the fastapi you just imported(app)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or use ["*"] to allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#ST7  
app.include_router(entry_root)
#ST16 include in youe router
app.include_router(blog_root)