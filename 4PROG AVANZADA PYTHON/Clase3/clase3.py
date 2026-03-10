#UML y diagrama de clase
"""
+-------------------------+
|        Persona          |
+-------------------------+
| + nombre: String        |
| + edad: int             |
+-------------------------+
| - saludar() void        |
| - cumplir_anios() void  |
+-------------------------+

Modificadores de acceso:

+ publico
- privado
# protegido

### Relaciones entre clases ###

Asociación Unidireccional: Una clase usa o conoce a otra.
Cliente -------> Pedido

Asociación Bidireccional: Ambas clases interactuan entre si, se representa con felchas a ambos lados.
Cliente ------ Pedido

Agregación: Una clase que forma parte de otra pero que puede existir de forma independiente.
Curso ◇-------> Estudiante

Composición: Una clase que depende completamente de otra.
Automovil ◆-------> Motor

Dependencia: Una clase usa temporalmente a otra clase.
Cliente - - - - - - -> ServicioPago

Generalización: Representa la relación Padre-Hijo.
Animal ᐊ------------------ Perro

1 # uno a uno
0..1 # cero a uno
* muchos (cero o más)
1..* Uno a muchos

Equipo 1 ------->* Jugador


### Ejercicio:
Definir 4 clases:
Escuela
Aula
Profesor
Estudiante
Definir atributos y métodos de cada clase con sus respectivos datos y modificadores de acceso.

---------------------------------------


+-------------------------+
|        Escuela          |
+-------------------------+
| - nombre: String        |
| - dirección: String             |
+-------------------------+
| + Registrar_aula(aula: Aula)
| + info_escuela() String  |
+-------------------------+

+-------------------------+
|        Aula            |
+-------------------------+
| - numero: int             |
| - capacidad: int         |
+-------------------------+
| + asignar_profe(profe: Profesor)        |
| + asignar_estudiante(est: Estudiante)
+-------------------------+

+-------------------------+
|        Profesor          |
+-------------------------+
| + nombre: String        |
| + materia: String             |
+-------------------------+
| + dictar_clase() void        |
| + calificarExamen(estudiante: Estudiante, nota: float)  |
+-------------------------+

+-------------------------+
|        Estudiante          |
+-------------------------+
| - nombre: String        |
| - matricula: String
| - promedio: float          |
+-------------------------+
| + estudiar() void        |
| + promedioEstudiante() float  |
+-------------------------+

Escuela ------->* Aula
Aula 1 -------> Profe
Aula 1 ------->* Estudiantes

"""

'''
Colaboración: Es la interacción entre clases.
Tipos de colabvoración:
Colaboración mediante asociaciones: Las clases interactúan mediante relación directa.
colaboración clases auxiliares: Cuando una clase intermedia facilita la comunicación entre dos clases.
colaboración en patrones de diseño: Clase notifica a otra cambios de su estado.

Composición ◆ : Relación duerte entre clases. Depende completamente de otra.
Agregación ◇ : Relación débil entre clases. No depende de la existencia de otra.

------------------

Buenas prácticas:
Mantener la simplicidad
Agrupar elementos relacionados
Nombres descriptivos (Clases, Atributos y métodos)
Herencia sólo cuando sea necesario
Asegurar la cohesión (Evitar dependencias inecesarias)

'''
"""
########################################################################
Tipos de colaboración:
Colaboración mediante asociaciones: Ocurre cuando dos clases interactúan
mediante una relación directa.
● Colaboración con clases auxiliares: Cuando una clase intermedia facilita
la comunicación entre dos clases principales.
● Colaboración en patrones de diseño: Como el patrón de observador,
donde una clase notifica a otras sobre cambios en su estado.


Composición en UML:
    La composición es un tipo especial de asociación en UML que representa una relación de contención fuerte, donde una clase depende completamente de otra.
Si la clase contenedora es eliminada, las clases contenidas también desaparecen.
Diferencia entre composición y agregación:
● Composición (◆): Relación fuerte. Si el objeto principal es eliminado, los objetos dependientes también lo son.
● Agregación (◇): Relación débil. La vida del objeto agregado no depende de la existencia del objeto contenedor.



Pasos para leer un diagrama de clases

1. Identificar las clases principales: Localiza los rectángulos en el diagrama,
ya que representan las clases. Cada clase tiene su nombre en la parte
superior del rectángulo.
(ver la jerarquía, identificar clases principales)

2. Examinar los atributos y métodos: Dentro de cada clase, analiza los
atributos (propiedades) y métodos (operaciones). Observa sus tipos de
datos y niveles de visibilidad (+, -, #).

3. Observar las relaciones entre clases: Fíjate en los distintos tipos de líneas que conectan las clases, ya que indican asociaciones, herencia, dependencia, composición o agregación. ()

4. Analizar la multiplicidad: Busca los números cercanos a las líneas de asociación (1, 0..1, *, 1..*) que indican cuántas instancias de una clase pueden estar relacionadas con otra.

5. Determinar la jerarquía de clases: Si hay flechas triangulares, significa que existe una relación de herencia (generalización/especialización).

6. Buscar patrones de diseño comunes: Algunos diagramas pueden seguir patrones de diseño conocidos como el patrón de fábrica, el patrón
singleton, entre otros.


Errores comunes al leer diagramas de clases:
● Confundir herencia con asociación: Las líneas con flechas triangulares (◁) indican herencia, mientras que las líneas simples representan asociaciones.
● Ignorar la multiplicidad: No considerar los valores 1, * o 0..1 puede llevar a interpretaciones erróneas sobre la cantidad de instancias relacionadas.
● No analizar visibilidad de atributos y métodos: La falta de atención a los símbolos +, -, # puede hacer que no se comprendan bien los niveles de acceso a los datos.
● Pasar por alto dependencias o agregaciones: Líneas punteadas 
(---->) indican dependencias y rombos (◇ 'no dependiente' o ◆  'dependiente en su totalidad') indican agregación y composición, lo que es crucial para entender la relación entre clases.



Buenas prácticas:
Pasos para crear un diagrama de clases:

1. Identificar las clases principales: Determina las entidades fundamentales del sistema (por ejemplo, Usuario, Producto, Pedido).

- Agrupar elementos relacionados
- Utilizar nombres descriptivos

2. Definir atributos y métodos: Para cada clase, especifica sus atributos y métodos, asegurándote de usar los niveles de visibilidad adecuados (+, -, #).

3. Establecer relaciones entre clases: Identifica asociaciones, herencias (sólo cuando sea necesario!), agregaciones y composiciones según corresponda.

- Asegurar la cohesión.

4. Definir multiplicidad: Indica cuántas instancias de una clase pueden relacionarse con otra (1, *, 0..1, 1..*).

5. Aplicar principios de diseño: Usa encapsulación, herencia y modularidad para garantizar un diseño flexible y reutilizable.

6. Revisar y refinar el diagrama: Asegúrate de que el diagrama sea claro, preciso y fácil de entender.

########################################################################


"""

