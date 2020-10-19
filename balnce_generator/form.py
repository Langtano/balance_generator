from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, validators, FloatField
from wtforms.validators import DataRequired, length


class RegistrationForm(FlaskForm):
    name = StringField('Cliente', validators=[DataRequired(), length(min=2, max=30)])
    amount = FloatField('Capital inicial', [validators.required()])
    typ = SelectField('Tipo', choices=['Clásico', 'Dinámico'])
    isr = SelectField('ISR', choices=['1.04%', '1.45%'])
    submit = SubmitField('Generar')
