# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # utf-8 support
from flask import Flask
from flask_dmango import Dmango

app = Flask(__name__)
dmango = Dmango(app)
dmango.register_mongodb('server1', URI='mongodb://test:test@ds061701.mlab.com:61701/pkast')

from views import bp
app.register_blueprint(bp)


if __name__ == '__main__':
    app.run('0.0.0.0', port=6757, debug=True)
