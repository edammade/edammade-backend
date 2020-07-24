from database import init_db
import responder
from schema import schema

api = responder.API()
view = responder.ext.GraphQLView(api=api, schema=schema)

api.add_route("/graph", view)

if __name__ == '__main__':
    init_db()
    api.run(port=5000)