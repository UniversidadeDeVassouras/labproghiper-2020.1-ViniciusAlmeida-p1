from flask import Flask 
import os
from application.model.dao.categoryDAO import CategoryDAO
from application.model.dao.videoDAO import videoDAO
from application.model.dao.commentsDAO import CommentaryDAO


template_folder = os.path.abspath("application/view/templates")
static_folder = os.path.abspath("application/view/static")


app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)



categories = CategoryDAO ()
videos = VideoDAO ()
comments = CommentaryDAO ()

app.config ['categories'] = categories
app.config ['videos'] = videos
app.config ['comments'] = comments



from application.controller import home_controller
from application.controller import category_controller
from application.controller import video_controller
