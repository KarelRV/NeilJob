import os

from flask import Flask, request

from functions import ugly_load_to_sftp, ugly_load_to_db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
    #    SECRET_KEY='dev',
    #    DATABASE=os.path.join(app.instance_path, 'Neiljob.sqlite'),
    # )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/heyheyhey')
    def heyheyhey():

        return "Heyheyhey"

    @app.route('/load_to_sftp')
    def load_to_sftp():
        ugly_load_to_sftp()
        return

    @app.route('/load_to_db/', methods=['GET'])
    def load_to_db():

        FIRSTNAME = request.args.get('FIRSTNAME')
        LASTNAME = request.args.get('LASTNAME')
        INITIAL = request.args.get('INITIAL')
        IDNUMBER = request.args.get('IDNUMBER')
        POSTALCODE = request.args.get('POSTALCODE')
        FROM = request.args.get('FROM')
        EMAIL = request.args.get('EMAIL')
        REPLYMESSAGE = request.args.get('REPLYMESSAGE')
        ORIGINALMESSAGE = request.args.get('ORIGINALMESSAGE')
        ALTCONTACTNUM = request.args.get('ALTCONTACTNUM')
        DATEOFBIRTH = request.args.get('DATEOFBIRTH')
        CAMPAIGNID = request.args.get('CAMPAIGNID')
        CAMPAIGNNAME = request.args.get('CAMPAIGNNAME')
        SMSSENTTIME = request.args.get('SMSSENTTIME')
        SMSREPLYTIME = request.args.get('SMSREPLYTIME')
        ugly_load_to_db(FIRSTNAME, LASTNAME, INITIAL, IDNUMBER, POSTALCODE, FROM, EMAIL, REPLYMESSAGE, ORIGINALMESSAGE,
                        ALTCONTACTNUM, DATEOFBIRTH, CAMPAIGNID, CAMPAIGNNAME, SMSSENTTIME, SMSREPLYTIME)
        return

    return app
