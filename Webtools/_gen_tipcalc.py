import pathlib

css = r"""
:root {
 --cDeep: #07405E;
 --cInk: #0B5C8A;
 --cBlue2: #1F86C8;
 --cGreen2: #4CA22B;
 --cAmber2: #E08C1E;
 --cRed2: #C63C22;
 --Muted: #2C5F7E;
 --shadow: 0 2px 16px rgba(10, 58, 86, .28);
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { height: 100%; }
body {
 font-family: "Segoe UI", system-ui, sans-serif;
 color: var(--cDeep);
 background:
 linear-gradient(0deg, rgba(151,220,95,.85) 0%, rgba(103,208,196,.82) 18%, rgba(77,187,236,.82) 40%, rgba(149,217,246,.85) 70%, rgba(227,244,253,.89) 100%),
 linear-gradient(105deg, #E3F4FD 0%, #95D9F6 30%, #4DBBEC 60%, #67D0C4 82%, #97DC5F 100%);
 background-blend-mode: normal;
 min-height: 100vh;
 overflow-x: hidden;
}
body::before {
 content: ""; position: fixed; top: 0; left: 0; right: 0; height: 170px;
 pointer-events: none; z-index: 0;
 background: linear-gradient(180deg, rgba(255,255,255,.63) 0%, rgba(255,255,255,.26) 55%, transparent 100%);
}
.bubble { position: fixed; border-radius: 50%; pointer-events: none; z-index: 0;
 background: radial-gradient(circle at 35% 30%, #fff 0%, var(--t) 58%, transparent 100%); }
.b1 { width: 300px; height: 300px; left: -70px; top: 38%; opacity: .30; --t: rgba(111,199,240,.9); }
.b2 { width: 380px; height: 380px; right: -90px; top: -110px; opacity: .26; --t: rgba(182,231,122,.9); }
.b3 { width: 180px; height: 180px; left: 52%; bottom: -60px; opacity: .22; --t: rgba(255,217,122,.9); }
.window { position: relative; z-index: 1; max-width: 640px; margin: 46px auto; padding: 0 24px 60px; }
.titlebar { display: flex; align-items: center; gap: 12px; height: 46px; padding: 0 6px; }
.titlebar .logo {
 width: 26px; height: 26px; border-radius: 7px;
 background: linear-gradient(180deg, #8FD9F7 0%, #39A5DC 49%, #1B7FC0 51%, #39B0E4 100%);
 border: 1px solid rgba(255,255,255,.55); box-shadow: var(--shadow);
 display: grid; place-items: center; color: #fff; font-size: 14px; font-weight: 600;
}
.titlebar h1 { font-size: 25px; font-weight: 300; color: var(--cDeep); }
.titlebar h1 b { font-weight: 600; }
.titlebar .sub { margin-left: auto; font-size: 12.5px; color: var(--Muted); }
.card {
 background: linear-gradient(180deg, rgba(255,255,255,.93) 0%, rgba(255,255,255,.77) 45%, rgba(235,248,255,.69) 100%);
 border: 1px solid rgba(255,255,255,.5); border-radius: 14px; padding: 18px;
 box-shadow: var(--shadow); backdrop-filter: blur(12px); margin-bottom: 18px;
}
h2 { font-size: 15px; font-weight: 600; margin-bottom: 10px; color: var(--cDeep); }
input[type="number"], input[type="text"] {
 height: 40px; padding: 0 12px; border-radius: 8px;
 border: 1px solid rgba(44,95,126,.30); background: rgba(255,255,255,.70); color: var(--cDeep);
 font-family: inherit; font-size: 15px;
}
input:focus { outline: 2px solid rgba(31,134,200,.45); outline-offset: -1px; }
.amount-row { display: flex; align-items: center; gap: 10px; }
.amount-row .cur {
 font-size: 20px; font-weight: 600; color: var(--cInk); width: 34px; text-align: center;
 background: rgba(255,255,255,.45); border-radius: 8px; height: 40px; line-height: 40px;
}
#amount { flex: 1; font-size: 19px; font-weight: 600; }
.field-label { font-size: 12.5px; color: var(--Muted); margin: 12px 0 6px; }
.row { display: flex; gap: 10px; flex-wrap: wrap; align-items: center; margin-top: 12px; }
.tipbtn {
 position: relative; height: 40px; min-width: 64px; padding: 0 16px; border: none; border-radius: 9px;
 font-family: inherit; font-size: 14px; font-weight: 600; color: #fff; cursor: pointer; overflow: hidden;
 box-shadow: var(--shadow), inset 0 0 0 1px rgba(255,255,255,.35);
 transition: transform .05s, filter .15s;
}
.tipbtn::before { content: ""; position: absolute; inset: 0; border-radius: 8px; opacity: 0;
 background: rgba(255,255,255,.24); transition: .15s; }
.tipbtn:hover::before { opacity: 1; }
.tipbtn:active { transform: translateY(1px); filter: brightness(.92); }
.tipbtn .shine { position: absolute; left: 1px; right: 1px; top: 1px; height: 17px; border-radius: 8px 8px 0 0;
 background: linear-gradient(180deg, rgba(255,255,255,.72) 0%, rgba(255,255,255,.22) 48%, transparent 50%); pointer-events: none; }
.tipbtn-blue { background: linear-gradient(180deg, #8FD9F7 0%, #39A5DC 49%, #1B7FC0 51%, #39B0E4 100%); }
.tipbtn.selected {
 outline: 3px solid rgba(74,162,43,.65); outline-offset: 1px;
 background: linear-gradient(180deg, #CBF08F 0%, #74C23C 49%, #4E9C22 51%, #7FCF43 100%);
}
.tipbtn.selected::after { content: "\2713"; position: absolute; top: 1px; right: 5px; font-size: 10px; opacity: .9; }
#customTip { width: 110px; }
.slider-row { display: flex; align-items: center; gap: 12px; margin-top: 10px; }
.slider-row label { font-size: 12.5px; color: var(--Muted); white-space: nowrap; }
.slider-row input[type="range"] {
 flex: 1; -webkit-appearance: none; appearance: none; height: 6px; border-radius: 3px;
 background: linear-gradient(90deg, #8FD9F7, #39A5DC, #1B7FC0); outline: none; cursor: pointer;
}
.slider-row input[type="range"]::-webkit-slider-thumb {
 -webkit-appearance: none; width: 20px; height: 20px; border-radius: 50%;
 background: linear-gradient(180deg, #fff 0%, #E3F4FD 100%);
 border: 2px solid #39A5DC; box-shadow: 0 2px 6px rgba(10,58,86,.3); cursor: pointer;
}
.slider-row input[type="range"]::-moz-range-thumb {
 width: 20px; height: 20px; border-radius: 50%;
 background: linear-gradient(180deg, #fff 0%, #E3F4FD 100%);
 border: 2px solid #39A5DC; box-shadow: 0 2px 6px rgba(10,58,86,.3); cursor: pointer;
}
.slider-val { font-size: 14px; font-weight: 600; color: var(--cInk); min-width: 42px; text-align: right; }
.stepper { display: flex; align-items: center; gap: 0; }
.stepper button {
 width: 40px; height: 40px; border: none; cursor: pointer; font-size: 18px; font-weight: 600; color: #fff;
 box-shadow: var(--shadow), inset 0 0 0 1px rgba(255,255,255,.35); position: relative; overflow: hidden;
 transition: filter .15s;
}
.stepper button::before { content: ""; position: absolute; inset: 0; opacity: 0; transition: .15s;
 background: rgba(255,255,255,.24); }
.stepper button:hover::before { opacity: 1; }
.stepper button:active { filter: brightness(.92); }
.stepper button:disabled { opacity: .45; cursor: default; }
.stepper button:disabled::before { opacity: 0; }
.stepper button .shine { position: absolute; left: 1px; right: 1px; top: 1px; height: 17px; border-radius: 7px 7px 0 0;
 background: linear-gradient(180deg, rgba(255,255,255,.72) 0%, rgba(255,255,255,.22) 48%, transparent 50%); pointer-events: none; }
.stepper .minus { border-radius: 8px 0 0 8px; background: linear-gradient(180deg, #FFB6A6 0%, #DD5C3E 49%, #B63B22 51%, #E0704F 100%); }
.stepper .plus { border-radius: 0 8px 8px 0; background: linear-gradient(180deg, #CBF08F 0%, #74C23C 49%, #4E9C22 51%, #7FCF43 100%); }
.stepper .val {
 width: 70px; height: 40px; display: grid; place-items: center; font-size: 17px; font-weight: 600;
 background: rgba(255,255,255,.70);
 border-top: 1px solid rgba(44,95,126,.30); border-bottom: 1px solid rgba(44,95,126,.30);
}
.results { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-top: 6px; }
.res {
 background: linear-gradient(180deg, rgba(255,255,255,.85) 0%, rgba(255,255,255,.55) 48%, rgba(235,248,255,.45) 52%, rgba(255,255,255,.65) 100%);
 border: 1px solid rgba(255,255,255,.6); border-radius: 12px;
 padding: 14px 10px; text-align: center; box-shadow: var(--shadow);
 backdrop-filter: blur(10px); position: relative; overflow: hidden;
 transition: transform .15s, box-shadow .15s;
}
.res:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(10,58,86,.32); }
.res::before { content: ""; position: absolute; left: 0; right: 0; top: 0; height: 14px;
 background: linear-gradient(180deg, rgba(255,255,255,.7), transparent); pointer-events: none; }
.res::after { content: ""; position: absolute; left: 0; top: 0; bottom: 0; width: 4px; pointer-events: none;
 background: linear-gradient(180deg, var(--accent, #1F86C8), rgba(255,255,255,.25)); opacity: .85; }
.res .lbl { font-size: 11.5px; color: var(--Muted); text-transform: uppercase; letter-spacing: .4px; line-height: 1.35; }
.res .num { font-size: 22px; font-weight: 600; margin-top: 6px; word-break: break-all; font-variant-numeric: tabular-nums; color: var(--cInk); }
.res.t-blue { --accent: var(--cBlue2); } .res.t-blue .num { color: var(--cBlue2); }
.res.t-green { --accent: var(--cGreen2); } .res.t-green .num { color: var(--cGreen2); }
.res.t-amber { --accent: var(--cAmber2); } .res.t-amber .num { color: var(--cAmber2); }
.res.total {
 border: 1px solid rgba(116,194,60,.55);
 background: linear-gradient(180deg, rgba(233,248,215,.85) 0%, rgba(255,255,255,.62) 45%, rgba(226,244,206,.55) 100%);
}
.res.total .num { color: var(--cGreen2); font-size: 24px; }
.res.total::after { content: ""; position: absolute; left: 0; right: 0; top: 0; height: 4px; width: 100%;
 background: linear-gradient(90deg, transparent, rgba(116,194,60,.7), transparent); opacity: 1; }
.breakdown { margin-top: 14px; padding: 12px 14px; border-radius: 10px;
 background: linear-gradient(180deg, rgba(255,255,255,.60) 0%, rgba(235,248,255,.40) 100%);
 border: 1px solid rgba(255,255,255,.40); font-size: 13px; color: var(--cDeep); }
.breakdown .bk-row { display: flex; justify-content: space-between; padding: 4px 0; }
.breakdown .bk-row + .bk-row { border-top: 1px dashed rgba(44,95,126,.15); }
.breakdown .bk-label { color: var(--Muted); }
.breakdown .bk-val { font-weight: 600; color: var(--cInk); }
.btn {
 position: relative; height: 40px; padding: 0 22px; border: none; border-radius: 9px;
 font-family: inherit; font-size: 13.5px; color: #fff; cursor: pointer; overflow: hidden;
 box-shadow: var(--shadow), inset 0 0 0 1px rgba(255,255,255,.35);
 transition: transform .05s, filter .15s;
}
.btn::before { content: ""; position: absolute; inset: 0; border-radius: 8px; opacity: 0;
 background: rgba(255,255,255,.24); transition: .15s; }
.btn:hover::before { opacity: 1; }
.btn:active { transform: translateY(1px); filter: brightness(.92); }
.btn .shine { position: absolute; left: 1px; right: 1px; top: 1px; height: 17px; border-radius: 8px 8px 0 0;
 background: linear-gradient(180deg, rgba(255,255,255,.72) 0%, rgba(255,255,255,.22) 48%, transparent 50%); pointer-events: none; }
.btn-blue { background: linear-gradient(180deg, #8FD9F7 0%, #39A5DC 49%, #1B7FC0 51%, #39B0E4 100%); }
.btn-green { background: linear-gradient(180deg, #CBF08F 0%, #74C23C 49%, #4E9C22 51%, #7FCF43 100%); }
.btn-red { background: linear-gradient(180deg, #FFB6A6 0%, #DD5C3E 49%, #B63B22 51%, #E0704F 100%); }
.btn-amber { background: linear-gradient(180deg, #FFE0A6 0%, #E08C1E 49%, #B8700A 51%, #F0A830 100%); }
.history-list { list-style: none; margin-top: 8px; }
.history-item {
 display: flex; justify-content: space-between; align-items: center; gap: 8px;
 padding: 10px 12px; border-radius: 8px; cursor: pointer;
 background: linear-gradient(180deg, rgba(255,255,255,.70) 0%, rgba(235,248,255,.50) 100%);
 border: 1px solid rgba(255,255,255,.40); margin-bottom: 6px;
 transition: transform .1s, box-shadow .15s;
}
.history-item:hover { transform: translateX(3px); box-shadow: 0 3px 10px rgba(10,58,86,.2); }
.history-item .hi-main { font-weight: 600; color: var(--cInk); font-size: 14px; }
.history-item .hi-sub { font-size: 12px; color: var(--Muted); }
.toast {
 position: fixed; bottom: 30px; left: 50%; transform: translateX(-50%) translateY(100px);
 padding: 12px 24px; border-radius: 10px; color: #fff; font-size: 14px; font-weight: 600;
 box-shadow: 0 4px 20px rgba(0,0,0,.25); z-index: 9999; opacity: 0;
 transition: transform .3s ease, opacity .3s ease;
}
.toast.show { transform: translateX(-50%) translateY(0); opacity: 1; }
.toast.success { background: linear-gradient(135deg, #4CA22B, #74C23C); }
.toast.error { background: linear-gradient(135deg, #C63C22, #E0704F); }
.toast.info { background: linear-gradient(135deg, #1F86C8, #39A5DC); }
@media(max-width: 600px) {
 .window { margin: 24px auto; padding: 0 14px 40px; }
 .results { grid-template-columns: 1fr; }
 .row { flex-direction: column; align-items: stretch; }
 .tipbtn { min-width: auto; }
}
"""

