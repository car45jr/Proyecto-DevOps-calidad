# Proyecto DevOps - Aseguramiento de la Calidad

> **Curso:** Aseguramiento de la Calidad de Software  
> **Tema:** Integración Continua (CI) y Prácticas DevOps  
> **Proyecto:** `proyecto-devops-calidad`  
> **Entorno:** Python 3.10+ / Pytest / GitHub Actions  

---

## 1. Descripción del Proyecto

Este repositorio constituye un proyecto práctico de nivel universitario diseñado para demostrar, de forma clara, reproducible y didáctica, los pilares fundamentales del **Aseguramiento de la Calidad de Software** a través de la cultura y herramientas **DevOps** e **Integración Continua (CI)**.

A través de una arquitectura minimalista, el proyecto ilustra el ciclo de vida moderno del software:
1. Control de versiones riguroso con Git.
2. Construcción y validación de software mediante pruebas automatizadas con `pytest`.
3. Medición objetiva de la cobertura de código con `pytest-cov`.
4. Automatización del flujo de integración continua con **GitHub Actions**.
5. Análisis estático y métricas de calidad de código con **SonarQube / SonarCloud**.
6. Portabilidad del flujo CI/CD hacia otras plataformas de la industria (**Jenkins**, **GitLab CI**, **CircleCI**, **Azure DevOps**).

---

## 2. Objetivo

El propósito central **NO es construir un sistema complejo**, sino centrar toda la atención en los mecanismos de calidad, automatización y prevención de errores.

La aplicación desarrollada es una **calculadora aritmética deliberadamente sencilla**, lo que permite:
- Comprender con total transparencia qué hace cada función.
- Evitar ruidos o complejidades ajenas a DevOps (bases de datos, librerías web, frameworks pesados).
- Demostrar cómo una batería de pruebas automatizadas previene la introducción de defectos (regresiones) en el repositorio central.

---

## 3. Tecnologías Utilizadas

| Tecnología | Rol en el Proyecto |
|---|---|
| **Python (3.10+)** | Lenguaje de desarrollo base, simple, legible y estándar. |
| **pytest (8+)** | Framework para diseño y ejecución de pruebas unitarias automatizadas. |
| **pytest-cov (5+)** | Extensión para cálculo y análisis de cobertura de código. |
| **Git** | Sistema de control de versiones distribuido con historial semántico. |
| **GitHub** | Plataforma de alojamiento de código y colaboración. |
| **GitHub Actions** | Orquestador de Integración Continua (CI) en la nube (pipeline principal). |
| **SonarQube / SonarCloud** | Herramienta de análisis estático de código y Quality Gate (configuración lista). |
| **Jenkins / GitLab / CircleCI / Azure** | Ejemplos académicos de definición de pipelines multiplataforma. |

---

## 4. Estructura del Proyecto

```text
proyecto-devops-calidad/
│
├── app.py                      # Código fuente de la aplicación (funciones aritméticas)
├── test_app.py                 # Pruebas unitarias automatizadas con pytest
├── requirements.txt            # Dependencias mínimas y estables del proyecto
├── README.md                   # Documentación principal del proyecto (este archivo)
├── .gitignore                  # Reglas de exclusión para Git (venv, caché, etc.)
├── .coveragerc                 # Configuración del reporte de cobertura
├── sonar-project.properties    # Configuración para análisis con SonarQube / SonarCloud
│
├── .github/
│   └── workflows/
│       └── ci.yml              # Pipeline principal de CI en GitHub Actions
│
├── docs/
│   └── evidencias.md           # Guía detallada para toma de capturas del informe académico
│
├── Jenkinsfile                 # Ejemplo académico de pipeline declarativo en Jenkins
├── .gitlab-ci.yml              # Ejemplo académico de pipeline en GitLab CI/CD
├── .circleci/
│   └── config.yml              # Ejemplo académico de pipeline en CircleCI
└── azure-pipelines.yml         # Ejemplo académico de pipeline en Azure DevOps
```

### Descripción de los archivos clave

- **[`app.py`](app.py)**: Define las operaciones `sumar`, `restar`, `multiplicar` y `dividir`. Esta última valida que el divisor no sea cero, lanzando `ZeroDivisionError`.
- **[`test_app.py`](test_app.py)**: Contiene 7 casos de prueba que cubren enteros positivos, negativos, números con coma flotante (decimales) y la verificación del lanzamiento de excepciones.
- **[`.github/workflows/ci.yml`](.github/workflows/ci.yml)**: Define el flujo de trabajo automático que se activa en cada `push` o `pull_request` sobre la rama principal.
- **[`sonar-project.properties`](sonar-project.properties)**: Establece los metadatos y la ruta de reportes de cobertura para el análisis de deuda técnica, bugs y olores de código.
- **[`docs/evidencias.md`](docs/evidencias.md)**: Manual con los 9 puntos de evidencia gráfica exigidos para el reporte o informe de cátedra.

