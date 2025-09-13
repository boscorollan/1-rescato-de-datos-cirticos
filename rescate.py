from typing import List, Dict

#copiamos el enunciado
Presentación:

Bienvenidos, estimados alumnos. Este ejercicio simula una situación de emergencia tecnológica en la que deberán aplicar sus habilidades analíticas para diseñar una solución eficiente, lógica y bien comunicada.

Enunciado:

Imagina que eres el responsable de sistemas en una empresa que gestiona datos médicos sensibles. A las 8:00 de la mañana, se detecta un ataque de ransomware que ha comprometido parcialmente la infraestructura. El equipo de seguridad ha logrado aislar el ataque, pero solo tienes 120 minutos para rescatar los datos más críticos antes de que el sistema se reinicie automáticamente y se pierdan.

Dispones de un conjunto de tareas que deben ejecutarse en orden lógico, algunas en paralelo, y otras dependen de recursos limitados (como personal técnico o acceso físico a servidores).

Objetivos del Reto:

Definir el Objetivo del Proyecto: ¿Qué se debe lograr exactamente en estos 120 minutos?
Diagrama de Flujo del Cronograma: Representa las tareas y sus dependencias.
Nivelación de Recursos: Optimiza el uso de personal técnico y herramientas disponibles.
Plan de Comunicación de Crisis: ¿Cómo se informa a los stakeholders internos y externos?
Tareas, Descripciones y Duraciones:

A: Identificar servidores afectados (15 min)
B: Priorizar datos críticos (20 min)
C: Activar protocolo de recuperación (10 min)
D: Asignar técnicos a servidores (5 min)
E: Recuperar datos de servidor 1 (30 min)
F: Recuperar datos de servidor 2 (25 min)
G: Validar integridad de datos recuperados (15 min)
H: Generar informe preliminar para dirección (10 min)
I: Comunicar a clientes afectados (20 min)
J: Coordinar con equipo legal (15 min)
K: Preparar plan de contingencia (25 min)
Restricciones:

Solo hay 3 técnicos disponibles.
Solo se pueden recuperar datos de un servidor a la vez.
Las tareas H, I, J y K deben comenzar después de validar los datos (tarea G).




Instrucciones para la Entrega:

Fecha límite: lunes 15 de septiembre de 2025, 23:55 hrs.
Entrega en formato PDF.
Nombre del archivo: C1_Nombre_Apellido.pdf




Rúbrica de Evaluación:

  Categoría

Descripción

Ponderación

   Definición de Objetivos

Claridad y enfoque en el propósito del proyecto

20%

   Diagrama de Flujo del Cronograma

Precisión en dependencias y lógica del flujo

 25%

   Nivelación de Recursos

 Optimización del uso de técnicos y tiempos

20%

   Comunicación del Proyecto

Claridad y eficacia con stakeholders

20%

   Presentación y Formato

Organización y cumplimiento de instrucciones

15%

#le pedimos a la ia que haga el ejercicio
class Task:
    def __init__(self, code: str, description: str, duration: int, dependencies: List[str] = []):
        self.code = code
        self.description = description
        self.duration = duration
        self.dependencies = dependencies
        self.start_time = None
        self.end_time = None

    def __repr__(self):
        return f"{self.code}: {self.description} ({self.duration} min)"

class Technician:
    def __init__(self, name: str):
        self.name = name
        self.available_at = 0

class RescuePlan:
    def __init__(self):
        self.tasks = self._init_tasks()
        self.technicians = [Technician(f"Tecnico{i+1}") for i in range(3)]
        self.timeline = []

    def _init_tasks(self) -> Dict[str, Task]:
        return {
            "A": Task("A", "Identificar servidores afectados", 15),
            "B": Task("B", "Priorizar datos críticos", 20, ["A"]),
            "C": Task("C", "Activar protocolo de recuperación", 10, ["A"]),
            "D": Task("D", "Asignar técnicos a servidores", 5, ["B", "C"]),
            "E": Task("E", "Recuperar datos de servidor 1", 30, ["D"]),
            "F": Task("F", "Recuperar datos de servidor 2", 25, ["E"]),
            "G": Task("G", "Validar integridad de datos recuperados", 15, ["F"]),
            "H": Task("H", "Generar informe preliminar para dirección", 10, ["G"]),
            "I": Task("I", "Comunicar a clientes afectados", 20, ["G"]),
            "J": Task("J", "Coordinar con equipo legal", 15, ["G"]),
            "K": Task("K", "Preparar plan de contingencia", 25, ["G"]),
        }

    def schedule(self):
        completed = set()
        current_time = 0
        while len(completed) < len(self.tasks):
            for code, task in self.tasks.items():
                if code in completed:
                    continue
                if all(dep in completed for dep in task.dependencies):
                    # Asignar técnicos si es necesario
                    if code in ["E", "F"]:
                        tech = min(self.technicians, key=lambda t: t.available_at)
                        start = max(current_time, tech.available_at)
                        tech.available_at = start + task.duration
                        task.start_time = start
                        task.end_time = start + task.duration
                    else:
                        task.start_time = current_time
                        task.end_time = current_time + task.duration
                    self.timeline.append((task.code, task.start_time, task.end_time))
                    completed.add(code)
                    current_time = max(current_time, task.end_time)
        return self.timeline

    def print_schedule(self):
        print("Cronograma de Rescate de Datos Críticos:")
        for code, start, end in self.timeline:
            print(f"Tarea {code}: inicia en minuto {start}, termina en minuto {end}")

    def objetivos(self):
        print("Objetivo del Proyecto:")
        print("Rescatar los datos médicos más críticos en 120 minutos, asegurando la integridad y comunicación efectiva con todos los stakeholders.")

    def diagrama_flujo(self):
        print("\nDiagrama de Flujo (texto):")
        for code, task in self.tasks.items():
            deps = ", ".join(task.dependencies) if task.dependencies else "Ninguna"
            print(f"{code}: depende de [{deps}]")

    def nivelacion_recursos(self):
        print("\nNivelación de Recursos:")
        print("3 técnicos disponibles. Solo se recupera datos de un servidor a la vez. Técnicos asignados secuencialmente a tareas E y F.")

    def comunicacion_crisis(self):
        print("\nPlan de Comunicación de Crisis:")
        print("1. Informe preliminar a dirección tras validación de datos.")
        print("2. Comunicación a clientes afectados tras validación.")
        print("3. Coordinación con equipo legal tras validación.")
        print("4. Preparación de plan de contingencia tras validación.")

if __name__ == "__main__":
    plan = RescuePlan()
    plan.objetivos()
    plan.diagrama_flujo()
    plan.nivelacion_recursos()
    plan.comunicacion_crisis()
    plan.schedule()
    plan.print_schedule()