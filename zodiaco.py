from wtforms import Form
from wtforms import StringField, DateField, RadioField
from wtforms import validators

class ZodiacoChinoForm(Form):
    nombre = StringField('Nombre', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=3, max=20, message='de 3 a 20 caracteres')
    ])
    apellido_paterno = StringField('Apellido Paterno', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=3, max=20, message='de 3 a 20 caracteres')
    ])
    apellido_materno = StringField('Apellido Materno', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=3, max=20, message='de 3 a 20 caracteres')
    ])
    fecha_nacimiento = DateField('Fecha de Nacimiento', format='%Y-%m-%d', validators=[
        validators.DataRequired(message='El campo es requerido')
    ])
    sexo = RadioField('Sexo', choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], validators=[
        validators.DataRequired(message='El campo es requerido')
    ])
