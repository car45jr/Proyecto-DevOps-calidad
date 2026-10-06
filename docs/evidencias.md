# Guía de Evidencias Prácticas para el Informe Académico

> **Curso:** Aseguramiento de la Calidad de Software  
> **Tema:** Integración Continua y DevOps  
> **Proyecto:** `proyecto-devops-calidad`  

Este documento sirve como manual paso a paso para ejecutar las pruebas, activar el pipeline de Integración Continua y recolectar las capturas de pantalla requeridas para el informe escrito y la exposición del proyecto.

---

## Índice de Evidencias

1. [Evidencia 1 — Proyecto funcionando localmente](#evidencia-1--proyecto-funcionando-localmente)
2. [Evidencia 2 — Pruebas automatizadas con pytest](#evidencia-2--pruebas-automatizadas-con-pytest)
3. [Evidencia 3 — Medición de cobertura de código](#evidencia-3--medición-de-cobertura-de-código)
4. [Evidencia 4 — Repositorio en GitHub](#evidencia-4--repositorio-en-github)
5. [Evidencia 5 — Workflow de GitHub Actions exitoso](#evidencia-5--workflow-de-github-actions-exitoso)
6. [Evidencia 6 — Pipeline fallido (error provocado intencionalmente)](#evidencia-6--pipeline-fallido-error-provocado-intencionalmente)
7. [Evidencia 7 — Detalle del error en los logs de GitHub Actions](#evidencia-7--detalle-del-error-en-los-logs-de-github-actions)
8. [Evidencia 8 — Corrección del código y pipeline exitoso](#evidencia-8--corrección-del-código-y-pipeline-exitoso)
9. [Evidencia 9 — Análisis de calidad con SonarQube / SonarCloud](#evidencia-9--análisis-de-calidad-con-sonarqube--sonarcloud)

---

## Evidencia 1 — Proyecto funcionando localmente

### Propósito
Demostrar que la aplicación Python ejecuta correctamente sus operaciones aritméticas en el entorno de desarrollo local.

### Comando a ejecutar (Terminal / PowerShell):
```powershell
python app.py
```
*(O con el entorno virtual activo: `.\venv\Scripts\python app.py`)*

### Salida esperada en consola:
```text
=== Calculadora DevOps - Aseguramiento de la Calidad ===
Suma (10 + 5):         15
Resta (10 - 5):        5
Multiplicación (10 * 5): 50
División (10 / 5):      2.0
```

### Qué parte de la pantalla capturar:
- La ventana de la terminal completa mostrando el comando ejecutado y la salida impresa con los 4 resultados correctos.

### Leyenda académica para el informe:
> **Figura 1.** Ejecución local satisfactoria de la aplicación aritmética demostrando las operaciones básicas.

---

## Evidencia 2 — Pruebas automatizadas con pytest

### Propósito
Verificar que la suite de pruebas unitarias valida de forma automatizada los 7 casos de prueba (suma, resta, multiplicación, división exacta, división entre cero, números negativos y números decimales).

### Comando a ejecutar:
```powershell
pytest -v
```

### Salida esperada en consola:
```text
============================= test session starts =============================
platform win32 -- Python 3.14.x, pytest-9.x.x
rootdir: ...\proyecto-devops-calidad
collected 7 items

test_app.py::test_sumar_positivos PASSED                                 [ 14%]
test_app.py::test_restar_positivos PASSED                                [ 28%]
test_app.py::test_multiplicar_positivos PASSED                           [ 42%]
test_app.py::test_dividir_exacta PASSED                                  [ 57%]
test_app.py::test_dividir_entre_cero PASSED                              [ 71%]
test_app.py::test_operaciones_con_negativos PASSED                       [ 85%]
test_app.py::test_operaciones_con_decimales PASSED                       [100%]

============================== 7 passed in 0.10s ==============================
```

### Qué parte de la pantalla capturar:
- La consola donde se aprecien los 7 tests con estado `PASSED` en verde y el resumen final `7 passed in 0.XXs`.

### Leyenda académica para el informe:
> **Figura 2.** Ejecución exitosa de la suite completa de pruebas unitarias automatizadas mediante el framework pytest.

---

## Evidencia 3 — Medición de cobertura de código

### Propósito
Comprobar objetivamente el porcentaje de líneas y bifurcaciones de código evaluadas por las pruebas mediante la herramienta `pytest-cov`.

### Comando a ejecutar:
```powershell
pytest --cov=app --cov-report=term-missing
```

### Salida esperada en consola:
```text
Name     Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------
app.py      10      0      2      0   100%
----------------------------------------------------
TOTAL       10      0      2      0   100%
============================== 7 passed in 0.13s ==============================
```

### Qué parte de la pantalla capturar:
- La tabla de cobertura generada en la terminal, resaltando la columna `Cover` con el valor `100%`.

### Leyenda académica para el informe:
> **Figura 3.** Reporte cuantitativo de cobertura de código alcanzando el 100% de declaraciones y bifurcaciones en app.py.

---

## Evidencia 4 — Repositorio en GitHub

### Propósito
Evidenciar la estructura de archivos en la nube, el control de versiones con Git y la presencia de los workflows de integración continua.

### Cómo visualizarlo:
1. Abrir el navegador e ingresar a la URL del repositorio en GitHub:  
   `https://github.com/<TU_USUARIO>/proyecto-devops-calidad`
2. Asegurarse de estar en la pestaña **Code** y en la rama `main`.

### Qué archivos deben aparecer en la captura:
- Directorio `.github/workflows/`
- Directorio `docs/`
- `app.py`
- `test_app.py`
- `requirements.txt`
- `README.md`
- `.gitignore`
- `Jenkinsfile`, `.gitlab-ci.yml`, `azure-pipelines.yml`, `.circleci/`
- El mensaje del último commit limpio y el badge o indicador de estado verde (si está habilitado).

### Leyenda académica para el informe:
> **Figura 4.** Vista general del repositorio del proyecto en GitHub con la estructura de archivos y configuración CI/CD.

---

## Evidencia 5 — Workflow de GitHub Actions exitoso

### Propósito
Demostrar la ejecución automática y exitosa del pipeline de Integración Continua ante un evento `push`.

### Cómo visualizarlo:
1. En GitHub, hacer clic en la pestaña superior **Actions**.
2. Seleccionar el workflow llamado **`CI - Pruebas y Calidad`** en la barra lateral izquierda.
3. Observar la lista de ejecuciones. El commit más reciente debe mostrar un icono de check verde `✔` con el título del commit.
4. Hacer clic sobre la ejecución para ver el resumen del job `Pruebas Automatizadas y Cobertura`.

### Qué parte de la pantalla capturar:
- La interfaz de GitHub Actions con el check verde, el nombre del evento (`push`), la rama (`main`), el autor y la duración de la ejecución.

### Leyenda académica para el informe:
> **Figura 5.** Pipeline de Integración Continua (GitHub Actions) ejecutado con éxito tras la integración de cambios en main.

---

## Evidencia 6 — Pipeline fallido (error provocado intencionalmente)

### Propósito
Demostrar cómo la Integración Continua detecta automáticamente una regresión o defecto antes de que llegue a producción o se fusione en ramas estables.

### Pasos exactos para provocar el fallo:
1. Abrir `app.py` en el editor.
2. Modificar la función `sumar` introduciendo un defecto lógico:
   ```python
   def sumar(a: float | int, b: float | int) -> float | int:
       """Retorna la suma de dos números (ERROR PROVOCADO)."""
       return a - b  # Debería ser a + b
   ```
3. Guardar el archivo y ejecutar en la terminal:
   ```powershell
   git add app.py
   git commit -m "test: provocar fallo intencional en suma para validacion de CI"
   git push origin main
   ```
4. Ingresar inmediatamente a GitHub → **Actions**.
5. Esperar aproximadamente 20-30 segundos mientras el workflow se ejecuta.
6. El workflow cambiará a una cruz roja `✖` con estado **Failed**.

### Qué parte de la pantalla capturar:
- La pantalla principal de GitHub Actions mostrando la ejecución con el icono rojo de fallo `✖` y el mensaje del commit correspondiente.

### Leyenda académica para el informe:
> **Figura 6.** Detección automática de fallo en GitHub Actions al recibir un commit con un defecto lógico en la función sumar.

---

## Evidencia 7 — Detalle del error en los logs de GitHub Actions

### Propósito
Mostrar cómo la herramienta de CI proporciona trazabilidad y diagnóstico preciso del error al equipo de desarrollo.

### Cómo visualizarlo:
1. Hacer clic sobre la ejecución fallida en GitHub Actions.
2. Hacer clic en el trabajo **`Pruebas Automatizadas y Cobertura`**.
3. Desplegar el paso **`Ejecutar pruebas automatizadas con pytest`**.
4. Se observará en texto rojo el desglose del error:
   ```text
   >       assert resultado == 8
   E       assert 2 == 8
   E        +  where 2 = sumar(5, 3)
   test_app.py:16: AssertionError
   ```

### Qué parte de la pantalla capturar:
- La sección del log en GitHub Actions donde se visualiza el fallo específico de la aserción `assert 2 == 8`.

### Leyenda académica para el informe:
> **Figura 7.** Detalle del log de ejecución en GitHub Actions indicando la línea exacta y la aserción de pytest que falló.

---

## Evidencia 8 — Corrección del código y pipeline exitoso

### Propósito
Demostrar el ciclo completo de resolución de incidentes: corrección local, nueva integración y restauración del estado saludable del pipeline.

### Pasos para corregir el código:
1. Abrir `app.py` y restaurar la implementación correcta:
   ```python
   def sumar(a: float | int, b: float | int) -> float | int:
       """Retorna la suma de dos números."""
       return a + b
   ```
2. Guardar y verificar localmente antes de subir:
   ```powershell
   pytest
   ```
   *(Todos los 7 tests pasan).*
3. Subir la corrección:
   ```powershell
   git add app.py
   git commit -m "fix: corregir logica de suma y restaurar salud del pipeline"
   git push origin main
   ```
4. Ir a GitHub → **Actions** y esperar la finalización.

### Qué parte de la pantalla capturar:
- La lista de ejecuciones de GitHub Actions mostrando la secuencia completa:
  1. Ejecución verde inicial.
  2. Ejecución roja con el fallo provocado.
  3. Nueva ejecución verde con la corrección `fix: corregir logica de suma`.

### Leyenda académica para el informe:
> **Figura 8.** Historial de ejecuciones en GitHub Actions evidenciando el ciclo completo de detección, reporte y corrección de un defecto.

---

## Evidencia 9 — Análisis de calidad con SonarQube / SonarCloud

### Propósito
Mostrar el análisis estático de calidad de código, deuda técnica y cumplimiento del Quality Gate.

### Qué métricas capturar del dashboard de SonarCloud / SonarQube:
- **Quality Gate:** Estado `PASSED` (verde).
- **Reliability (Confiabilidad):** 0 Bugs (Rating A).
- **Security (Seguridad):** 0 Vulnerabilities, 0 Security Hotspots (Rating A).
- **Maintainability (Mantenibilidad):** 0 Code Smells, Deuda técnica 0 min (Rating A).
- **Coverage (Cobertura):** Porcentaje reportado (> 80% o 100%).
- **Duplications (Duplicación):** 0.0%.

*(Si ejecutas SonarQube localmente mediante Docker con `docker run -d -p 9000:9000 sonarqube`, capturar la pantalla del dashboard web en `http://localhost:9000`).*

### Leyenda académica para el informe:
> **Figura 9.** Panel de control de SonarQube / SonarCloud exhibiendo la aprobación del Quality Gate y métricas óptimas de mantenibilidad y seguridad.
