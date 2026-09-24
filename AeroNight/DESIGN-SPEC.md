# AeroNight — UI Kit Specification

Sistema de diseño oscuro inspirado en el menú de la Wii / Wii Shop Channel.
Fondo azul profundo con ondas animadas, tiles glossy y glow cyan.

---

## Paleta de colores

| Token | Hex | Uso |
|-------|-----|-----|
| `--bg-deep` | `#051525` | Fondo más oscuro (esquinas) |
| `--bg-mid` | `#0a2540` | Fondo medio |
| `--bg-light` | `#1a4a7a` | Centro del gradiente radial |
| `--glow-cyan` | `#6dd5fa` | Glow activo, bordes seleccionados |
| `--glow-blue` | `rgba(100,180,255,.3)` | Glow ambiental |
| `--text-primary` | `#ffffff` | Texto principal |
| `--text-secondary` | `rgba(255,255,255,.8)` | Descripciones |
| `--text-muted` | `rgba(255,255,255,.5)` | Hints, placeholders |
| `--glass-light` | `rgba(255,255,255,.15)` | Tiles, paneles |
| `--glass-border` | `rgba(255,255,255,.1)` | Bordes sutiles |
| `--glass-hover` | `rgba(255,255,255,.2)` | Hover states |

## Gradientes de iconos

| Clase | Gradiente |
|-------|-----------|
| `.icon-green` | `#8fd95f → #4ca22b` |
| `.icon-blue` | `#6fc7f0 → #1f86c8` |
| `.icon-amber` | `#ffd97a → #e08c1e` |
| `.icon-red` | `#ffa694 → #c63c22` |
| `.icon-purple` | `#c79cff → #7b4cd9` |
| `.icon-cyan` | `#7fffff → #00b8b8` |

Todos los iconos llevan un overlay `::after` con brillo superior:
```css
background: linear-gradient(to bottom, rgba(255,255,255,.4) 0%, rgba(255,255,255,.05) 100%);
```

## Fondo

Gradiente radial elíptico centrado abajo:
```css
background: radial-gradient(ellipse at 50% 120%, #1a4a7a 0%, #0a2540 40%, #051525 100%);
```

### Ondas SVG animadas

Dos capas de ondas en la parte inferior, moviéndose en direcciones opuestas:
- **Onda 1:** `animation: waveMove 12s linear infinite` — opacidad 0.15
- **Onda 2:** `animation: waveMove 18s linear infinite reverse` — opacidad 0.10

```css
@keyframes waveMove {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
```

### Estrellas / partículas

50 puntos generados aleatoriamente con `twinkle`:
```css
@keyframes twinkle {
  0%, 100% { opacity: .2; }
  50% { opacity: .8; }
}
```

## Layout

Pantalla completa dividida en dos paneles:

| Panel | Ancho | Contenido |
|-------|-------|-----------|
| Izquierdo | 45% | Canal seleccionado (icono grande, título, descripción, botón descarga) |
| Derecho | 55% | Grid de canales (tiles cuadrados) |

### Barra inferior (60px)

- Logo en itálica blanca con glow azul
- Reloj en tiempo real (formato 12h AM/PM)
- Botones circulares (búsqueda, correo)

## Componentes

### Channel Tile (cuadradito del grid)

```
aspect-ratio: 1
border-radius: 16px
background: linear-gradient(to bottom, rgba(255,255,255,.15), rgba(255,255,255,.05))
border: 2px solid rgba(255,255,255,.1)
box-shadow: 0 4px 16px rgba(0,0,0,.3)
```

**Hover:** `scale(1.08)`, borde más brillante, glow azul
**Activo:** borde `#6dd5fa`, glow intenso `0 0 30px rgba(100,180,255,.5)`

Icono interno: 64×64px, `border-radius: 14px`, con overlay de brillo.
Nombre: 12px, blanco, centrado debajo del icono.

### Selected Channel (panel izquierdo)

Icono: 180×180px, `border-radius: 24px`, borde 3px blanco semitransparente.
Glow: `0 0 60px rgba(100,180,255,.3)`.
Título: 28px, bold, blanco, `text-shadow: 0 2px 8px rgba(0,0,0,.5)`.
Descripción: 14px, `rgba(255,255,255,.8)`, max-width 320px.

### Botón de descarga

```
border-radius: 30px
background: linear-gradient(to bottom, #6dd5fa, #2980b9)
border: 2px solid rgba(255,255,255,.3)
box-shadow: 0 4px 20px rgba(0,100,200,.4), inset 0 1px 0 rgba(255,255,255,.4)
```

**Hover:** `scale(1.05)`, glow más intenso.

### Audio Control

Pill con barras animadas + icono de nota musical.
Barras: 3px ancho, gradiente `#6dd5fa`, animación `bar .8s ease-in-out infinite alternate`.
Estado pausado: barras estáticas a 3px.

### Search Overlay

Fondo `rgba(0,10,20,.8)` con `backdrop-filter: blur(8px)`.
Caja: `border-radius: 20px`, gradiente azul oscuro, borde blanco semitransparente.
Input: fondo `rgba(0,0,0,.3)`, foco con borde `#6dd5fa`.

## Animaciones

| Nombre | Duración | Uso |
|--------|----------|-----|
| `channelPop` | 0.4s | Entrada del canal seleccionado (scale .8→1 + fade) |
| `waveMove` | 12-18s | Ondas de fondo |
| `twinkle` | 3s | Estrellas |
| `bar` | 0.8s | Barras del visualizador de audio |

## Responsive

En pantallas < 900px:
- Layout vertical (panel izquierdo arriba, grid abajo)
- Icono seleccionado: 120×120px
- Tiles: min 100px
- Iconos de tile: 48×48px

## Autoplay de audio (5 estrategias)

1. Intento inmediato al ejecutar script
2. `DOMContentLoaded`
3. `window.load`
4. Primera interacción (7 eventos) con Web Audio API unlock
5. Retry cada 2s durante 30s

Volumen por defecto: 0.4