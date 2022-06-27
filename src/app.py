from flask import Flask, jsonify, request, make_response
from conf import conf

app = Flask(__name__)

    
def page_not_found(error):
    return "<h1>The page you are trying to access does not exist...</h1>", 404

if __name__ == '__main__':
    app.config.from_object(conf["development"])
    app.register_error_handler(404, page_not_found)
    app.run()