import sys
from PySide2 import *
from PyQt5 import*
from PyQt5.QtCore import *
from PySide2.QtCore import *
from PyQt5 import QtCore as Qt
from ui_base import *

from Custom_Widgets.Widgets import *
from mysql.connector.utils import init_bytearray, validate_normalized_unicode_string
import conexion


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #loadJsonStyle(self, self.ui)


# ===============================================
        # ACCION BOTONES NAVEGACION
# ===============================================
# Las funciones vienen en modulo PyQt5

        # Minimizar ventana
        self.ui.btn_minii.clicked.connect(lambda: self.showMinimized())

        # Maximizar o restaurar ventana
        # self.ui.btn_expandd.clicked.connect(lambda: self.fnt_restaurar_o_maximizar_ventana())

        # Cerrar ventana
        self.ui.btn_cerrarr.clicked.connect(lambda: self.close())

        # quitar barra de navegacion por defecto
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Abrir menu desplegable azul
        self.ui.btn_desplegar.clicked.connect(
            lambda: self.fnt_abrir_primer_menu())

        # boton y pagina home
        self.ui.btn_home.clicked.connect(
            lambda: self.ui.stw_contenedor_paginas.setCurrentWidget(self.ui.pg_home))

        # boton y pagina agregar estudante
        self.ui.btn_agregar_desplegable.clicked.connect(
            lambda: self.ui.stw_contenedor_paginas.setCurrentWidget(self.ui.pg_agregar_alumnos))
        
        # boton y pagina agregar docente
        self.ui.btn_agregar_desplegable_docente.clicked.connect(
            lambda: self.ui.stw_contenedor_paginas.setCurrentWidget(self.ui.pg_agregar_docente))

        # boton y pagina gestion alumnos
        self.ui.btn_gestionar_alumnos_desplegable.clicked.connect(
            lambda: self.ui.stw_contenedor_paginas.setCurrentWidget(self.ui.pg_gestion_alumnos))

        # boton y pagina gestion docente
        self.ui.btn_gestionar_docentes_desplegable.clicked.connect(
            lambda: self.ui.stw_contenedor_paginas.setCurrentWidget(self.ui.pg_gestion_docentes))

        # boton y pagina gestion docentes
        self.ui.btn_gestionar_docentes_desplegable.clicked.connect(
            lambda: self.ui.stw_contenedor_paginas.setCurrentWidget(self.ui.pg_gestion_docentes))

        # boton y pagina home
        # self.ui.btn_configuracion.clicked.connect(lambda: self.ui.stw_contenedor_paginas.setCurrentWidget(self.ui.pg_configuracion))



        # ------------------------------------------
        # boton guardar docente 
        self.ui.btn_guardar_docente.clicked.connect(lambda: self.guardarContactoDocente())


        #llamo al empaquetado de botones y funciones
        self.empaquetado_funcion_botones()

        #llamo a la función al init
        self.botones_desplegables()


        # ventana modificable tamaño
        QSizeGrip(self.ui.Qzise)