"""
TAREAAAAAAAAAAAAA para practicar:

---------------------------------
| Escuela |
---------------------------------
| - nombre : str |
| - direccion : str |
| - telefono : str |
| - aulas : List<Aula> |
---------------------------------
| + agregarAula(a: Aula) |
| + eliminarAula(a: Aula) |
| + buscarAula(num:int):Aula |
| + listarProfesores(): List |
---------------------------------

Escuela ◆────── 1..* Aula

---------------------------------
| Aula |
---------------------------------
| - numero : int |
| - capacidad : int |
| - profesor : Profesor |
| - estudiantes : List<Est> |
---------------------------------
| + asignarProfesor(p:Prof) |
| + agregarEstudiante(e:Est) |
| + eliminarEstudiante(e:Est) |
| + estaLlena(): bool |
---------------------------------

Aula ─────── 1 Profesor

---------------------------------
| Profesor |
---------------------------------
| - nombre : str |
| - especialidad : str |
| - salario : float |
| - aulas : List<Aula> |
---------------------------------
| + calcularSalarioAnual():flt |
| + listarAulas(): List |
---------------------------------

Aula ─────── 0..* Estudiante

---------------------------------
| Estudiante |
---------------------------------
| - nombre : str |
| - edad : int |
| - grado : int |
| - promedio : float |
| - aula : Aula |
---------------------------------
| + calcularPromedio(): float |
| + obtenerInfo(): str |
---------------------------------

Profesor ─────── 0..* Aula
Estudiante ─────── 1 Aula

"""


"""

class Escuela():
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.aulas = []

        def agregar_aula():
            pass

        def eliminar_aula():
            pass

        def buscar_aula():
            pass

        def listar_profesores():
            pass


class aula():
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.profesor = None
        self.estudiantes = []

        def asignar_profesor():
            pass

        def agregar_estudiante():
            pass

        def eliminar_estudiante():
            pass

        def esta_llena():
            pass


class Profesor():
    def __init__(self, nombre, especialidad, salario):
        self.nombre = nombre
        self.especialidad = especialidad
        self.salario = salario
        self.aulas = []

    def calcular_salario():
        pass

    def listar_aulas():
        pass


class Estudiante():
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.promedio = 0.0
        self.aula = None

    def calcular_promedio():
        pass

    def obtener_informacion():
        pass
        

        
"""

### Inicio proyecto de módulo ###


'''
Crear las siguientes clases mediante UML
----
Cliente:
id (int), nombre (str), email (str), Privado
get_id(), get_nombre(), set_nombre(), calcular_descuento() Publico
----
Cliente Regular
puntos (int) Privado
calcular_descuento() Publico
----
Cliente Premium
membresia (str) Privado
calcular_descuento() Publico
----
Cliente Corporativo
empresa (str) Privado
calcular_descuento() Publico
-----
GestorClientes
clientes (list) Privada
agregar(), listar(), buscar(), eliminar() Publico
'''
