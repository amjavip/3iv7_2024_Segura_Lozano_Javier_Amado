import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class EcoLoopApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle("EcoLoop - Iniciar Sesión")
        self.setGeometry(100, 100, 1280, 720)

        # Establecer el fondo con imagen desenfocada
        fondo_imagen = QtGui.QImage("C:/Users/javie/Downloads/4969c4bfa5a17947cdf8116c7a40a909.jpg")
        fondo_pixmap = QtGui.QPixmap.fromImage(fondo_imagen).scaled(self.size(), QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
        fondo_blur = fondo_pixmap.copy()
        blur_effect = QtWidgets.QGraphicsBlurEffect()
        blur_effect.setBlurRadius(10)
        fondo_label = QtWidgets.QLabel(self)
        fondo_label.setPixmap(fondo_blur)
        fondo_label.setGeometry(0, 0, 1280, 720)

        # Configuración del Frame de Formulario con border-radius y transparencia
        formulario_frame = QtWidgets.QFrame(self)
        formulario_frame.setGeometry(390, 160, 500, 600)
        formulario_frame.setStyleSheet("""
            QFrame {
                background-color: rgba(224, 242, 241, 200);  /* Fondo semi-transparente */
                border-radius: 20px;
            }
        """)

        # Logo
        logo_label = QtWidgets.QLabel(formulario_frame)
        logo_pixmap = QtGui.QPixmap("C:/Users/javie/Downloads/Screenshot_20240905_152458_WhatsApp-removebg-preview (3).png")
        logo_pixmap = logo_pixmap.scaled(80, 80, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(QtCore.Qt.AlignCenter)
        logo_label.setGeometry(210, 20, 80, 80)

        # Título
        titulo_label = QtWidgets.QLabel("Bienvenido", formulario_frame)
        titulo_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #004d40;")
        titulo_label.setAlignment(QtCore.Qt.AlignCenter)
        titulo_label.setGeometry(150, 120, 200, 40)

        # Subtítulo
        subtitulo_label = QtWidgets.QLabel("Inicie su sesión para continuar", formulario_frame)
        subtitulo_label.setStyleSheet("font-size: 12px; color: #004d40;")
        subtitulo_label.setAlignment(QtCore.Qt.AlignCenter)
        subtitulo_label.setGeometry(150, 160, 200, 20)

        # Campos de entrada
        nombre_entry = QtWidgets.QLineEdit(formulario_frame)
        nombre_entry.setPlaceholderText("Nombre (s)")
        nombre_entry.setGeometry(75, 200, 350, 30)

        apellido_entry = QtWidgets.QLineEdit(formulario_frame)
        apellido_entry.setPlaceholderText("Apellido (s)")
        apellido_entry.setGeometry(75, 240, 350, 30)

        clave_entry = QtWidgets.QLineEdit(formulario_frame)
        clave_entry.setPlaceholderText("Clave única de Registro")
        clave_entry.setEchoMode(QtWidgets.QLineEdit.Password)
        clave_entry.setGeometry(75, 280, 350, 30)

        # Botón de inicio de sesión
        boton_iniciar = QtWidgets.QPushButton("Iniciar Sesión", formulario_frame)
        boton_iniciar.setStyleSheet("""
            QPushButton {
                background-color: #00e676;
                color: white;
                font-size: 14px;
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #00c853;
            }
        """)
        boton_iniciar.setGeometry(150, 340, 200, 40)

        # Texto de registro
        registro_label = QtWidgets.QLabel("¿No tiene Cuenta? Vamos a Crear una", formulario_frame)
        registro_label.setStyleSheet("font-size: 10px; color: #00796b;")
        registro_label.setAlignment(QtCore.Qt.AlignCenter)
        registro_label.setGeometry(150, 400, 200, 20)

# Inicializar y ejecutar la aplicación
app = QtWidgets.QApplication(sys.argv)
window = EcoLoopApp()
window.show()
sys.exit(app.exec_())
