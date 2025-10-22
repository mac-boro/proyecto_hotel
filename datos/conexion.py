from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# pip install sqlalchemy
# pip install mysql-connector-python

# Definir cadena de conexion
# mysql+mysqlconnector://user:password@host:port/database_name
# Reemplazar user, password, host, port, y database con sus credenciales de DB
DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/proyecto_hotel"
motor_db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=motor_db)