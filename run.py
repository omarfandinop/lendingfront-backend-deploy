from app import app, Config

if __name__ == "__main__":
    app.run(port=Config.PORT)
