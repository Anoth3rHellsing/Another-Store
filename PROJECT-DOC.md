# Another Store — Documentación del Proyecto

## Visión General
Tienda web estática con estética **Frutiger Aero** (2004-2013) inspirada en Windows Vista/7, Wii Menu y diseño glossy. Hosteada en NeoCities. Sin frameworks, sin build tools — HTML/CSS/JS vanilla puro.

**Lema:** "Making internet funny again since 2026"

---

## Estructura de Archivos

```
Another Store/
├── index.html              ← Página principal (Frutiger Aero claro)
├── appstore.html           ← Tienda de apps (estilo Wii azul oscuro)
├── musicstore.html         ← Tienda de música (estilo vinilo/neón púrpura)
├── uikits.html             ← Fun UI Kits (estilo galería de arte clara)
├── DESIGN-SPEC.md          ← Especificación del sistema de diseño Aero Glass
├── QA-CHECKLIST.md         ← Checklist de calidad
├── SKILL.md                ← Skill/instrucciones para Claude Code
├── PROJECT-DOC.md          ← Este archivo
├── AeroGlassResources.xaml ← Recursos XAML del UI Kit Aero Glass (WPF)
├── AeroNight/
│   ├── aeronight.css       ← CSS reutilizable del UI Kit AeroNight (prefijo an-)
│   └── DESIGN-SPEC.md      ← Especificación del UI Kit AeroNight
├── Music/
│   ├── Another Shop Theme.mp3      ← Música del index y uikits
│   └── Another Appstore Theme.mp3  ← Música del appstore y musicstore
├── Ressources/
│   ├── EmiToolkitLogo.png           ← Logo de Emi Toolkit (523KB)
│   └── EmiToolkitScreenshotPreview.png  ← Captura de pantalla de Emi Toolkit (604KB)
└── Store Links/
    ├── Apps.txt            ← Enlaces de descarga de apps (vacío por ahora)
    └── UIKits.txt          ← Enlaces de descarga de UI kits
```

---

## Páginas y sus Identidades Visuales

### 1. `index.html` — Página Principal
- **Estilo:** Frutiger Aero claro
- **Fondo:** Gradiente diagonal azul-verde-blanco (`#EAF6FF → #D0ECFB → #A8DCF4 → #B8E8D0 → #D4F1E8`)
- **Elementos decorativos:** Burbujas flotantes con `radial-gradient`, top-gloss overlay fijo
- **Secciones:**
  - Header: título "Another Store", slogan, buscador funcional, botón de música con visualizador de 5 barras
  - Carrusel: 3 slides auto-rotativos (5s), con dots y flechas prev/next
    - Slide 1: Emi Toolkit con screenshot real como fondo + overlay oscuro gradiente
    - Slide 2: Fun UI Kits (gradiente verde-azul)
    - Slide 3: Music Store (gradiente púrpura)
  - Canales (3 items): App Store, Fun UI Kits, Music Store — cada uno es un `<a>` que redirige
  - Novedades: 4 entradas con badges (Nuevo/Actualización/Próximamente)
- **Música:** `Music/Another Shop Theme.mp3`
- **Colores principales:** `#07405E` (texto), `#1F86C8` (acento azul), `#2C5F7E` (texto secundario)

### 2. `appstore.html` — App Store
- **Estilo:** Wii Menu / Wii Shop Channel (azul oscuro)
- **Fondo:** Gradiente radial elíptico azul profundo (`#1a4a7a → #0a2540 → #051525`)
- **Elementos decorativos:** Ondas SVG animadas (2 capas, direcciones opuestas), 50 estrellas con twinkle
- **Layout:** Dos paneles
  - Izquierdo (45%): App seleccionada con icono grande (160px), nombre, versión, descripción, lista de características, requisitos mínimos, precio, botón descargar. **Scrollable** (`overflow-y: auto`)
  - Derecho (55%): Grid de tiles cuadrados (aspect-ratio 1) con hover scale y glow cyan
- **Apps disponibles (2):**
  - **Emi Toolkit** (verde, usa imagen real `Ressources/EmiToolkitLogo.png`)
  - **Zen Browser** (ámbar, icono SVG)
