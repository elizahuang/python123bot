from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request,render_template
from app import app, db
from models import mediapp_patient, mediapp_userinfo, post, mediapp_problems
import datetime,os


@app.route('/addUser',methods=['GET','POST'])
def showAddUserPage():
    #fileDir = os.path.join(os.path.dirname(os.path.realpath('__file__')),'static')
    #targetPath=os.path.join(fileDir,'index.html')
    #print(targetPath)
    return render_template("index.html")


@app.route('/test')
def index():

    sql_cmd = """
        select *
        from disease
        """
    query_data = db.engine.execute(sql_cmd)
    for row in query_data:
        print("id:", row)
    print(query_data)
    print("OK")
    return 'OK'


@app.route('/user/<lineID>',methods=['GET'])
def users(lineID):
    lineID = "'"+lineID+"'"
    sql_cmd = """
        select *
        from mediapp_patient
        where lineID = 
        """+lineID

    
    data = []

    query_data = db.engine.execute(sql_cmd)
    for row in query_data:
        diction = {}
        phID = row['PharmacyID']
        print("user:", row['Name'],row['Sex'],row['PharmacyID'])
        diction['name'] = row['Name']
        diction['gender'] = row['Sex']
        userName = row['Name']
        userGender = row['Sex']

        sql_cmd2 = """
            select *
            from mediapp_userinfo
            where id = 
            """ + phID

        query_data2 = db.engine.execute(sql_cmd2)

        for row2 in query_data2:
            # phID = row['PharmacyID']
            print("user:", row2['PhName'])
            diction['phName'] = row2['PhName']
            phName = row2['PhName']
                
        data.append(diction)
    print(data)
    print(query_data2)
    print('ok')


    return jsonify(data), 200

@app.route('/phInfo/<lineID>', methods=['GET'])
def phInfo(lineID):
    # lineID = "'"+lineID+"'"

    data = []

    # sql_cmd = """
    #     select *
    #     from mediapp_patient
    #     where lineID = 
    # """ + lineID

    # query_data = db.engine.execute(sql_cmd)

    # for row in query_data:
        
    #     print("user:", row)
    #     phId = row['PharmacyID']

    # sql_cmd2 = """
    #     select *
    #     from mediapp_userinfo
    #     where id = 
    # """ + phId

    # query_data2 = db.engine.execute(sql_cmd2)

    # for row in query_data2:
    #     diction = {}
    #     print("phInfo:", row)
    #     diction['phName'] = row['PhName']
    #     diction['phTel'] = row['Telephone']
    #     diction['phAdd'] = row['Address']
    #     diction['LineID'] = row['LineID']
    #     diction['WebURL'] = row['WebURL']
    #     data.append(diction)

    query = mediapp_patient.query.filter_by(lineID=lineID).all()
    if query:
        for num in query:
            query2 = mediapp_userinfo.query.filter_by(id=num.PharmacyID).first()
            if query2 != None:
                
                diction = {}
                print("phInfo:", query2)
                diction['phName'] = query2.PhName
                diction['phTel'] = query2.Telephone
                diction['phAdd'] = query2.Address
                diction['LineID'] = query2.LineID
                diction['WebURL'] = query2.WebURL
                data.append(diction)

            else:
                dictionErr = {}
                # dictionErr['result'] = 'Not Found'
                # dictionErr['userName'] = num.Name
                # data.append(dictionErr)

    else:
        dictionErr = {}
        # dictionErr['lineID'] = lineID
        # dictionErr['result'] = 'Not Found'
        # data.append(dictionErr)
    
    
    return jsonify(data) , 200


@app.route('/addUser/', methods=['POST'])
def addUser():
    # , cardNumber, lineID, photo

    req_data = request.form
    cardID = req_data['cardID']
    cardNumber = req_data['cardNumber']
    # celePhone = req_data['celePhone']
    lineID = req_data['lineID']
    lineName = req_data['lineName']

    check = mediapp_patient.query.filter_by(lineID = lineID).first()
    
    if check == None:
        query = mediapp_patient.query.filter_by(cardID=cardID).first()

        query.cardNumber = cardNumber
        # query.Celephone = celePhone
        query.lineID = lineID
        query.lineName = lineName
        query.Certified = 2
        db.session.commit()

    else:
        query = mediapp_patient.query.filter_by(cardID=cardID).first()

        query.cardNumber = cardNumber
        # query.Celephone = celePhone
        query.lineID = lineID
        query.lineName = lineName
        query.Certified = 1
        db.session.commit()
    
    
    return 'ok', 200

@app.route('/checkUser/<cardID>', methods=['GET'])
def checkUser(cardID):

    res = ''

    query = mediapp_patient.query.filter_by(cardID=cardID).first()
    if query == None:
        print('Not Found')
        res = 'Not Found'
    else:
        print(query.id)
        res = 'Found'


    return res, 200
    
