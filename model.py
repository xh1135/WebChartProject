import datetime
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = ""
    email = ""
    password = ""


class MyFormData(db.Model):
    __tablename__ = 'myform_data'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    first_name = ""
    last_name = ""
    email = ""
    password = ""
    my_date = ""
    comments = ""
    my_date_range = ""
    multiple_button = []
    single_button = ""
    multiple_states = []
    single_state = ""
    toggle_switch = ""
    custom_range = ""

    multiple_options = []
    single_option = ""

    radio1 = ""
    check_list = []


class OpplanData(db.Model):
    __tablename__ = 'opplan_data'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # header
    change_date = db.Column(db.String(80), nullable=True)
    access_code = db.Column(db.String(80), nullable=True)
    probability = db.Column(db.String(80), nullable=True)

    # current
    current_tier = db.Column(db.String(80), nullable=True)
    current_position = db.Column(db.String(80), nullable=True)
    current_restriction = db.Column(db.String(80), nullable=True)

    # future
    future_tier = db.Column(db.String(80), nullable=True)
    future_position = db.Column(db.String(80), nullable=True)
    future_restriction = db.Column(db.String(80), nullable=True)

    file_photo_filename = db.Column(db.String(80), nullable=True)
    file_photo_code = db.Column(db.String(80), nullable=True)
    comments = db.Column(db.String(1000), nullable=True)

    def remove_none_values(self):
        self.change_date = self.change_date if self.change_date else ""
        self.access_code = self.access_code if self.access_code else ""
        self.probability = self.probability if self.probability else ""

        self.current_tier = self.current_tier if self.current_tier else ""
        self.current_position = self.current_position if self.current_position else ""
        self.current_restriction = self.current_restriction if self.current_restriction else ""

        self.future_tier = self.future_tier if self.future_tier else ""
        self.future_position = self.future_position if self.future_position else ""
        self.future_restriction = self.future_restriction if self.future_restriction else ""

        self.comments = self.comments if self.comments else ""


class Profile(db.Model):
    __tablename__ = 'profile'

    # primary key
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # full_name
    first_name = db.Column(db.String(80), nullable=True)
    last_name = db.Column(db.String(80), nullable=True)

    #
    email = db.Column(db.String(80), nullable=True)
    dob = db.Column(db.String(80), nullable=True)

    # attachment
    file_photo_filename = db.Column(db.String(80), nullable=True)
    file_photo_code = db.Column(db.String(80), nullable=True)

    # excel/csv attachment
    file_data_filename = db.Column(db.String(80), nullable=True)
    file_data_code = db.Column(db.String(80), nullable=True)

    def remove_none_values(self):
        self.first_name = self.first_name if self.first_name else ""
        self.last_name = self.last_name if self.last_name else ""
        self.file_photo_filename = self.file_photo_filename if self.file_photo_filename else ""
        self.file_photo_code = self.file_photo_code if self.file_photo_code else ""
        self.file_data_filename = self.file_data_filename if self.file_data_filename else ""
        self.file_data_code = self.file_data_code if self.file_data_code else ""
        self.email = self.email if self.email else ""
        self.dob = self.dob if self.dob else ""


class Restaurant(db.Model):
    __tablename__ = 'restaurant'

    # primary key
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    bill = db.Column(db.Float, nullable=True)
    tip = db.Column(db.Float, nullable=True)

    def to_dict(self):
        return {"bill": self.bill, "tip": self.tip}

    def to_x_y(self):
        return {'x': self.bill, 'y': self.tip}


class Tables(db.Model):
    __tablename__ = 'tables'

    # primary key
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # full_name
    first_name = db.Column(db.String(80), nullable=True)
    last_name = db.Column(db.String(80), nullable=True)

    #
    email = db.Column(db.String(80), nullable=True)
    dob = db.Column(db.String(80), nullable=True)

    # attachment
    file_photo_filename = db.Column(db.String(80), nullable=True)
    file_photo_code = db.Column(db.String(80), nullable=True)

    skills = db.Column(db.String(80))

    # excel/csv attachment
    file_data_filename = db.Column(db.String(80), nullable=True)
    file_data_code = db.Column(db.String(80), nullable=True)

    def remove_none_values(self):
        self.first_name = self.first_name if self.first_name else ""
        self.last_name = self.last_name if self.last_name else ""
        self.file_photo_filename = self.file_photo_filename if self.file_photo_filename else ""
        self.file_photo_code = self.file_photo_code if self.file_photo_code else ""
        self.file_data_filename = self.file_data_filename if self.file_data_filename else ""
        self.file_data_code = self.file_data_code if self.file_data_code else ""
        self.email = self.email if self.email else ""
        self.dob = self.dob if self.dob else ""

    def list_2_string(self, my_skills, delim=","):
        my_str = ""
        if my_skills != None:
            for i in my_skills:
                my_str += i + delim
            self.skills = my_str

    def string_2_list(self, my_string):
        my_list = []


class Employee(db.Model):
    __tablename__ = 'py_employee'

    # primary key
    id = db.Column(db.Integer, primary_key=True)

    employee_id = db.Column(db.Integer)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone_number = db.Column(db.String(100))
    hire_date = db.Column(db.Date)
    job_id = db.Column(db.String(100))
    salary = db.Column(db.Float)
    commission_pct = db.Column(db.Float)
    department_id = db.Column(db.Integer)
    department_name = db.Column(db.String(100))

    def __str__(self):
        return self.first_name

    def __add__(self, value):
        return self.first_name + "+" + value.first_name

    def __gt__(self, value):
        return self.salary > value.salary

    def to_dict(self):
        return {"employee_id": self.employee_id, "salary": self.salary, "job_id": self.job_id}

    def to_x_y(self):
        return {'x': self.employee_id, 'y': self.salary}

    def to_x_y2(self):
        return {'x': self.employee_id, 'y': self.salary*.9}

    @classmethod
    def from_dict(cls, in_dict):
        cls = Employee()
        cls.employee_id = in_dict['EMPLOYEE_ID']
        cls.first_name = in_dict['FIRST_NAME']
        cls.last_name = in_dict['LAST_NAME']
        cls.email = in_dict['EMAIL']
        cls.phone_number = in_dict['PHONE_NUMBER']
        if in_dict['HIRE_DATE']:
            cls.hire_date = datetime.datetime.strptime(
                in_dict['HIRE_DATE'], "%m/%d/%Y")

        cls.job_id = in_dict['JOB_ID']
        cls.salary = in_dict['SALARY']
        cls.commission_pct = in_dict['COMMISSION_PCT']
        cls.department_id = in_dict['DEPARTMENT_ID']
        cls.department_name = in_dict['DEPARTMENT_NAME']

        return cls