- **Soporte de hash URL:** `appstore.html#emi` selecciona automáticamente ese canal
- **Música:** `Music/Another Appstore Theme.mp3`
- **Extras:** Reloj en tiempo real (formato 12h AM/PM), overlay de búsqueda con ESC para cerrar, barra inferior con logo
- **Colores:** Glow cyan `#6dd5fa`, texto blanco, glass `rgba(255,255,255,.15)`

### 3. `musicstore.html` — Music Store
- **Estilo:** Reproductor de vinilo / Neon Purple
- **Fondo:** Púrpura neón oscuro (`#2a0a4a → #150525 → #0a0515`) con mesh orbs animados (blur 80px) y grid lines sutiles
- **Layout:** Dos paneles
  - Izquierdo (48%): "Now Playing" con disco de vinilo giratorio (CSS `conic-gradient` + grooves), ecualizador de 12 barras animadas, detalles del track, botones Reproducir/Pausar + Descargar
  - Derecho (52%): Tracklist vertical estilo playlist (no grid) con número, thumbnail, nombre, artista, duración. Track activo muestra mini-ecualizador animado
- **Tracks disponibles (4):**
  - **Sunlight In The Lobby** (ámbar, DEFAULT) → `Music/Sunlight_In_The_Lobby.mp3`
  - **Morning In The Lobby** (cyan) → `Music/Morning_in_the_Lobby.mp3`
  - **Shop Theme** (púrpura) → `Music/Another Shop Theme.mp3`
  - **Appstore Theme** (rosa) → `Music/Another Appstore Theme.mp3`
- **Audio individual por track:** Cada canción tiene su propio elemento `<audio>` independiente. Al cambiar de track se detiene el anterior y se carga el nuevo.
- **Vinilo:** Gira solo cuando la música está sonando (`animation-play-state: paused/running`)
- **Música de fondo:** Usa los mismos archivos que los tracks (el track seleccionado es el que suena)
- **Colores:** Púrpura `#7b4cd9`, rosa `#d94c8b`, cyan glow `#c79cff`

### 4. `uikits.html` — Fun UI Kits
- **Estilo:** Galería de arte / Moodboard (fondo claro)
- **Fondo:** Blanco-gris claro (`#f8fafc → #e8f0f8 → #f0f8f4 → #faf8f0`) con formas orgánicas flotantes (blobs con `border-radius` asimétrico animados)
- **Layout:** Dos paneles
  - Izquierdo (50%): Preview en vivo del kit seleccionado dentro de una card con barra de colores arriba. Cada kit tiene una mini-preview visual real:
    - Aero Glass: botón glossy + card con backdrop blur sobre fondo SkyBrush
    - AeroNight: tiles oscuros con glow cyan sobre fondo radial azul
    - Neon Pulse: botón neón rosa sobre fondo negro
    - Retro Wave: texto monospace amarillo sobre gradiente synthwave
  - Derecho (50%): Galería de cards con preview visual arriba (100px) + info abajo. Badge "soon" para kits en desarrollo
- **Kits disponibles (4):**
  - **Aero Glass** (azul) — disponible
  - **AeroNight** (púrpura) — disponible
  - **Neon Pulse** (rojo/neón) — próximamente
  - **Retro Wave** (ámbar) — próximamente
- **Música:** `Music/Morning_in_the_Lobby.mp3`
- **Colores:** `#1a2a3a` (texto), `#39A5DC` (acento), `#5a7a9a` (secundario)

---

## Sistema de Autoplay de Audio (5 Estrategias)

Todas las páginas usan el mismo sistema agresivo de autoplay:

1. **Intento inmediato** al ejecutar el script
2. **DOMContentLoaded** event
3. **window.load** event
4. **Primera interacción** (7 eventos: click, mousedown, touchstart, keydown, mousemove, scroll, pointerdown) con Web Audio API unlock (crea AudioContext, buffer silencioso, resume)
5. **Retry cada 2s** durante 30s (15 intentos max)

- Volumen por defecto: `0.4`
- Estado tracked con variable `unlocked` para evitar múltiples intentos
- Visualizador de barras se sincroniza con estado playing/paused

---

## Paleta de Colores Global