@app.route('/checkTime/<lineID>',methods=['GET'])
def checkMul(lineID):
    # data = []
    # lineID = "'"+lineID+"'"
    # sql_cmd = """
    #     select *
    #     from mediapp_patient
    #     where lineID = """+lineID 
    
    # query_data = db.engine.execute(sql_cmd)

    # for row in query_data:
    #     print("info: ",row['id'])
    #     sql_cmd2 = """
    #         select TakeMedDate
    #         from post
    #         where PatientID_id ={id}
    #     """.format(id=row['id'])
    #     query_data2 = db.engine.execute(sql_cmd2)    
    #     for row2 in query_data2:
    #         diction = {}
    #         print("time: ",row2['TakeMedDate'])
    #         diction['dayStart'] = row2['TakeMedDate']
    #         d = datetime.datetime.strptime(row2['TakeMedDate'],'%Y-%m-%d')
    #         delta = datetime.timedelta(days=10)
    #         n_days = d + delta
    #         print (n_days.strftime('%Y-%m-%d'))
    #         diction['dayEnd'] = n_days.strftime('%Y-%m-%d')
    #         data.append(diction)

        
    #     # query_data = db.engine.execute(sql_cmd2)
    data=[]
    query = mediapp_patient.query.filter_by(lineID=lineID).all()
    if query:
        for num in query:
            query2 = post.query.filter_by(PatientID_id=num.id).all()
            if query2:
                for row2 in query2:
                    if row2:
                        diction = {}
                        diction['userName'] = num.Name
                        diction['dayStart'] = row2.TakeMedDate_start
                        d = datetime.datetime.strptime(row2.TakeMedDate_start,'%Y-%m-%d')
                        diction['weekDayStart'] = d.weekday()
                        delta = datetime.timedelta(days=10)
                        n_days = d + delta
                        diction['dayEnd'] = n_days.strftime('%Y-%m-%d')
                        diction['weekDayEnd'] = n_days.weekday()
                        diction['symptom']=row2.symptom
                        data.append(diction)
                        # print(data)
                    else:
                        diction2 = {}
                        diction2['userName'] = num.Name
                        diction2['result'] = 'Not Found'
                        data.append(diction2)
            else:
                diction2 = {}
                # diction2['userName'] = num.Name
                # diction2['result'] = 'Not Found'
                # data.append(diction2)              
    else:
        diction3 = {}
        # diction3['lineID'] = lineID
        # diction3['result'] = 'Not Found'
        # data.append(diction3)       

    return jsonify(data), 200
'''
@app.route('/notify/<postID>',methods=['GET'])
def notify(postID):
    sql_cmd = """
        update post
        set RemindStatus = 2
        where id = {id}""".format(id=postID)
    
    db.engine.execute(sql_cmd)

    return 'ok', 200

@app.route('/problem',methods=['POST'])
def problem():
    req_data = request.form
    Type = req_data['Type']
    LineID = req_data['LineID']

    query = mediapp_patient.query.filter_by(lineID=LineID).first()
    if query is None:
        return 'Not Found', 400

    else:
        problemAns = mediapp_problems(Type=Type,LineID=LineID)
        db.session.add(problemAns)
        db.session.commit()

    return 'ok', 200
'''
@app.route('/notify/<postID>',methods=['GET'])
def notify(postID):
    # sql_cmd = """
    #     update post
    #     set RemindStatus = 2
    #     where id = {id}""".format(id=postID)
    
    # db.engine.execute(sql_cmd)

    query = post.query.filter_by(id=postID).first()

    if query is None:
        return 'Not Found', 400
    else:
        query.RemindStatus = 2
        db.session.commit()

    return 'ok', 200

@app.route('/postPh/<PhName>',methods=['GET'])
def postUser(PhName):
    data = []
    query = mediapp_userinfo.query.filter_by(PhName=PhName).first()
    if query == None:
        return 'Not Found', 200
    else:
        diction = {}
        # print("phInfo:", query)
        diction['phName'] = query.PhName
        diction['phTel'] = query.Telephone
        diction['phAdd'] = query.Address
        diction['LineID'] = query.LineID
        diction['WebURL'] = query.WebURL
        data.append(diction)

    return jsonify(data), 200

@app.route('/postInfo/<int:id>',methods=['GET'])
def postInfo(id):
    data = []
    diction = {}
    diction['postID'] = id
    query = post.query.filter_by(id=id).first()
    if query == None:
        return 'Post not exist', 200
    else:
        query2 = mediapp_patient.query.filter_by(id=query.PatientID_id).first()
        if query2 == None:
            return 'Patient not exist', 200
        else:
            diction['Gender'] = query2.Sex
            diction['Name'] = query2.Name
            diction['lineID'] = query2.lineID

        query3 = mediapp_userinfo.query.filter_by(id=query.PharmacyID).first()
    
        if query3 == None:
            return 'Pharmacy null', 200
        else:
            diction['PhName'] = query3.PhName

        diction['dayStart'] = query.TakeMedDate_start
        d = datetime.datetime.strptime(query.TakeMedDate_start,'%Y-%m-%d')
        diction['weekDayStart'] = d.weekday()
        delta = datetime.timedelta(days=10)
        n_days = d + delta
        diction['dayEnd'] = n_days.strftime('%Y-%m-%d')
        diction['weekDayEnd'] = n_days.weekday()
        diction['symptom']=query.symptom
        data.append(diction)
        return jsonify(data),200
    