# ===============================================
# FUNCION MOVER VENTANA CLICK SOSTENIDO EN CABECERA
# ===============================================


        def fnt_moveWindow(e):
            # Detecta si la ventana tiene el tamaño normal
            if self.isMaximized() == False:  # No esta maximizar
                # se mueve la ventana solo si esta en tamaño normal
                # si el click izquierdo es apretado
                if e.buttons() == Qt.LeftButton:
                    # se mueve la ventana
                    self.move(self.pos() + e.globalPos() -
                              self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
            # se agrega de donde se quiere y pueda mover, en mi caso, solo de la cabecera
        self.ui.frm_cabecera.mouseMoveEvent = fnt_moveWindow

        self.show()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()


# ===============================================
        # FUNCIONES DE BOTONES
# ===============================================

    def empaquetado_funcion_botones(self):
    #ESTAS SON LAS FUNCIONES DE AGREGAR ESTUDIANTE*****

        #al presionar enter busca los estudiantes en el campo de buscar estudiantes insercion
        self.ui.txt_buscar_estudiante_2.returnPressed.connect(self.consultaarEstudiante_2)
        # boton buscar estudiantes2
        self.ui.btn_buscar_estudiante_2.clicked.connect(lambda: self.consultaarEstudiante_2())
        # boton actualizar en agregar estudiantes
        self.ui.btn_actualizar_estudiante_2.clicked.connect(lambda: self.actualizar())
        # boton guardar estudiante
        self.ui.btn_guardar_estudiantes.clicked.connect(lambda: self.guardarContacto())
        # boton cancelar estudiante
        self.ui.btn_cancelar_estudiantes.clicked.connect(lambda: self.cancelar())

    #ESTAS SON LAS FUNCIONES DE GESTIONAR ESTUDIANTE*****

        #presionar enter para buscar en la parte de gestion estudiante
        self.ui.txt_buscar_estudiante.returnPressed.connect(self.consultarEstudiante)
        # boton buscar estudiante
        self.ui.btn_buscar_estudiante.clicked.connect(lambda: self.consultarEstudiante())
        # boton guardar de la gestion estudiante
        self.ui.btn_guardar_estudiantes_ges.clicked.connect(lambda: self.guardarEstudianteGestion())
        # boton eliminar estudiantes
        self.ui.btn_eliminar_estudiante_ges.clicked.connect(lambda: self.eliminarEstudiante())
    def botones_desplegables(self):
        self.ui.btn_add.clicked.connect(lambda: self.abrir_agregar())
        self.ui.btn_gestion.clicked.connect(lambda: self.abrir_gestionar())



    def fnt_abrir_primer_menu(self):
        # meto en variable el menu
        ancho = self.ui.contenedor_contenedores.width()
        # si esta minimizado
        if ancho == 0:
            # expandir menu
            nuevo_ancho = 80
            # arreglar ruta
            # self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/icons/chevron-left.svg"))
        # si esta maximizado
        else:
            # volver a minimizar
            nuevo_ancho = 0
            # arreglar ruta
            # self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/icons/align-left.svg"))
        # animar el menu
        self.animacion = QPropertyAnimation(
        self.ui.contenedor_contenedores, b"maximumWidth")  # Animate minimumWidht
        self.animacion.setDuration(230)
        # Start value is the current menu ancho
        self.animacion.setStartValue(ancho)
        # end value is the new menu width
        self.animacion.setEndValue(nuevo_ancho)
        self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacion.start()


    def abrir_agregar(self):
                    # meto en variable el menu
        ancho = self.ui.frm_contenedor_agregar.width()

        # si esta minimizado
        if ancho == 0:
            # expandir menu
            nuevo_ancho = 120
        else:
            # volver a minimizar
            nuevo_ancho = 0
            # arreglar ruta


        self.animacion = QPropertyAnimation(
        self.ui.frm_contenedor_agregar, b"maximumWidth")  # Animate minimumWidht
        
        self.animacion.setDuration(230)
        # Start value is the current menu ancho
        self.animacion.setStartValue(ancho)
        # end value is the new menu width
        self.animacion.setEndValue(nuevo_ancho)
        self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacion.start()


    def abrir_gestionar(self):
                    # meto en variable el menu
        ancho = self.ui.frm_contenedor_gestionar_pri.width()

        # si esta minimizado
        if ancho == 0:
            # expandir menu
            nuevo_ancho = 120
        else:
            # volver a minimizar
            nuevo_ancho = 0
            # arreglar ruta


        self.animacion = QPropertyAnimation(
        self.ui.frm_contenedor_gestionar_pri, b"maximumWidth")  # Animate minimumWidht
        
        self.animacion.setDuration(230)
        # Start value is the current menu ancho
        self.animacion.setStartValue(ancho)
        # end value is the new menu width
        self.animacion.setEndValue(nuevo_ancho)
        self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacion.start()


# ===============================================
    # FUNCIONES DE VALIDAR CAMPOS
# ===============================================
    def validarCampos(self):
        PKIdentificacion = self.ui.txt_documento_estudiantes.text()
        Telefono = self.ui.txt_telefono_estudiantes.text()

        Nombre = self.ui.txt_nombres_estudiantes.text()
        Apellidos = self.ui.txt_apellidos_estudiantes.text()

        Busqueda_añadir_alumnos = self.ui.txt_buscar_estudiante_2.text()

        #verifica que no esten vacios
        if self.ui.txt_nombres_estudiantes.text()=="" or self.ui.txt_apellidos_estudiantes.text()=="" or self.ui.txt_documento_estudiantes.text()=="":
            alerta = QMessageBox()
            alerta.setText('¡Debes llenar los campos!')
            alerta.setIcon(QMessageBox.Information)
            alerta.exec()
            return True    

        # verificar que no esten vacios los campos de agregar docente
        """ if self.ui.txt_nombres_docente.text() == "" or self.ui.txt_apellidos_docente.text() == "" or self.ui.txt_documento_docente.text() == "":
            alerta = QMessageBox()
            alerta.setText('¡Debes todos llenar los campos!')
            alerta.setIcon(QMessageBox.Information)
            alerta.exec()
            return True """

        #verifica que no traiga numeros 
        if Nombre.isalpha() == False or Apellidos.isalpha() == False:
            alerta = QMessageBox()
            alerta.setText('¡Los campos "Nombre" y "Apellidos" solo admiten letras!')
            alerta.setIcon(QMessageBox.Information)
            alerta.exec()
            return True 

        #verifica que solo sean numeros
        try:
            PKIdentificacion = int(PKIdentificacion)
            Telefono = int(Telefono)
        except Exception:
            alerta = QMessageBox()
            alerta.setText('¡Los campos "Documento"  y "Telefono" solo admiten números!')
            alerta.setIcon(QMessageBox.Information)
            alerta.exec()
            return True
    

# ===============================================
    # FUNCIONES DE BOTONES DE LAS VENTANAS AGREGAR ESTUDIANTE
# ===============================================

    def guardarContacto(self):
        if self.validarCampos():
            return False
        PKIdentificacion = self.ui.txt_documento_estudiantes.text()
        Nombre = self.ui.txt_nombres_estudiantes.text()
        Apellidos = self.ui.txt_apellidos_estudiantes.text()
        Telefono = self.ui.txt_telefono_estudiantes.text()
        FKId_tblsexo = self.sexoEstudiante()

        FKId_tblgrado = self.gradoEstudiante(seleccion = self.ui.cbx_grado_estudiantes.currentText())
        objEst = conexion.SistemaDB()
        tblestudiante = objEst.guardarContacto((PKIdentificacion, Nombre, Apellidos, Telefono, FKId_tblsexo, FKId_tblgrado))

        #cada que se registre un alumno se le asigna una PKId de la tabla con su numero de documento
        PKId_tblgestion_alumno = objEst.guardar_PKId_tblgestion_Alumno_graciasA_PKIdentificacion((PKIdentificacion,PKIdentificacion,"1"))
        
        tbl_det_gestion_alumno = objEst.guardarNotaAndMateria((PKIdentificacion,"E01","0"))

        alerta = QMessageBox()
        alerta.setText('El alumno ha sido registrado de manera exitosa')
        alerta.setIcon(QMessageBox.Information)
        alerta.exec()
        
        self.limpiarCampos()


    def actualizar(self):
        if self.validarCampos():
            return False
        PKIdentificacion = self.ui.txt_documento_estudiantes.text()
        Nombre = self.ui.txt_nombres_estudiantes.text()
        Apellidos = self.ui.txt_apellidos_estudiantes.text()
        Telefono = self.ui.txt_telefono_estudiantes.text()
        FKId_tblsexo = self.sexoEstudiante()

        FKId_tblgrado = self.gradoEstudiante(seleccion = self.ui.cbx_grado_estudiantes.currentText())
        objEst = conexion.SistemaDB()
        tblestudiante = objEst.modificarContactos((Nombre, Apellidos, Telefono, FKId_tblsexo, FKId_tblgrado, PKIdentificacion))

        
        alerta = QMessageBox()
        alerta.setText('El alumno ha sido actualizado de manera exitosa')
        alerta.setIcon(QMessageBox.Information)
        alerta.exec()


        self.limpiarCampos()

    def cancelar(self):
        self.limpiarCampos()


# ===============================================
# FUNCION GENERAL DE LAS VENTANAS AGREGAR ESTUDIANTE
# ===============================================

    def sexoConsulta(self):

        if self.sexo == 1:
            self.ui.rb_hombre_estudiantes.setChecked(1)
        elif self.sexo == 2:
            self.ui.rb_mujer_estudiantes.setChecked(1)

    def sexoEstudiante(self):

        if self.ui.rb_hombre_estudiantes.isChecked():
            return 1
        elif self.ui.rb_mujer_estudiantes.isChecked():
            return 2

# este grado estudiante es cuando seleccionen en el combobox devuelva el valor numero
# para que se registre en la base de datos gracias a dicho valor
    def gradoEstudiante(self,seleccion):
        seleccion = seleccion
        
        if seleccion == "Primero":
            return 1
        elif seleccion == "Segundo":
            return 2
        elif seleccion == "Tercero":
            return 3
        elif seleccion == "Cuarto":
            return 4
        elif seleccion == "Quinto":
            return 5
        elif seleccion == "Sexto":
            return 6
        elif seleccion == "Septimo":
            return 7
        elif seleccion == "Octavo":
            return 8
        elif seleccion == "Noveno":
            return 9
        elif seleccion == "Diez":
            return 10
        elif seleccion == "Once":
            return 11

# este grado se usa cuando se realiza un consulta, si en la base de datos
# hay un usuario con "1" en la interfaz va a ver "primero"
# utilizo setcurrentindex para asigar la posicion de item
    def gradoEstudiante_consulta(self, grado, combo):
        grado = grado
        combo = combo
        if grado == 1:
            combo.setCurrentIndex(0)
        elif grado == 2:
            combo.setCurrentIndex(1)
        elif grado == 3:
            combo.setCurrentIndex(2)
        elif grado == 4:
            combo.setCurrentIndex(3)
        elif grado == 5:
            combo.setCurrentIndex(4)
        elif grado == 6:
            combo.setCurrentIndex(5)
        elif grado == 7:
            combo.setCurrentIndex(6)
        elif grado == 8:
            combo.setCurrentIndex(7)
        elif grado == 9:
            combo.setCurrentIndex(8)
        elif grado == 10:
            combo.setCurrentIndex(9)
        elif grado == 11:
            combo.setCurrentIndex(10)



    def limpiarCampos(self):
        self.ui.txt_nombres_estudiantes.setText("")
        self.ui.txt_apellidos_estudiantes.setText("")
        self.ui.txt_documento_estudiantes.setText("")
        self.ui.txt_telefono_estudiantes.setText("")
        self.ui.txt_buscar_estudiante.setText("")
        self.ui.txt_buscar_estudiante_2.setText("")

        # para el modulo docente
        self.ui.txt_nombres_docente.setText("")
        self.ui.txt_apellidos_docente.setText("")
        self.ui.txt_documento_docente.setText("")
        self.ui.txt_telefono_docente.setText("")
        self.ui.txt_buscar_docente.setText("")
        self.ui.txt_buscar_docente_2.setText("")
        


# ============================================================
    # FUNCIONES DE BOTONES DE LAS VENTANAS GESTION ESTUDIANTE
# ============================================================
    def consultarEstudiante(self):
    # seleccionar todas las columnas y no editar las columnas
    #configuración tabla de gestion alumnos
        self.ui.tbl_info_estudiante.setEditTriggers(
            QTableWidget.NoEditTriggers)
        self.ui.tbl_info_estudiante.setSelectionBehavior(
            QTableWidget.SelectRows)

        self.ui.tbl_info_estudiante.setRowCount(0)
        indiceControl = 0



#===========CONSULTAR============#

        #declaro variable para tomar el documento y asi poder realizar las busquedas
        PKIdentificacion = self.ui.txt_buscar_estudiante.text()
        objBuscarEst = conexion.SistemaDB()
        
        # declaro variables para especificar donde quiero consultar y que clave voy a usar
        tabla = "tblestudiante"
        clave = "PKIdentificacion"
        tblestudiante = objBuscarEst.consultarRegistro(
            tabla, clave, PKIdentificacion)

        # consulto directamente sin usar variables
        tblgestion_alumno = objBuscarEst.consultarRegistro(
            "tblgestion_alumno", "FKIdentificacion", PKIdentificacion)
        print(tblgestion_alumno)

        #consulta materia 
        tbl_det_gestion_alumno = objBuscarEst.consultarRegistro(
            "tbl_det_gestion_alumno", "FKId_tblGestion_Alumno", PKIdentificacion)


        # buscar en la tupla el grado del estudiante
        for buscador in tblestudiante:
            self.identificacion = buscador[0]
            self.grado_segu = buscador[5]
            self.grado_segu = self.gradoEstudiante_consulta(
                self.grado_segu, self.ui.cbx_edit_grado_est)
          

        # buscar en la tupla el grado del estudiante
        for buscador in tblgestion_alumno:
            self.periodo_consulta = buscador[2]
            self.PKId_tblgestion_alumno = buscador[0]
            # utilizo gradoEstudiante_consulta para traer los mismos metodos de return item
            self.periodo_consulta = self.gradoEstudiante_consulta(
                self.periodo_consulta, self.ui.cbx_edit_periodo_est)
            #print(self.PKId_tblgestion_alumno)


        #bucle para traer la materia
        for buscador in tbl_det_gestion_alumno:
            self.PKId_tbl_det_gestion_alumno = buscador[0]
            self.nota_final = buscador[3]
            self.nota_final = self.ui.txt_edit_nota_est.setText(str(self.nota_final))
            self.materias_consulta = buscador[2]
            self.materias_consulta = self.materiaEstudiante_Consulta(
                self.materias_consulta, self.ui.cbx_edit_materia_est
            )

            #print(tbl_det_gestion_alumno)

        #este bucle es para traer los 3 elementos a la tabla de gestion
        for contacto in tblestudiante:
            self.ui.tbl_info_estudiante.setRowCount(indiceControl+1)
            self.ui.tbl_info_estudiante.setItem(
                indiceControl, 0, QTableWidgetItem(str(contacto[0])))
            self.ui.tbl_info_estudiante.setItem(
                indiceControl, 1, QTableWidgetItem(str(contacto[1])))
            self.ui.tbl_info_estudiante.setItem(
                indiceControl, 2, QTableWidgetItem(str(contacto[2])))

        
        self.limpiarCampos()


# consulta de estudiantes en el campo agregar


    def consultaarEstudiante_2(self):
        buscar = self.ui.txt_buscar_estudiante_2.text()
        objBuscarEst_2 = conexion.SistemaDB()
        tabla = "tblestudiante"
        clave = "PKIdentificacion"
        corredor = objBuscarEst_2.consultarRegistro(
            tabla, clave, buscar)

        print(corredor)

        for x in corredor:
            self.ui.txt_nombres_estudiantes.setText(x[1])
            self.ui.txt_apellidos_estudiantes.setText(x[2])
            self.ui.txt_telefono_estudiantes.setText(x[3])
            self.ui.txt_documento_estudiantes.setText(x[0])
            self.sexo = x[4]
            self.sexo = self.sexoConsulta()
            self.grado = x[5]
            self.grado = self.gradoEstudiante_consulta(
                self.grado, self.ui.cbx_grado_estudiantes)


# funcion del boton guardar gestion estudiante
    def guardarEstudianteGestion(self):
        id_estudiante = self.identificacion #self.identificacion
        id_det_gestion_alumno = self.PKId_tbl_det_gestion_alumno
        # sePKId_tblgestion_alumno = self.PKId_tblgestion_alumno
        NotaFinal = self.ui.txt_edit_nota_est.text()
        Materia = self.materiaEstudiante()
        Grado = self.gradoEstudiante(seleccion = self.ui.cbx_edit_grado_est.currentText())
        Periodo = self.periodoEstudiante()
        
        objEst = conexion.SistemaDB()
        MateriaAc = objEst.ActualizarMateria(( Materia, id_det_gestion_alumno))
        NotaAc = objEst.ActualizarNota((NotaFinal,id_det_gestion_alumno))
        GradoAc = objEst.ActualizarGrado((Grado,id_estudiante))
        PeriodoAc = objEst.ActualizarPeriodo((Periodo,id_estudiante))
        
        alerta = QMessageBox()
        alerta.setText('Datos del alumno guardados correctamente')
        alerta.setIcon(QMessageBox.Information)
        alerta.exec()



    def periodoEstudiante(self):
        seleccion = self.ui.cbx_edit_periodo_est.currentText()

        if seleccion == "Primero":
            return 1
        elif seleccion == "Segundo":
            return 2
        elif seleccion == "Tercero":
            return 3
        elif seleccion == "Cuarto":
            return 4


    def materiaEstudiante(self):
        seleccion = self.ui.cbx_edit_materia_est.currentText()
        mat1 = "E01"
        mat2 = "E02"
        mat3 = "E03"
        mat4 = "E04"
        mat5 = "E05"
        mat6 = "E06"
        mat7 = "E07"
        if seleccion == "Edu.Fisica":
            return mat1
        elif seleccion == "Quimica":
            return mat2
        elif seleccion == "Matematica":
            return mat3
        elif seleccion == "Física":
            return mat4
        elif seleccion == "Tecnologia":
            return mat5
        elif seleccion == "Español":
            return mat6
        elif seleccion == "Etica":
            return mat7

    def materiaEstudiante_Consulta(self,codigo,combo):
        codigo = codigo
        combo = combo
        if codigo == "E01":
            combo.setCurrentIndex(0)
        elif codigo == "E02":
            combo.setCurrentIndex(1)
        elif codigo == "E03":
            combo.setCurrentIndex(2)
        elif codigo == "E04":
            combo.setCurrentIndex(3)
        elif codigo == "E05":
            combo.setCurrentIndex(4)
        elif codigo == "E06":
            combo.setCurrentIndex(5)
        elif codigo == "E07":
            combo.setCurrentIndex(6)
        
# funcion eliminar estudiantes en gestion
    def eliminarEstudiante(self):
        MensajeBorrar = QMessageBox()
        MensajeBorrar.setText("Eliminar estudiante")
        MensajeBorrar.setInformativeText("¿Está seguro que desea guardar los cambios?")
        MensajeBorrar.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel)
        MensajeBorrar.setDefaultButton(QMessageBox.Save)
        decision = MensajeBorrar.exec_()
        if decision == QMessageBox.Save:

            objEliminarEst = conexion.SistemaDB()
            objEliminarEst.borrarAlumno("tbl_det_gestion_alumno","PKId",self.PKId_tbl_det_gestion_alumno)
            objEliminarEst.borrarAlumno("tblgestion_alumno","PKId",self.PKId_tblgestion_alumno)
            objEliminarEst.borrarAlumno("tblestudiante","PKIdentificacion",self.identificacion)
            self.consultarEstudiante()
        else:
            pass

