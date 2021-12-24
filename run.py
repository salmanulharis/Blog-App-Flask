from flaskblog import create_app                #this create_app is from __init__.py(calling the folder take to __inti__.py)

app = create_app()

if __name__ == '__main__':
	app.run(debug=True)
