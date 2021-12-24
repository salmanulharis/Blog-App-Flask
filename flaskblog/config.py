import os

class Config():
	SECRET_KEY =  #os.environ.get('SECRET_KEY')
	SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Pass123@localhost/flaskblog' #os.environ.get('SQLALCHEMY_DATABASE_URI')
	#mail configuration
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME =  #os.environ.get('EMAIL_USER')  # for more details https://www.youtube.com/watch?v=5iWhQWVXosU&t=0s
	MAIL_PASSWORD =  #os.environ.get('EMAIL_PASS')