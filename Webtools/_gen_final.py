import subprocess, pathlib, os

repo = r"C:\Users\nicol\OneDrive\Documents\ClaudeCode\Another Store"
target = pathlib.Path(os.path.join(repo, "Webtools", "TipCalc.html"))

# Get original file from git HEAD
r = subprocess.run(["git", "show", "HEAD:Webtools/TipCalc.html"],
                   capture_output=True, text=True, cwd=repo)
orig = r.stdout

# Extract body and script from original
body_start = orig.index("<body>")
body_and_script = orig[body_start:]

# New Aero Glass CSS
new_css = """/* === VARIABLES CSS — Design Spec Aero Glass === */
:root{
  --cDeep:#07405E; --cInk:#0B5C8A; --cBlue2:#1F86C8; --cGreen2:#4CA22B;
  --cAmber2:#E08C1E; --cRed2:#C63C22; --Muted:#2C5F7E;
  --shadow:0 2px 16px rgba(10,58,86,.28);
}
/* === RESET Y BASE === */
*{box-sizing:border-box; margin:0; padding:0;}
html,body{height:100%;}
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
/* === TopGloss overlay — brillo superior tipo cristal === */
body::before{
  content:""; position:fixed; top:0; left:0; right:0; height:170px; pointer-events:none; z-index:0;
  background:linear-gradient(180deg, rgba(255,255,255,.63) 0%, rgba(255,255,255,.26) 55%, transparent 100%);
}
/* === BURBUJAS DECORATIVAS === */
.bubble{position:fixed; border-radius:50%; pointer-events:none; z-index:0;
  background:radial-gradient(circle at 35% 30%, #fff 0%, var(--t) 58%, transparent 100%);}
.b1{width:300px;height:300px; left:-70px; top:38%; opacity:.30; --t:rgba(111,199,240,.9);}
.b2{width:380px;height:380px; right:-90px; top:-110px; opacity:.26; --t:rgba(182,231,122,.9);}
.b3{width:180px;height:180px; left:52%; bottom:-60px; opacity:.22; --t:rgba(255,217,122,.9);}
/* === CONTENEDOR PRINCIPAL === */
.window{
  position:relative; z-index:1; max-width:640px; margin:46px auto; padding:0 24px 60px;
}
/* === BARRA DE TITULO === */
.titlebar{display:flex; align-items:center; gap:12px; height:46px; padding:0 6px;}
.titlebar .logo{width:26px;height:26px;border-radius:7px;
  background:linear-gradient(180deg,#8FD9F7 0%,#39A5DC 49%,#1B7FC0 51%,#39B0E4 100%);
  border:1px solid rgba(255,255,255,.55); box-shadow:var(--shadow);
  display:grid;place-items:center;color:#fff;font-size:14px;font-weight:600;}
.titlebar h1{font-size:25px; font-weight:300; color:var(--cDeep);}
.titlebar h1 b{font-weight:600;}
.titlebar .sub{margin-left:auto; font-size:12.5px; color:var(--Muted);}
/* === CARD — Panel de cristal con backdrop-filter === */
.card{
  background:linear-gradient(180deg, rgba(255,255,255,.93) 0%, rgba(255,255,255,.77) 45%, rgba(235,248,255,.69) 100%);
  border:1px solid rgba(255,255,255,.5);
  border-radius:14px; padding:18px; box-shadow:var(--shadow);
  backdrop-filter:blur(12px);
  margin-bottom:18px;
}
/* === ENCABEZADOS === */
h2{font-size:15px; font-weight:600; margin-bottom:10px; color:var(--cDeep);}
/* === INPUTS NUMERICOS Y DE TEXTO — Estilo glass === */
input[type="number"], input[type="text"]{
  height:40px; padding:0 12px; border-radius:8px;
  border:1px solid rgba(44,95,126,.30); background:rgba(255,255,255,.70); color:var(--cDeep);
  font-family:inherit; font-size:15px;
}
input:focus{outline:2px solid rgba(31,134,200,.45); outline-offset:-1px;}
/* === FILA DE MONTO CON SIMBOLO === */
.amount-row{display:flex; align-items:center; gap:10px;}
.amount-row .cur{font-size:20px; font-weight:600; color:var(--cInk); width:34px; text-align:center;
  background:rgba(255,255,255,.45); border-radius:8px; height:40px; line-height:40px;}
#amount{flex:1; font-size:19px; font-weight:600;}
.field-label{font-size:12.5px; color:var(--Muted); margin:12px 0 6px;}
/* === FILAS GENERICAS === */
.row{display:flex; gap:10px; flex-wrap:wrap; align-items:center; margin-top:12px;}
/* === BOTONES RAPIDOS DE PROPINA — Pills glossy con hard stop 49%/51% === */
.tipbtn{
  position:relative; height:40px; min-width:64px; padding:0 16px; border:none; border-radius:9px;
  font-family:inherit; font-size:14px; font-weight:600; color:#fff; cursor:pointer; overflow:hidden;
  box-shadow:var(--shadow), inset 0 0 0 1px rgba(255,255,255,.35);
  transition:transform .05s, filter .15s;
}
.tipbtn::before{content:""; position:absolute; inset:0; border-radius:8px; opacity:0;
  background:rgba(255,255,255,.24); transition:.15s;}
.tipbtn:hover::before{opacity:1;}
.tipbtn:active{transform:translateY(1px); filter:brightness(.92);}
.tipbtn .shine{position:absolute; left:1px; right:1px; top:1px; height:17px; border-radius:8px 8px 0 0;
  background:linear-gradient(180deg, rgba(255,255,255,.72) 0%, rgba(255,255,255,.22) 48%, transparent 50%); pointer-events:none;}
.tipbtn-blue{background:linear-gradient(180deg,#8FD9F7 0%,#39A5DC 49%,#1B7FC0 51%,#39B0E4 100%);}
.tipbtn.selected{
  outline:3px solid rgba(74,162,43,.65); outline-offset:1px;
  background:linear-gradient(180deg,#CBF08F 0%,#74C23C 49%,#4E9C22 51%,#7FCF43 100%);
}
.tipbtn.selected::after{content:"\\2713"; position:absolute; top:1px; right:5px; font-size:10px; opacity:.9;}
#customTip{width:110px;}
/* === STEPPER DE PERSONAS — Botones +/- glossy === */
.stepper{display:flex; align-items:center; gap:0;}
.stepper button{
  width:40px; height:40px; border:none; cursor:pointer; font-size:18px; font-weight:600; color:#fff;
  box-shadow:var(--shadow), inset 0 0 0 1px rgba(255,255,255,.35); position:relative; overflow:hidden;
  transition:filter .15s;
}
.stepper button::before{content:""; position:absolute; inset:0; opacity:0; transition:.15s;
  background:rgba(255,255,255,.24);}
.stepper button:hover::before{opacity:1;}
.stepper button:active{filter:brightness(.92);}
.stepper button:disabled{opacity:.45; cursor:default;}
.stepper button:disabled::before{opacity:0;}
.stepper button .shine{position:absolute; left:1px; right:1px; top:1px; height:17px; border-radius:7px 7px 0 0;
  background:linear-gradient(180deg, rgba(255,255,255,.72) 0%, rgba(255,255,255,.22) 48%, transparent 50%); pointer-events:none;}
.stepper .minus{border-radius:8px 0 0 8px; background:linear-gradient(180deg,#FFB6A6 0%,#DD5C3E 49%,#B63B22 51%,#E0704F 100%);}
.stepper .plus{border-radius:0 8px 8px 0; background:linear-gradient(180deg,#CBF08F 0%,#74C23C 49%,#4E9C22 51%,#7FCF43 100%);}
.stepper .val{
  width:70px; height:40px; display:grid; place-items:center; font-size:17px; font-weight:600;
  background:rgba(255,255,255,.70); border-top:1px solid rgba(44,95,126,.30); border-bottom:1px solid rgba(44,95,126,.30);
}
/* === TILES DE RESULTADO — Glass con accent bar lateral y backdrop-filter === */
.results{display:grid; grid-template-columns:repeat(3,1fr); gap:12px; margin-top:6px;}
.res{
  background:linear-gradient(180deg, rgba(255,255,255,.85) 0%, rgba(255,255,255,.55) 48%, rgba(235,248,255,.45) 52%, rgba(255,255,255,.65) 100%);
  border:1px solid rgba(255,255,255,.6); border-radius:12px;
  padding:14px 10px; text-align:center; box-shadow:var(--shadow);
  backdrop-filter:blur(10px); position:relative; overflow:hidden;
  transition:transform .15s, box-shadow .15s;
}
.res:hover{transform:translateY(-2px); box-shadow:0 6px 20px rgba(10,58,86,.32);}
.res::before{content:""; position:absolute; left:0; right:0; top:0; height:14px;
  background:linear-gradient(180deg, rgba(255,255,255,.7), transparent); pointer-events:none;}
.res::after{content:""; position:absolute; left:0; top:0; bottom:0; width:4px; pointer-events:none;
  background:linear-gradient(180deg, var(--accent,#1F86C8), rgba(255,255,255,.25)); opacity:.85;}
.res .lbl{font-size:11.5px; color:var(--Muted); text-transform:uppercase; letter-spacing:.4px; line-height:1.35;}
.res .num{font-size:22px; font-weight:600; margin-top:6px; word-break:break-all; font-variant-numeric:tabular-nums; color:var(--cInk);}
.res.t-blue{--accent:var(--cBlue2);} .res.t-blue .num{color:var(--cBlue2);}
.res.t-green{--accent:var(--cGreen2);} .res.t-green .num{color:var(--cGreen2);}
.res.t-amber{--accent:var(--cAmber2);} .res.t-amber .num{color:var(--cAmber2);}
.res.total{
  border:1px solid rgba(116,194,60,.55);
  background:linear-gradient(180deg, rgba(233,248,215,.85) 0%, rgba(255,255