html_body = """
<div class="bubble b1"></div>
<div class="bubble b2"></div>
<div class="bubble b3"></div>
<div class="window">
 <div class="titlebar">
 <div class="logo">$</div>
 <h1>Tip<b>Calc</b></h1>
 <span class="sub">Calculadora de propinas</span>
 </div>
 <div class="card">
 <h2>Monto de la cuenta</h2>
 <div class="amount-row">
 <span class="cur">$</span>
 <input type="number" id="amount" placeholder="0.00" min="0" step="0.01">
 </div>
 <div class="field-label">Porcentaje de propina</div>
 <div class="row" id="tipButtons">
 <button class="tipbtn tipbtn-blue" data-pct="10">10%<span class="shine"></span></button>
 <button class="tipbtn tipbtn-blue" data-pct="15">15%<span class="shine"></span></button>
 <button class="tipbtn tipbtn-blue" data-pct="18">18%<span class="shine"></span></button>
 <button class="tipbtn tipbtn-blue selected" data-pct="20">20%<span class="shine"></span></button>
 <button class="tipbtn tipbtn-blue" data-pct="25">25%<span class="shine"></span></button>
 <input type="number" id="customTip" placeholder="Custom %" min="0" max="100" step="0.5">
 </div>
 <div class="slider-row">
 <label>Propina:</label>
 <input type="range" id="tipSlider" min="0" max="50" value="20" step="0.5">
 <span class="slider-val" id="sliderVal">20%</span>
 </div>
 <div class="field-label">N\u00famero de personas</div>
 <div class="row">
 <div class="stepper">
 <button class="minus" id="removePerson"><span class="shine"></span>&minus;</button>
 <div class="val" id="personCount">1</div>
 <button class="plus" id="addPerson"><span class="shine"></span>+</button>
 </div>
 </div>
 </div>
 <div class="card">
 <h2>Resultados</h2>
 <div class="results">
 <div class="res t-blue"><div class="lbl">Propina</div><div class="num" id="tipAmount">$0.00</div></div>
 <div class="res t-green"><div class="lbl">Total con propina</div><div class="num" id="totalWithTip">$0.00</div></div>
 <div class="res t-amber"><div class="lbl">Por persona</div><div class="num" id="perPerson">$0.00</div></div>
 </div>
 <div class="res total" style="margin-top:12px"><div class="lbl">Total por persona (sin propina)</div><div class="num" id="perPersonNoTip">$0.00</div></div>
 <div class="breakdown" id="breakdown">
 <div class="bk-row"><span class="bk-label">Monto original:</span><span class="bk-val" id="bdOriginal">$0.00</span></div>
 <div class="bk-row"><span class="bk-label">Propina calculada:</span><span class="bk-val" id="bdTip">$0.00</span></div>
 <div class="bk-row"><span class="bk-label">Total general:</span><span class="bk-val" id="bdTotal">$0.00</span></div>
 <div class="bk-row"><span class="bk-label">Personas:</span><span class="bk-val" id="bdPersons">1</span></div>
 <div class="bk-row"><span class="bk-label">Cada uno paga:</span><span class="bk-val" id="bdEach">$0.00</span></div>
 </div>
 <div class="row" style="margin-top:16px">
 <button class="btn btn-blue" id="copyBtn"><span class="shine"></span>Copiar resumen</button>
 </div>
 </div>
 <div class="card">
 <h2>Historial</h2>
 <ul class="history-list" id="historyList"></ul>
 <div class="row" style="margin-top:12px">
 <button class="btn btn-red" id="clearHistory"><span class="shine"></span>Limpiar historial</button>
 </div>
 </div>
</div>
"""