### Frutiger Aero (index, uikits)
| Token | Hex | Uso |
|-------|-----|-----|
| Texto principal | `#07405E` | Títulos, texto body |
| Texto secundario | `#2C5F7E` | Descripciones, hints |
| Acento azul | `#1F86C8` | Bordes, badges, links |
| Azul claro | `#39A5DC` | Gradientes, iconos |
| Azul cielo | `#8FD9F7` | Gradientes glossy |
| Verde | `#74C23C` | Iconos green, badges "nuevo" |
| Ámbar | `#F0A93A` | Iconos amber, badges "soon" |
| Rojo | `#DD5C3E` | Iconos red |
| Púrpura | `#8B5CF6` | Iconos purple |
| Fondo base | `#EAF6FF → #D4F1E8` | Gradiente diagonal |

### AeroNight / Wii (appstore)
| Token | Hex | Uso |
|-------|-----|-----|
| Fondo profundo | `#051525` | Esquinas |
| Fondo medio | `#0a2540` | Medio |
| Fondo claro | `#1a4a7a` | Centro gradiente |
| Glow cyan | `#6dd5fa` | Bordes activos, glow |
| Texto | `#ffffff` | Todo el texto |
| Glass | `rgba(255,255,255,.15)` | Tiles, paneles |

### Neon Purple (musicstore)
| Token | Hex | Uso |
|-------|-----|-----|
| Fondo profundo | `#0a0515` | Base |
| Púrpura | `#7b4cd9` | Acento principal |
| Rosa | `#d94c8b` | Acento secundario |
| Cyan glow | `#c79cff` | Ecualizador, highlights |
| Mesh orb azul | `#4c7bd9` | Fondo animado |

---

## Gradientes de Iconos (Glossy)

Todos los iconos llevan un overlay `::after` con brillo superior:
```css
background: linear-gradient(to bottom, rgba(255,255,255,.4) 0%, rgba(255,255,255,.05) 100%);
```

| Clase | Gradiente |
|-------|-----------|
| `.icon-green` / `.channel-icon.green` | `#8fd95f → #4ca22b` (o 4-stop glossy) |
| `.icon-blue` / `.channel-icon.blue` | `#6fc7f0 → #1f86c8` (o 4-stop glossy) |
| `.icon-amber` / `.channel-icon.amber` | `#ffd97a → #e08c1e` (o 4-stop glossy) |
| `.icon-red` / `.channel-icon.red` | `#ffa694 → #c63c22` (o 4-stop glossy) |
| `.icon-purple` / `.channel-icon.purple` | `#c79cff → #7b4cd9` (o 4-stop glossy) |
| `.icon-cyan` | `#7fffff → #00b8b8` |
| `.icon-pink` | `#ff9ecd → #d94c8b` |

Los iconos en `index.html` usan gradientes de 4 stops con línea dura al 49-51% para efecto glossy más pronunciado.

---

## Navegación entre Páginas

```
index.html
  ├── Carrusel slide 1 → appstore.html#emi
  ├── Carrusel slide 2 → uikits.html#aero
  ├── Carrusel slide 3 → musicstore.html
  ├── Canal "App Store" → appstore.html
  ├── Canal "Fun UI Kits" → uikits.html
  └── Canal "Music Store" → musicstore.html

appstore.html → index.html (botón "Volver")
musicstore.html → index.html (botón "Volver")
uikits.html → index.html (botón "Volver")
```

---

## Productos / Contenido

### Emi Toolkit
- **Tipo:** Aplicación de mantenimiento para Windows 11
- **Formato:** Portable (carpeta, sin instalación)
- **Tecnología:** WPF con transparencia acrylic nativa
- **Features:** Limpieza de disco, 19 optimizaciones Win11, 17 ajustes privacidad, gestión arranque/procesos/RAM, firewall ESET KB332, Zen Browser predeterminado, deshacer todo
- **Requisitos:** Windows 11 (build 26200+) o Win 10 1809+, PowerShell 5.1, .NET 4.8
- **Descarga:** Google Drive (enlace placeholder `1YOUR_FOLDER_ID`)
- **Logo:** `Ressources/EmiToolkitLogo.png`
- **Screenshot:** `Ressources/EmiToolkitScreenshotPreview.png`

