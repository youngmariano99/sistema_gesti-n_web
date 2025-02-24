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

class products(BaseModel):
    Product_ID = AutoField()
    Name = CharField()
    Stock = IntegerField()
    Price = DecimalField(max_digits=10, decimal_places=2)
    Cost = DecimalField(max_digits=10, decimal_places=2)
    Category_ID = IntergerField()

db.connect()