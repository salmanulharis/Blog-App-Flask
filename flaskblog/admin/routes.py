from flask import Blueprint
from flask_admin.contrib.sqla import ModelView
from flaskblog.models import *
from flaskblog import admins

admins.add_view(ModelView(User, db.session, endpoint="manage-user"))
admins.add_view(ModelView(Post, db.session, endpoint="manage-post"))