### Zen Browser
- **Tipo:** Navegador web open-source basado en Firefox
- **Features:** Privacidad, minimalismo, sin rastreo, compatible con extensiones Firefox
- **Requisitos:** Win 10+, macOS 10.15+, Linux
- **Descarga:** https://zen-browser.app/

### Aero Glass UI Kit
- **Tipo:** Sistema de diseño Frutiger Aero para WPF
- **Formato:** XAML resources + especificación
- **Archivo:** `AeroGlassResources.xaml` (25KB)
- **Spec:** `DESIGN-SPEC.md`
- **Features:** 12 tokens de color, gradientes GlossBlue/Green/Amber/Red, SkyBrush, TopGloss, SoftShadow, componentes (Button, Ghost, Nav, Switch, Card, ProgressBar)
- **Requisitos:** Visual Studio 2019+, WPF .NET Framework 4.8+

### AeroNight UI Kit
- **Tipo:** Sistema de diseño oscuro estilo Wii Menu
- **Formato:** CSS puro reutilizable
- **Archivo:** `AeroNight/aeronight.css` (10KB, prefijo `an-`)
- **Spec:** `AeroNight/DESIGN-SPEC.md`
- **Features:** Paleta oscura con glow cyan, ondas SVG, tiles, layout dos paneles, responsive
- **Requisitos:** Cualquier navegador moderno

### Música
- **Another Shop Theme.mp3** (1.5MB) — Tema principal, usado en index y uikits
- **Another Appstore Theme.mp3** (2.1MB) — Tema appstore, usado en appstore y musicstore

---

## Pendientes / TODO

1. **Reemplazar enlaces placeholder:** Buscar `1YOUR_FOLDER_ID` en `appstore.html` y `uikits.html` y sustituir por enlaces reales de Google Drive
2. **Store Links/Apps.txt:** Está vacío — agregar enlaces de descarga reales
3. **Neon Pulse y Retro Wave UI Kits:** Marcados como "próximamente" — crear cuando estén listos
4. **Chill Vibes y Retro Beats (música):** Eliminados de musicstore para evitar problemas en preview — agregar cuando existan los archivos MP3
5. **NeoCities deploy:** Subir toda la carpeta como sitio estático

---

## Decisiones de Diseño Tomadas

1. **Sin morado/violeta en el index:** El usuario pidió explícitamente no usar púrpura como default en la página principal. El púrpura solo aparece en la Music Store y en iconos específicos.
2. **ESET Firewall no es app independiente:** Se eliminó como canal/app separada. Solo se menciona dentro de las features de Emi Toolkit.
3. **Emi Toolkit y Zen Browser no están en los canales del index:** Están en el carrusel (destacados) y en el App Store, pero no como canales directos en la página principal.
4. **Cada tienda tiene identidad visual única:** No son variaciones del mismo template. App Store = Wii azul, Music Store = vinilo neón púrpura, UI Kits = galería de arte clara.
5. **Audio individual por track en Music Store:** Cada canción tiene su propio `<audio>` element para que se reproduzca la correcta al seleccionar.
6. **Solo 2 tracks en Music Store:** Para evitar problemas en preview con archivos que no existen aún.
7. **Screenshot real en carrusel:** El slide de Emi Toolkit usa la captura real con overlay oscuro gradiente para legibilidad.

---

## Responsive

- **Index:** Breakpoint 700px — carrusel 16:9, canales 1 columna, burbujas ocultas
- **App Store / Music Store / UI Kits:** Breakpoint 900px — layout vertical, iconos más pequeños, grids adaptativos

---

## Notas Técnicas

- Todo es HTML/CSS/JS vanilla inline (sin archivos externos excepto CSS de AeroNight y recursos)
- Sin dependencias npm, sin build step
- Las animaciones usan CSS `@keyframes` puras
- El carrusel usa `transform: translateX()` con transición cubic-bezier
- Los iconos son SVG inline (no dependencias de librerías de iconos)
- `backdrop-filter: blur()` usado extensivamente para efecto glass
- Scrollbars personalizados con `::-webkit-scrollbar`
- `font-variant-numeric: tabular-nums` para el reloj