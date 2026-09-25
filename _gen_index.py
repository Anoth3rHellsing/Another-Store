import pathlib

html = r'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Another Store — Making Internet Funny Again</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
html{height:100%;scroll-behavior:smooth}
body{min-height:100%;font-family:'Nunito','Segoe UI',sans-serif;-webkit-font-smoothing:antialiased;overflow-x:hidden;color:#07405E;background:linear-gradient(135deg,#EAF6FF 0%,#D0ECFB 25%,#A8DCF4 50%,#B8E8D0 75%,#D4F1E8 100%);background-attachment:fixed}
#particleCanvas{position:fixed;top:0;left:0;width:100%;height:100%;z-index:0;pointer-events:none}
.aurora-wrap{position:fixed;top:0;left:0;width:100%;height:100%;z-index:0;pointer-events:none;overflow:hidden}
.aurora-wave{position:absolute;width:200%;height:300px;opacity:.18;filter:blur(40px);animation:auroraDrift 25s ease-in-out infinite alternate}
.aurora-wave:nth-child(1){top:-80px;left:-50%;background:linear-gradient(90deg,transparent,#7EC8E3,#B6E77A,transparent);animation-duration:28s}
.aurora-wave:nth-child(2){top:30%;left:-30%;background:linear-gradient(90deg,transparent,#A8DCF4,#D4B8FF,transparent);animation-duration:35s;animation-delay:-8s;opacity:.12}
.aurora-wave:nth-child(3){bottom:-60px;left:-40%;background:linear-gradient(90deg,transparent,#B8E8D0,#8FD9F7,transparent);animation-duration:22s;animation-delay:-15s;opacity:.15}
@keyframes auroraDrift{0%{transform:translateX(-10%) rotate(-2deg)}100%{transform:translateX(10%) rotate(2deg)}}
@keyframes fadeUp{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:translateY(0)}}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-12px)}}
@keyframes pulse{0%,100%{opacity:.22}50%{opacity:.35}}
@keyframes visBar{0%{height:3px}100%{height:14px}}
@keyframes sheenSlide{0%{left:-100%}100%{left:200%}}
.anim-up{animation:fadeUp .7s ease-out both}
.anim-fade{animation:fadeIn .6s ease-out both}
.d1{animation-delay:.1s}.d2{animation-delay:.2s}.d3{animation-delay:.3s}.d4{animation-delay:.4s}.d5{animation-delay:.5s}.d6{animation-delay:.6s}
.top-gloss{position:fixed;top:0;left:0;right:0;height:200px;z-index:0;pointer-events:none;background:linear-gradient(to bottom,rgba(255,255,255,.68) 0%,rgba(255,255,255,.30) 50%,transparent 100%)}
.light-streak{position:fixed;z-index:0;pointer-events:none;border-radius:50%;filter:blur(60px)}
.light-streak.ls1{width:500px;height:500px;top:-120px;right:-100px;background:radial-gradient(circle,rgba(143,217,247,.35),transparent 70%);animation:pulse 8s ease-in-out infinite}
.light-streak.ls2{width:400px;height:400px;bottom:10%;left:-80px;background:radial-gradient(circle,rgba(182,231,122,.25),transparent 70%);animation:pulse 10s ease-in-out infinite 3s}
.bubble{position:fixed;border-radius:50%;pointer-events:none;z-index:0}
.bubble-lg{width:320px;height:320px;left:-70px;top:38%;opacity:.30;background:radial-gradient(circle at 35% 30%,#fff 0%,#BFE9FB 55%,transparent 100%);animation:pulse 6s ease-in-out infinite}
.bubble-md{width:400px;height:400px;right:-90px;top:-70px;opacity:.26;background:radial-gradient(circle at 35% 30%,#fff 0%,#A8DCF4 58%,transparent 100%);animation:pulse 8s ease-in-out infinite 1s}
.bubble-sm{width:190px;height:190px;left:42%;bottom:4%;opacity:.22;background:radial-gradient(circle at 35% 30%,#fff 0%,#B6E77A 60%,transparent 100%);animation:float 7s ease-in-out infinite}
.bubble-xs{width:120px;height:120px;right:15%;top:55%;opacity:.18;background:radial-gradient(circle at 35% 30%,#fff 0%,#D4F1E8 60%,transparent 100%);animation:float 9s ease-in-out infinite 2s}
.page{position:relative;z-index:1;max-width:1020px;margin:0 auto;padding:40px 24px 80px}
.shop-header{text-align:center;margin-bottom:40px}
.shop-header h1{font-size:38px;font-weight:300;color:#07405E;letter-spacing:1px;margin-bottom:4px;text-shadow:0 1px 2px rgba(255,255,255,.8)}
.shop-header .slogan{font-size:15px;color:#0B5C8A;font-weight:500;letter-spacing:.8px;margin-bottom:18px;text-transform:uppercase}
.search-wrap{max-width:480px;margin:0 auto 12px;position:relative}
.search-input{width:100%;height:44px;padding:0 44px 0 20px;border-radius:22px;border:1px solid rgba(255,255,255,.5);background:rgba(255,255,255,.55);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);font-family:inherit;font-size:14px;color:#07405E;outline:none;transition:border-color .3s,box-shadow .3s,background .3s}
.search-input::placeholder{color:#2C5F7E;opacity:.6}
.search-input:focus{border-color:rgba(31,134,200,.6);background:rgba(255,255,255,.82);box-shadow:0 0 0 4px rgba(31,134,200,.12),0 0 20px rgba(31,134,200,.15)}
.search-icon{position:absolute;right:14px;top:50%;transform:translateY(-50%);width:18px;height:18px;fill:#2C5F7E;pointer-events:none;transition:fill .3s}
.search-input:focus~.search-icon{fill:#1F86C8}
.audio-bar{display:flex;align-items:center;justify-content:center;gap:10px;margin-top:14px}
.audio-btn{display:inline-flex;align-items:center;gap:6px;padding:6px 18px;border-radius:20px;border:1px solid rgba(255,255,255,.5);background:rgba(255,255,255,.45);color:#0B5C8A;font-size:12px;font-weight:600;cursor:pointer;backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);transition:background .2s,border-color .2s,transform .1s,box-shadow .3s}
.audio-btn:hover{background:rgba(255,255,255,.7);border-color:rgba(255,255,255,.8);box-shadow:0 2px 12px rgba(31,134,200,.15)}
.audio-btn:active{transform:scale(.96)}
.audio-vis{display:flex;align-items:end;gap:2px;height:14px}
.audio-vis span{display:block;width:3px;border-radius:2px;background:linear-gradient(to top,#39A5DC,#8FD9F7);animation:visBar .8s ease-in-out infinite alternate}
.audio-vis span:nth-child(1){height:6px;animation-delay:0s}
.audio-vis span:nth-child(2){height:12px;animation-delay:.15s}
.audio-vis span:nth-child(3){height:8px;animation-delay:.3s}
.audio-vis span:nth-child(4){height:14px;animation-delay:.1s}
.audio-vis span:nth-child(5){height:5px;animation-delay:.25s}
.audio-vis.paused span{animation:none;height:3px!important}
.section-title{font-size:18px;font-weight:400;color:#07405E;margin:44px 0 18px;padding-left:14px;border-left:4px solid #1F86C8;letter-spacing:.3px}
.carousel-wrap{position:relative;margin-bottom:12px}
.carousel{position:relative;border-radius:16px;overflow:hidden;box-shadow:0 4px 24px rgba(10,58,86,.25),inset 0 1px 0 rgba(255,255,255,.3);aspect-ratio:21/9;border:1px solid rgba(255,255,255,.35)}
.carousel-track{display:flex;transition:transform .6s cubic-bezier(.4,0,.2,1);height:100%}
.carousel-slide{min-width:100%;height:100%;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden;cursor:pointer}
.carousel-slide .slide-bg{position:absolute;inset:0;background-size:cover;background-position:center}
.carousel-slide .slide-content{position:relative;z-index:1;text-align:center;padding:32px;backdrop-filter:blur(2px);-webkit-backdrop-filter:blur(2px)}
.carousel-slide .slide-content h3{font-size:26px;font-weight:600;color:#fff;text-shadow:0 2px 16px rgba(0,0,0,.7),0 0 40px rgba(0,0,0,.4);margin-bottom:8px}
.carousel-slide .slide-content p{font-size:15px;font-weight:500;color:rgba(255,255,255,.92);text-shadow:0 1px 8px rgba(0,0,0,.6);max-width:520px;margin:0 auto;line-height:1.5}
.carousel-reflection{height:40px;margin-top:-2px;background:linear-gradient(to bottom,rgba(10,58,86,.08),transparent);border-radius:0 0 16px 16px;filter:blur(2px);opacity:.6;pointer-events:none}
.carousel-dots{display:flex;justify-content:center;gap:8px;margin-top:14px}
.carousel-dot{width:10px;height:10px;border-radius:50%;border:1px solid rgba(255,255,255,.6);background:rgba(255,255,255,.4);cursor:pointer;transition:all .3s}
.carousel-dot.active{background:#1F86C8;border-color:#1F86C8;transform:scale(1.25);box-shadow:0 0 8px rgba(31,134,200,.4)}
.carousel-nav{position:absolute;top:50%;transform:translateY(-50%);z-index:2;width:38px;height:38px;border-radius:50%;border:1px solid rgba(255,255,255,.5);background:rgba(255,255,255,.5);backdrop-filter:blur(8px);cursor:pointer;display:flex;align-items:center;justify-content:center;transition:background .2s,transform .15s,box-shadow .2s}
.carousel-nav:hover{background:rgba(255,255,255,.85);box-shadow:0 2px 12px rgba(10,58,86,.2)}
.carousel-nav:active{transform:translateY(-50%) scale(.9)}
.carousel-nav svg{width:16px;height:16px;fill:#07405E}
.carousel-prev{left:12px}.carousel-next{right:12px}
.channel-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px}
.channel-item{display:flex;align-items:center;gap:14px;padding:14px 16px;border-radius:14px;border:1px solid rgba(255,255,255,.55);background:linear-gradient(180deg,rgba(240,255,255,.95) 0%,rgba(225,248,255,.82) 45%,rgba(205,242,250,.95) 100%);box-shadow:0 2px 12px rgba(10,58,86,.18),inset 0 1px 0 rgba(255,255,255,.7);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);cursor:pointer;transition:transform .25s,box-shadow .25s;text-decoration:none;color:inherit;position:relative;overflow:hidden}
.channel-item::before{content:'';position:absolute;top:0;left:-100%;width:60%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.45),transparent);transform:skewX(-20deg);transition:none;pointer-events:none;z-index:2}
.channel-item:hover::before{animation:sheenSlide .7s ease-out}
.channel-item:hover{transform:translateY(-4px) scale(1.015);box-shadow:0 8px 28px rgba(10,58,86,.28),inset 0 1px 0 rgba(255,255,255,.9)}
.channel-item:active{transform:translateY(0) scale(.98)}
.channel-icon{flex-shrink:0;width:54px;height:54px;border-radius:12px;display:flex;align-items:center;justify-content:center;box-shadow:0 3px 10px rgba(10,58,86,.25),inset 0 1px 0 rgba(255,255,255,.45),inset 0 -1px 0 rgba(0,0,0,.08);position:relative;overflow:hidden;transition:box-shadow .25s}
.channel-item:hover .channel-icon{box-shadow:0 4px 14px rgba(10,58,86,.35),inset 0 1px 0 rgba(255,255,255,.5),inset 0 -1px 0 rgba(0,0,0,.1)}
.channel-icon::after{content:'';position:absolute;top:0;left:0;right:0;height:50%;background:linear-gradient(to bottom,rgba(255,255,255,.5) 0%,rgba(255,255,255,.05) 100%);border-radius:12px 12px 0 0;pointer-events:none}
.channel-icon svg{width:26px;height:26px;fill:#fff;position:relative;z-index:1}
.channel-icon img{width:38px;height:38px;object-fit:contain;position:relative;z-index:1}
.channel-icon.blue{background:linear-gradient(to bottom,#8FD9F7 0%,#39A5DC 49%,#1B7FC0 51%,#39B0E4 100%)}
.channel-icon.green{background:linear-gradient(to bottom,#CBF08F 0%,#74C23C 49%,#4E9C22 51%,#7FCF43 100%)}
.channel-icon.amber{background:linear-gradient(to bottom,#FFE6A8 0%,#F0A93A 49%,#D5871B 51%,#F7B950 100%)}
.channel-icon.red{background:linear-gradient(to bottom,#FFB6A6 0%,#DD5C3E 49%,#B63B22 51%,#E0704F 100%)}
.channel-icon.purple{background:linear-gradient(to bottom,#D4B8FF 0%,#8B5CF6 49%,#6D3FD4 51%,#A78BFA 100%)}
.channel-text{flex:1;min-width:0}
.channel-text h3{font-size:14.5px;font-weight:600;color:#07405E;margin-bottom:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;letter-spacing:.2px}
.channel-text p{font-size:12px;color:#2C5F7E;line-height:1.45;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.channel-arrow{flex-shrink:0;width:20px;height:20px;fill:#2C5F7E;opacity:.35;transition:opacity .25s,transform .25s}
.channel-item:hover .channel-arrow{opacity:.85;transform:translateX(4px)}
.news-list{display:flex;flex-direction:column;gap:12px}
.news-item{display:flex;gap:16px;align-items:flex-start;padding:16px 18px;border-radius:14px;border:1px solid rgba(255,255,255,.5);background:rgba(255,255,255,.42);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);transition:background .25s,transform .25s,box-shadow .25s;position:relative;overflow:hidden}
.news-item::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,rgba(255,255,255,.6),transparent);opacity:0;transition:opacity .25s}
.news-item:hover{background:rgba(255,255,255,.65);transform:translateX(5px);box-shadow:0 4px 16px rgba(10,58,86,.12)}
.news-item:hover::before{opacity:1}
.news-date{flex-shrink:0;text-align:center;min-width:52px}
.news-date .day{font-size:22px;font-weight:700;color:#1F86C8;line-height:1}
.news-date .month{font-size:11px;font-weight:600;color:#2C5F7E;text-transform:uppercase;letter-spacing:.5px;margin-top:2px}
.news-body{flex:1;min-width:0}
.news-body h4{font-size:14px;font-weight:600;color:#07405E;margin-bottom:4px;line-height:1.4}
.news-body p{font-size:12.5px;color:#2C5F7E;line-height:1.5}
.news-badge{display:inline-block;padding:2px 10px;border-radius:10px;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.5px;margin-bottom:6px;background:linear-gradient(135deg,#39A5DC,#1F86C8);color:#fff;box-shadow:0 2px 6px rgba(31,134,200,.3)}
footer{text-align:center;padding:40px 0 20px;font-size:12px;color:#2C5F7E;opacity:.7}
@media(max-width:640px){.shop-header h1{font-size:28px}.carousel{aspect-ratio:16/9}.carousel-slide .slide-content h3{font-size:20px}.channel-grid{grid-template-columns:1fr}.page{padding:24px 16px 60px}}
</style>
</head>
<body>
<canvas id="particleCanvas"></canvas>
<div class="aurora-wrap"><div class="aurora-wave"></div><div class="aurora-wave"></div><div class="aurora-wave"></div></div>
<div class="top-gloss"></div>
<div class="light-streak ls1"></div>
<div class="light-streak ls2"></div>
<div class="bubble bubble-lg"></div>
<div class="bubble bubble-md"></div>
<div class="bubble bubble-sm"></div>
<div class="bubble bubble-xs"></div>
<div class="page">
<header class="shop-header anim-up">
<h1>Another Store</h1>
<p class="slogan">Making Internet Funny Again</p>
<div class="search-wrap">
<input type="text" class="search-input" placeholder="Buscar apps, canales, herramientas..." aria-label="Buscar">
<svg class="search-icon" viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27A6.47 6.47 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.0