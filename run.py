from flaskblog import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=False) # run this when the file is executed

