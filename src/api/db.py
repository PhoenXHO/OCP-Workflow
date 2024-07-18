from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

db = SQLAlchemy()

def init_db(app):
	load_dotenv()

	app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI').replace('mysql://', 'mysql+pymysql://')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
	
	db.init_app(app)

	with app.app_context():
		db.create_all()
		print('\033[92m + Database initialized successfully\033[0m')

	return db

class Personnel(db.Model):
	__tablename__ = 'personnel'
	reg_num = db.Column(db.String(255), primary_key=True)
	cin = db.Column(db.String(255), unique=True)
	first_name = db.Column(db.String(255), nullable=False)
	last_name = db.Column(db.String(255), nullable=False)
	dept = db.Column(db.String(255), nullable=False)
	phone = db.Column(db.String(255), nullable=False)
	email = db.Column(db.String(255), nullable=False, unique=True)
	password = db.Column(db.String(255), nullable=False)
	deleted = db.Column(db.Boolean, nullable=False, default=False)
	is_admin = db.Column(db.Boolean, nullable=False, default=False)
	photo = db.Column(db.String(255), nullable=False)
	#face_encoding = db.Column(db.JSON, nullable=False)

class TimeTable(db.Model):
	__tablename__ = 'timetable'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	personnel_reg_num = db.Column(db.String(255), db.ForeignKey('personnel.reg_num'), nullable=False)
	json = db.Column(db.JSON, nullable=False)