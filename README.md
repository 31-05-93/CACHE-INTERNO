# Caché Interiores · Gestión interna

El módulo OKR usa almacenamiento compartido Cloudflare D1 y la identidad de ChatGPT validada en el servidor. Los demás módulos mantienen su almacenamiento local previo y la misma clave de localStorage.

## OKR
- Estimaciones y CxC: 41 resultados clave, 18 registros mensuales de enero a septiembre de 2026. Totales verificados contra las fórmulas de los archivos.
- Los meses importados están cerrados; un administrador puede reabrirlos. La fuente y los valores originales se conservan por periodo.
- Progreso = realizado/meta; resultado ponderado = progreso*ponderación; resultado mensual = suma de ponderados. No se normalizan pesos ni se limita artificialmente el progreso de mediciones por cantidad.
- Solo administradores pueden definir objetivos, metas, ponderaciones, departamentos, meses y roles. Cada usuario asignado captura únicamente el avance y comentarios de su departamento en meses abiertos. Los administradores también pueden corregir avances de meses cerrados, con bitácora.
- Administrador inicial: gescobedo@cacheinteriores.com. Captura Estimaciones: estimaciones@cacheinteriores.com. CxC: cuentasporcobrar1@cacheinteriores.com y cuentasporcobrar2@cacheinteriores.com. Segundo administrador: rdominguez@cacheinteriores.com.
- El servidor impide cambios entre departamentos, cambios de objetivos desde solicitudes de avance y escritura sin identidad. Guarda bitácora y controla conflictos de versión.
- Crear un mes copiando otro conserva los objetivos y reinicia los avances, sin reemplazar el historial.

## Desarrollo
Editar web/index.html y worker/api.js. `npm run db:generate` crea nuevas migraciones ante cambios al esquema; nunca editar migraciones aplicadas. `python scripts/build-worker.py` prepara dist/server/index.js y las migraciones. La importación inicial se ejecuta idempotentemente al acceder a la API por primera vez; las migraciones solo definen esquema.

Los porcentajes realizados se editan en la tabla con Guardar por fila. La última columna muestra el resultado global mensual. Las vistas previas se identifican como sin guardar. Ver detalle abre una consulta real; el historial del navegador conserva sección, departamento y mes para Atrás/Adelante.

Resultado anual por departamento: promedio aritmético de los resultados mensuales guardados del año seleccionado, con al menos un KR y pesos que sumen 100%, hasta el mes actual. No cuenta meses vacíos, futuros ni incompletos. Incluye meses abiertos como provisionales, informa cobertura y ofrece gráfica mensual consultable. El promedio no incluye borradores sin guardar.

Pantalla de entrada: vista general con cuatro accesos principales, CxC, Urgencias, Incidencias y OKR. CxC tiene una sección inicial pendiente de definición funcional. El panorama operativo anterior se conserva como herramienta secundaria.

Actividad de usuarios: historial OKR separado de las pantallas de los departamentos y exclusivo de administradores, con filtros por usuario y departamento. El endpoint de auditoría rechaza usuarios de departamento y visitantes. El endpoint general de OKR no entrega bitácora ni autor de modificaciones.

Diseño Caché Studio: tonos marfil y azul profundo, detalles dorados, composiciones abstractas inspiradas en arquitectura y materiales, tipografía editorial y formularios de alto contraste. Adaptación móvil y reducción de movimiento según preferencias del navegador.

Navegación: barra lateral azul retirada. Cabecera clara con marca Caché Interiores, botón Menú desplegable, cierre al elegir un módulo, clic externo y tecla Escape. Pantalla completa para el contenido en escritorio y móvil.

Inicio con cinco módulos compactos: CxC, Urgencias, Incidencias, OKR y Seguimiento de obra. Cinco columnas en escritorio amplio, tres en tamaño intermedio, dos en móvil y una en pantallas estrechas.

Departamentos: solo administradores pueden editar nombres o eliminar desde las tarjetas. Eliminar retira el departamento del selector y bloquea nuevas capturas, preservando los objetivos, meses y bitácora en el servidor. La eliminación requiere confirmación en la interfaz.

Portada: imagen generada de inspiración de acabados (madera, travertino y paneles con textiles), incorporada al Worker y servida con caché. No se presenta como un proyecto realizado por Caché.

Departamentos compactos con imágenes generadas alusivas a cada área e iconos accesibles de edición/eliminación. Análisis de empresa con filtros de año, mes y periodos cerrados o en curso, comparación entre departamentos, cobertura, evolución mensual y CSV. Cada mes promedia por igual los departamentos activos con datos y pesos completos; el resultado anual promedia los meses disponibles. No convierte datos ausentes en cero ni incluye futuros.

CxC se organiza en cuatro reportes: Reporte CxC, Relación clientes, Proyección de presupuesto y PDT. Cada acceso tiene su vista y navegación. Los campos y cálculos están pendientes de definición con los formatos del usuario; no se incorporan registros financieros ficticios.

## Reporte CxC y actualizaciones
Importación inicial de 295 cuentas del PDF del 13/10/2026 y 121 comentarios del Excel. Se conservan 56 cuentas comentadas fuera del corte actual. Los saldos se separan por moneda, manteniendo centavos enteros. Los comentarios del Excel conservan hoja y fila sin inventar fecha histórica ni autor personal. Los usuarios de CxC y administradores publican actualizaciones con identidad y fecha del servidor; las notas son independientes e inmutables. Historial paginado, corte seleccionable, PDF/Excel originales, filtros y CSV. PDF.js importa futuros PDF del mismo formato (hasta 3 MB y 100 páginas), valida subtotales y guarda nuevos cortes sin reemplazar datos anteriores. Archivos en R2 y cuentas/cortes/comentarios en D1. Vinculación estable por pedido, tipo y moneda; envío idempotente de notas y detección de PDF ya importado.
