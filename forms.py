from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, TextAreaField, PasswordField, SelectMultipleField, FileField, DateField, SelectField
from wtforms.validators import DataRequired, Email, Length, Optional


class RegisterForm(FlaskForm):
    name = StringField("Name: ", validators=[
                       DataRequired(), Length(min=4, max=20)])
    email = StringField("Email: ", validators=[Email()])
    password = PasswordField("Password", validators=[
                             DataRequired(), Length(min=4, max=20)])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField("Email: ", validators=[Email()])
    password = PasswordField("Password", validators=[
                             DataRequired(), Length(min=4, max=20)])
    submit = SubmitField("Login")


class UploadForm(FlaskForm):

    first_name = StringField()
    last_name = StringField()

    dob = DateField()
    email = StringField()
    file_photo = FileField()
    file_csv = FileField()
    comments = TextAreaField()

    submit = SubmitField("Upload")


class OpplanForm(FlaskForm):

    # header
    change_date = StringField()
    access_code = SelectField()
    probability = SelectField()

    # changes
    current_tier = SelectField()
    current_position = SelectField()
    current_restriction = SelectField()

    future_tier = SelectField()
    future_position = SelectField()
    future_restriction = SelectField()

    comments = TextAreaField("Comments", validators=[Length(max=2000)])

    submit = SubmitField("Save")


class ProfileForm(FlaskForm):
    first_name = StringField()
    last_name = StringField()
    email = StringField()
    dob = StringField()


class FormUtil():

    @staticmethod
    def get_choices(my_list):
        # print("my_list",my_list)
        tuple_options = [(x, x) for x in my_list]
        # print(tuple_options)
        return tuple_options
        #my_field.choices = tuple_options


class TableForm(FlaskForm):
    first_name = StringField()
    last_name = StringField()
    email = StringField()
    dob = StringField()


class EmployeeForm(FlaskForm):
    file_csv = FileField()
