# Plan: Corregir findings de verificación — Another Store

## Contexto

La verificación runtime de `anotherstore.neocities.org` identificó tres áreas de mejora. Este plan aborda cada una con cambios concretos en los archivos locales del proyecto.

---

## Finding 1: Reloj duplicado sin timezone

**Problema:** La función `updateClock()` está copiada verbatim en `appstore.html` (L275), `uikits.html` (L286) y `musicstore.html` (L346). No hay manejo de timezone y cualquier cambio requiere editar 3 archivos.

**Fix:** Extraer a un script compartido `js/clock.js` y referenciarlo desde las 3 páginas.

### Pasos
1. Crear `js/clock.js` con la función `updateClock()` y el `setInterval(updateClock, 1000)`.
2. En `appstore.html`: eliminar el bloque inline de `updateClock` (L275-276) y agregar `<script src="js/clock.js"></script>` antes del cierre de `</body>`.
3. Repetir paso 2 en `uikits.html` (eliminar L286-287) y `musicstore.html` (eliminar L346-347).
4. Verificar que el elemento `<span id="clock">` sigue presente en cada HTML (no se mueve, solo el JS).

**Archivos afectados:**
- `js/clock.js` (nuevo)
- `appstore.html` (~L275)
- `uikits.html` (~L286)
- `musicstore.html` (~L346)

---

## Finding 2: Descarga MP3 usa ruta local relativa vs Google Drive

**Problema:** Los botones de descarga individual en `musicstore.html` apuntan a rutas relativas (`Music/Sunlight_In_The_Lobby.mp3`) mientras que el botón "Drive (todas)" apunta a Google Drive. Si los MP3 se mueven o Neocities tiene límites de ancho de banda, los enlaces locales se rompen.

**Fix:** ✅ DECIDIDO — Redirigir todos los botones de descarga individual al folder compartido de Google Drive (consistente con App Store y UI Kits), manteniendo la ruta local en `<audio>` para reproducción in-page.

### Pasos
1. En `musicstore.html`, localizar el array `tracks` (~L218-240).
2. Para cada track, cambiar `downloadUrl` de la ruta local relativa al folder de Drive: `https://drive.google.com/drive/folders/1ugiv_jZ-w7x6GJ0EJalAc_nQMbgrMBnz?usp=sharing`.
3. Mantener las rutas locales en los elementos `<audio>` (L154-157) para que la reproducción in-page siga funcionando sin depender de Drive.
4. Actualizar el texto del botón de descarga de "Descargar" a "Descargar (Drive)" para clarificar el destino.

**Archivos afectados:**
- `musicstore.html` (~L218-240, ~L302)

---

## Finding 3: Entradas "Próximamente" son clickeables pero sin feedback claro

**Problema:** "Another Suite" y "Studio Textil Pro" en `appstore.html` tienen `downloadUrl:'#'` y `badge:'soon'`. Al hacer clic muestran el panel de detalle pero ocultan el botón de descarga. No hay indicador visual claro de que están en desarrollo.

**Fix:** Agregar estado visual diferenciado para items con `badge:'soon'` — opacidad reducida en el tile + mensaje explícito en el panel de detalle.

### Pasos
1. En `appstore.html`, en la función de renderizado de tiles del sidebar (~L248-256), agregar clase CSS condicional: si `app.badge === 'soon'`, añadir clase `app-soon` al div del tile.
2. Agregar regla CSS `.app-soon { opacity: 0.6; cursor: default; }` en el bloque `<style>`.
3. En la función `selectChannel()` (~L258-273), cuando `app.badge === 'soon'`, mostrar mensaje adicional en el panel de detalle: "🚧 Esta aplicación está en desarrollo. Vuelve pronto para novedades." debajo del precio.

**Archivos afectados:**
- `appstore.html` (~L248-273, bloque `<style>`)

---

## Verificación post-fix

1. Abrir cada página en el navegador integrado y confirmar:
   - El reloj se actualiza correctamente en las 3 páginas.
   - Los botones de descarga en Music Store llevan a Google Drive.
   - Los items "Próximamente" en App Store tienen opacidad reducida y mensaje de "en desarrollo".
2. Confirmar que la reproducción de audio in-page en Music Store sigue funcionando (usa `<audio>` con ruta local, independiente del botón de descarga).
3. Verificar que no hay errores en consola del navegador tras los cambios.