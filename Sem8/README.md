# Registro de Consumo de Agua

##  Planteamiento de la problemática
En la vida cotidiana, muchas personas olvidan beber suficiente agua durante el día, lo que puede causar deshidratación y afectar la salud.  
Aunque existen aplicaciones móviles, no siempre son accesibles en la computadora de escritorio o laptop, donde mucha gente pasa gran parte del día trabajando o estudiando.

Por ello, se propone desarrollar una **aplicación de escritorio en Python con PyQt5** que permita registrar la cantidad de agua que una persona bebe durante el día y mostrar si está cumpliendo con la **meta diaria recomendada (2 litros)**.

---

##  Solución propuesta
La aplicación cuenta con una interfaz gráfica sencilla en la que el usuario puede:

- Ingresar su **nombre**.  
- Registrar la **cantidad de agua** que acaba de beber (en mililitros).  
- Al presionar un botón, la aplicación sumará esa cantidad al total diario.  
- Mostrar en pantalla la **cantidad acumulada** y un mensaje indicando si ya alcanzó la meta.  
- Reiniciar los datos del día con un botón.  
- Visualizar una **barra de progreso** que se llena conforme se avanza hacia la meta.  

---

##  Diseño de la interfaz (Widgets utilizados)
- **QLabel** → etiquetas para mostrar títulos e instrucciones.  
- **QLineEdit** → campos de texto para ingresar nombre y cantidad de agua.  
- **QPushButton** → botones para registrar la cantidad y reiniciar los datos.  
- **QLabel** → etiqueta para mostrar resultados.  
- **QProgressBar** → barra de progreso para mostrar visualmente el avance hacia la meta.  

---

## Instalación
1. Asegúrate de tener Python 3 instalado.  
2. Instala la librería **PyQt5** con el siguiente comando:

```bash
pip install pyqt5
```

---

## Ejecución
Para ejecutar el programa, usa el siguiente comando en la terminal (ubicándote en la carpeta del archivo):

```bash
python nombre_del_archivo.py
```

---

##  Aprendizaje esperado
Este proyecto muestra cómo **aplicar PyQt5 para resolver problemas de la vida real**, utilizando:  

- Widgets básicos de PyQt5.  
- Manejo de entradas de usuario.  
- Retroalimentación visual con etiquetas y barra de progreso.  

Además, refuerza la importancia de **desarrollar hábitos saludables** apoyados en herramientas tecnológicas.
