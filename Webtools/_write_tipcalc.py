import pathlib
p = pathlib.Path(r'C:/Users/nicol/OneDrive/Documents/ClaudeCode/Another Store/Webtools/TipCalc.html')
parts = []
parts.append(r'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TipCalc — Calculadora de propinas</title>
<style>
:root{--cDeep:#07405E;--cInk:#0B5C8A;--cBlue2:#1F86C8;--cGreen2:#4CA22B;--cAmber2:#E08C1E;--cRed2:#C63C22;--Muted:#2C5F7E;--shadow:0 2px 16px rgba(10,58,86,.28)}
*{box-sizing:border-box;margin:0;padding:0}html,body{height:100%}
body{font-family:"Segoe UI",system-ui,sans-serif;color:var(--cDeep);background:linear-gradient(0deg,rgba(151,220,95,.85) 0%,rgba(103,208,196,.82) 18%,rgba(77,187,236,.82) 40%,rgba(149,217,246,.85) 70%,rgba(227,244,253,.89) 100%),linear-gradient(105deg,#E3F4FD 0%,#95D9F6 30%,#4DBBEC 60%,#67D0C4 82%,#97DC5F 100%);background-blend-mode:normal;min-height:100vh;overflow-x:hidden}
body::before{content:"";position:fixed;top:0;left:0;right:0;height:170px;pointer-events:none;z-index:0;background:linear-gradient(180deg,rgba(255,255,255,.63) 0%,rgba(255,255,255,.26) 55%,transparent 100%)}
.bubble{position:fixed;border-radius:50%;pointer-events:none;z-index:0;background:radial-gradient(circle at 35% 30%,#fff 0%,var(--t) 58%,transparent 100%)}
.b1{width:300px;height:300px;left:-70px;top:38%;opacity:.30;--t:rgba(111,199,240,.9)}.b2{width:380px;height:380px;right:-90px;top:-110px;opacity:.26;--t:rgba(182,231,122,.9)}.b3{width:180px;height:180px;left:52%;bottom:-60px;opacity:.22;--t:rgba(255,217,122,.9)}
.window{position:relative;z-index:1;max-width:640px;margin:46px auto;padding:0 24px 60px}
.titlebar{display:flex;align-items:center;gap:12px;height:46px;padding:0 6px}
.titlebar .logo{width:26px;height:26px;border-radius:7px;background:linear-gradient(180deg,#8FD9F7 0%,#39A5DC 49%,#1B7FC0 51%,#39B0E4 100%);border:1px solid rgba(255,255,255,.55);box-shadow:var(--shadow);display:grid;place-items:center;color:#fff;font-size:14px;font-weight:600}
.titlebar h1{font-size:25px;font-weight:300;color:var(--cDeep)}.titlebar h1 b{font-weight:600}.titlebar .sub{margin-left:auto;font-size:12.5px;color:var(--Muted)}
.card{background:linear-gradient(180deg,rgba(255,255,255,.93) 0%,rgba(255,255,255,.77) 45%,rgba(235,248,255,.69) 100%);border:1px solid rgba(255,255,255,.5);border-radius:14px;padding:18px;box-shadow:var(--shadow);backdrop-filter:blur(12px);margin-bottom:18px}
h2{font-size:15px;font-weight:600;margin-bottom:10px;color:var(--cDeep)}
input[type="number"],input[type="text"]{height:40px;padding:0 12px;border-radius:8px;border:1px solid rgba(44,95,126,.30);background:rgba(255,255,255,.70);color:var(--cDeep);font-family:inherit;font-size:15px}
input:focus{outline:2px solid rgba(31,134,200,.45);outline-offset:-1px}
.amount-row{display:flex;align-items:center;gap:10px}.amount-row .cur{font-size:20px;font-weight:600;color:var(--cInk);width:34px;text-align:center;background:rgba(255,255,255,.45);border-radius:8px;height:40px;line-height:40px}
#amount{flex:1;font-size:19px;font-weight:600}.field-label{font-size:12.5px;color:var(--Muted);margin:12px 0 6px}
.row{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-top:12px}
.tipbtn{position:relative;height:40px;min-width:64px;padding:0 16px;border:none;border-radius:9px;font-family:inherit;font-size:14px;font-weight:600;color:#fff;cursor:pointer;overflow:hidden;box-shadow:var(--shadow),inset 0 0 0 1px rgba(255,255,255,.35);transition:transform .05s,filter .15s}
.tipbtn::before{content:"";position:absolute;inset:0;border-radius:8px;opacity:0;background:rgba(255,255,255,.24);transition:.15s}.tipbtn:hover::before{opacity:1}.tipbtn:active{transform:translateY(1px);filter:brightness(.92)}
.tipbtn .shine{position:absolute;left:1px;right:1px;top:1px;height:17px;border-radius:8px 8px 0 0;background:linear-gradient(180deg,rgba(255,255,255,.72) 0%,rgba(255,255,255,.22) 48%,transparent 50%);pointer-events:none}
.tipbtn-blue{background:linear-gradient(180deg,#8FD9F7 0%,#39A5DC 49%,#1B7FC0 51%,#39B0E4 100%)}
.tipbtn.selected{outline:3px solid rgba(74,162,43,.65);outline-offset:1px;background:linear-gradient(180deg,#CBF08F 0%,#74C23C 49%,#4E9C22 51%,#7FCF43 100%)}
.tipbtn.selected::after{content:"\2713";position:absolute;top:1px;right:5px;font-size:10px;opacity:.9}
#customTip{width:110px}
.slider-row{display:flex;align-items:center;gap:12px;margin-top:10px}.slider-row label{font-size:12.5px;color:var(--Muted);white-space:nowrap}
.slider-row input[type="range"]{flex:1;-webkit-appearance:none;appearance:none;height:6px;border-radius:3px;background:linear-gradient(90deg,#8FD9F7,#39A5DC,#1B7FC0);outline:none;cursor:pointer}
.slider-row input[type="range"]::-webkit-slider-thumb{-webkit-appearance:none;width:20px;height:20px;border-radius:50%;background:linear-gradient(180deg,#fff 0%,#E3F4FD 100%);border:2px solid #39A5DC;box-shadow:0 2px 6px rgba(10,58,86,.3);cursor:pointer}
.slider-row input[type="range"]::-moz-range-thumb{width:20px;height:20px;border-radius:50%;background:linear-gradient(180deg,#fff 0%,#E3F4FD 100%);border:2px solid #39A5DC;box-shadow:0 2px 6px rgba(10,58,86,.3);cursor:pointer}
.slider-val{font-size:14px;font-weight:600;color:var(--cInk);min-width:42px;text-align:right}
.stepper{display:flex;align-items:center;gap:0}
.stepper button{width:40px;height:40px;border:none;cursor:pointer;font-size:18px;font-weight:600;color:#fff;box-shadow:var(--shadow),inset 0 0 0 1px rgba(255,255,255,.35);position:relative;overflow:hidden;transition:filter .15s}
.stepper button::before{content:"";position:absolute;inset:0;opacity:0;transition:.15s;background:rgba(255,255,255,.24)}.stepper button:hover::before{opacity:1}.stepper button:active{filter:brightness(.92)}
.stepper button:disabled{opacity:.45;cursor:default}.stepper button:disabled::before{opacity:0}
.stepper button .shine{position:absolute;left:1px;right:1px;top:1px;height:17px;border-radius:7px 7px 0 0;background:linear-gradient(180deg,rgba(255,255,255,.72) 0%,rgba(255,255,255,.22) 48%,transparent 50%);pointer-events:none}
.stepper .minus{border-radius:8px 0 0 8px;background:linear-gradient(180deg,#FFB6A6 0%,#DD5C3E 49%,#B63B22 51%,#E0704F 100%)}
.stepper .plus{border-radius:0 8px 8px 0;background:linear-gradient(180deg,#CBF08F 0%,#74C23C 49%,#4E9C22 51%,#7FCF43 100%)}
.stepper .val{width:70px;height:40px;display:grid;place-items:center;font-size:17px;font-weight:600;background:rgba(255,255,255,.70);border-top:1px solid rgba(44,95,126,.30);border-bottom:1px solid rgba(44,95,126,.30)}
.results{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:6px}
.res{background:linear-gradient(180deg,rgba(255,255,255,.85) 0%,rgba(255,255,255,.55) 48%,rgba(235,248,255,.45) 52%,rgba(255,255,255,.65) 100%);border:1px solid rgba(255,255,255,.6);border-radius:12px;padding:14px 10px;text-align:center;box-shadow:var(--shadow);backdrop-filter:blur(10px);position:relative;overflow:hidden;transition:transform .15s,box-shadow .15s}
.res:hover{transform:translateY(-2px);box-shadow:0 6px 20px rgba(10,58,86,.32)}
.res::before{content:"";position:absolute;left:0;right:0;top:0;height:14px;background:linear-gradient(180deg,rgba(255,255,255,.7),transparent);pointer-events:none}
.res::after{content:"";position:absolute;left:0;top:0;bottom:0;width:4px;pointer-events:none;background:linear-gradient(180deg,var(--accent,#1F86C8),rgba(255,255,255,.25));opacity:.85}
.res .lbl{font-size:11.5px;color:var(--Muted);text-transform:uppercase;letter-spacing:.4px;line-height:1.35}
.res .num{font-size:22px;font-weight:600;margin-top:6px;word-break:break-all;font-variant-numeric:tabular-nums;color:var(--cInk)}
.res.t-blue{--accent:var(--cBlue2)}.res.t-blue .num{color:var(--cBlue2)}
.res.t-green{--accent:var(--cGreen2)}.res.t-green .num{color:var(--cGreen2)}
.res.t-amber{--accent:var(--cAmber2)}.res.t-amber .num{color:var(--cAmber2)}
.res.total{border:1px solid rgba(116,194,60,.55);background:linear-gradient(180deg,rgba(233,248,215,.85) 0%,rgba(255,255,255,.62) 45%,rgba(226,244,206,.55) 100%)}
.res.total .num{color:var(--cGreen2);font-size:24px}
.res.total::after{content:"";position:absolute;left:0;right:0;top:0;height:4px;width:100%;background:linear-gradient(90deg,transparent,rgba(116,194,60,.7),transparent);opacity:1}
.breakdown{margin-top:14px;padding:12px 14px;border-radius:10px;background:linear-gradient(180deg,rgba(255,255,255,.60) 0%,rgba(235,248,255,.40) 100%);border:1px solid rgba(255,255,255,.40);font-size:13px;color:var(--cDeep)}
.breakdown .bk-row{display:flex;justify-content:space-between;padding:4px 0}.breakdown .bk-row+.bk-row{border-top:1px dashed rgba(44,95,126,.15)}
.breakdown .bk-label{color:var(--Muted)}.breakdown .bk-val{font-weight:600;color:var(--cInk)}
.btn{position:relative;height:40px;padding:0 22px;border:none;border-radius:9px;font-family:inherit;font-size:13.5px;color:#fff;cursor:pointer;overflow:hidden;box-shadow:var(--shadow),inset 0 0 0 1px rgba(255,255,255,.35);transition:transform .05s,filter .15s}
.btn::before{content:"";position:absolute;inset:0;border-radius:8px;opacity:0;background:rgba(255,255,255,.24);transition:.15s}.btn:hover::before{opacity:1}.btn:active{transform:translateY(1px);filter:brightness(.92)}
.btn .shine{position:absolute;left:1px;right:1px;top:1px;height:17px;border-radius:8px 8px 0 0;background:linear-gradient(180deg,rgba(255,255,255,.72) 0%,rgba(255,255,255,.22) 48%,transparent 50%);pointer-events:none}
.btn-green{background:linear-gradient(180deg,#CBF08F 0%,#74C23C 49%,#4E9C22 51%,#7FCF43 100%)}
.btn-blue{background:linear-gradient(180deg,#8FD9F7 0%,#39A5DC 49%,#1B7FC0 51%,#39B0E4 100%)}
.toast{position:fixed;bottom:24px;left:50%;transform:translateX(-50%) translateY(20px);opacity:0;pointer-events:none;z-index:999;background:linear-gradient(180deg,rgba(255,255,255,.95) 0%,rgba(235,248,255,.88) 100%);border:1px solid rgba(255,255,255,.6);border-radius:10px;padding:12px 22px;box-shadow:0 4px 20px rgba(10,58,86,.30);backdrop-filter:blur(12px);font-size:13.5px;color:var(--cDeep);font-weight:500;transition:opacity .25s,transform .25s}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0);pointer-events:auto}
.history-list{list-style:none;margin-top:8px}
.history-list li{display:flex;justify-content:space-between;align-items:center;padding:8px 12px;border-radius:8px;margin-bottom:6px;font-size:13px;background:linear-gradient(180deg,rgba(255,255,255,.70) 0%,rgba(235,248,255,.50) 100%);border:1px solid rgba(255,255,255,.45);color:var(--cDeep);cursor:pointer;transition:background .15s,transform .1s}
.history-list li:hover{background:linear-gradient(180deg,rgba(255,255,255,.88) 0%,rgba(220,242,255,.70) 100%);transform:translateX(2px)}
.history-list li .h-detail{font-weight:600;color:var(--cInk)}.history-list li .h-meta{font-size:11.5px;color:var(--Muted)}
.history-empty{font-size:13px;color:var(--Muted);text-align:center;padding:12px 0;cursor:default!important}
.history-empty:hover{background:transparent!important;transform:none!important}
.actions{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px}
@media(max-width:520px){.window{margin:24px auto;padding:0 14px 40px}.results{grid-template-columns:1fr;gap:10px}.titlebar h1{font-size:20px}.tipbtn{min-width:52px;padding:0 12px;font-size:13px}}
</style>
</head>
<body>
<div class="bubble b1"></div><div class="bubble b2"></div><div class="bubble b3"></div>
<div class="window">
<div class="titlebar"><div class="logo">$</div><h1>Tip<b>Calc</b></h1><span class="sub">Calculadora de propinas</span></div>
''')
parts.append(r'''
<div class="card">
<h2>Monto de la cuenta</h2>
<div class="amount-row"><span class="cur">$</span><input type="number" id="amount" placeholder="0.00" min="0" step="0.01"></div>
<div class="field-label">Porcentaje de propina</div>
<div class="row" id="tipButtons">
<button class="tipbtn tipbtn-blue" data-tip="10"><span class="shine"></span>10%</button>
<button class="tipbtn tipbtn-blue selected" data-tip="15"><span class="shine"></span>15%</button>
<button class="tipbtn tipbtn-blue" data-tip="18"><span class="shine"></span>18%</button>
<button class="tipbtn tipbtn-blue" data-tip="20"><span class="shine"></span>20%</button>
<button class="tipbtn tipbtn-blue" data-tip="25"><span class="shine"></span>25%</button>
<input type="number" id="customTip" placeholder="Otro %" min="0" max="100" step="1">
</div>
<div class="slider-row"><label>Propina:</label><input type="range" id="tipSlider" min="0" max="50" value="15" step="1"><span class="slider-val" id="sliderVal">15%</span></div>
<div class="field-label">Numero de personas</div>
<div class="stepper">
<button class="minus" id="pplMinus"><span class="shine"></span>-</button>
<div class="val" id="pplVal">1</div>
<button class="plus" id="pplPlus"><span class="shine"></span>+</button>
</div>
</div>
''')
parts.append(r'''
<div class="card">
<h2>Resultados</h2>
<div class="results">
<div class="res t-blue"><div class="lbl">Propina</div><div class="num" id="resTip">$0.00</div></div>
<div class="res total t-green"><div class="lbl">Total</div><div class="num" id="resTotal">$0.00</div></div>
<div class="res t-amber"><div class="lbl">Por persona</div><div class="num" id="resPerson">$0.00</div></div>
</div>
<div class="breakdown" id="breakdown">
<div class="bk-row"><span class="bk-label">Subtotal</span><span class="bk-val" id="bkSub">$0.00</span></div>
<div class="bk-row"><span class="bk-label">Propina</span><span class="bk-val" id="bkTip">$0.00</span></div>
<div class="bk-row"><span class="bk-label">Total</span><span class="bk-val" id="bkTotal">$0.00</span></div>
<div class="bk-row"><span class="bk-label">Subtotal / persona</span><span class="bk-val" id="bkSubP">$0.00</span></div>
<div class="bk-row"><span class="bk-label">Total / persona</span><span class="bk-val" id="bkTotalP">$0.00</span></div>
</div>
<div class="actions">
<button class="btn btn-blue" id="btnCopy"><span class="shine"></span>Copiar resumen</button>
<button class="btn btn-green" id="btnClearHist"><span class="shine"></span>Borrar historial</button>
</div>
</div>
''')
parts.append(r'''
<div class="card">
<h2>Historial (ultimos 5)</h2>
<ul class="history-list" id="histList"><li class="history-empty">Sin calculos recientes</li></ul>
</div>
</div>
<div class="toast" id="toast"></div>
<script>
/* === TipCalc - JavaScript funcional completo === */
(function(){
"use strict";

/* --- Referencias DOM --- */
const $=id=>document.getElementById(id);
const amountInput=$("amount");
const tipBtns=document.querySelectorAll(".tipbtn[data-tip]");
const customTipInput=$("customTip");
const tipSlider=$("tipSlider");
const sliderVal=$("sliderVal");
const pplMinus=$("pplMinus");
const pplPlus=$("pplPlus");
const pplVal=$("pplVal");
const resTip=$("resTip");
const resTotal=$("resTotal");
const resPerson=$("resPerson");
const bkSub=$("bkSub");
const bkTip=$("bkTip");
const bkTotal=$("bkTotal");
const bkSubP=$("bkSubP");
const bkTotalP=$("bkTotalP");
const btnCopy=$("btnCopy");
const btnClearHist=$("btnClearHist");
const histList=$("histList");
const toastEl=$("toast");

/* --- Estado --- */
let tipPercent=15;
let people=1;
const HIST_KEY="tipcalc_history";
const MAX_HIST=5;

/* --- Formateo de moneda segun locale del navegador --- */
const fmt=new Intl.NumberFormat(undefined,{style:"currency",currency:"USD",minimumFractionDigits:2,maximumFractionDigits:2});
/* Detectar simbolo de moneda del locale */
function getCurSymbol(){try{const p=new Intl.NumberFormat(undefined,{style:"currency",currency:"USD"}).formatToParts(0);const s=p.find(x=>x.type==="currency");return s?s.value:"$";}catch(e){return "$";"}}
const CUR=getCurSymbol();
/* Actualizar simbolo en UI */
document.querySelector(".amount-row .cur").textContent=CUR;

function formatMoney(n){return fmt.format(n);}

/* --- Toast notifications --- */
let toastTimer=null;
function showToast(msg,type){
type=type||"info";
toastEl.textContent=msg;
toastEl.className="toast show";
if(type==="error")toastEl.style.borderLeft="4px solid var(--cRed2)";
else if(type==="success")toastEl.style.borderLeft="4px solid var(--cGreen2)";
else toastEl.style.borderLeft="4px solid var(--cBlue2)";
clearTimeout(toastTimer);
toastTimer=setTimeout(()=>{toastEl.classList.remove("show");},2500);
}

/* --- Validacion --- */
function parseAmount(){
const v=parseFloat(amountInput.value);
if(isNaN(v)||v<0)return 0;
return v;
}

/* --- Calculo principal --- */
function calcular(){
const monto=parseAmount();
const propina=monto*(tipPercent/100);
/* Correccion floating point */
const total=Math.round((monto+propina)*100)/100;
const subPer=Math.round((monto/people)*100)/100;
const totalPer=Math.round((total/people)*100)/100;
const propinaR=Math.round(propina*100)/100;

resTip.textContent=formatMoney(propinaR);
resTotal.textContent=formatMoney(total);
resPerson.textContent=formatMoney(totalPer);
bkSub.textContent=formatMoney(monto);
bkTip.textContent=formatMoney(propinaR);
bkTotal.textContent=formatMoney(total);
bkSubP.textContent=formatMoney(subPer);
bkTotalP.textContent=formatMoney(totalPer);

/* Guardar en historial si hay monto valido */
if(monto>0){
guardarHistorial(monto,tipPercent,people,propinaR,total,totalPer);
}
}

/* --- Historial localStorage --- */
function getHistorial(){
try{return JSON.parse(localStorage.getItem(HIST_KEY))||[];}catch(e){return[];}
}
function guardarHistorial(monto,pct,ppl,prop,total,perPerson){
const hist=getHistorial();
const entry={monto:+monto.toFixed(2),pct:pct,ppl:ppl,prop:+prop.toFixed(2),total:+total.toFixed(2),per:+perPerson.toFixed(2),ts:Date.now()};
/* Evitar duplicados consecutivos identicos */
if(hist.length>0){
const last=hist[0];
if(last.monto===entry.monto&&last.pct===entry.pct&&last.ppl===entry.ppl)return;
}
hist.unshift(entry);
if(hist.length>MAX_HIST)hist.length=MAX_HIST;
localStorage.setItem(HIST_KEY,JSON.stringify(hist));
renderHistorial();
}
function renderHistorial(){
const hist=getHistorial();
if(hist.length===0){
histList.innerHTML='<li class="history-empty">Sin calculos recientes</li>';
return;
}
let html="";
for(let i=0;i<hist.length;i++){
const h=hist[i];
const fecha=new Date(h.ts);
const hora=fecha.toLocaleTimeString(undefined,{hour:"2-digit",minute:"2-digit"});
const dia=fecha.toLocaleDateString(undefined,{day:"numeric",month:"short"});
html+='<li data-idx="'+i+'">';
html+='<span class="h-detail">'+formatMoney(h.monto)+' + '+h.pct+'% = '+formatMoney(h.total)+'</span>';
html+='<span class="h-meta">'+dia+' '+hora+' | '+h.ppl+' pers.</span>';
html+='</li>';
}
histList.innerHTML=html;
/* Click para restaurar */
histList.querySelectorAll("li:not(.history-empty)").forEach(li=>{
li.addEventListener("click",()=>{
const idx=parseInt(li.getAttribute("data-idx"),10);
const h=hist[idx];
if(!h)return;
amountInput.value=h.monto;
setTipPercent(h.pct);
people=h.ppl;
pplVal.textContent=people;
actualizarStepperUI();
calcular();
showToast("Calculo restaurado","success");
});
});
}

/* --- Tip percent management --- */
function setTipPercent(pct){
tipPercent=pct;
/* Sync UI */
tipBtns.forEach(b=>{
b.classList.toggle("selected",parseInt(b.getAttribute("data-tip"),10)===pct);
});
tipSlider.value=pct;
sliderVal.textContent=pct+"%";
customTipInput.value=(pct!==10&&pct!==15&&pct!==18&&pct!==20&&pct!==25)?pct:"";
}

/* --- Event listeners --- */
amountInput.addEventListener("input",calcular);

tipBtns.forEach(btn=>{
btn.addEventListener("click",()=>{
const pct=parseInt(btn.getAttribute("data-tip"),10);
setTipPercent(pct);
customTipInput.value="";
calcular();
});
});

customTipInput.addEventListener("input",()=>{
const v=parseFloat(customTipInput.value);
if(!isNaN(v)&&v>=0&&v<=100){
tipPercent=v;
tipBtns.forEach(b=>b.classList.remove("selected"));
tipSlider.value=v;
sliderVal.textContent=v+"%";
calcular();
}else if(customTipInput.value===""){
/* No cambiar nada si se borra */
}
});

tipSlider.addEventListener("input",()=>{
const v=parseInt(tipSlider.value,10);
tipPercent=v;
sliderVal.textContent=v+"%";
tipBtns.forEach(b=>{
b.classList.toggle("selected",parseInt(b.getAttribute("data-tip"),10)===v);
});
customTipInput.value=(v!==10&&v!==15&&v!==18&&v!==20&&v!==25)?v:"";
calcular();
});

/* --- Stepper personas --- */
function actualizarStepperUI(){
pplVal.textContent=people;
pplMinus.disabled=people<=1;
}
pplMinus.addEventListener("click",()=>{
if(people>1){people--;actualizarStepperUI();calcular();}
});
pplPlus.addEventListener("click",()=>{
if(people<99){people++;actualizarStepperUI();calcular();}
});

/* --- Copiar resumen --- */
btnCopy.addEventListener("click",()=>{
const monto=parseAmount();
if(monto<=0){showToast("Ingresa un monto primero","error");return;}
const propina=monto*(tipPercent/100);
const total=Math.round((monto+propina)*100)/100;
const perP=Math.round((total/people)*100)/100;
const lines=[
"TipCalc - Resumen",
"Subtotal: "+formatMoney(monto),
"Propina ("+tipPercent+"%): "+formatMoney(Math.round(propina*100)/100),
"Total: "+formatMoney(total),
"Personas: "+people,
"Por persona: "+formatMoney(perP)
];
const text=lines.join("\n");
if(navigator.clipboard&&navigator.clipboard.writeText){
navigator.clipboard.writeText(text).then(()=>{
showToast("Resumen copiado al portapapeles","success");
}).catch(()=>{
fallbackCopy(text);
});
}else{
fallbackCopy(text);
}
});

function fallbackCopy(text){
const ta=document.createElement("textarea");
ta.value=text;
ta.style.position="fixed";
ta.style.left="-9999px";
document.body.appendChild(ta);
ta.select();
try{document.execCommand("copy");showToast("Resumen copiado (fallback)","success");}
catch(e){showToast("No se pudo copiar","error");}
document.body.removeChild(ta);
}

/* --- Borrar historial --- */
btnClearHist.addEventListener("click",()=>{
localStorage.removeItem(HIST_KEY);
renderHistorial();
showToast("Historial borrado","info");
});

/* --- Inicializacion --- */
actualizarStepperUI();
renderHistorial();
calcular();

})();
</script>
</body>
</html>
''')

html = "".join(parts)
p.write_text(html, encoding="utf-8")
print("DONE", len(html))