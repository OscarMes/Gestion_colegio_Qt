from logging import error
from re import X
import mysql.connector


class SistemaDB:
    def iniciarConexion(self):
        self.conexion = mysql.connector.connect(host="localhost", user="root", 
        passwd="", database="cindy_dbsistema")
        return self.conexion

    def consultarRegistro(self, tabla,clave,datoContacto):
        tabla = tabla
        clave = clave
        conexion = self.iniciarConexion()
        cursor = conexion.cursor()
        sql = f"SELECT * FROM {tabla} WHERE {clave} = {datoContacto}"
        cursor.execute(sql)
        return cursor.fetchall()
        # conexion.close()
        

    def guardarContacto(self,datosContacto):
        conexion = self.iniciarConexion()
        cursor = conexion.cursor()
        sql = "INSERT INTO tblestudiante(PKIdentificacion, Nombre, Apellidos, Telefono, FKId_tblsexo, FKId_tblgrado) \
        VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, datosContacto)
        conexion.commit()
        conexion.close()
#----------------------------------------------------
#------ GESTION ESTUDIANTE FUNCIONES ---------------
    def guardarPeriodo(self,datosContacto):
        conexion = self.iniciarConexion()
        cursor = conexion.cursor()
        sql_periodo = "INSERT INTO tblgestion_alumno(FKId_tblPeriodo) \
        VALUES (%s)"
        cursor.execute(sql_periodo, datosContacto)
        conexion.commit()
        conexion.close()

#========================================#
    #Actualizo cada parte de gestion#
#========================================#
    def guardarNotaAndMateria(self, datos):
        conexion = self.iniciarConexion()
        cursor = conexion.cursor()
        sql = "INSERT INTO tbl_det_gestion_alumno(FKId_tblGestion_Alumno, FKId_tblMaterias, Nota_final) \
        VALUES (%s, %s, %s)"
        cursor.execute(sql, datos)
        conexion.commit()
        conexion.close()




    def ActualizarMateria(self, datos):
        conexion = self.iniciarConexion()
        cursor = conexion.cursor()
        sql = "UPDATE tbl_det_gestion_alumno SET FKId_tblMaterias = %s WHERE PKId= %s"
        cursor.execute(sql, datos)
        conexion.commit()
        conexion.close()   

    def ActualizarNota(self,datos):
        conexion = self.iniciarConexion()
        cursor = conexion.cursor()
        sql = "UPDATE tbl_det_gestion_alumno SET Nota_final = %s WHERE PKId= %s"
        cursor.execute(sql, datos)
        conexion.commit()
        conexion.close()  

    def ActualizarGrado(self,datos):
        conexion = self.iniciarConexion()
        cursor = conexion.cursor()
        sql = "UPDATE tblestudiante SET FKId_tblgrado = %s WHERE PKIdentificacion= %s"
        cursor.execute(sql, datos)
        conexion.commit()
        conexion.close()  

    def ActualizarPeriodo(self,datos):
        conexion = self.iniciarConexion()
        cursor = conexion.cursor()
        sql = "UPDATE tblgestion_alumno SET FKId_tblPeriodo = %s WHERE PKId= %s"
        cursor.execute(sql, datos)
        conexion.commit()
        conexion.close()  


#======
    def guardar_PKId_tblgestion_Alumno_graciasA_PKIdentificacion(self,datos):
        conexion = self.iniciarConexion()
        cursor = conexion.cursor()
        sql = "INSERT INTO tblgestion_alumno(PKId, FKIdentificacion, FKId_tblPeriodo) \
        VALUES (%s, %s, %s)"
        cursor.execute(sql, datos)
        conexion.commit()
        conexion.close() 


    def borrarAlumno(self,tabla,PKId,id):
        conexion = self.iniciarConexion()
        cursor = conexion.cursor()
        sql = f"DELETE FROM {tabla} WHERE {PKId} = {id}"
        cursor.execute(sql)
        conexion.commit()
        conexion.close()

    def modificarContactos(self,datosContacto):
        conexion = self.iniciarConexion()
        cursor = conexion.cursor()
        sql = "UPDATE tblestudiante SET Nombre =%s,Apellidos =%s, Telefono =%s, FKId_tblsexo=%s,FKId_tblgrado=%s WHERE PKIdentificacion= %s"
        cursor.execute(sql,datosContacto)
        conexion.commit()
        conexion.close()


#----------------------------------------------------
#------ FUNCIONES DEL MODULO DOCENTE ---------------
    def guardarContactoDocente(self,datosContacto):
        conexion = self.iniciarConexion()
        cursor = conexion.cursor()
        sql = "INSERT INTO tbldocente(PKIdentificacion, Nombre, Apellidos, Telefono, FKId_tblsexo) \
        VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, datosContacto)
        conexion.commit()
        conexion.close()

    def modificarContactosDocente(self,datosContacto):
        conexion = self.iniciarConexion()
        cursor = conexion.cursor()
        sql = "UPDATE tbldocente SET Nombre =%s,Apellidos =%s, Telefono =%s, FKId_tblsexo=%s,FKId_tblgrado=%s WHERE PKIdentificacion= %s"
        cursor.execute(sql,datosContacto)
        conexion.commit()
        conexion.close()
