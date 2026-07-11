# Cómo automatizamos la creación de publicaciones para un e-commerce utilizando Inteligencia Artificial

## Contexto

Durante el desarrollo de un pequeño proyecto de automatización para un e-commerce detectamos que una de las tareas que más tiempo consumía era crear las publicaciones de los productos. Cada artículo requería redactar un título atractivo, una descripción comercial, una lista de características y, en algunos casos, contenido para redes sociales.

El objetivo fue reducir el trabajo manual mediante un flujo automatizado que utilizara Inteligencia Artificial para generar ese contenido de forma consistente.

## Problema

El principal desafío era que la información provenía de distintas fuentes y con formatos diferentes. Algunos productos tenían descripciones muy completas mientras que otros solo incluían especificaciones técnicas.

En las primeras pruebas, la IA generaba respuestas demasiado largas, repetía información y utilizaba un tono poco adecuado para una tienda online. Además, era necesario integrar el proceso con herramientas de automatización para evitar tareas manuales.

## Acciones

Se diseñó un flujo utilizando Google Forms para ingresar los datos del producto, Google Sheets como almacenamiento y Make como herramienta de automatización.

Cada nuevo registro era enviado automáticamente a OpenAI mediante un prompt especialmente diseñado para generar:

- Un título optimizado.
- Una descripción comercial.
- Cinco características principales.
- Un texto corto para redes sociales.

Durante el desarrollo se realizó un post-mortem para analizar los primeros resultados. Se detectó que el problema principal no estaba en el modelo de IA sino en la calidad del prompt utilizado.

A partir de esa conclusión se realizaron varias mejoras:

- Se limitaron las longitudes máximas de las respuestas.
- Se solicitó un tono comercial en lugar de técnico.
- Se evitaron repeticiones.
- Se agregó una estructura fija para todas las publicaciones.

Estas modificaciones mejoraron considerablemente la calidad del contenido generado.

## Aprendizajes

Este proyecto permitió comprobar que la Inteligencia Artificial ofrece mejores resultados cuando recibe instrucciones claras y específicas.

También se aprendió que automatizar procesos no consiste únicamente en conectar herramientas, sino en diseñar correctamente el flujo completo de información.

Finalmente, se comprobó la importancia de realizar pruebas continuas y ajustar el sistema en función de los resultados obtenidos.

## Control de versiones

Durante el desarrollo se utilizó Git para registrar los avances del proyecto.

Entre los cambios realizados se incluyeron:

- Creación inicial de la estructura del proyecto.
- Incorporación del workflow de automatización.
- Mejora del prompt utilizado por la IA.
- Corrección de errores detectados durante las pruebas.
- Actualización de la documentación.

El uso de commits permitió mantener un historial claro de la evolución del proyecto y facilitar posibles modificaciones futuras.

## Reflexión sobre el feedback radicalmente sincero

Durante el desarrollo se aplicó una metodología basada en recibir y ofrecer comentarios honestos sobre el funcionamiento del sistema. En lugar de justificar los errores iniciales, se analizaron objetivamente los resultados y se identificaron oportunidades de mejora.

Este enfoque permitió modificar el prompt, optimizar el flujo de trabajo y obtener un producto final de mayor calidad. La experiencia demostró que aceptar críticas constructivas desde etapas tempranas acelera el aprendizaje y mejora el resultado final.