from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SelectMultipleField, TimeField, DateTimeField, widgets
from wtforms.validators import DataRequired, Email, Length


class NewPatientForm(FlaskForm):
    """Form for adding new patiens."""

    name = StringField('Name', validators=[DataRequired()])

    address = StringField('Address', validators=[DataRequired()])

    city = StringField('City', validators=[DataRequired()])

    frequency = StringField('Weekly Frequency', validators=[DataRequired()])

    timeframe_start = StringField('Start Date', validators=[DataRequired()])

    timeframe_end = StringField('End Date', validators=[DataRequired()])

class CheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class PatientEditForm(FlaskForm):
    """Form to edit patient information and preferences."""

    name = StringField('Name', validators=[DataRequired()])

    address = StringField('Address', validators=[DataRequired()])

    city = StringField('City', validators=[DataRequired()])

    frequency = StringField('Weekly Frequency', validators=[DataRequired()])

    timeframe_start = StringField('Start Date', validators=[DataRequired()])

    timeframe_end = StringField('End Date', validators=[DataRequired()])

    preferred_days = CheckboxField('Preferred Days:', choices=["Monday", "Tuesday", "Wednesday", "Thurdsay", "Friday"])

    preferred_times = CheckboxField("Preferred Times:", choices=["9am-11am", "11am-1pm", "1pm-3pm", "3pm-5pm"])
