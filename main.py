from flask import Flask, request
import logging
app = Flask(__name__)


logging.basicConfig(filename="log.txt", level=logging.DEBUG)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):

    r = request
    message = '_Method: ' + r.method + ' _Url: ' + r.url  + ' _Length: ' + str(r.content_length) + ' _Data:' + str(r.data) + ' _User_agent: ' + r.user_agent.string

    logging.log(msg=message, level=logging.DEBUG)

    return 'You want path: %s' % path

