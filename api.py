from database import init_db
import responder

api = responder.API()

if __name__ == '__main__':
    init_db()
    api.run(port=5000)
