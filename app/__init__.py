import os

from flask import Flask, request

from functions import ugly_load_to_sftp, ugly_load_to_db,ugly_load_to_db_stops,ugly_load_to_db_om


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

    @app.route('/test')
    def test():
        # test2()
        return "this is a test response"

    @app.route('/load_to_sftp')
    def load_to_sftp():
        ugly_load_to_sftp()
        return "loaded to sftp"

    @app.route('/load_to_sftp_om')
    def load_to_sftp_om():
        ugly_load_to_sftp_om()
        return "loaded to sftp om"
		
    @app.route('/load_to_sftp_stops_om')
    def load_to_sftp_stops_om():
        ugly_load_to_sftp_om()
        return "loaded to sftp stops om"
		
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
        return "loaded to db"
    @app.route('/load_to_db_stops/', methods=['GET'])
    def load_to_db_stops():

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
        ugly_load_to_db_stops(FIRSTNAME, LASTNAME, INITIAL, IDNUMBER, POSTALCODE, FROM, EMAIL, REPLYMESSAGE, ORIGINALMESSAGE,
                        ALTCONTACTNUM, DATEOFBIRTH, CAMPAIGNID, CAMPAIGNNAME, SMSSENTTIME, SMSREPLYTIME)
        return "loaded to db stops"
		
    @app.route('/load_to_db_om/', methods=['GET'])
    def load_to_db_om():

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
        ugly_load_to_db_om(FIRSTNAME, LASTNAME, INITIAL, IDNUMBER, POSTALCODE, FROM, EMAIL, REPLYMESSAGE, ORIGINALMESSAGE,
                        ALTCONTACTNUM, DATEOFBIRTH, CAMPAIGNID, CAMPAIGNNAME, SMSSENTTIME, SMSREPLYTIME)
        return "loaded to db old mutual"
		
    @app.route('/load_to_db_stops_om/', methods=['GET'])
    def load_to_db_stops_om():

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
        ugly_load_to_db_om(FIRSTNAME, LASTNAME, INITIAL, IDNUMBER, POSTALCODE, FROM, EMAIL, REPLYMESSAGE, ORIGINALMESSAGE,
                        ALTCONTACTNUM, DATEOFBIRTH, CAMPAIGNID, CAMPAIGNNAME, SMSSENTTIME, SMSREPLYTIME)
        return "loaded to db om stops"		
		
    return app
