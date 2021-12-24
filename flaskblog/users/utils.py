import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail

def save_picture(form_picture):
	random_hex = secrets.token_hex(8)                             #this will be the new file name(renaming) to avoid file name collision on saving all file in same folder while uploading
	f_name, f_ext = os.path.splitext(form_picture.filename)        # to split the file name and extension(.png,.jpg,etc.) to store the file in the same extension of uploading, then we need to know the extension of the file uploaded
	picture_fn = random_hex + f_ext                               # picture_fn='picture file name', we are no usinf f_name since we not neede, but while spliting we need to give the variable
	picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

	output_size = (125, 125)
	i = Image.open(form_picture)      # i is the new image with redused size
	i.thumbnail(output_size)
	i.save(picture_path)
	# form_picture.save(picture_path)

	return picture_fn

def send_reset_email(user):
	token = user.get_reset_token()          #function from models.py
	msg = Message('Password Reset request', sender='noreply@demo.com', recipients=[user.email])
	msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}
If you did not make this request, please ignore this mesage
''' 
	#since f string is used, there is no need to {{url_for(...)}}, and also need to take the other line to starting point
	mail.send(msg)