js = r"""
const STORAGE_KEY = 'tipcalc_history';
let currentTipPct = 20;
let historyArr = [];

/* ── Currency formatter ─────────────────────────────── */
function formatCurrency(amount) {
 const n = Number(amount);
 if (isNaN(n)) return '$0.00';
 return n.toLocaleString('es-MX', { style: 'currency', currency: 'MXN' });
}

/* ── Input validation ───────────────────────────────── */
function validateInputs() {
 const raw = document.getElementById('amount').value;
 const amount = parseFloat(raw);
 if (raw !== '' && (isNaN(amount) || amount < 0)) {
 showToast('Monto inv\u00e1lido. Ingrese un valor positivo.', 'error');
 return false;
 }
 const persons = parseInt(document.getElementById('personCount').textContent, 10);
 if (persons <= 0) {
 showToast('Debe haber al menos 1 persona.', 'error');
 return false;
 }
 return true;
}

/* ── Core calculation ────────────────────────────────── */
function calculate() {
 const raw = document.getElementById('amount').value;
 const amount = parseFloat(raw);
 if (isNaN(amount) || amount < 0) {
 updateDisplay(0, 0, 0, 0, 0);
 return;
 }
 const tipPercent = currentTipPct;
 const tipAmount = Math.round(amount * tipPercent) / 100;
 const totalWithTip = Math.round((amount + tipAmount) * 100) / 100;
 const persons = parseInt(document.getElementById('personCount').textContent, 10) || 1;
 const perPerson = Math.round((totalWithTip / persons) * 100) / 100;
 const perPersonNoTip = Math.round((amount / persons) * 100) / 100;
 updateDisplay(tipAmount, totalWithTip, perPerson, perPersonNoTip, amount);
}

/* ── Display updater ────────────────────────────────── */
function updateDisplay(tip, total, perPerson, perPersonNoTip, original) {
 document.getElementById('tipAmount').textContent = formatCurrency(tip);
 document.getElementById('totalWithTip').textContent = formatCurrency(total);
 document.getElementById('perPerson').textContent = formatCurrency(perPerson);
 document.getElementById('perPersonNoTip').textContent = formatCurrency(perPersonNoTip);
 document.getElementById('bdOriginal').textContent = formatCurrency(original);
 document.getElementById('bdTip').textContent = formatCurrency(tip);
 document.getElementById('bdTotal').textContent = formatCurrency(total);
 document.getElementById('bdPersons').textContent = document.getElementById('personCount').textContent;
 document.getElementById('bdEach').textContent = formatCurrency(perPerson);
}

/* ── Quick tip buttons ──────────────────────────────── */
function setTipPercent(pct) {
 currentTipPct = pct;
 document.getElementById('tipSlider').value = pct;
 document.getElementById('sliderVal').textContent = pct + '%';
 document.getElementById('customTip').value = '';
 document.querySelectorAll('.tipbtn').forEach(function(btn) {
 btn.classList.remove('selected');
 if (parseInt(btn.dataset.pct, 10) === pct) {
 btn.classList.add('selected');
 }
 });
 calculate();
}

/* ── Slider sync ────────────────────────────────────── */
function updateSlider() {
 const slider = document.getElementById('tipSlider');
 const val = parseFloat(slider.value);
 currentTipPct = val;
 document.getElementById('sliderVal').textContent = val + '%';
 document.querySelectorAll('.tipbtn').forEach(function(btn) {
 btn.classList.remove('selected');
 if (parseFloat(btn.dataset.pct) === val) {
 btn.classList.add('selected');
 }
 });
 calculate();
}

/* ── Person stepper ─────────────────────────────────── */
function addPerson() {
 const el = document.getElementById('personCount');
 let count = parseInt(el.textContent, 10) || 1;
 if (count < 99) { count++; }
 el.textContent = count;
 calculate();
}

function removePerson() {
 const el = document.getElementById('personCount');
 let count = parseInt(el.textContent, 10) || 1;
 if (count > 1) { count--; }
 el.textContent = count;
 calculate();
}

/* ── Copy summary ───────────────────────────────────── */
function copySummary() {
 const tip = document.getElementById('tipAmount').textContent;
 const total = document.getElementById('totalWithTip').textContent;
 const pp = document.getElementById('perPerson').textContent;
 const persons = document.getElementById('personCount').textContent;
 const orig = document.getElementById('bdOriginal').textContent;
 const lines = [
 '--- TipCalc Resumen ---',
 'Monto: ' + orig,
 'Propina (' + currentTipPct + '%): ' + tip,
 'Total con propina: ' + total,
 'Personas: ' + persons,
 'Cada uno paga: ' + pp,
 '-----------------------'
 ];
 const text = lines.join('\n');
 if (navigator.clipboard && navigator.clipboard.writeText) {
 navigator.clipboard.writeText(text).then(function() {
 showToast('Resumen copiado al portapapeles', 'success');
 saveToHistory();
 }).catch(function() { fallbackCopy(text); });
 } else {
 fallbackCopy(text);
 }
}

function fallbackCopy(text) {
 const ta = document.createElement('textarea');
 ta.value = text;
 ta.style.cssText = 'position:fixed;left:-9999px;top:-9999px;opacity:0';
 document.body.appendChild(ta);
 ta.focus();
 ta.select();
 try {
 document.execCommand('copy');
 showToast('Resumen copiado al portapapeles', 'success');
 saveToHistory();
 } catch (e) {
 showToast('Error al copiar', 'error');
 }
 document.body.removeChild(ta);
}

/* ── History management ─────────────────────────────── */
function saveToHistory() {
 const amount = parseFloat(document.getElementById('amount').value);
 if (isNaN(amount) || amount <= 0) return;
 const entry = {
 amount: amount,
 tipPct: currentTipPct,
 persons: parseInt(document.getElementById('personCount').textContent, 10) || 1,
 timestamp: new Date().toLocaleString('es-MX')
 };
 historyArr.unshift(entry);
 if (historyArr.length > 5) { historyArr = historyArr.slice(0, 5); }
 try { localStorage.setItem(STORAGE_KEY, JSON.stringify(historyArr)); } catch(e) { /* quota */ }
 renderHistory();
}

function loadHistory() {
 try {
 const stored = localStorage.getItem(STORAGE_KEY);
 if (stored) { historyArr = JSON.parse(stored); }
 } catch(e) { historyArr = []; }
 renderHistory();
}

function renderHistory() {
 const list = document.getElementById('historyList');
 list.innerHTML = '';
 if (historyArr.length === 0) {
 list.innerHTML = '<li style="padding:12px;color:var(--Muted);text-align:center;font-size:13px;">Sin c\u00e1lculos recientes</li>';
 return;
 }
 historyArr.forEach(function(item, idx) {
 const li = document.createElement('li');
 li.className = 'history-item';
 const mainSpan = document.createElement('span');
 mainSpan.className = 'hi-main';
 mainSpan.textContent = formatCurrency(item.amount) + ' \u2014 ' + item.tipPct + '% propina';
 const subSpan = document.createElement('span');
 subSpan.className = 'hi-sub';
 subSpan.textContent = item.persons + ' persona(s) \u00b7 ' + item.timestamp;
 const wrapper = document.createElement('div');
 wrapper.appendChild(mainSpan);
 wrapper.appendChild(document.createElement('br'));
 wrapper.appendChild(subSpan);
 li.appendChild(wrapper);
 li.addEventListener('click', function() { restoreFromHistory(idx); });
 list.appendChild(li);
 });
}

function restoreFromHistory(idx) {
 const item = historyArr[idx];
 if (!item) return;
 document.getElementById('amount').value = item.amount;
 document.getElementById('personCount').textContent = item.persons;
 setTipPercent(item.tipPct);
 showToast('C\u00e1lculo restaurado del historial', 'info');
}

function clearHistory() {
 historyArr = [];
 try { localStorage.removeItem(STORAGE_KEY); } catch(e) { /* ok */ }
 renderHistory();
 showToast('Historial limpiado correctamente', 'info');
}

/* ── Toast notifications ────────────────────────────── */
function showToast(msg, type) {
 const existing = document.querySelector('.toast');
 if (existing) { existing.remove(); }
 const toast = document.createElement('div');
 toast.className = 'toast ' + (type || 'info');
 toast.textContent = msg;
 document.body.appendChild(toast);
 requestAnimationFrame(function() {
 requestAnimationFrame(function() {
 toast.classList.add('show');
 });
 });
 setTimeout(function() {
 toast.classList.remove('show');
 setTimeout(function() { if (toast.parentNode) toast.remove(); }, 350);
 }, 2800);
}

/* ── Initialization ─────────────────────────────────── */
function init() {
 /* Amount input */
 document.getElementById('amount').addEventListener('input', function() {
 if (validateInputs()) { calculate(); }
 });
 document.getElementById('amount').addEventListener('change', function() {
 if (validateInputs()) { calculate(); saveToHistory(); }
 });

 /* Tip slider */
 document.getElementById('tipSlider').addEventListener('input', function() {
 updateSlider();
 });

 /* Quick tip buttons */
 document.querySelectorAll('.tipbtn').forEach(function(btn) {
 btn.addEventListener('click', function() {
 setTipPercent(parseInt(btn.dataset.pct, 10));
 });
 });

 /* Custom tip input */
 document.getElementById('customTip').addEventListener('input', function() {
 const val = parseFloat(this.value);
 if (!isNaN(val) && val >= 0 && val <= 100) {
 currentTipPct = val;
 document.getElementById('tipSlider').value = Math.min(val, 50);
 document.getElementById('sliderVal').textContent = val + '%';
 document.querySelectorAll('.tipbtn').forEach(function(b) { b.classList.remove('selected'); });
 calculate();
 }
 });

 /* Person stepper */
 document.getElementById('addPerson').addEventListener('click', function() {
 addPerson();
 });
 document.getElementById('removePerson').addEventListener('click', function() {
 removePerson();
 });

 /* Copy button */
 document.getElementById('copyBtn').addEventListener('click', function() {
 copySummary();
 });

 /* Clear history */
 document.getElementById('clearHistory').addEventListener('click', function() {
 clearHistory();
 });

 /* Load saved history and initial calc */
 loadHistory();
 calculate();
}

document.addEventListener('DOMContentLoaded', init);
"""

full_html = '<!DOCTYPE html>\n<html lang="es">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>TipCalc \u2014 Calculadora de Propinas</title>\n<style>' + css + '</style>\n</head>\n<body>' + html_body + '<script>' + js + '</script>\n</body>\n</html>'

out = pathlib.Path(r'C:/Users/nicol/OneDrive/Documents/ClaudeCode/Another Store/Webtools/TipCalc.html')
out.write_text(full_html, encoding='utf-8')
print(f'WRITTEN: {len(full_html)} bytes, {full_html.count(chr(10))} lines')
print(f'SCRIPT_TAGS: {full_html.count("<script>")}')
print(f'FUNC_COUNT: {full_html.count("function ")}')
print(f'CONST_COUNT: {full_html.count("const ")}')
print(f'EVENT_COUNT: {full_html.count("addEventListener")}')