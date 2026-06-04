from waitress import serve

from GameDiary.wsgi import application

if __name__ == '__main__':
    print("Open browser in https://localhost:8000")
    print("Shut down server with 'control + c'")
    serve(application, port='8000')