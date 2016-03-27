# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask_dmango import Dmango

bp = Blueprint('name1', __name__)


@bp.route('/')
def index():
    try:
        connection = Dmango.find_mongodb('server1')
        database = connection.cx["pkast"]
        collection = database['p1']
        result = collection.find()
        return render_template('index.html', result=result)
    except:
        import traceback
        print traceback.format_exc()


@bp.route('/test')
def test():
    return "Test"