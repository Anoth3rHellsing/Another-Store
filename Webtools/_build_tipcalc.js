const fs = require('fs');
const path = 'C:\\Users\\nicol\\OneDrive\\Documents\\ClaudeCode\\Another Store\\Webtools\\TipCalc.html';

const html = `<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TipCalc - Calculadora de Propinas</title>
<style>
/* Layout minimo - estilos Aero Glass seran aplicados por otro agente */
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:system-ui,-apple-system,sans-serif;min-height:100vh;padding:20px}
.bubbles{max-width:900px;margin:0 auto}
.window{margin-bottom:20px}
.titlebar{display:flex;align-items:center;gap:10px;padding:12px 16px}
.titlebar h1{font-size:1.25rem;font-weight:600}
.card{padding:20px;margin-bottom:16px}
.grid{display:grid;gap:16px}
.grid-3{grid-template-columns:repeat(auto-fit,minmax(150px,1fr))}
.flex{display:flex;gap:8px;align-items:center}
.flex-wrap{flex-wrap:wrap}
.flex-center{justify-content:center}
.flex-between{justify-content:space-between}
.gap-md{gap:8px}
.mt-sm{margin-top:8px}
.mt-md{margin-top:16px}
.mb-sm{margin-bottom:8px}
.mb-md{margin-bottom:16px}
.my-md{margin-top:16px;margin-bottom:16px}
.text-center{text-align:center}
.text-right{text-align:right}
.text-sm{font-size:.875rem}
.text-lg{font-size:1.125rem}
.text-xl{font-size:1.5rem}
.font-bold{font-weight:700}
.w-full{width:100%}
.hidden{display:none!important}
.block{display:block}
input[type=number],input[type=text],select{padding:8px;border-radius:4px;border:1px solid #ccc}
input[type=range]{width:100%;cursor:pointer}
.btn-group{display:flex;gap:4px;flex-wrap:wrap}
.stepper{display:flex;align-items:center;gap:4px}
.result-box{padding:16px;text-align:center}
.item-row{display:flex;gap:8px;align-items:center;margin-bottom:8px;flex-wrap:wrap}
.person-share{display:flex;justify-content:space-between;padding:8px;margin-bottom:4px}
.toast-container{position:fixed;bottom:20px;right:20px;z-index:9999;display:flex;flex-direction:column;gap:8px}
.toast{padding:12px 20px;border-radius:8px;background:rgba(30,30,30,.9);color:#fff;opacity:0;transform:translateY(20px);transition:all .3s ease;max-width:320px}
@media(max-width:600px){
.grid-3{grid-template-columns:1fr}
.btn-group{justify-content:center}
.item-row{flex-direction:column;align-items:stretch}
}
</style>
</head>
<body>
<div class="bubbles">
<div class="window">
<div class="titlebar"><span class="icon">&#x1F4B0;</span><h1>TipCalc - Calculadora de Propinas</h1></div>
<!-- Card: Inputs principales -->
<div class="card">
<div class="mb-md">
<label for="billAmount" class="text-lg font-bold mb-sm block">Monto de la cuenta</label>
<input type="number" id="billAmount" class="w-full" placeholder="0.00" step="0.01" min="0">
</div>
<div class="mb-md">
<label class="text-lg font-bold mb-sm block">Porcentaje de propina</label>
<div class="btn-group mb-sm">
<button class="btn btn-blue tip-btn" data-tip="10">10%</button>
<button class="btn btn-green tip-btn" data-tip="15">15%</button>
<button class="btn btn-blue tip-btn" data-tip="18">18%</button>
<button class="btn btn-blue tip-btn" data-tip="20">20%</button>
<button class="btn btn-blue tip-btn" data-tip="25">25%</button>
</div>
<div class="flex gap-md mt-sm">
<input type="range" id="tipSlider" min="0" max="50" value="15" step="1" style="flex:1">
<input type="number" id="tipCustom" placeholder="%" min="0" max="100" value="15" style="width:70px">
</div>
</div>
<div class="mb-md">
<label class="text-lg font-bold mb-sm block">Numero de personas</label>
<div class="stepper">
<button class="btn btn-ghost" id="decPpl">-</button>
<input type="number" id="pplCount" value="1" min="1" max="50" style="width:70px;text-align:center">
<button class="btn btn-ghost" id="incPpl">+</button>
</div>
</div>
<div class="text-center mt-md">
<button class="btn btn-amber" id="togAdv">Modo Avanzado &#x25BC;</button>
</div>
</div>
<!-- Card: Modo avanzado -->
<div class="card hidden" id="advMode">
<h2 class="text-lg font-bold mb-md">Division Desigual</h2>
<div class="flex gap-md mb-md">
<button class="btn btn-blue" id="splitPct">Por porcentaje</button>
<button class="btn btn-ghost" id="splitAmt">Por monto fijo</button>
</div>
<div id="pplList"></div>
<button class="btn btn-green mt-sm" id="addPpl">+ Anadir persona</button>
<hr class="my-md">
<h2 class="text-lg font-bold mb-md">Items Individuales</h2>
<div id="itmList"></div>
<div class="flex gap-md mt-sm flex-wrap">
<input type="text" id="itmName" placeholder="Nombre del item" style="flex:1;min-width:120px">
<input type="number" id="itmPrice" placeholder="Precio" step="0.01" min="0" style="width:100px">
<select id="itmPerson" style="width:130px"><option value="">Todos</option></select>
<button class="btn btn-blue" id="addItm">Anadir</button>
</div>
<div class="mt-sm text-right">
<span class="text-lg font-bold">Subtotal items: $<span id="itmSub">0.00</span></span>
</div>
</div>
<!-- Card: Resultados -->
<div class="card">
<h2 class="text-lg font-bold mb-md">Resultados</h2>
<div class="grid grid-3">
<div class="tile result-box"><div class="text-sm">Propina</div><div class="text-xl font-bold" id="rTip">$0.00</div></div>
<div class="tile result-box"><div class="text-sm">Total con propina</div><div class="text-xl font-bold" id="rTotal">$0.00</div></div>
<div class="tile result-box"><div class="text-sm">Por persona</div><div class="text-xl font-bold" id="rPP">$0.00</div></div>
</div>
<div class="mt-md" id="breakdown">
<h3 class="font-bold mb-sm">Desglose</h3>
<div class="flex flex-between mb-sm"><span>Monto de la cuenta:</span><span id="dBill">$0.00</span></div>
<div class="flex flex-between mb-sm"><span>Propina (<span id="dTipP">15</span>%):</span><span id="dTip">$0.00</span></div>
<hr class="my-md">
<div class="flex flex-between font-bold"><span>Total:</span><span id="dTotal">$0.00</span></div>
<div class="flex flex-between mt-sm text-sm"><span>Por persona (sin propina):</span><span id="dPPNT">$0.00</span></div>
<div class="flex flex-between text-sm"><span>Por persona (con propina):</span><span id="dPPT">$0.00</span></div>
</div>
<div class="mt-md hidden" id="pBreak">
<h3 class="font-bold mb-sm">Por persona (desigual)</h3>
<div id="pShares"></div>
</div>
<div class="flex flex-center gap-md mt-md flex-wrap">
<button class="btn btn-green" id="saveHist">Guardar en historial</button>
<button class="btn btn-blue" id="copySum">Copiar resumen</button>
<button class="btn btn-ghost" id="resetAll">Reiniciar</button>
</div>
</div>
<!-- Card: Historial -->
<div class="card">
<h2 class="text-lg font-bold mb-md">Historial (ultimos 5)</h2>
<div id="histList"><p class="text-sm text-center">No hay calculos guardados</p></div>
</div>
</div>
</div>
<div class="toast-container" id="toastC"></div>
<script>
// =============================================
// REFERENCIAS DOM
// =============================================
var billIn = document.getElementById('billAmount');
var tipSl = document.getElementById('tipSlider');
var tipCu = document.getElementById('tipCustom');
var pplIn = document.getElementById('pplCount');
var decP = document.getElementById('decPpl');
var incP = document.getElementById('incPpl');
var togA = document.getElementById('togAdv');
var advD = document.getElementById('advMode');
var spP = document.getElementById('splitPct');
var spA = document.getElementById('splitAmt');
var pplL = document.getElementById('pplList');
var addP = document.getElementById('addPpl');
var itmL = document.getElementById('itmList');
var itmN = document.getElementById('itmName');
var itmPr = document.getElementById('itmPrice');
var itmPe = document.getElementById('itmPerson');
var addI = document.getElementById('addItm');
var itmS = document.getElementById('itmSub');
var eTip = document.getElementById('rTip');
var eTot = document.getElementById('rTotal');
var ePP = document.getElementById('rPP');
var dB = document.getElementById('dBill');
var dTP = document.getElementById('dTipP');
var dT = document.getElementById('dTip');
var dTo = document.getElementById('dTotal');
var dPN = document.getElementById('dPPNT');
var dPT = document.getElementById('dPPT');
var pBr = document.getElementById('pBreak');
var pSh = document.getElementById('pShares');
var savB = document.getElementById('saveHist');
var copB = document.getElementById('copySum');
var resB = document.getElementById('resetAll');
var hL = document.getElementById('histList');
var tC = document.getElementById('toastC');

// =============================================
// ESTADO DE LA APLICACION
// =============================================
var S = {
  bill: 0,
  tip: 15,
  ppl: 1,
  adv: false,
  split: 'percent',
  people: [{ id: 1, name: 'Persona 1', share: 100 }],
  items: [],
  npid: 2,
  niid: 1
};

// =============================================
// TOAST NOTIFICATIONS
// =============================================
function toast(m, t) {
  t = t || 'info';
  var e = document.createElement('div');
  e.className = 'toast';
  e.textContent = m;
  var c = t === 'success' ? '#22c55e' : t === 'error' ? '#ef4444' : t === 'warning' ? '#f59e0b' : '#3b82f6';
  e.style.borderLeft = '4px solid ' + c;
  tC.appendChild(e);
  requestAnimationFrame(function() {
    e.style.opacity = '1';
    e.style.transform = 'translateY(0)';
  });
  setTimeout(function() {
    e.style.opacity = '0';
    e.style.transform = 'translateY(-20px)';
    setTimeout(function() { if (e.parentNode) e.remove(); }, 300);
  }, 3000);
}

// =============================================
// CALCULO PRINCIPAL
// =============================================
function calc() {
  var b = Math.max(0, parseFloat(billIn.value) || 0);
  var tp = Math.max(0, Math.min(100, parseFloat(tipCu.value) || 0));
  var p = Math.max(1, Math.min(50, parseInt(pplIn.value) || 1));
  S.bill = b;
  S.tip = tp;
  S.ppl = p;
  var ta = b * (tp / 100);
  var tw = b + ta;
  var pp = tw / p;
  var ppn = b / p;
  eTip.textContent = '$' + ta.toFixed(2);
  eTot.textContent = '$' + tw.toFixed(2);
  ePP.textContent = '$' + pp.toFixed(2);
  dB.textContent = '$' + b.toFixed(2);
  dTP.textContent = tp;
  dT.textContent = '$' + ta.toFixed(2);
  dTo.textContent = '$' + tw.toFixed(2);
  dPN.textContent = '$' + ppn.toFixed(2);
  dPT.textContent = '$' + pp.toFixed(2);
  if (S.adv) { calcAdv(ta, tw); } else { pBr.classList.add('hidden'); }
  var sub = 0;
  for (var i = 0; i < S.items.length; i++) sub += S.items[i].price;
  itmS.textContent = sub.toFixed(2);
}

// =============================================
// DIVISION DESIGUAL (MODO AVANZADO)
// =============================================
function calcAdv(ta, tw) {
  pSh.innerHTML = '';
  if (S.split === 'percent') {
    var tot = 0;
    for (var i = 0; i < S.people.length; i++) tot += S.people[i].share;
    for (var i = 0; i < S.people.length; i++) {
      var pr = S.people[i].share;
      var pt = tw * (pr / 100);
      var d = document.createElement('div');
      d.className = 'person-share tile';
      d.innerHTML = '<span>' + S.people[i].name + ' (' + pr + '%)</span><span class="font-bold">$' + pt.toFixed(2) + '</span>';
      pSh.appendChild(d);
    }
    if (Math.abs(tot - 100) > 0.01) {
      var w = document.createElement('div');
      w.className = 'text-sm mt-sm';
      w.style.color = '#f59e0b';
      w.textContent = 'Suma: ' + tot.toFixed(1) + '% (debe ser 100%)';
      pSh.appendChild(w);
    }
  } else {
    var asg = 0;
    for (var i = 0; i < S.people.length; i++) {
      var am = S.people[i].share;
      asg += am;
      var d = document.createElement('div');
      d.className = 'person-share tile';
      d.innerHTML = '<span>' + S.people[i].name + '</span><span class="font-bold">$' + am.toFixed(2) + '</span>';
      pSh.appendChild(d);
    }
    var rem = tw - asg;
    if (rem > 0.01) {
      var d = document.createElement('div');
      d.className = 'person-share tile';
      d.style.opacity = '0.7';
      d.innerHTML = '<span>Sin asignar</span><span class="font-bold">$' + rem.toFixed(2) + '</span>';
      pSh.appendChild(d);
    }
  }
  pBr.classList.remove('hidden');
}

// =============================================
// RENDER LISTA DE PERSONAS
// =============================================
function renderPpl() {
  pplL.innerHTML = '';
  for (var i = 0; i < S.people.length; i++) {
    (function(idx) {
      var p = S.people[idx];
      var r = document.createElement('div');
      r.className = 'item-row';
      var ni = document.createElement('input');
      ni.type = 'text';
      ni.value = p.name;
      ni.style.flex = '1';
      ni.addEventListener('input', function(e) {
        p.name = e.target.value || 'Persona ' + (idx + 1);
        updSel();
      });
      var si = document.createElement('input');
      si.type = 'number';
      si.value = p.share;
      si.min = '0';
      si.step = S.split === 'percent' ? '1' : '0.01';
      si.style.width = '100px';
      si.addEventListener('input', function(e) {
        p.share = parseFloat(e.target.value) || 0;
        calc();
      });
      var rb = document.createElement('button');
      rb.className = 'btn btn-ghost';
      rb.textContent = 'X';
      rb.addEventListener('click', function() {
        if (S.people.length > 1) {
          S.people.splice(idx, 1);
          renderPpl();
          updSel();
          calc();
        } else {
          toast('Minimo una persona', 'warning');
        }
      });
      r.appendChild(ni);
      r.appendChild(si);
      r.appendChild(rb);
      pplL.appendChild(r);
    })(i);
  }
}

// =============================================
// RENDER LISTA DE ITEMS
// =============================================
function renderItm() {
  itmL.innerHTML = '';
  for (var i = 0; i < S.items.length; i++) {
    (function(idx) {
      var it = S.items[idx];
      var r = document.createElement('div');
      r.className = 'item-row';
      var ns = document.createElement('span');
      ns.textContent = it.name;
      ns.style.flex = '1';
      var ps = document.createElement('span');
      ps.textContent = '$' + it.price.toFixed(2);
      ps.className = 'font-bold';
      var cs = document.createElement('span');
      cs.textContent = it.pName || 'Todos';
      cs.className = 'text-sm';
      var rb = document.createElement('button');
      rb.className = 'btn btn-ghost';
      rb.textContent = 'X';
      rb.addEventListener('click', function() {
        S.items.splice(idx, 1);
        renderItm();
        calc();
      });
      r.appendChild(ns);
      r.appendChild(ps);
      r.appendChild(cs);
      r.appendChild(rb);
      itmL.appendChild(r);
    })(i);
  }
}

// =============================================
// ACTUALIZAR SELECT DE PERSONAS PARA ITEMS
// =============================================
function updSel() {
  var cv = itmPe.value;
  itmPe.innerHTML = '<option value="">Todos</option>';
  for (var i = 0; i < S.people.length; i++) {
    var o = document.createElement('option');
    o.value = S.people[i].id;
    o.textContent = S.people[i].name;