from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://samvela_g9ol_user:XGLsFJAwwX7LxEmohUYOtOaWx3KkMGZp@dpg-cups7ga3esus738ic0kg-a.oregon-postgres.render.com/samvela_g9ol'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desactivar el seguimiento de modificaciones de objetos

# Inicializar SQLAlchemy
db = SQLAlchemy(app)

# Definir el modelo para la tabla 'alumnos'
class Alumno(db.Model):
    __tablename__ = 'alumnos'  # El nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True)
    no_control = db.Column(db.String(50), unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    ap_paterno = db.Column(db.String(100), nullable=False)
    ap_materno = db.Column(db.String(100), nullable=False)
    semestre = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Alumno {self.nombre} {self.ap_paterno}>'

# Ruta principal, que obtiene los alumnos desde la base de datos
@app.route('/')
def index():
    # Obtener todos los alumnos desde la base de datos
    alumnos = Alumno.query.all()
    return render_template('index.html', alumnos=alumnos)

if __name__ == '__main__':
    app.run(debug=True)
# Crear las tablas si no existen
with app.app_context():
    db.create_all()
