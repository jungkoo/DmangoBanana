from flask import Blueprint, render_template
from flask.ext.dmango import Dmango

bp = Blueprint('name1', __name__)


@bp.route('/')
def index():
    try:
        db = Dmango.find_mongodb('server1')
        print db, dir(db)
        r1 = db.db['p1'].find()
        print r1.count()
        result = db["p1"].find()
        render_template('index.html', data=result)
    except:
        import traceback
        print traceback.format_exc()


@bp.route('/test')
def test():
    return "Test"