import sqlite3

con = sqlite3.connect('../../MyGym.db')

con.execute('CREATE TABLE Usuario(idusuario INTEGER PRIMARY KEY,correoelectronico STRING VARCHAR(100) NOT NULL, contraseña STRING NOT NULL, nombreusuario STRING NOT NULL)')

con.execute('CREATE TABLE reseñas(IDreseña INTEGER PRYMARY KEY,ID_USUARIO STRING, reseña STRING, ID_LOCAL STRING ,FOREIGN KEY(ID_USUARIO) REFERENCES Usuario(nombreusuario), FOREIGN KEY(ID_LOCAL) REFERENCES LocalClubGym(idlocal))')

con.execute('CREATE TABLE LocalClubGym(idlocal INTEGER PRIMARY KEY ,nombreLocal STRING NOT NULL, direccion STRING NOT NULL, telefono INTEGER NOT NULL, correoelectronico STRING VARCHAR(100) NOT NULL, instagram STRING, info STRING NOT NULL)')

con.execute('CREATE TABLE Sesiones(ID INTEGER PRIMARY KEY, ID_USUARIO INTEGER, FECHA_HORA TEXT, FOREIGN KEY(ID_USUARIO) REFERENCES Usuario(idusuario))')

con.execute('CREATE TABLE datosusuario(ID INTEGER PRIMARY KEY, edad TEXT,año TEXT, peso TEXT,altura TEXT , infogen TEXT, FOREIGN KEY(ID) REFERENCES Usuario(idusuario))')

con.execute('ALTER TABLE LocalClubGym ADD idusuario INTEGER REFERENCES Usuario (idusuario)')