# ===============================================================
# ===============================================================
    # FUNCIONES DE BOTONES DE LAS VENTANAS AGREGAR DOCENTE
# ===============================================================
# ===============================================================

    def guardarContactoDocente(self):
        if self.validarCampos():
            return False
        PKIdentificacion = self.ui.txt_documento_docente.text()
        Nombre = self.ui.txt_nombres_docente.text()
        Apellidos = self.ui.txt_apellidos_docente.text()
        Telefono = self.ui.txt_telefono_docente.text()
        FKId_tblsexo = self.sexo()
        objDoc = conexion.SistemaDB()
        tblestudiante = objDoc.guardarContactoDocente((PKIdentificacion, Nombre, Apellidos, Telefono, FKId_tblsexo))

        self.limpiarCampos()


    def actualizarDocente(self):
        if self.validarCampos():
            return False
        PKIdentificacion = self.ui.txt_documento_docente.text()
        Nombre = self.ui.txt_nombres_docente.text()
        Apellidos = self.ui.txt_apellidos_docente.text()
        Telefono = self.ui.txt_telefono_docente.text()
        FKId_tblsexo = self.sexo()
        objEst = conexion.SistemaDB()
        tblestudiante = objEst.modificarContactosDocente((Nombre, Apellidos, Telefono, FKId_tblsexo, PKIdentificacion))

        self.limpiarCampos()

    def cancelar(self):
        self.limpiarCampos()

    # esta para la ventana de agregar docente
    def consultaarDocente_2(self):
        buscar = self.ui.txt_buscar_docente_2.text()
        objBuscarDoc_2 = conexion.SistemaDB()
        tabla = "tbldocente"
        clave = "PKIdentificacion"
        corredor = objBuscarDoc_2.consultarRegistro(
            tabla, clave, buscar)

        print(corredor)

        for x in corredor:
            self.ui.txt_nombres_docente.setText(x[1])
            self.ui.txt_apellidos_docente.setText(x[2])
            self.ui.txt_telefono_docente.setText(x[3])
            self.ui.txt_documento_docente.setText(x[0])
            self.sexo = x[4]
            self.sexo = self.sexoConsulta()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