---

## 5. Instalación y Entorno Local

Para replicar este proyecto en tu máquina local, sigue las instrucciones acordes a tu sistema operativo.

### Requisitos previos
- Tener instalado **Python 3.10** o superior.
- Tener instalado **Git**.

### Paso 1: Clonar o ingresar al directorio del proyecto
```bash
git clone <URL_DEL_REPOSITORIO>
cd proyecto-devops-calidad
```

### Paso 2: Crear el entorno virtual (`venv`)

- **En Windows:**
  ```bash
  python -m venv venv
  ```
- **En Linux / macOS:**
  ```bash
  python3 -m venv venv
  ```

### Paso 3: Activar el entorno virtual

- **En Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
- **En Windows (CMD):**
  ```cmd
  venv\Scripts\activate.bat
  ```
- **En Linux / macOS:**
  ```bash
  source venv/bin/activate
  ```

### Paso 4: Instalar dependencias
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Paso 5: Ejecución manual de la aplicación
```bash
python app.py
```
Salida esperada:
```text
=== Calculadora DevOps - Aseguramiento de la Calidad ===
Suma (10 + 5):         15
Resta (10 - 5):        5
Multiplicación (10 * 5): 50
División (10 / 5):      2.0
```

---

## 6. Ejecución de Pruebas Automatizadas

El proyecto utiliza **pytest** para validar las reglas de negocio de forma no supervisada.

### Ejecutar todas las pruebas:
```bash
pytest
```
O con reporte detallado (modo verbose):
```bash
pytest -v
```

### Salida esperada:
```text
test_app.py::test_sumar_positivos PASSED                                 [ 14%]
test_app.py::test_restar_positivos PASSED                                [ 28%]
test_app.py::test_multiplicar_positivos PASSED                           [ 42%]
test_app.py::test_dividir_exacta PASSED                                  [ 57%]
test_app.py::test_dividir_entre_cero PASSED                              [ 71%]
test_app.py::test_operaciones_con_negativos PASSED                       [ 85%]
test_app.py::test_operaciones_con_decimales PASSED                       [100%]

============================== 7 passed in 0.10s ==============================
```

---

## 7. Medición de Cobertura de Código

La cobertura de código indica qué porcentaje de nuestras líneas de código fuente fueron realmente ejecutadas por la suite de pruebas.

### Comando:
```bash
pytest --cov=app --cov-report=term-missing
```

### Salida esperada:
```text
Name     Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------
app.py      10      0      2      0   100%
----------------------------------------------------
TOTAL       10      0      2      0   100%
```

El proyecto alcanza un **100% de cobertura de sentencias y ramas**, garantizando que cada instrucción y cada bifurcación lógica (como la condición `if b == 0`) están verificadas por pruebas automáticas.

---

## 8. Integración Continua (CI) con GitHub Actions

El pipeline configurado en [`.github/workflows/ci.yml`](.github/workflows/ci.yml) representa el corazón de la práctica de Integración Continua.

### ¿Cómo funciona el flujo automático?

```text
  +------------------+
  |  Desarrollador   |
  +--------+---------+
           | git push / pull_request
           v
  +------------------+
  |  GitHub Actions  |  (Servidor en la nube: ubuntu-latest)
  +--------+---------+
           | 1. Descarga repositorio (actions/checkout@v4)
           | 2. Configura Python 3.11 (actions/setup-python@v5)
           | 3. Instala dependencias (pip install -r requirements.txt)
           | 4. Ejecuta pruebas (pytest -v)
           | 5. Mide cobertura (pytest --cov=app)
           v
  +------------------+
  | ¿Pruebas pasan?  |
  +----+--------+----+
       |        |
   SI  |        | NO
       v        v
  [ EXITOSO ]  [ FALLIDO ]
  (Check verde) (Check rojo + alerta al equipo)
```

Cada vez que un desarrollador envía un cambio a la rama `main`, GitHub crea una máquina virtual limpia, descarga el código, instala las dependencias y ejecuta las pruebas de forma totalmente desatendida. Si una prueba falla, el pipeline aborta y previene que el código defectuoso sea considerado apto.

---

## 9. Demostración de Fallo Intencional

Para comprender el valor preventivo del pipeline, se realiza una prueba de fallo controlado:

