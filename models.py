from app import db
import datetime

class mediapp_patient(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    cardID = db.Column(db.String(100), nullable=True)
    Name = db.Column(db.String(20), nullable=True)
    Address = db.Column(db.String(100), nullable=True)
    Birth = db.Column(db.String(15), nullable=True)
    Celephone = db.Column(db.String(15), nullable=True)
    Mail = db.Column(db.String(50), nullable=True)
    Sex = db.Column(db.String(10), nullable=True)
    Telephone = db.Column(db.String(15), nullable=True)
    PharmacyID = db.Column(db.String(100), nullable=True)
    pwd = db.Column(db.String(30), nullable=True)
    newUser = db.Column(db.Integer, nullable=True)
    cardNumber = db.Column(db.String(100), nullable=True)
    customerService = db.Column(db.Integer, nullable=True)
    lineID = db.Column(db.String(100), nullable=True)
    Certified = db.Column(db.String(4), nullable=True)
    lineName = db.Column(db.String(100), nullable=True)
    NotificationStatus = db.Column(db.Integer, nullable=True)

class mediapp_userinfo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    PhName = db.Column(db.String(100), nullable=True)
    Telephone = db.Column(db.String(100), nullable=True)
    user_id = db.Column(db.Integer, nullable=True)
    PageStatus = db.Column(db.Integer, nullable=True)
    TakeStatus = db.Column(db.Integer, nullable=True)
    CardReaderStatus = db.Column(db.Integer, nullable=True)
    CardReaderCardNo = db.Column(db.String(100), nullable=True)
    Address = db.Column(db.String(100), nullable=True)
    LineID = db.Column(db.String(100), nullable=True)
    WebURL = db.Column(db.String(200), nullable=True)

class post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    symptom = db.Column(db.String(100), nullable=True)
    Days = db.Column(db.Integer, nullable=True)
    CreateDate = db.Column(db.String(15), nullable=True)
    TakeMedDate = db.Column(db.String(15), nullable=True)
    AvaTimes = db.Column(db.Integer, nullable=True)
    Times = db.Column(db.Integer, nullable=True)
    Division = db.Column(db.String(30), nullable=True)
    CreateTime = db.Column(db.String(15), nullable=True)
    Status = db.Column(db.String(100), nullable=True)
    PatientID_id = db.Column(db.Integer, nullable=True)
    PharmacyID = db.Column(db.String(100), nullable=True)
    MedStatus = db.Column(db.String(6), nullable=True)
    MedFeature = db.Column(db.String(4), nullable=True)
    Description = db.Column(db.String(100), nullable=True)
    TakeMedDate_start = db.Column(db.String(15), nullable=True)
    RemindTime = db.Column(db.DateTime, default=None)
    RemindStatus = db.Column(db.String(4), nullable=True)
    TakeStatus = db.Column(db.String(4), nullable=True)
    Certified = db.Column(db.String(4), nullable=True)
    
class mediapp_problems(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Type = db.Column(db.Integer, nullable=True)
    LineID = db.Column(db.String(100), nullable=True)
    Created_time = db.Column(db.DateTime, default=datetime.datetime.now())