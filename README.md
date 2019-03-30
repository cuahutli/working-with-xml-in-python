# Leer y Escribir archivos XML

**Pasos para arrancar proyecto:**

1. Crear un carpeta y acceder a ella:
    ```sh
    mkdir readwritexmlpy && cd readwritexmlpy
    ```
2. Clonar el repositorio en la carpeta; 
    > *el `.` al final de la linea indica que se clonará en la carpeta raíz sin crear una subcarpeta*:
    ```sh
    git clone https://github.com/cuahutli/working-with-xml-in-python.git .
    ```
3. Crear un entorno virtual con `virtualenv` llamado `venv`:
    ```sh
    virtualenv venv
    ```
    > si se tiene más de una instalación local de python y se necesita crear el entorno virtual con una versión diferente a la versión por default del sistema usar `virtualenv -p path/to/python.exe venv`
4. Activar el entorno virtual:
    ```sh
    #Windows
    venv\Script\activate
    
    #Linux - Mac
    source venv/bin/activate
    ```
5. Instalar las librerias de las que depende el proyecto con `pip`:
    ```sh
    pip install -r requirements.txt
    ```

#### **A probar el proyecto y disfrutar!!**

## Fuentes utilizadas para el aprendizaje

* https://www.datacamp.com/community/tutorials/python-xml-elementtree
* https://stackabuse.com/reading-and-writing-xml-files-in-python/
* https://pymotw.com/2/xml/etree/ElementTree/create.html

