# -------------------------------------------------------------
# Planteamiento de la problemática
#
# En la vida cotidiana, muchas personas olvidan beber suficiente
# agua durante el día, lo que puede causar deshidratación y afectar 
# la salud. Aunque existen aplicaciones móviles, no siempre son accesibles 
# en la computadora de escritorio o laptop, donde mucha gente pasa gran parte 
# del día trabajando o estudiando.
#
# Por ello, se propone desarrollar una aplicación de escritorio que permita 
# registrar la cantidad de agua que una persona bebe durante el día y mostrar 
# si está cumpliendo con la meta diaria recomendada (2 litros).
# -------------------------------------------------------------
#
# Solución propuesta
#
# La aplicación tendrá una interfaz gráfica sencilla con PyQt5 en la que:
#
# - El usuario ingrese su nombre.
# - Ingrese la cantidad de agua que acaba de beber (en mililitros).
# - Al presionar un botón, la aplicación sumará esa cantidad al total diario.
# - Se mostrará en pantalla la cantidad acumulada y un mensaje indicando si 
#   ya alcanzó la meta.
# - También habrá un botón para reiniciar los datos del día.
# -------------------------------------------------------------
#
# Diseño de la interfaz 
#
# - QLabel: etiquetas para mostrar títulos e instrucciones.
# - QLineEdit: campos de texto para ingresar nombre y cantidad de agua.
# - QPushButton: botones para registrar la cantidad y reiniciar los datos.
# - QLabel: etiqueta para mostrar resultados.
# -------------------------------------------------------------





import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox, QProgressBar
)

class RegistroAgua(QWidget):
    def __init__(self):
        super().__init__()
        self.total_agua = 0      # Acumulador de agua bebida
        self.meta = 2000         # Meta diaria en ml
        self.initUI()

    def initUI(self):
        """Configura la interfaz gráfica"""
        self.setWindowTitle("Control de Consumo de Agua")
        self.setGeometry(200, 200, 400, 350)

        # Layout principal
        layout = QVBoxLayout()

        # Widgets
        self.label_nombre = QLabel("Ingrese su nombre:")
        self.input_nombre = QLineEdit()

        self.label_cantidad = QLabel("Cantidad de agua bebida (ml):")
        self.input_cantidad = QLineEdit()

        self.boton_registrar = QPushButton("Registrar consumo")
        self.boton_registrar.clicked.connect(self.registrar_agua)

        self.boton_reiniciar = QPushButton("Reiniciar datos")
        self.boton_reiniciar.clicked.connect(self.reiniciar)

        self.label_resultado = QLabel("Resultado: aún no hay registros.")

        # Barra de progreso
        self.barra_progreso = QProgressBar()
        self.barra_progreso.setMinimum(0)
        self.barra_progreso.setMaximum(self.meta)
        self.barra_progreso.setValue(0)
        self.barra_progreso.setStyleSheet("QProgressBar::chunk {background-color: green;}")

        # Agregar widgets al layout
        layout.addWidget(self.label_nombre)
        layout.addWidget(self.input_nombre)
        layout.addWidget(self.label_cantidad)
        layout.addWidget(self.input_cantidad)
        layout.addWidget(self.boton_registrar)
        layout.addWidget(self.boton_reiniciar)
        layout.addWidget(self.label_resultado)
        layout.addWidget(self.barra_progreso)

        self.setLayout(layout)

    def registrar_agua(self):
        """Suma la cantidad ingresada al total y actualiza la barra de progreso"""
        try:
            cantidad = float(self.input_cantidad.text())
            self.total_agua += cantidad
            nombre = self.input_nombre.text() or "Usuario"

            # Actualizar barra de progreso
            if self.total_agua > self.meta:
                self.total_agua = self.meta
            self.barra_progreso.setValue(int(self.total_agua))

            # Mostrar resultado
            if self.total_agua >= self.meta:
                self.label_resultado.setText(f"{nombre}, ¡Felicidades! Ya cumpliste tu meta de {self.meta} ml.")
            else:
                self.label_resultado.setText(f"{nombre}, llevas {self.total_agua} ml. ¡Sigue adelante!")
            
            self.input_cantidad.clear()
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor ingrese una cantidad válida en mililitros.")

    def reiniciar(self):
        """Reinicia los registros diarios"""
        self.total_agua = 0
        self.barra_progreso.setValue(0)
        self.label_resultado.setText("Resultado: aún no hay registros.")
        self.input_cantidad.clear()
        self.input_nombre.clear()

# Programa principal
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = RegistroAgua()
    ventana.show()
    sys.exit(app.exec_())
