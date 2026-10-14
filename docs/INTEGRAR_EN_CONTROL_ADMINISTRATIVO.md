# Código de Caché Interiores para Control Administrativo

Este ZIP contiene la interfaz HTML/CSS/JavaScript, el servidor Worker, los lectores de PDF y Excel, los recursos gráficos utilizados, los archivos originales importados, las semillas iniciales y el esquema/migraciones D1. No contiene contraseñas ni credenciales de publicación.

## Instrucción para pegar en la otra conversación

> Integra este proyecto Caché Interiores en mi página de Control Administrativo. Conserva el diseño de Caché, los módulos CxC, Urgencias, Incidencias, OKR y Seguimiento de obra, la selección y los cálculos de la proyección, las fichas de clientes, y los permisos del servidor. Inspecciona el proyecto de destino antes de editarlo. Usa el identificador de hosting del destino; no sobrescribas el sitio original. Mantén la autenticación y los datos financieros privados. Los datos iniciales del ZIP no son un respaldo de los registros nuevos del sitio en producción. Define cómo conectar o migrar esos registros antes de activar el destino. No uses directamente como nuevos los números de las migraciones: compara el esquema y genera migraciones propias para el destino.

## Archivos

- `web/index.html`: toda la interfaz, estilos y comportamiento del navegador.
- `worker/api.js`: OKR, identidad, roles y bitácora.
- `worker/cxc-api.js`: cuentas por cobrar, PDF y actualizaciones.
- `worker/projection-api.js`: ventas y proyecciones mensuales.
- `worker/clients-api.js`: fichas y requisitos de clientes.
- `worker/xlsx-reader.mjs`, `worker/pdfjs/`: lectores de Excel y PDF.
- `worker/*-seed.json`, `worker/seed.json`: datos de la importación inicial.
- `worker/*-source.xlsx`, `worker/cxc-source.pdf`, `worker/cxc-comments.xlsx`: archivos originales.
- `db/schema.ts`, `drizzle/`: esquema y migraciones del sitio original.
- `scripts/build-worker.py`: genera el servidor de distribución; ejecutar desde el proyecto con Python 3.
- `.openai/hosting.json`: declara los bindings `DB` (D1) y `BUCKET` (R2). Se omitió el identificador del sitio para evitar publicar sobre el original.
- `ORIGEN.json`: identifica la procedencia del paquete; no es configuración para publicar.

## Integración

Si solo se muestra la página existente dentro de Control Administrativo, basta un iframe con la URL de ORIGEN.json. Eso mantiene la misma base de datos y permisos. Debe comprobarse en el sitio de destino que la plataforma y el inicio de sesión permitan la incrustación.

Si se copia todo el código al destino, debe conservarse el backend: el HTML por sí solo llama `/api/okr` y `/api/cxc` y no implementa las operaciones compartidas. En el destino, adapta estos prefijos si hay otras APIs con esos nombres, y adapta las rutas de assets. No cambies los endpoints del HTML sin actualizar también el servidor.

La identidad se recibe por cabeceras verificadas por ChatGPT Sites. En otra plataforma hay que reemplazar ese proveedor por su autenticación real; nunca confiar en un correo enviado por el navegador ni en cabeceras públicas que un visitante pueda falsificar. Conserva las comprobaciones de rol en el servidor.

Administradores iniciales: `gescobedo@cacheinteriores.com` y `rdominguez@cacheinteriores.com`.
Captura CxC: `cuentasporcobrar1@cacheinteriores.com`, `cuentasporcobrar2@cacheinteriores.com`.
Captura Estimaciones: `estimaciones@cacheinteriores.com`.
El acceso al sitio y el rol de captura son controles distintos. Publicar en un proyecto diferente no traslada automáticamente invitaciones ni sesiones.

## Datos y respaldos

OKR, CxC, notas, clientes, ventas y proyecciones se guardan en D1. PDF y Excel importados se guardan en R2. Urgencias, Incidencias y Seguimiento de obra usan el almacenamiento local del navegador, con datos iniciales en el HTML. El ZIP no incluye las modificaciones privadas guardadas en esos almacenamientos ni todos los archivos nuevos subidos después de la importación inicial. Usar un iframe conserva el origen y evita duplicar esos datos. Copiar el código requiere migrar/conectar esos datos de forma explícita; no volver a sembrar los datos iniciales sobre información vigente.

## Preparar el proyecto de destino

1. Inspeccionar su manifiesto y su esquema. Conservar el ID del destino.
2. Integrar interfaz/API, adaptar rutas y reutilizar o crear bindings compatibles.
3. Crear migraciones nuevas para el destino, sin modificar migraciones ya aplicadas.
4. Ejecutar `python scripts/build-worker.py` después de configurar el manifiesto del destino.
5. Verificar login, lectura, captura por departamento, administradores, comentarios, importaciones, monedas separadas, pagos parciales y conflictos de versión antes de publicar.

Fecha del paquete: 13 de octubre de 2026 (America/Mexico_City).
