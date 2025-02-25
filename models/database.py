from os import environ

#Importa la clase MySQLDatabase del ORM (Object-Relational Mapping) Peewee, que se usa para interactuar 
# con bases de datos MySQL de manera más sencilla.
from peewee import MySQLDatabase

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configurar la conexión a la base de datos
db = MySQLDatabase(
    environ.get("DB_NAME"),
    user=environ.get("DB_USER"),
    password=environ.get("DB_PASSWORD"),
    port=int(environ.get("DB_PORT")),
    host=environ.get("DB_HOST")
)

class BaseModel(Model):
    class Meta:
        database = db  # Aquí db está configurado para conectarse a sistema_gestion_may


#Una vez establecida el modelo de la base de datos, y su conexión, establecemos cada clase en relación a las tablas de la base de datos

class Tipo_Usuario(BaseModel):
    ID = AutoField()
    Nombre = CharField(max_length=50, null=False)
    Descripcion = CharField(max_length=250, null=True)

class Usuario(BaseModel):
    ID = AutoField()
    Nombre = CharField(max_length=50, null=False)
    Apellido = CharField(max_length=50, null=True)
    Email = CharField(max_length=100, unique=True)
    Fecha_nacimiento = DateTimeField(null=True)
    Activo = BooleanField(default=False)
    ID_Tipo_Usuario = ForeignKeyField(Tipo_Usuario, backref='usuarios', on_delete='CASCADE')
    Fecha_creacion = DateTimeField(null=False)

class Historial_Conexion(BaseModel):
    ID = AutoField()
    ID_Usuario = ForeignKeyField(Usuario, backref='historial_conexion', on_delete='CASCADE')
    Fecha_Hora = DateTimeField(null=True)
    IP = CharField(max_length=45, null=True)
    Navegador = CharField(max_length=120, null=True)
    Duracion_Sesion = IntegerField(null=True)

class Cuentas_Vinculadas(BaseModel):
    ID = AutoField()
    ID_Usuario = ForeignKeyField(Usuario, backref='cuentas_vinculadas', on_delete='CASCADE')
    Nombre = CharField(max_length=50, null=True)
    URL = CharField(max_length=150, null=True)

class Menu(BaseModel):
    ID = AutoField()
    Titulo = CharField(max_length=50, null=True)
    Descripcion = CharField(max_length=200, null=True)
    URL = CharField(max_length=250, null=True)
    Activo = BooleanField(null=True)

class Menu_Usuario(BaseModel):
    ID_Usuario = ForeignKeyField(Usuario, backref='menu_usuario', on_delete='CASCADE')
    ID_Menu = ForeignKeyField(Menu, backref='menu_usuario', on_delete='CASCADE')

    class Meta:
        primary_key = CompositeKey('ID_Usuario', 'ID_Menu')

db.connect()