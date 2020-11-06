from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, validators, FloatField
from wtforms.validators import DataRequired, length
from wtforms import DateField


class RegistrationForm(FlaskForm):
    dateofissue = DateField('Fecha de emisión:', default= date.today() format='%d-%m-%Y')
    name = StringField('Cliente:', validators=[DataRequired(), length(min=2, max=30)])
    amount = FloatField('Capital inicial:', validators= [DataRequired(),length(min=1)])
    product= SelectField('Producto:', choices=['Portafolio','Moneybox'])
    typ = SelectField('Tipo:', choices=['Clásico', 'Dinámico'])
    annualrate = SelectField('Tasa anual:', choices=["10%"])
    startdate = DateField('Fecha de inicio', default= date.today() format='%d-%m-%Y')
    isr = SelectField('ISR', choices=['1.04%', '1.45%'])
    generate = SelectField('Generar', choices=['Estado de cuenta' 'Proyección'])
    cutoffdate = DateField('Fecha de corte', default=date() format='%d-%m-%Y' )
    submit = SubmitField('Calcular')

