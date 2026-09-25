import pathlib

target = pathlib.Path(r'C:/Users/nicol/OneDrive/Documents/ClaudeCode/Another Store/Webtools/HashTool.html')

html = '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>HashTool \u2014 Generador y Verificador Aero Glass</title>
<style>
/* =============================================
   AERO GLASS \u2014 HashTool
   Patron canonico copiado de WordMeter.html
   ============================================= */
/* Tokens de color del Design Spec */
:root{
  --cDeep:#07405E; --cInk:#0B5C8A; --cBlue2:#1F86C8; --cGreen2:#4CA22B;
  --cAmber2:#E08C1E; --cRed2:#C63C22; --Muted:#2C5F7E;
  --shadow:0 2px 16px rgba(10,58,86,.28);
}
/* Reset basico */
*{box-sizing:border-box; margin:0; padding:0;}
html,body{height:100%;}
/* Fondo SkyBrush con doble gradiente superpuesto */
body{
  font-family:"Segoe UI",system-ui,sans-serif;
  color:var(--cDeep);
  background:
    linear-gradient(0deg, rgba(151,220,95,.85) 0%, rgba(103,208,196,.82) 18%, rgba(77,187,236,.82) 40%, rgba(149,217,246,.85) 70%, rgba(227,244,253,.89) 100%),
    linear-gradient(105deg,#E3F4FD 0%, #95D9F6 30%, #4DBBEC 60%, #67D0C4 82%, #97DC5F 100%);
  background-blend-mode:normal;
  min-height:100vh;
  overflow-x:hidden;
}
/* TopGloss overlay \u2014 brillo superior simulando luz cenital sobre vidrio */
body::before{
  content:""; position:fixed; top:0; left:0; right:0; height:170px; pointer-events:none; z-index:0;
  background:linear-gradient(180deg, rgba(255,255,255,.63) 0%, rgba(255,255,255,.26) 55%, transparent 100%);
}
/* Burbujas decorativas con radial-gradient descentrado */
.bubble{position:fixed; border-radius:50%; pointer-events:none; z-index:0;
  background:radial-gradient(circle at 35% 30%, #fff 0%, var(--t) 58%, transparent 100%);}
.b1{width:300px;height:300px; left:-70px; top:38%; opacity:.30; --t:rgba(111,199,240,.9);}
.b2{width:380px;height:380px; right:-90px; top:-110px; opacity:.26; --t:rgba(182,231,122,.9);}
.b3{width:180px;height:180px; left:52%; bottom:-60px; opacity:.22; --t:rgba(255,217,122,.9);}
/* Contenedor principal de la ventana */
.window{
  position:relative; z-index:1; max-width:980px; margin:46px auto; padding:0 24px 60px;
}
/* Barra de titulo con logo glossy */
.titlebar{display:flex; align-items:center; gap:12px; height:46px; padding:0 6px;}
.titlebar .logo{width:26px;height:26px;border-radius:7px;
  background:linear-gradient(180deg,#8FD9F7 0%,#39A5DC 49%,#1B7FC0 51%,#39B0E4 100%);
  border:1px solid rgba(255,255,255,.55); box-shadow:var(--shadow);
  display:grid;place-items:center;color:#fff;font-size:14px;font-weight:600;}
.titlebar h1{font-size:25px; font-weight:300; color:var(--cDeep);}
.titlebar h1 b{font-weight:600;}
.titlebar .sub{margin-left:auto; font-size:12.5px; color:var(--Muted);}
/* Tarjetas con efecto vidrio esmerilado (CardBrush) */
.card{
  background:linear-gradient(180deg, rgba(255,255,255,.93) 0%, rgba(255,255,255,.77) 45%, rgba(235,248,255,.69) 100%);
  border:1px solid rgba(255,255,255,.5);
  border-radius:14px; padding:18px; box-shadow:var(--shadow);
  backdrop-filter:blur(12px);
  margin-bottom:18px;
}
/* Encabezados dentro de tarjetas */
h2,h3{font-size:15px; font-weight:600; margin-bottom:10px; color:var(--cDeep);}
/* Textarea estilo glass */
textarea{
  width:100%; min-height:120px; resize:vertical; padding:12px;
  border-radius:8px; border:1px solid rgba(44,95,126,.25);
  background:rgba(255,255,255,.70); color:var(--cDeep);
  font-family:Consolas,monospace; font-size:13px; line-height:1.5;
}
textarea:focus{outline:2px solid rgba(31,134,200,.45); outline-offset:-1px;}
/* Inputs de texto estilo glass */
input[type=text]{
  height:36px; padding:0 12px; border-radius:8px;
  border:1px solid rgba(44,95,126,.30); background:rgba(255,255,255,.70);
  color:var(--cDeep); font-family:inherit; font-size:13px; flex:1; min-width:180px;
}
input[type=text]:focus{outline:2px solid rgba(31,134,200,.45); outline-offset:-1px;}
/* Input file estilo glass */
input[type=file]{
  width:100%; padding:10px; border-radius:8px;
  border:1px solid rgba(44,95,126,.25); background:rgba(255,255,255,.70);
  color:var(--cDeep); font-family:inherit; font-size:13px;
}
input[type=file]::file-selector-button{
  height:32px; padding:0 14px; border:none; border-radius:7px; margin-right:10px;
  background:linear-gradient(180deg,#8FD9F7 0%,#39A5DC 49%,#1B7FC0 51%,#39B0E4 100%);
  color:#fff; font-family:inherit; font-size:12.5px; cursor:pointer;
  box-shadow:0 1px 6px rgba(10,58,86,.18), inset 0 0 0 1px rgba(255,255,255,.35);
}
/* Select / dropdown estilizado glass */
select{
  height:36px; padding:0 12px; border-radius:8px;
  border:1px solid rgba(44,95,126,.30); background:rgba(255,255,255,.70);
  color:var(--cDeep); font-family:inherit; font-size:13px; min-width:200px;
  appearance:none; -webkit-appearance:none;
  background-image:url("data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' width=\'12\' height=\'8\'%3E%3Cpath d=\'M1 1l5 5 5-5\' stroke=\'%2307405E\' stroke-width=\'1.5\' fill=\'none\'/%3E%3C/svg%3E");
  background-repeat:no-repeat; background-position:right 12px center;
  padding-right:32px;
}
select:focus{outline:2px solid rgba(31,134,200,.45); outline-offset:-1px;}
/* Filas flex para layout de controles */
.row,.flex-row{display:flex; gap:10px; flex-wrap:wrap; align-items:center; margin-top:12px;}
.mb-10{margin-bottom:10px;}
.mt-10{margin-top:10px;}
/* === Pills glass para radio buttons de modo === */
.toggle-group{display:flex; gap:8px; flex-wrap:wrap; margin:10px 0;}
.toggle-group label{
  display:inline-flex; align-items:center; gap:6px;
  padding:7px 16px; border-radius:999px; cursor:pointer;
  background:linear-gradient(180deg, rgba(255,255,255,.85) 0%, rgba(255,255,255,.55) 48%, rgba(235,248,255,.45) 52%, rgba(255,255,255,.65) 100%);
  border:1px solid rgba(255,255,255,.6);
  box-shadow:0 1px 4px rgba(10,58,86,.14), inset 0 1px 0 rgba(255,255,255,.8);
  font-size:13px; color:var(--cDeep); transition:.15s; user-select:none;
  backdrop-filter:blur(8px);
}
.toggle-group label:hover{background:rgba(255,255,255,.80);}
.toggle-group input[type=radio]{accent-color:var(--cBlue2); margin:0;}
.toggle-group input[type=checkbox]{accent-color:var(--cBlue2); margin:0;}
/* === Botones glossy con hard-stop 49%/51% === */
.btn{
  position:relative; height:40px; padding:0 22px; border:none; border-radius:9px;
  font-family:inherit; font-size:13.5px; color:#fff; cursor:pointer; overflow:hidden;
  box-shadow:var(--shadow), inset 0 0 0 1px rgba(255,255,255,.35);
  transition:transform .05s, filter .15s;
}
.btn::before{content:""; position:absolute; inset:0; border-radius:8px; opacity:0;
  background:rgba(255,255,255,.24); transition:.15s;}
.btn:hover::before{opacity:1;}
.btn:active{transform:translateY(1px); filter:brightness(.92);}
/* Shine interno del boton (reflejo humedo superior) */
.btn .shine{position:absolute; left:1px; right:1px; top:1px; height:17px; border-radius:8px 8px 0 0;
  background:linear-gradient(180deg, rgba(255,255,255,.72) 0%, rgba(255,255,255,.22) 48%, transparent 50%); pointer-events:none;}
/* Variantes de color de botones glossy */
.btn-blue{background:linear-gradient(180deg,#8FD9F7 0%,#39A5DC 49%,#1B7FC0 51%,#39B0E4 100%);}
.btn-green{background:linear-gradient(180deg,#CBF08F 0%,#74C23C 49%,#4E9C22 51%,#7FCF43 100%);}
.btn-amber{background:linear-gradient(180deg,#FFE6A8 0%,#F0A93A 49%,#D5871B 51%,#F7B950 100%);}
.btn-red{background:linear-gradient(180deg,#FFB6A6 0%,#DD5C3E 49%,#B63B22 51%,#E0704F 100%);}
/* Boton ghost (semi-transparente) */
.btn-ghost{
  height:34px; padding:0 16px; border-radius:8px; border:1px solid rgba(255,255,255,.5);
  background:rgba(255,255,255,.4); color:var(--cDeep); font-family:inherit; font-size:13px; cursor:pointer; transition:.15s;
}
.btn-ghost:hover{background:rgba(255,255,255,.67);}
/* === Tile / Result box con gradient glass y accent bar lateral === */
.tile,.result-box{
  background:linear-gradient(180deg, rgba(255,255,255,.85) 0%, rgba(255,255,255,.55) 48%, rgba(235,248,255,.45) 52%, rgba(255,255,255,.65) 100%);
  border:1px solid rgba(255,255,255,.6);
  border-radius:12px; padding:14px 12px 12px;
  box-shadow:var(--shadow); backdrop-filter:blur(10px);
  position:relative; overflow:hidden;
  margin-bottom:12px;
}
/* Gloss superior del tile */
.tile::before,.result-box::before{content:""; position:absolute; left:0; right:0; top:0; height:14px;
  background:linear-gradient(180deg, rgba(255,255,255,.7), transparent); pointer-events:none;}
/* Accent bar lateral izquierdo */
.tile::after,.result-box::after{content:""; position:absolute; left:0; top:0; bottom:0; width:4px; pointer-events:none;
  background:linear-gradient(180deg, var(--accent,var(--cBlue2)), rgba(255,255,255,.25)); opacity:.85;}
/* Etiqueta del resultado (HEX, Base64) */
.result-label{
  display:inline-block; font-size:11px; font-weight:600; text-transform:uppercase; letter-spacing:.5px;
  color:var(--Muted); margin-bottom:6px;
}
/* Valor hash en monospace sobre fondo glass ligeramente mas oscuro */
.result-box div[id$="Result"]{
  font-family:Consolas,monospace; font-size:13px; line-height:1.55;
  word-break:break-all; color:var(--cInk);
  background:rgba(7,64,94,.06); border-radius:6px; padding:8px 10px;
  border:1px solid rgba(44,95,126,.12);
}
/* === Indicador de verificacion === */
.verify-status{font-size:18px; font-weight:600; margin-left:10px;}
.verify-match{color:var(--cGreen2);}
.verify-no-match{color:var(--cRed2);}
/* === Progress bar estilo Design Spec === */
.progress-container{margin:15px 0; display:none;}
.progress-bar{
  height:10px; border-radius:6px;
  background:#59FFFFFF; border:1px solid #73FFFFFF;
  overflow:hidden;
}
.progress-fill{
  height:100%; border-radius:5px; width:0%;
  background:linear-gradient(180deg,#8FD9F7 0%,#39A5DC 49%,#1B7FC0 51%,#39B0E4 100%);
  transition:width .3s;
  position:relative;
}
/* Highlight blanco superior de la barra de progreso */
.progress-fill::after{
  content:""; position:absolute; left:0; right:0; top:0; height:4px;
  background:rgba(255,255,255,.45); border-radius:5px 5px 0 0;
}
.progress-text{text-align:center; margin-top:5px; font-size:12px; color:var(--Muted);}
/* === Tabla batch con hover glass === */
.batch-table{width:100%; border-collapse:collapse; margin:15px 0; font-size:13px;}
.batch-table th{
  padding:10px; text-align:left; font-weight:600; font-size:12px;
  background:#4DFFFFFF; color:var(--cDeep);
  border-bottom:1px solid rgba(255,255,255,.5);
}
.batch-table td{
  padding:10px; text-align:left; color:var(--cDeep);
  border-bottom:1px solid rgba(44,95,126,.10);
  transition:background .15s;
}
.batch-table tr:hover td{background:rgba(255,255,255,.35);}
.batch-table td.hash-cell{font-family:Consolas,monospace; word-break:break-all; font-size:11px; color:var(--cInk);}
/* === Toast con backdrop-filter y animacion slideUp === */
.toast{
  position:fixed; bottom:24px; left:50%; transform:translateX(-50%) translateY(20px);
  background:rgba(255,255,255,.9); backdrop-filter:blur(10px); color:var(--cDeep);
  border:1px solid rgba(255,255,255,.6); border-radius:10px; padding:10px 20px;
  box-shadow:var(--shadow); font-size:13px; opacity:0; pointer-events:none; transition:.25s; z-index:9;
}
.toast.show{opacity:1; transform:translateX(-50%) translateY(0);}
/* === Info educativa con borde ambar sutil === */
.algo-info{font-size:12.5px; color:var(--Muted); line-height:1.6; padding:4px 0;}
.algo-info strong{display:block; margin-top:10px; color:var(--cDeep); font-size:13px