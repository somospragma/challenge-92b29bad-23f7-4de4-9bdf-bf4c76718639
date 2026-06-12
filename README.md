# Automatización de Pruebas en Aplicación Móvil de Finanzas Personales

Una aplicación de finanzas personales para dispositivos móviles requiere una suite de pruebas automatizadas para asegurar la calidad y funcionalidad en diferentes dispositivos y versiones de sistema operativo. El objetivo es integrar un servicio de granja de dispositivos para ejecutar estas pruebas y obtener resultados confiables.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Automatizacion de pruebas moviles |
| **Nivel** | advanced-l2 |
| **Tipo** | practical |
| **Tiempo estimado** | 4-6 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Configuración del Entorno de Pruebas

**Objetivo:** Definir y configurar el entorno necesario para ejecutar pruebas automatizadas en dispositivos móviles.

**Tiempo estimado:** 1 hora

**Instrucciones:**

- Identificar los dispositivos y versiones de sistema operativo a cubrir.
- Seleccionar un servicio de granja de dispositivos que permita ejecutar pruebas en múltiples configuraciones.
- Configurar las credenciales y accesos necesarios para utilizar el servicio seleccionado.

**Entregable:** Documento con la configuración y selección del servicio de granja de dispositivos.

<details>
<summary>Pistas de conocimiento</summary>

- Considera la diversidad de dispositivos y versiones de sistema operativo en el mercado.
- Evalúa la cobertura y costo de diferentes servicios de granja de dispositivos.

</details>

### Fase 2: Desarrollo de Pruebas Automatizadas

**Objetivo:** Crear un conjunto de pruebas automatizadas que cubran funcionalidades críticas de la aplicación.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Identificar las funcionalidades críticas de la aplicación que deben ser probadas.
- Desarrollar pruebas automatizadas para estas funcionalidades utilizando un framework de pruebas compatible con el servicio de granja de dispositivos.
- Asegurar que las pruebas incluyen casos de éxito y de error.

**Entregable:** Conjunto de pruebas automatizadas con casos de éxito y de error.

<details>
<summary>Pistas de conocimiento</summary>

- Prioriza las funcionalidades que tienen mayor impacto en la experiencia del usuario.
- Considera la mantenibilidad y escalabilidad de las pruebas desarrolladas.

</details>

### Fase 3: Ejecución y Análisis de Resultados

**Objetivo:** Ejecutar las pruebas automatizadas en la granja de dispositivos y analizar los resultados obtenidos.

**Tiempo estimado:** 1 hora

**Instrucciones:**

- Ejecutar las pruebas automatizadas en la granja de dispositivos seleccionada.
- Analizar los resultados de las pruebas, identificando fallos y áreas de mejora.
- Documentar los hallazgos y proponer acciones correctivas.

**Entregable:** Informe de resultados de las pruebas con hallazgos y acciones correctivas propuestas.

<details>
<summary>Pistas de conocimiento</summary>

- Prioriza la revisión de los fallos más críticos para la aplicación.
- Considera la posibilidad de automatizar la generación de informes de resultados.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es un servicio de granja de dispositivos y por qué es útil para la automatización de pruebas móviles?
- **paraQueSirve**: ¿Para qué sirve desarrollar pruebas automatizadas en una aplicación móvil?
- **comoSeUsa**: ¿Cómo se usa un framework de pruebas para crear pruebas automatizadas en dispositivos móviles?
- **erroresComunes**: ¿Qué errores comunes se pueden encontrar al ejecutar pruebas automatizadas en diferentes dispositivos y versiones de sistema operativo?
- **queDecisionesImplica**: ¿Qué decisiones implica la selección de un servicio de granja de dispositivos para la automatización de pruebas?

## Criterios de Evaluacion

- Configuración del entorno de pruebas con selección de servicio de granja de dispositivos.
- Desarrollo de pruebas automatizadas con casos de éxito y de error.
- Ejecución de pruebas en la granja de dispositivos y análisis de resultados.
- Documentación de hallazgos y propuestas de acciones correctivas.

---

*Reto generado automaticamente por Challenge Generator - Pragma*