1. **Inyección del fallo:** Modificar temporalmente en `app.py` la función `sumar`:
   ```python
   def sumar(a, b):
       return a - b  # ERROR INTENCIONAL
   ```
2. **Commit y Push:**
   ```bash
   git add app.py
   git commit -m "test: provocar fallo intencional en suma"
   git push origin main
   ```
3. **Observación en GitHub:**  
   GitHub Actions ejecuta el pipeline. `pytest` detecta que `sumar(5, 3)` dio `2` en lugar de `8`. El workflow se marca en **rojo (FAILED)**.
4. **Corrección:** Se restaura `return a + b`, se realiza otro commit y push, y el workflow retorna inmediatamente a **verde (SUCCESS)**.

*(Ver pasos detallados con capturas en [`docs/evidencias.md`](docs/evidencias.md)).*

---

## 10. Análisis Estático con SonarQube / SonarCloud

**SonarQube** (o su versión en la nube **SonarCloud**) complementa las pruebas dinámicas analizando estáticamente el código:
- **Bugs y vulnerabilidades:** Detección de patrones propensos a fallas o brechas de seguridad.
- **Code Smells (Olores de código):** Malas prácticas que afectan la mantenibilidad y legibilidad.
- **Deuda Técnica:** Estimación del tiempo necesario para sanear el código.
- **Quality Gate (Puerta de Calidad):** Criterio de aceptación estricto (ej. "cobertura > 80%", "0 vulnerabilidades") antes de aprobar un cambio.

### Configuración en este proyecto
El archivo [`sonar-project.properties`](sonar-project.properties) ya está preparado. Para activarlo en GitHub Actions:
1. Crear una cuenta en [SonarCloud](https://sonarcloud.io) y vincular el repositorio.
2. Añadir en GitHub (`Settings > Secrets and variables > Actions`):
   - `SONAR_TOKEN`: Token generado en SonarCloud.
3. El pipeline detectará automáticamente la presencia del token y ejecutará el análisis. Si no está configurado, el paso se omite de forma segura sin romper las pruebas unitarias principales.

---

## 11. Comparación Técnica de Herramientas CI/CD

El proyecto incluye archivos de configuración para las herramientas de CI/CD más relevantes de la industria, demostrando la portabilidad del concepto de pipeline:

| Herramienta | Archivo de Configuración | Filosofía / Características |
|---|---|---|
| **GitHub Actions** | `.github/workflows/ci.yml` | Integración nativa en GitHub, runners administrados, ecosistema de Actions reutilizables. |
| **Jenkins** | `Jenkinsfile` | Estándar de facto en infraestructuras on-premise, extensible vía plugins, sintaxis Groovy/declarativa. |
| **GitLab CI/CD** | `.gitlab-ci.yml` | Integración profunda con GitLab, orientación nativa a contenedores Docker y Kubernetes. |
| **CircleCI** | `.circleci/config.yml` | Optimizado para alta velocidad, almacenamiento en caché avanzado y paralelización de tareas. |
| **Azure DevOps** | `azure-pipelines.yml` | Solución empresarial de Microsoft, soporte multiplataforma e integración con Azure Cloud. |
| **SonarQube / SonarCloud** | `sonar-project.properties` | Análisis estático, evaluación de métricas de calidad, seguridad y Quality Gates. |

> **Nota académica:** La demostración en vivo y la validación principal de este proyecto se ejecutan sobre **GitHub Actions**. Los archivos `Jenkinsfile`, `.gitlab-ci.yml`, `.circleci/config.yml` y `azure-pipelines.yml` se entregan con fines comparativos y de estudio de interoperabilidad DevOps.

---

## 12. Relación con el Aseguramiento de la Calidad (QA)

En la ingeniería de software tradicional, las pruebas solían realizarse al final del ciclo de desarrollo (fase tardía), provocando que los defectos fueran detectados tarde, con un coste de corrección exponencialmente mayor.

La adopción de **DevOps e Integración Continua** aplica el principio de **Shift-Left Testing** (probar temprano y frecuentemente):
- **Feedback inmediato:** El programador recibe notificación de fallos pocos segundos después de subir su código.
- **Detección temprana de regresiones:** Se asegura que las nuevas funciones no rompan lo que ya funcionaba.
- **Objetividad:** La máquina valida el código bajo un entorno limpio y reproducible, eliminando el clásico problema de *"en mi máquina sí funcionaba"*.
- **Cultura de calidad compartida:** La calidad deja de ser responsabilidad exclusiva del departamento de testing para convertirse en una propiedad intrínseca del pipeline de entrega.
