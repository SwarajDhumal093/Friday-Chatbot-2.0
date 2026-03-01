"""
FRIDAY AI  —  Single Python file
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 1. Set GROQ_API_KEY on line 7
 2. streamlit run friday.py
 3. Login: admin / friday
 Get free key → https://console.groq.com
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
import os
from dotenv import load_dotenv
load_dotenv()  # loads .env file automatically

# ↓↓↓ PASTE YOUR GROQ KEY HERE (for local VS Code use) ↓↓↓
_LOCAL_KEY = ""
# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "") or _LOCAL_KEY

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="FRIDAY AI", page_icon="🤖",
    layout="wide", initial_sidebar_state="collapsed"
)

st.markdown("""<style>
#MainMenu,footer,header,.stDeployButton,
[data-testid="collapsedControl"],
section[data-testid="stSidebar"]
{display:none!important;visibility:hidden!important}
.block-container,.stMainBlockContainer
{padding:0!important;max-width:100%!important;margin:0!important}
.stApp{overflow:hidden!important;background:#030008!important}
iframe{border:none!important}
</style>""", unsafe_allow_html=True)

_HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>FRIDAY AI</title>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;900&family=Share+Tech+Mono&family=Rajdhani:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/atom-one-dark.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;900&family=Share+Tech+Mono&family=Rajdhani:wght@300;400;500;600;700&display=swap');
:root{
  --r:#e63946;--r2:rgba(230,57,70,.12);--r3:rgba(230,57,70,.28);
  --bg:#030008;--pn:rgba(6,1,16,.98);--tx:#c8c8d4;--w:#f0f0ff;
  --g:#2ecc71;--sw:282px;
}
*{margin:0;padding:0;box-sizing:border-box}
html,body{height:100%;overflow:hidden;background:var(--bg);
  font-family:'Rajdhani',sans-serif;color:var(--tx)}
::-webkit-scrollbar{width:3px}
::-webkit-scrollbar-thumb{background:var(--r);border-radius:4px}
.bgr{position:fixed;inset:0;z-index:0;pointer-events:none;
  background-image:linear-gradient(rgba(230,57,70,.035)1px,transparent 1px),
    linear-gradient(90deg,rgba(230,57,70,.035)1px,transparent 1px);
  background-size:55px 55px;
  mask-image:radial-gradient(ellipse at 50% 50%,black 25%,transparent 72%)}
.scn{position:fixed;left:0;right:0;height:1px;z-index:1;pointer-events:none;
  background:linear-gradient(90deg,transparent,rgba(230,57,70,.4),transparent);
  animation:scanD 6s linear infinite}
@keyframes scanD{0%{top:-2%}100%{top:102%}}
@keyframes fUp{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:translateY(0)}}
@keyframes fIn{from{opacity:0}to{opacity:1}}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.1}}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes orbit{from{transform:rotate(0deg)translateX(32px)rotate(0deg)}
  to{transform:rotate(360deg)translateX(32px)rotate(-360deg)}}
@keyframes flt{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
@keyframes shim{0%{background-position:-300% center}100%{background-position:300% center}}
@keyframes glitch{0%,88%,100%{clip-path:inset(0 0 100% 0);transform:translate(0)}
  91%{clip-path:inset(18% 0 62% 0);transform:translate(-3px,0)}
  94%{clip-path:inset(55% 0 25% 0);transform:translate(3px,0)}
  97%{clip-path:inset(80% 0 5% 0);transform:translate(-2px,0)}}
@keyframes popIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
@keyframes typ{0%,60%,100%{transform:translateY(0)}30%{transform:translateY(-5px)}}
@keyframes glow{0%,100%{box-shadow:0 0 8px rgba(230,57,70,.18)}
  50%{box-shadow:0 0 22px rgba(230,57,70,.48)}}
@keyframes wave{0%,100%{transform:scaleY(.28)}50%{transform:scaleY(1)}}
@keyframes starT{0%,100%{opacity:.3}50%{opacity:1}}
@keyframes slIn{from{opacity:0;transform:translateX(-10px)}to{opacity:1;transform:translateX(0)}}

/* ── APP LAYOUT ── */
#app{display:flex;height:100vh;position:relative;z-index:2}

/* ── SIDEBAR ── */
#sb{width:var(--sw);flex-shrink:0;background:var(--pn);
  border-right:1px solid var(--r3);display:flex;flex-direction:column;
  height:100vh;overflow:hidden;transition:transform .28s cubic-bezier(.4,0,.2,1),width .28s}
#sb.off{transform:translateX(calc(-1*var(--sw)));width:0;min-width:0;border:none}
#sbt{position:fixed;top:50%;left:var(--sw);transform:translateY(-50%);
  width:22px;height:48px;z-index:20;cursor:pointer;
  background:rgba(230,57,70,.18);border:1px solid rgba(230,57,70,.45);
  border-left:none;border-radius:0 10px 10px 0;
  display:flex;align-items:center;justify-content:center;
  color:var(--r);font-size:.72rem;font-weight:900;
  transition:left .28s,background .18s;
  box-shadow:3px 0 14px rgba(230,57,70,.22);user-select:none}
#sbt:hover{background:rgba(230,57,70,.35)}
#sbt.off{left:0}
.sbi{flex:1;min-height:0;overflow-y:auto;overflow-x:hidden}
.sbb{padding:18px 14px 14px;border-bottom:1px solid rgba(230,57,70,.1);flex-shrink:0}
.sbt2{display:flex;align-items:center;gap:10px;margin-bottom:9px}
.ico{position:relative;width:38px;height:38px;flex-shrink:0;
  display:flex;align-items:center;justify-content:center}
.ico .e{font-size:1.4rem;filter:drop-shadow(0 0 9px rgba(230,57,70,.65));animation:flt 4s ease-in-out infinite}
.ico .rg{position:absolute;inset:0;border-radius:50%;border:1px dashed rgba(230,57,70,.3);animation:spin 9s linear infinite}
.ico .ob{position:absolute;width:5px;height:5px;background:var(--r);border-radius:50%;
  top:3px;left:50%;margin-left:-2.5px;box-shadow:0 0 6px var(--r);animation:orbit 2.5s linear infinite}
.sbn{font-family:'Orbitron',monospace;font-size:1.08rem;font-weight:900;color:#fff;
  letter-spacing:.2em;text-shadow:0 0 18px rgba(230,57,70,.5)}
.sbtg{font-family:'Share Tech Mono',monospace;font-size:.5rem;
  color:rgba(255,255,255,.22);letter-spacing:.13em;margin-top:1px}
.sbst{display:flex;align-items:center;gap:6px;margin-bottom:10px}
.sbsd{width:6px;height:6px;border-radius:50%;background:var(--g);
  box-shadow:0 0 7px var(--g);animation:pulse 1.8s infinite}
.sbst2{font-family:'Share Tech Mono',monospace;font-size:.55rem;
  color:rgba(46,204,113,.72);letter-spacing:.14em}
.sbdv{height:1px;background:linear-gradient(90deg,rgba(230,57,70,.3),transparent);margin:7px 0 9px}
.sbu{display:flex;align-items:center;gap:8px}
.sbav{width:29px;height:29px;border-radius:50%;background:var(--r2);
  border:1px solid rgba(230,57,70,.4);display:flex;align-items:center;
  justify-content:center;font-size:.82rem}
.sbun{font-family:'Orbitron',monospace;font-size:.62rem;color:#fff;letter-spacing:.1em}
.sbrl{font-family:'Share Tech Mono',monospace;font-size:.52rem;
  color:rgba(255,255,255,.26);margin-top:1px}
.sbs{padding:10px 13px 6px}
.sbl{font-family:'Orbitron',monospace;font-size:.52rem;font-weight:700;
  color:rgba(230,57,70,.78);letter-spacing:.2em;text-transform:uppercase;
  margin-bottom:6px;display:flex;align-items:center;gap:5px}
.sbl::before{content:'';width:4px;height:4px;border-radius:50%;
  background:var(--r);display:inline-block;box-shadow:0 0 5px var(--r)}
select{width:100%;padding:8px 10px;background:rgba(230,57,70,.06);
  border:1px solid rgba(230,57,70,.2);border-radius:8px;color:var(--w);
  font-family:'Rajdhani',sans-serif;font-size:.86rem;outline:none;
  cursor:pointer;transition:all .2s;appearance:none;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='6'%3E%3Cpath d='M0 0l5 6 5-6z' fill='%23e63946'/%3E%3C/svg%3E");
  background-repeat:no-repeat;background-position:right 10px center;
  background-color:rgba(230,57,70,.06)}
select option{background:#0d001a;color:#fff}
select:focus{border-color:var(--r);box-shadow:0 0 12px rgba(230,57,70,.22)}
.stg{display:grid;grid-template-columns:1fr 1fr;gap:5px;margin-top:4px}
.stc{background:rgba(230,57,70,.05);border:1px solid rgba(230,57,70,.14);
  border-radius:7px;padding:7px 8px;text-align:center}
.stv{font-family:'Orbitron',monospace;font-size:.92rem;font-weight:700;
  color:var(--r);text-shadow:0 0 10px rgba(230,57,70,.35)}
.stl{font-family:'Share Tech Mono',monospace;font-size:.48rem;
  color:rgba(255,255,255,.28);letter-spacing:.1em;margin-top:2px}
.sbtn{width:100%;padding:9px 12px;margin-bottom:5px;background:transparent;
  border:1px solid rgba(255,255,255,.07);border-radius:8px;
  color:rgba(255,255,255,.5);font-family:'Rajdhani',sans-serif;
  font-size:.8rem;font-weight:500;letter-spacing:.04em;cursor:pointer;
  transition:all .18s;text-align:left;display:flex;align-items:center;gap:7px}
.sbtn:hover{background:var(--r2);border-color:rgba(230,57,70,.4);color:#fff}
.sbtn.pr{background:rgba(230,57,70,.1);border:1px solid rgba(230,57,70,.32);
  color:#fff;font-family:'Orbitron',monospace;font-size:.68rem;
  letter-spacing:.1em;justify-content:center;animation:glow 3s infinite}
.sbtn.pr:hover{background:rgba(230,57,70,.22)}
.sbtn.dr:hover{background:rgba(255,50,50,.1);border-color:rgba(255,80,80,.4);color:#f88}
.sbdiv{margin:7px 13px;display:flex;align-items:center;gap:7px}
.sbdiv::before,.sbdiv::after{content:'';flex:1;height:1px;background:rgba(230,57,70,.16)}
.sbdiv span{font-family:'Orbitron',monospace;font-size:.46rem;
  color:rgba(230,57,70,.5);letter-spacing:.18em;white-space:nowrap}
.ssl{padding:3px 9px}
.ssi{padding:8px 10px;margin-bottom:4px;border-radius:8px;
  border:1px solid rgba(255,255,255,.05);cursor:pointer;
  transition:all .18s;display:flex;align-items:center;
  justify-content:space-between;animation:slIn .25s ease both}
.ssi:hover{background:var(--r2);border-color:rgba(230,57,70,.28)}
.ssi.ac{background:rgba(230,57,70,.08);border-color:rgba(230,57,70,.3);
  border-left:3px solid var(--r)}
.sti{font-family:'Rajdhani',sans-serif;font-size:.83rem;font-weight:600;
  color:rgba(255,255,255,.7);white-space:nowrap;overflow:hidden;
  text-overflow:ellipsis;flex:1}
.ssi.ac .sti{color:#fff}
.smeta{font-family:'Share Tech Mono',monospace;font-size:.52rem;
  color:rgba(230,57,70,.5);margin-top:2px}
.sdel{opacity:0;padding:2px 6px;background:transparent;border:none;
  color:rgba(255,100,100,.55);cursor:pointer;font-size:.72rem;
  transition:opacity .15s;flex-shrink:0}
.ssi:hover .sdel{opacity:1}
.semp{font-family:'Share Tech Mono',monospace;font-size:.6rem;
  color:rgba(255,255,255,.13);text-align:center;padding:12px 0;
  letter-spacing:.1em}
.sbft{padding:10px 13px;border-top:1px solid rgba(230,57,70,.1);display:flex;gap:7px;flex-shrink:0;background:var(--pn)}
.sbft .sbtn{margin:0;flex:1;justify-content:center;
  font-family:'Orbitron',monospace;font-size:.6rem;letter-spacing:.08em}

/* ── MAIN ── */
#main{flex:1;display:flex;flex-direction:column;overflow:hidden;min-width:0}
#hdr{padding:18px 30px 14px;border-bottom:1px solid rgba(230,57,70,.1);
  text-align:center;flex-shrink:0;
  background:linear-gradient(180deg,rgba(230,57,70,.025)0%,transparent 100%)}
.hst{display:flex;align-items:center;justify-content:center;gap:14px;margin-bottom:2px}
.hstr{font-size:.8rem;color:rgba(230,57,70,.4);animation:starT 2.5s ease-in-out infinite}
.hstr:last-child{animation-delay:1.1s}
#htit{font-family:'Orbitron',monospace;font-size:1.9rem;font-weight:900;
  letter-spacing:.12em;line-height:1;margin-bottom:6px;
  background:linear-gradient(90deg,#fff 0%,#e63946 35%,#fff 65%,#e63946 100%);
  background-size:300% auto;-webkit-background-clip:text;
  -webkit-text-fill-color:transparent;animation:shim 5s linear infinite}
#hsub{font-family:'Share Tech Mono',monospace;font-size:.6rem;
  color:rgba(255,255,255,.28);letter-spacing:.22em;
  text-transform:uppercase;margin-bottom:8px}
#hbdg{display:inline-flex;align-items:center;gap:6px;
  background:rgba(230,57,70,.06);border:1px solid rgba(230,57,70,.2);
  border-radius:20px;padding:4px 14px}
.bdt{width:5px;height:5px;border-radius:50%;background:var(--g);box-shadow:0 0 6px var(--g)}
#bdgt{font-family:'Share Tech Mono',monospace;font-size:.56rem;
  color:rgba(255,255,255,.42);letter-spacing:.08em}
#hscn{height:1px;margin-top:10px;
  background:linear-gradient(90deg,transparent,rgba(230,57,70,.35),rgba(230,57,70,.08),transparent)}
#msgs{flex:1;min-height:0;overflow-y:auto;overflow-x:hidden;padding:16px 30px 6px;
  display:flex;flex-direction:column;scroll-behavior:smooth}
#emp{flex:1;display:flex;flex-direction:column;align-items:center;
  justify-content:center;gap:12px;animation:fIn .8s ease}
.ei{position:relative;width:72px;height:72px;display:flex;align-items:center;
  justify-content:center;animation:flt 3.5s ease-in-out infinite}
.ei .e{font-size:2.4rem;opacity:.18;filter:drop-shadow(0 0 12px rgba(230,57,70,.4))}
.ei .rg{position:absolute;inset:0;border-radius:50%;
  border:1px dashed rgba(230,57,70,.18);animation:spin 12s linear infinite}
.el{font-family:'Orbitron',monospace;font-size:.55rem;
  color:rgba(230,57,70,.38);letter-spacing:.26em;text-transform:uppercase}
.es2{font-family:'Share Tech Mono',monospace;font-size:.65rem;
  color:rgba(255,255,255,.1);letter-spacing:.08em}
.mw{display:flex;gap:10px;margin-bottom:18px;animation:popIn .28s ease both}
.mw.u{flex-direction:row-reverse}
.mav{width:34px;height:34px;border-radius:50%;flex-shrink:0;margin-top:3px;
  display:flex;align-items:center;justify-content:center;font-size:.9rem}
.mw.u .mav{background:rgba(230,57,70,.1);border:1px solid rgba(230,57,70,.45);
  box-shadow:0 0 12px rgba(230,57,70,.18)}
.mw.ai .mav{background:#0c0a16;border:1px solid rgba(230,57,70,.38);
  box-shadow:0 0 14px rgba(230,57,70,.14)}
.mbd{max-width:70%}
.mw.u .mbd{display:flex;flex-direction:column;align-items:flex-end}
.mb{padding:11px 16px;line-height:1.72;font-size:.97rem;
  word-break:break-word;font-family:'Rajdhani',sans-serif}
.mw.u .mb{background:#fff;color:#111;font-weight:500;
  border-radius:18px 3px 18px 18px;box-shadow:0 4px 22px rgba(0,0,0,.5)}
.mw.ai .mb{background:rgba(10,6,22,.97);color:#e2e2e8;
  border-radius:3px 18px 18px 18px;
  border:1px solid rgba(230,57,70,.12);
  border-left:3px solid rgba(230,57,70,.62);
  box-shadow:0 4px 22px rgba(0,0,0,.4)}
.mt{font-family:'Share Tech Mono',monospace;font-size:.53rem;
  margin-top:4px;letter-spacing:.04em}
.mw.u .mt{color:rgba(255,255,255,.18);text-align:right}
.mw.ai .mt{color:rgba(230,57,70,.42)}
.mb strong{font-weight:700}.mb em{font-style:italic}
.mb code{background:rgba(230,57,70,.13);padding:2px 6px;border-radius:4px;
  font-family:'Share Tech Mono',monospace;font-size:.86em}
.mb pre{background:rgba(0,0,0,.35);border:1px solid rgba(230,57,70,.18);
  border-radius:8px;padding:10px 14px;overflow-x:auto;margin:8px 0}
.mb pre code{background:transparent;padding:0;font-size:.82em}
.mb ul,.mb ol{margin:5px 0 5px 18px;padding:0}
.mb li{margin-bottom:3px}
#typ{display:none;padding:0 30px 12px}
.tw{display:flex;gap:10px}
.tav{width:34px;height:34px;border-radius:50%;background:#0c0a16;
  border:1px solid rgba(230,57,70,.38);display:flex;align-items:center;
  justify-content:center;font-size:.9rem}
.tbu{background:rgba(10,6,22,.97);padding:13px 17px;
  border-radius:3px 18px 18px 18px;
  border:1px solid rgba(230,57,70,.12);
  border-left:3px solid rgba(230,57,70,.55)}
.tdt{display:flex;gap:5px;align-items:center;height:12px}
.td{width:5px;height:5px;background:var(--r);border-radius:50%;
  animation:typ 1s ease-in-out infinite}
.td:nth-child(2){animation-delay:.18s}.td:nth-child(3){animation-delay:.36s}

#inp{padding:7px 30px 16px;flex-shrink:0;
  background:linear-gradient(0deg,rgba(230,57,70,.02)0%,transparent 100%)}
#vrow{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:9px}
#wvb{display:none;align-items:flex-end;gap:3px;height:22px}
.wb{width:3px;background:var(--r);border-radius:2px;height:100%;
  transform:scaleY(.28);animation:wave .7s ease-in-out infinite}
#vbtn{display:flex;align-items:center;gap:8px;padding:8px 16px;
  background:rgba(230,57,70,.08);border:1px solid rgba(230,57,70,.28);
  border-radius:8px;color:var(--r);font-family:'Orbitron',monospace;
  font-size:.64rem;font-weight:600;letter-spacing:.12em;cursor:pointer;transition:all .2s}
#vbtn:hover{background:rgba(230,57,70,.16)}
#vbtn.rc{background:rgba(230,57,70,.2);border-color:var(--r);
  box-shadow:0 0 20px rgba(230,57,70,.45);animation:glow 1.5s infinite}
#vclr{display:none;padding:6px 10px;background:transparent;
  border:1px solid rgba(255,255,255,.07);border-radius:6px;
  color:rgba(255,255,255,.28);font-family:'Share Tech Mono',monospace;
  font-size:.6rem;cursor:pointer}
#vst{font-family:'Share Tech Mono',monospace;font-size:.6rem;
  color:rgba(230,57,70,.6);letter-spacing:.1em}
#vtx{display:none;margin-bottom:9px;padding:9px 13px;
  background:rgba(230,57,70,.04);border:1px solid rgba(230,57,70,.14);
  border-radius:8px;font-family:'Share Tech Mono',monospace;
  font-size:.8rem;color:#ccc;min-height:32px;line-height:1.6}
#mf{display:flex;gap:9px;align-items:flex-end}
#mi{flex:1;padding:12px 16px;min-height:50px;max-height:136px;
  background:rgba(255,255,255,.025);border:1px solid rgba(230,57,70,.14);
  border-radius:13px;color:var(--w);font-family:'Rajdhani',sans-serif;
  font-size:.97rem;font-weight:500;resize:none;outline:none;
  transition:all .24s;letter-spacing:.02em;line-height:1.5}
#mi:focus{border-color:var(--r);
  box-shadow:0 0 0 3px rgba(230,57,70,.1),0 0 18px rgba(230,57,70,.14)}
#mi::placeholder{color:rgba(255,255,255,.18);
  font-family:'Share Tech Mono',monospace;font-size:.78rem}
#sndb{width:50px;height:50px;flex-shrink:0;
  background:linear-gradient(135deg,#e63946,#c1121f);
  border:none;border-radius:12px;color:#fff;font-size:1.15rem;
  cursor:pointer;transition:all .2s;
  box-shadow:0 4px 18px rgba(230,57,70,.38);
  display:flex;align-items:center;justify-content:center}
#sndb:hover{background:linear-gradient(135deg,#ff4757,#e63946);
  box-shadow:0 4px 28px rgba(230,57,70,.62);transform:translateY(-2px)}
#sndb:disabled{opacity:.5;cursor:not-allowed;transform:none}

/* ── LOGIN ── */
#lgn{position:fixed;inset:0;z-index:100;
  background:radial-gradient(ellipse at 50% 40%,#0e0018 0%,#030008 100%);
  display:flex;flex-direction:column;align-items:center;justify-content:center}
.lc{position:fixed;width:30px;height:30px;opacity:.38}
.lc.tl{top:15px;left:15px;border-top:2px solid var(--r);border-left:2px solid var(--r)}
.lc.tr{top:15px;right:15px;border-top:2px solid var(--r);border-right:2px solid var(--r)}
.lc.bl{bottom:15px;left:15px;border-bottom:2px solid var(--r);border-left:2px solid var(--r)}
.lc.br{bottom:15px;right:15px;border-bottom:2px solid var(--r);border-right:2px solid var(--r)}
.lic{position:relative;width:86px;height:86px;display:flex;align-items:center;
  justify-content:center;margin-bottom:16px;
  animation:fUp .5s ease .1s both,flt 4s ease-in-out .6s infinite}
.lic .e{font-size:3rem;filter:drop-shadow(0 0 22px rgba(230,57,70,.7))}
.lic .r1{position:absolute;inset:0;border-radius:50%;
  border:1px dashed rgba(230,57,70,.33);animation:spin 8s linear infinite}
.lic .r2{position:absolute;inset:8px;border-radius:50%;
  border:1px dashed rgba(230,57,70,.14);animation:spin 5s linear infinite reverse}
.lic .ob{position:absolute;width:7px;height:7px;background:var(--r);
  border-radius:50%;top:4px;left:50%;margin-left:-3.5px;
  box-shadow:0 0 10px var(--r);animation:orbit 2.8s linear infinite}
.ltw{position:relative;animation:fUp .5s ease .2s both;margin-bottom:4px}
.lt{font-family:'Orbitron',monospace;font-size:3.6rem;font-weight:900;color:#fff;
  letter-spacing:.22em;text-align:center;
  text-shadow:0 0 40px rgba(230,57,70,.5),0 0 80px rgba(230,57,70,.18);
  position:relative;z-index:1}
.ltg{font-family:'Orbitron',monospace;font-size:3.6rem;font-weight:900;
  color:var(--r);letter-spacing:.22em;position:absolute;top:0;left:0;
  opacity:.28;animation:glitch 5s steps(1) infinite;pointer-events:none}
.lsub{font-family:'Share Tech Mono',monospace;color:rgba(230,57,70,.6);
  font-size:.62rem;letter-spacing:.3em;text-transform:uppercase;
  margin-bottom:7px;animation:fUp .5s ease .3s both;text-align:center}
.lbdg{display:flex;align-items:center;gap:7px;
  background:rgba(230,57,70,.07);border:1px solid rgba(230,57,70,.2);
  border-radius:20px;padding:5px 15px;margin-bottom:24px;
  animation:fUp .5s ease .35s both}
.lbdd{width:6px;height:6px;border-radius:50%;background:var(--g);
  box-shadow:0 0 7px var(--g);animation:pulse 1.8s infinite}
.lbdt{font-family:'Share Tech Mono',monospace;font-size:.58rem;
  color:rgba(255,255,255,.45);letter-spacing:.1em}
.lcard{width:368px;background:rgba(8,2,20,.96);
  border:1px solid rgba(230,57,70,.22);border-radius:14px;
  padding:28px 26px;position:relative;overflow:hidden;
  box-shadow:0 0 60px rgba(230,57,70,.09);animation:fUp .5s ease .4s both}
.lcard::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;
  background:linear-gradient(90deg,transparent,var(--r),transparent)}
.lhd{font-family:'Orbitron',monospace;font-size:.57rem;letter-spacing:.2em;
  color:rgba(230,57,70,.52);text-align:center;margin-bottom:20px}
.lfl{margin-bottom:13px}
.llbl{font-family:'Orbitron',monospace;font-size:.55rem;
  color:rgba(230,57,70,.8);letter-spacing:.16em;text-transform:uppercase;
  display:block;margin-bottom:5px}
.lin{width:100%;padding:11px 15px;background:rgba(255,255,255,.04);
  border:1px solid rgba(230,57,70,.22);border-radius:9px;color:#fff;
  font-family:'Share Tech Mono',monospace;font-size:.88rem;
  outline:none;transition:all .2s}
.lin:focus{border-color:var(--r);box-shadow:0 0 16px rgba(230,57,70,.28)}
.lbtn{width:100%;padding:12px;margin-top:6px;
  background:linear-gradient(135deg,#e63946,#c1121f);
  border:none;border-radius:9px;color:#fff;
  font-family:'Orbitron',monospace;font-weight:700;font-size:.75rem;
  letter-spacing:.2em;cursor:pointer;transition:all .2s;
  box-shadow:0 4px 22px rgba(230,57,70,.38)}
.lbtn:hover{box-shadow:0 4px 34px rgba(230,57,70,.62);transform:translateY(-2px)}
.lerr{display:none;margin-top:9px;padding:8px 13px;
  background:rgba(230,57,70,.08);border:1px solid rgba(230,57,70,.28);
  border-radius:7px;font-family:'Share Tech Mono',monospace;
  font-size:.73rem;color:var(--r);text-align:center;letter-spacing:.07em}
#toast{display:none;position:fixed;bottom:22px;right:22px;z-index:999;
  background:rgba(10,3,24,.96);border:1px solid rgba(230,57,70,.45);
  border-radius:10px;padding:11px 17px;font-family:'Share Tech Mono',monospace;
  font-size:.77rem;color:var(--r);max-width:380px;
  box-shadow:0 0 24px rgba(230,57,70,.25);
  display:none;align-items:center;justify-content:space-between;gap:10px}

/* ── DEVELOPER MODE TOGGLE ── */
#devtog{display:flex;align-items:center;gap:0;background:rgba(0,0,0,.3);
  border:1px solid rgba(230,57,70,.25);border-radius:20px;padding:3px;
  margin-left:auto;flex-shrink:0}
.dtb{padding:5px 14px;border-radius:16px;font-family:'Orbitron',monospace;
  font-size:.54rem;font-weight:700;letter-spacing:.1em;cursor:pointer;
  border:none;background:transparent;color:rgba(255,255,255,.35);
  transition:all .22s;white-space:nowrap}
.dtb.on{background:linear-gradient(135deg,#e63946,#c1121f);color:#fff;
  box-shadow:0 0 14px rgba(230,57,70,.45)}

/* ── DEV MODE CODE BLOCKS ── */
.dev-pre{position:relative;margin:10px 0;border-radius:10px;overflow:hidden;
  border:1px solid rgba(230,57,70,.2);box-shadow:0 4px 20px rgba(0,0,0,.4)}
.dev-hdr{display:flex;align-items:center;justify-content:space-between;
  padding:7px 14px;background:rgba(230,57,70,.08);
  border-bottom:1px solid rgba(230,57,70,.15)}
.dev-lang{font-family:'Orbitron',monospace;font-size:.5rem;
  color:rgba(230,57,70,.7);letter-spacing:.15em;text-transform:uppercase}
.dev-btns{display:flex;gap:6px}
.dev-btn{padding:4px 10px;border-radius:5px;font-family:'Share Tech Mono',monospace;
  font-size:.62rem;cursor:pointer;border:1px solid;transition:all .18s}
.dev-copy{background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.15);
  color:rgba(255,255,255,.55)}
.dev-copy:hover{background:rgba(255,255,255,.12);color:#fff}
.dev-copy.ok{background:rgba(46,204,113,.15);border-color:rgba(46,204,113,.4);
  color:#2ecc71}
.dev-pre code.hljs{padding:16px;font-size:.82rem;line-height:1.6;
  font-family:'Share Tech Mono',monospace;background:#0d1117!important}

/* ── MODE BADGE IN HEADER ── */
#modebdg{display:inline-flex;align-items:center;gap:5px;
  padding:3px 10px;border-radius:12px;font-family:'Orbitron',monospace;
  font-size:.48rem;letter-spacing:.12em;margin-left:8px;
  background:rgba(230,57,70,.08);border:1px solid rgba(230,57,70,.2);color:rgba(255,255,255,.35);
  transition:all .3s}
#modebdg.dev{background:rgba(230,57,70,.18);border-color:var(--r);
  color:var(--r);box-shadow:0 0 10px rgba(230,57,70,.2)}

/* ── MEMORY MODE ── */
#mem-panel{background:rgba(230,57,70,.04);border:1px solid rgba(230,57,70,.18);
  border-radius:10px;padding:10px 12px;margin:0 13px 6px}
#mem-panel .sbl{margin-bottom:7px;display:flex;align-items:center;justify-content:space-between}
#mem-list{display:flex;flex-direction:column;gap:4px;max-height:160px;overflow-y:auto;margin-bottom:8px}
.mem-item{display:flex;align-items:flex-start;gap:6px;padding:5px 8px;
  background:rgba(230,57,70,.07);border:1px solid rgba(230,57,70,.14);
  border-radius:7px;animation:slIn .2s ease both}
.mem-tag{font-family:'Orbitron',monospace;font-size:.42rem;font-weight:700;
  color:var(--r);letter-spacing:.1em;text-transform:uppercase;
  background:rgba(230,57,70,.15);border:1px solid rgba(230,57,70,.3);
  border-radius:4px;padding:2px 5px;white-space:nowrap;flex-shrink:0;margin-top:1px}
.mem-text{font-family:'Rajdhani',sans-serif;font-size:.78rem;color:rgba(255,255,255,.72);
  flex:1;line-height:1.4;word-break:break-word}
.mem-del{background:transparent;border:none;color:rgba(255,100,100,.4);
  cursor:pointer;font-size:.72rem;padding:0 2px;flex-shrink:0;
  transition:color .15s;line-height:1}
.mem-del:hover{color:rgba(255,100,100,.9)}
.mem-empty{font-family:'Share Tech Mono',monospace;font-size:.58rem;
  color:rgba(255,255,255,.15);text-align:center;padding:8px 0;letter-spacing:.08em}
#mem-add-row{display:flex;gap:5px}
#mem-inp{flex:1;padding:6px 9px;background:rgba(255,255,255,.04);
  border:1px solid rgba(230,57,70,.2);border-radius:7px;color:#fff;
  font-family:'Rajdhani',sans-serif;font-size:.82rem;outline:none;
  transition:border-color .2s}
#mem-inp:focus{border-color:var(--r)}
#mem-inp::placeholder{color:rgba(255,255,255,.2);font-size:.75rem}
#mem-add-btn{padding:6px 10px;background:rgba(230,57,70,.15);
  border:1px solid rgba(230,57,70,.35);border-radius:7px;
  color:var(--r);font-family:'Orbitron',monospace;font-size:.6rem;
  font-weight:700;cursor:pointer;transition:all .18s;white-space:nowrap}
#mem-add-btn:hover{background:rgba(230,57,70,.28)}
.mem-on-badge{display:inline-flex;align-items:center;gap:4px;
  padding:2px 7px;border-radius:10px;font-family:'Orbitron',monospace;
  font-size:.44rem;letter-spacing:.1em;
  background:rgba(46,204,113,.12);border:1px solid rgba(46,204,113,.3);
  color:#2ecc71;animation:pulse 2.5s infinite}
@keyframes memPop{0%{transform:scale(0.85);opacity:0}60%{transform:scale(1.05)}100%{transform:scale(1);opacity:1}}
.mem-item{animation:memPop .25s ease both}
/* memory indicator pill in header */
#mem-hdr-pill{display:none;align-items:center;gap:4px;padding:3px 9px;
  border-radius:10px;font-family:'Orbitron',monospace;font-size:.44rem;
  letter-spacing:.1em;background:rgba(46,204,113,.1);
  border:1px solid rgba(46,204,113,.28);color:#2ecc71;cursor:pointer}
#mem-hdr-pill:hover{background:rgba(46,204,113,.2)}

/* ══ TOOL MODAL ══ */
#tool-overlay{display:none;position:fixed;inset:0;z-index:200;
  background:rgba(0,0,0,.72);backdrop-filter:blur(6px);
  align-items:center;justify-content:center;animation:fIn .18s ease}
#tool-overlay.open{display:flex}
#tool-modal{width:min(560px,94vw);max-height:88vh;overflow-y:auto;
  background:rgba(6,1,18,.97);border:1px solid rgba(230,57,70,.32);
  border-radius:16px;padding:0;position:relative;
  box-shadow:0 0 80px rgba(230,57,70,.18),0 24px 60px rgba(0,0,0,.7);
  animation:fUp .22s ease}
#tool-modal::before{content:'';position:absolute;top:0;left:0;right:0;
  height:2px;background:linear-gradient(90deg,transparent,var(--r),transparent);
  border-radius:16px 16px 0 0}
.tm-head{padding:20px 22px 16px;border-bottom:1px solid rgba(230,57,70,.1);
  display:flex;align-items:center;gap:13px}
.tm-icon{font-size:1.8rem;filter:drop-shadow(0 0 10px rgba(230,57,70,.5))}
.tm-title-wrap{flex:1}
.tm-title{font-family:'Orbitron',monospace;font-size:1rem;font-weight:900;
  color:#fff;letter-spacing:.12em;margin-bottom:3px}
.tm-desc{font-family:'Share Tech Mono',monospace;font-size:.58rem;
  color:rgba(230,57,70,.6);letter-spacing:.1em}
.tm-close{width:32px;height:32px;background:rgba(255,255,255,.05);
  border:1px solid rgba(255,255,255,.1);border-radius:8px;
  color:rgba(255,255,255,.4);font-size:1rem;cursor:pointer;
  transition:all .18s;display:flex;align-items:center;justify-content:center}
.tm-close:hover{background:rgba(230,57,70,.2);border-color:rgba(230,57,70,.4);color:#fff}
/* tool mode badge strip */
.tm-badge-strip{padding:8px 22px;background:rgba(230,57,70,.06);
  border-bottom:1px solid rgba(230,57,70,.08);
  display:flex;align-items:center;gap:8px}
.tm-mode-badge{display:inline-flex;align-items:center;gap:5px;
  padding:3px 10px;border-radius:10px;font-family:'Orbitron',monospace;
  font-size:.48rem;font-weight:700;letter-spacing:.14em;
  border:1px solid;animation:glow 3s infinite}
.tm-mode-badge.resume{background:rgba(244,162,97,.12);border-color:rgba(244,162,97,.4);color:#f4a261}
.tm-mode-badge.email{background:rgba(100,200,255,.1);border-color:rgba(100,200,255,.35);color:#64c8ff}
.tm-mode-badge.code{background:rgba(46,204,113,.1);border-color:rgba(46,204,113,.35);color:#2ecc71}
.tm-mode-badge.startup{background:rgba(255,200,60,.1);border-color:rgba(255,200,60,.35);color:#ffc83c}
.tm-mode-badge.sql{background:rgba(167,130,255,.1);border-color:rgba(167,130,255,.35);color:#a782ff}
.tm-mode-badge.prompt{background:rgba(230,57,70,.12);border-color:rgba(230,57,70,.38);color:var(--r)}
.tm-use-count{font-family:'Share Tech Mono',monospace;font-size:.52rem;
  color:rgba(255,255,255,.28);margin-left:auto;letter-spacing:.06em}
/* form fields */
.tm-body{padding:18px 22px 0}
.tm-field{margin-bottom:14px}
.tm-label{font-family:'Orbitron',monospace;font-size:.5rem;font-weight:700;
  color:rgba(230,57,70,.8);letter-spacing:.18em;text-transform:uppercase;
  display:block;margin-bottom:5px}
.tm-req{color:var(--r)}
.tm-input,.tm-select,.tm-textarea{width:100%;padding:10px 13px;
  background:rgba(255,255,255,.04);border:1px solid rgba(230,57,70,.18);
  border-radius:9px;color:var(--w);font-family:'Rajdhani',sans-serif;
  font-size:.9rem;outline:none;transition:all .22s;resize:none}
.tm-input:focus,.tm-select:focus,.tm-textarea:focus{
  border-color:var(--r);box-shadow:0 0 16px rgba(230,57,70,.18)}
.tm-input::placeholder,.tm-textarea::placeholder{color:rgba(255,255,255,.2)}
.tm-select{appearance:none;cursor:pointer;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='6'%3E%3Cpath d='M0 0l5 6 5-6z' fill='%23e63946'/%3E%3C/svg%3E");
  background-repeat:no-repeat;background-position:right 12px center;
  background-color:rgba(255,255,255,.04)}
.tm-select option{background:#0d001a;color:#fff}
.tm-textarea{min-height:72px;line-height:1.55}
.tm-hint{font-family:'Share Tech Mono',monospace;font-size:.52rem;
  color:rgba(255,255,255,.18);margin-top:4px;letter-spacing:.04em}
.tm-row{display:grid;grid-template-columns:1fr 1fr;gap:10px}
/* footer */
.tm-foot{padding:16px 22px 20px;display:flex;gap:9px;align-items:center;
  border-top:1px solid rgba(230,57,70,.08);margin-top:18px}
.tm-launch{flex:1;padding:11px 18px;
  background:linear-gradient(135deg,#e63946,#c1121f);
  border:none;border-radius:10px;color:#fff;
  font-family:'Orbitron',monospace;font-weight:700;font-size:.7rem;
  letter-spacing:.16em;cursor:pointer;transition:all .22s;
  box-shadow:0 4px 18px rgba(230,57,70,.38)}
.tm-launch:hover{box-shadow:0 4px 28px rgba(230,57,70,.6);transform:translateY(-2px)}
.tm-cancel{padding:11px 16px;background:transparent;
  border:1px solid rgba(255,255,255,.1);border-radius:10px;
  color:rgba(255,255,255,.35);font-family:'Orbitron',monospace;
  font-size:.62rem;letter-spacing:.1em;cursor:pointer;transition:all .18s}
.tm-cancel:hover{border-color:rgba(255,255,255,.25);color:rgba(255,255,255,.6)}

/* ══ TOOL MODE HEADER BADGE ══ */
#toolmode-hdr{display:none;align-items:center;gap:5px;padding:3px 10px;
  border-radius:10px;font-family:'Orbitron',monospace;font-size:.46rem;
  letter-spacing:.12em;border:1px solid;cursor:pointer;transition:all .25s}

/* ══ TOOL ANALYTICS PANEL ══ */
#analytics-modal{display:none;position:fixed;inset:0;z-index:201;
  background:rgba(0,0,0,.78);backdrop-filter:blur(7px);
  align-items:center;justify-content:center}
#analytics-modal.open{display:flex}
#analytics-box{width:min(480px,92vw);background:rgba(6,1,18,.98);
  border:1px solid rgba(230,57,70,.28);border-radius:16px;
  padding:22px 24px;box-shadow:0 0 80px rgba(230,57,70,.15);
  animation:fUp .2s ease;position:relative}
#analytics-box::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;
  background:linear-gradient(90deg,transparent,var(--r),transparent);border-radius:16px 16px 0 0}
.an-title{font-family:'Orbitron',monospace;font-size:.85rem;font-weight:900;
  color:#fff;letter-spacing:.14em;margin-bottom:4px}
.an-sub{font-family:'Share Tech Mono',monospace;font-size:.54rem;
  color:rgba(230,57,70,.55);letter-spacing:.1em;margin-bottom:16px}
.an-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:16px}
.an-card{background:rgba(230,57,70,.05);border:1px solid rgba(230,57,70,.14);
  border-radius:10px;padding:10px 12px;text-align:center}
.an-val{font-family:'Orbitron',monospace;font-size:1.1rem;font-weight:900;
  color:var(--r);text-shadow:0 0 12px rgba(230,57,70,.4)}
.an-lbl{font-family:'Share Tech Mono',monospace;font-size:.46rem;
  color:rgba(255,255,255,.3);letter-spacing:.1em;margin-top:3px}
.an-list{display:flex;flex-direction:column;gap:5px;margin-bottom:16px}
.an-row{display:flex;align-items:center;gap:9px;padding:7px 10px;
  background:rgba(255,255,255,.03);border-radius:8px;
  border:1px solid rgba(255,255,255,.05)}
.an-tool-icon{font-size:1rem;width:22px;text-align:center}
.an-tool-name{font-family:'Orbitron',monospace;font-size:.54rem;
  color:rgba(255,255,255,.7);letter-spacing:.08em;flex:1}
.an-bar-wrap{width:90px;height:5px;background:rgba(255,255,255,.07);
  border-radius:3px;overflow:hidden}
.an-bar{height:100%;border-radius:3px;transition:width .5s ease}
.an-count{font-family:'Share Tech Mono',monospace;font-size:.56rem;
  color:rgba(230,57,70,.7);min-width:28px;text-align:right}
.an-close-btn{width:100%;padding:9px;background:transparent;
  border:1px solid rgba(255,255,255,.1);border-radius:9px;
  color:rgba(255,255,255,.4);font-family:'Orbitron',monospace;
  font-size:.6rem;letter-spacing:.1em;cursor:pointer;transition:all .18s}
.an-close-btn:hover{border-color:rgba(230,57,70,.4);color:var(--r)}
/* analytics btn in sidebar */
#analytics-btn{background:rgba(255,200,60,.06);border:1px solid rgba(255,200,60,.2);
  color:rgba(255,200,60,.7)}
#analytics-btn:hover{background:rgba(255,200,60,.12);border-color:rgba(255,200,60,.4);color:#ffc83c}
</style>
</head>
<body>

<div class="bgr"></div><div class="scn"></div>

<!-- ══ LOGIN ══ -->
<div id="lgn">
  <div class="lc tl"></div><div class="lc tr"></div>
  <div class="lc bl"></div><div class="lc br"></div>
  <div class="bgr" style="opacity:.5"></div><div class="scn"></div>
  <div class="lic">
    <span class="e">🤖</span>
    <div class="r1"></div><div class="r2"></div><div class="ob"></div>
  </div>
  <div class="ltw"><div class="lt">FRIDAY</div><div class="ltg">FRIDAY</div></div>
  <p class="lsub">ADVANCED AI ASSISTANT v2.0</p>
  <div class="lbdg">
    <div class="lbdd"></div>
    <span class="lbdt">ONLINE · 10 FREE GROQ MODELS · 14 LANGUAGES · VOICE</span>
  </div>
  <div class="lcard">
    <p class="lhd">— AUTHENTICATION REQUIRED —</p>
    <div class="lfl">
      <label class="llbl">USER_ID</label>
      <input class="lin" id="lu" type="text" placeholder="Enter username" autocomplete="off">
    </div>
    <div class="lfl">
      <label class="llbl">ACCESS_KEY</label>
      <input class="lin" id="lp" type="password" placeholder="••••••••">
    </div>
    <button class="lbtn" id="lbtn">⚡ INITIALIZE SESSION</button>
    <div class="lerr" id="lerr">⚠ ACCESS DENIED — INVALID CREDENTIALS</div>
  </div>
</div>

<!-- ══ APP ══ -->
<div id="app" style="display:none">
  <div id="sbt" onclick="toggleSB()">❮</div>
  <div id="sb">
    <!-- .sbi scrolls all content. Footer is sibling OUTSIDE .sbi -->
    <div class="sbi">
      <div class="sbb">
        <div class="sbt2">
          <div class="ico">
            <span class="e">🤖</span><div class="rg"></div><div class="ob"></div>
          </div>
          <div><div class="sbn">FRIDAY</div><div class="sbtg">AI · FREE MODELS · MULTILINGUAL</div></div>
        </div>
        <div class="sbst"><div class="sbsd"></div><span class="sbst2">SYSTEM ONLINE</span></div>
        <div class="sbdv"></div>
        <div class="sbu">
          <div class="sbav">👤</div>
          <div><div class="sbun" id="sbun">USER</div><div class="sbrl">AUTHORIZED USER</div></div>
        </div>
      </div>
      <div class="sbs">
        <div class="sbl">AI MODEL</div>
        <select id="mdl" onchange="updBadge()">
          <option value="llama-3.1-8b-instant">⚡ LLaMA 3.1 8B — Fastest</option>
          <option value="llama-3.3-70b-versatile">🧠 LLaMA 3.3 70B — Smartest</option>
          <option value="llama3-70b-8192">🦙 LLaMA 3 70B — 8k ctx</option>
          <option value="llama3-8b-8192">🦙 LLaMA 3 8B — 8k ctx</option>
          <option value="mixtral-8x7b-32768">🔥 Mixtral 8x7B — 32k ctx</option>
          <option value="gemma2-9b-it">💎 Gemma 2 9B</option>
          <option value="gemma-7b-it">💎 Gemma 7B</option>
          <option value="deepseek-r1-distill-llama-70b">🔮 DeepSeek R1 70B</option>
          <option value="qwen-qwq-32b">🌟 Qwen QwQ 32B</option>
          <option value="meta-llama/llama-4-scout-17b-16e-instruct">🚀 LLaMA 4 Scout 17B</option>
        </select>
      </div>
      <div class="sbs" style="padding-top:4px">
        <div class="sbl">LANGUAGE</div>
        <select id="lng" onchange="updBadge()">
          <option value="en-US|English|Respond in English.">English</option>
          <option value="hi-IN|Hindi|हिंदी में जवाब दें।">Hindi</option>
          <option value="ta-IN|Tamil|தமிழில் பதிலளிக்கவும்.">Tamil</option>
          <option value="te-IN|Telugu|తెలుగులో సమాధానం చెప్పండి.">Telugu</option>
          <option value="bn-IN|Bengali|বাংলায় উত্তর দিন।">Bengali</option>
          <option value="es-ES|Spanish|Responde en español.">Spanish</option>
          <option value="fr-FR|French|Réponds en français.">French</option>
          <option value="de-DE|German|Antworte auf Deutsch.">German</option>
          <option value="zh-CN|Chinese|用中文回答。">Chinese</option>
          <option value="ar-SA|Arabic|أجب باللغة العربية.">Arabic</option>
          <option value="pt-BR|Portuguese|Responda em português.">Portuguese</option>
          <option value="ja-JP|Japanese|日本語で答えてください。">Japanese</option>
          <option value="ko-KR|Korean|한국어로 답변해 주세요。">Korean</option>
          <option value="ru-RU|Russian|Отвечай на русском языке.">Russian</option>
        </select>
      </div>
      <div class="sbs" style="padding-top:4px">
        <div class="sbl">SESSION STATS</div>
        <div class="stg">
          <div class="stc"><div class="stv" id="stm">0</div><div class="stl">MESSAGES</div></div>
          <div class="stc"><div class="stv" id="sts">0</div><div class="stl">SESSIONS</div></div>
          <div class="stc"><div class="stv" id="stw">0</div><div class="stl">WORDS</div></div>
          <div class="stc"><div class="stv" id="stt">0m</div><div class="stl">UPTIME</div></div>
        </div>
      </div>
      <div class="sbs" style="padding-top:6px;padding-bottom:2px">
        <button class="sbtn pr" onclick="newSess()">＋ NEW SESSION</button>
      </div>
      <div class="sbs" style="padding-top:4px">
        <div class="sbl">AI TOOLS</div>
        <button class="sbtn" onclick="openTool('resume')">📄 Resume Builder</button>
        <button class="sbtn" onclick="openTool('email')">✉ Email Generator</button>
        <button class="sbtn" onclick="openTool('code')">💻 Code Generator</button>
        <button class="sbtn" onclick="openTool('startup')">🚀 Startup Idea</button>
        <button class="sbtn" onclick="openTool('sql')">🗄 SQL Query Builder</button>
        <button class="sbtn" onclick="openTool('prompt')">✨ Prompt Enhancer</button>
        <button class="sbtn" id="analytics-btn" onclick="openAnalytics()" style="margin-top:4px">📊 Tool Analytics</button>
      </div>

      <!-- ══ MEMORY MODE PANEL ══ -->
      <div class="sbdiv"><span>MEMORY MODE</span></div>
      <div id="mem-panel">
        <div class="sbl" style="margin-bottom:6px">
          <span>🧠 FRIDAY REMEMBERS</span>
          <span class="mem-on-badge" id="mem-badge">● ACTIVE</span>
        </div>
        <div id="mem-list"><div class="mem-empty">No memories yet — tell me something!</div></div>
        <div id="mem-add-row">
          <input id="mem-inp" type="text" placeholder="e.g. I am preparing for UPSC" maxlength="120"
            onkeydown="if(event.key==='Enter') addMemory()">
          <button id="mem-add-btn" onclick="addMemory()">＋ ADD</button>
        </div>
      </div>
      <div class="sbdiv"><span>SESSION LOG</span></div>
      <div class="ssl" id="ssl"></div>
    </div>
    <!-- FOOTER: sibling of .sbi, direct child of #sb. ALWAYS pinned at bottom. -->
    <div class="sbft">
      <button class="sbtn dr" onclick="clearAll()">🗑 CLEAR ALL</button>
      <button class="sbtn dr" onclick="doLogout()">⏻ LOGOUT</button>
    </div>
  </div>

  <!-- Main chat -->
  <div id="main">
    <div id="hdr">
      <div class="hst">
        <span class="hstr">✦</span>
        <span id="htit">FRIDAY, HELLO SIR 👋</span>
        <span class="hstr">✦</span>
      </div>
      <p id="hsub">YOUR ADVANCED AI ASSISTANT — READY TO ASSIST</p>
      <div id="hbdg" style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;justify-content:center">
        <div style="display:flex;align-items:center;gap:6px;background:rgba(230,57,70,.06);border:1px solid rgba(230,57,70,.2);border-radius:20px;padding:4px 14px">
          <div class="bdt"></div>
          <span id="bdgt">Online · LLaMA 3.1 8B · English</span>
          <span id="modebdg">NORMAL</span>
        </div>
        <div id="mem-hdr-pill" onclick="toggleSB(); setTimeout(()=>$('mem-inp').focus(),350)" title="Memory Mode active — click to manage">
          🧠 <span id="mem-hdr-count">0</span> MEMORIES
        </div>
        <div id="toolmode-hdr" onclick="if(currentTool) openTool(currentTool)" title="Tool Mode active">
          <span id="toolmode-hdr-icon"></span> <span id="toolmode-hdr-label">TOOL MODE</span>
        </div>
        <div id="devtog">
          <button class="dtb on" id="dtnorm" onclick="setMode('normal')">⬜ NORMAL</button>
          <button class="dtb" id="dtdev" onclick="setMode('dev')">🧠 DEVELOPER</button>
        </div>
      </div>
      <div id="hscn"></div>
    </div>

    <div id="msgs"></div>

    <div id="typ">
      <div class="tw">
        <div class="tav">🤖</div>
        <div class="tbu"><div class="tdt">
          <div class="td"></div><div class="td"></div><div class="td"></div>
        </div></div>
      </div>
    </div>



    <div id="inp">
      <div id="vrow">
        <div id="wvb"></div>
        <button id="vbtn" onclick="vTog()">
          <span id="vic">🎤</span><span id="vtx2">VOICE INPUT</span>
        </button>
        <button id="vclr" onclick="vClr()">✕ CLEAR</button>
        <span id="vst"></span>
      </div>
      <div id="vtx"></div>
      <div id="mf">
        <textarea id="mi"
          id="miarea" placeholder="Type in any language... हिंदी, English, தமிழ், বাংলা..."
          rows="1"
          onkeydown="hKey(event)"
          oninput="autoR(this)"></textarea>
        <button id="sndb" onclick="send()">➤</button>
      </div>
    </div>
  </div>
</div>
<div id="toast"></div>

<!-- ══ TOOL MODAL ══ -->
<div id="tool-overlay" onclick="if(event.target===this)closeTool()">
  <div id="tool-modal">
    <div class="tm-head">
      <span class="tm-icon" id="tm-icon">🛠</span>
      <div class="tm-title-wrap">
        <div class="tm-title" id="tm-title">TOOL</div>
        <div class="tm-desc" id="tm-desc">AI-powered tool</div>
      </div>
      <button class="tm-close" onclick="closeTool()">✕</button>
    </div>
    <div class="tm-badge-strip">
      <span class="tm-mode-badge" id="tm-badge">⚡ TOOL MODE</span>
      <span class="tm-use-count" id="tm-use-count"></span>
    </div>
    <div class="tm-body" id="tm-body"></div>
    <div class="tm-foot">
      <button class="tm-cancel" onclick="closeTool()">CANCEL</button>
      <button class="tm-launch" onclick="launchTool()">⚡ GENERATE WITH FRIDAY</button>
    </div>
  </div>
</div>

<!-- ══ ANALYTICS MODAL ══ -->
<div id="analytics-modal" onclick="if(event.target===this)closeAnalytics()">
  <div id="analytics-box">
    <div class="an-title">📊 TOOL ANALYTICS</div>
    <div class="an-sub">YOUR AI TOOL USAGE STATS</div>
    <div class="an-grid" id="an-summary"></div>
    <div class="an-list" id="an-list"></div>
    <button class="an-close-btn" onclick="closeAnalytics()">CLOSE</button>
  </div>
</div>

<script>
// ══════════════════════════════════════════════
//  CONFIG  — key injected from Python, never in UI
// ══════════════════════════════════════════════
const GROQ_KEY = "";
const USERS    = {"admin":"friday"};

// ══════════════════════════════════════════════
//  STATE
// ══════════════════════════════════════════════
const STORE_KEY = 'fri6';
let S = {user:'', sessions:{}, curSid:null, sidebarOpen:true, memories:[], toolAnalytics:{}};
let history = [];   // current session messages (not persisted between loads)
let t0 = Date.now();

function loadS(){
  try {
    const raw = localStorage.getItem(STORE_KEY);
    if (!raw) return;
    const d = JSON.parse(raw);
    if (typeof d.user        === 'string')  S.user        = d.user;
    if (typeof d.sessions    === 'object')  S.sessions    = d.sessions || {};
    if (typeof d.curSid      === 'string')  S.curSid      = d.curSid;
    if (typeof d.sidebarOpen === 'boolean') S.sidebarOpen = d.sidebarOpen;
    if (Array.isArray(d.memories))          S.memories      = d.memories;
    if (typeof d.toolAnalytics === 'object') S.toolAnalytics = d.toolAnalytics || {};
  } catch(e) { console.warn('loadS:', e); }
}
function saveS(){
  try { localStorage.setItem(STORE_KEY, JSON.stringify(S)); } catch(e){}
}

// ══════════════════════════════════════════════
//  HELPERS
// ══════════════════════════════════════════════
const $ = id => document.getElementById(id);
function nowT(){ return new Date().toLocaleTimeString('en-GB',{hour:'2-digit',minute:'2-digit'}); }
function escH(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }

function toast(msg){
  const t = $('toast');
  t.textContent = msg;
  t.style.display = 'flex';
  clearTimeout(t._tmr);
  t._tmr = setTimeout(()=>{ t.style.display='none'; }, 7000);
}

// ══════════════════════════════════════════════
//  LOGIN  — wired up after DOM ready
// ══════════════════════════════════════════════
function doLogin(){
  const u = $('lu').value.trim();
  const p = $('lp').value;
  if (USERS[u] && USERS[u] === p) {
    S.user = u;
    saveS();
    showChat();
  } else {
    $('lerr').style.display = 'block';
    setTimeout(() => $('lerr').style.display = 'none', 3000);
  }
}

function showChat(){
  $('lgn').style.display = 'none';
  $('app').style.display = 'flex';
  $('sbun').textContent  = S.user.toUpperCase();
  applySB();
  buildWaves();
  renderSess();
  renderMemories();
  // load session
  const sids = Object.keys(S.sessions);
  if (S.curSid && S.sessions[S.curSid]) {
    history = [...(S.sessions[S.curSid].messages || [])];
    renderSess(); renderMsgs(); updStats();
    const isNew = S.sessions[S.curSid].title === 'New Session';
    showQ(isNew && history.length === 0);
    setHdr(isNew ? 'FRIDAY, HELLO SIR 👋' : S.sessions[S.curSid].title.toUpperCase().slice(0,44), isNew);
  } else if (sids.length > 0) {
    const last = sids.sort((a,b)=>
      (S.sessions[b].created||'').localeCompare(S.sessions[a].created||''))[0];
    loadSess(last);
  } else {
    newSess();
  }
  setInterval(updStats, 30000);
}

function doLogout(){
  S.user = '';
  saveS();
  $('app').style.display = 'none';
  $('lgn').style.display = 'flex';
  $('lu').value = ''; $('lp').value = '';
}

// ══════════════════════════════════════════════
//  SIDEBAR
// ══════════════════════════════════════════════
function toggleSB(){
  S.sidebarOpen = !S.sidebarOpen;
  saveS(); applySB();
}
function applySB(){
  const sb=$('sb'), t=$('sbt');
  if (S.sidebarOpen){
    sb.classList.remove('off'); t.classList.remove('off');
    t.textContent='❮'; t.style.left='var(--sw)';
  } else {
    sb.classList.add('off'); t.classList.add('off');
    t.textContent='❯'; t.style.left='0';
  }
}

// ══════════════════════════════════════════════
//  SESSIONS
// ══════════════════════════════════════════════
function newSess(){
  const sid = Math.random().toString(36).slice(2,10);
  S.sessions[sid] = {title:'New Session', messages:[], created:new Date().toISOString()};
  S.curSid = sid; history = [];
  saveS(); renderSess(); renderMsgs(); updStats();
  showQ(true); setHdr('FRIDAY, HELLO SIR 👋', true);
}
function loadSess(sid){
  if (!S.sessions[sid]) return;
  S.curSid = sid;
  history = [...(S.sessions[sid].messages || [])];
  saveS(); renderSess(); renderMsgs(); updStats();
  const isNew = S.sessions[sid].title === 'New Session';
  showQ(isNew && history.length === 0);
  setHdr(isNew ? 'FRIDAY, HELLO SIR 👋' : S.sessions[sid].title.toUpperCase().slice(0,44), isNew);
}
function delSess(sid, e){
  e.stopPropagation();
  delete S.sessions[sid];
  if (S.curSid === sid){
    const k = Object.keys(S.sessions);
    if (k.length > 0) loadSess(k[0]); else newSess();
  }
  saveS(); renderSess(); updStats();
}
function clearAll(){
  if (!confirm('Clear all sessions?')) return;
  S.sessions = {}; S.curSid = null; history = [];
  saveS(); newSess();
}

function renderSess(){
  const el = $('ssl');
  if (!el) return;
  const sids = Object.keys(S.sessions).sort((a,b)=>
    (S.sessions[b].created||'').localeCompare(S.sessions[a].created||''));
  if (!sids.length){ el.innerHTML='<div class="semp">— NO SESSIONS —</div>'; return; }
  el.innerHTML = sids.map(sid => {
    const s = S.sessions[sid], a = sid===S.curSid;
    const title = escH(s.title.slice(0,26));
    const cnt = (s.messages||[]).length, dt = (s.created||'').slice(0,10);
    return `<div class="ssi${a?' ac':''}" onclick="loadSess('${sid}')">
      <div style="flex:1;min-width:0">
        <div class="sti">${a?'▸ ':''}${title}</div>
        <div class="smeta">${cnt} MSG · ${dt}</div>
      </div>
      <button class="sdel" onclick="delSess('${sid}',event)">✕</button>
    </div>`;
  }).join('');
}

// ══════════════════════════════════════════════
//  HEADER / BADGE
// ══════════════════════════════════════════════
function setHdr(t, isNew){
  $('htit').textContent = t;
  $('hsub').textContent = isNew ? 'YOUR ADVANCED AI ASSISTANT — READY TO ASSIST' : 'ACTIVE SESSION';
}
function updBadge(){
  const m=$('mdl'), l=$('lng');
  const ml = m.options[m.selectedIndex].text.replace(/[⚡🧠🔥💎🦙🌪🔮🌟🚀]/gu,'').replace(/—.*/,'').trim();
  $('bdgt').textContent = `Online · ${ml} · ${l.options[l.selectedIndex].text} · ${history.length} MSG`;
}
function showQ(v){}
function qp(t){ $('mi').value=t; $('mi').focus(); autoR($('mi')); }

// ══════════════════════════════════════════════
//  TOOL MODE — Modal + Form + System Prompts + Analytics
// ══════════════════════════════════════════════
let currentTool = null;

const TOOL_DEFS = {
  resume: {
    icon:'📄', label:'RESUME BUILDER', cls:'resume',
    desc:'Craft a professional, ATS-friendly resume',
    badge:'📄 RESUME MODE',
    systemPrompt:'You are an expert career coach and professional resume writer. Create polished, ATS-optimized resumes with clear sections, action verbs, and quantified achievements. Format using clean markdown with bold headers.',
    fields:[
      {id:'name',    label:'Full Name',         type:'input',    placeholder:'e.g. Arjun Sharma',     required:true},
      {id:'role',    label:'Target Role',        type:'input',    placeholder:'e.g. Software Engineer at Google', required:true},
      {id:'skills',  label:'Key Skills',         type:'textarea', placeholder:'Python, React, AWS, Leadership...', required:true, rows:2},
      {id:'exp',     label:'Work Experience',    type:'textarea', placeholder:'Company | Role | Duration | Key achievements...', rows:3},
      {id:'edu',     label:'Education',          type:'input',    placeholder:'B.Tech Computer Science, IIT Delhi 2022'},
      {id:'extras',  label:'Extras (Certs/Projects)', type:'textarea', placeholder:'Optional: certifications, projects, awards...', rows:2},
      {id:'tone',    label:'Style',              type:'select',   options:['Professional & Formal','Creative & Modern','Minimal & Clean','Executive Level']},
    ],
    build: f => `Create a complete professional resume for ${f.name} applying for ${f.role}.\n\nSkills: ${f.skills}\nExperience: ${f.exp||'Not provided'}\nEducation: ${f.edu||'Not provided'}\nExtras: ${f.extras||'None'}\nStyle: ${f.tone}\n\nFormat with clear sections: Summary, Skills, Experience, Education, Achievements. Use bullet points and action verbs.`
  },
  email: {
    icon:'✉', label:'EMAIL GENERATOR', cls:'email',
    desc:'Compose any professional email in seconds',
    badge:'✉ EMAIL MODE',
    systemPrompt:'You are an expert business communication specialist. Write clear, compelling, professionally structured emails that achieve their goal. Match tone precisely. Use proper salutation, body structure, and sign-off.',
    fields:[
      {id:'purpose', label:'Email Purpose',      type:'input',    placeholder:'e.g. Follow up after interview', required:true},
      {id:'to',      label:'Recipient',          type:'input',    placeholder:'e.g. HR Manager, Client, Professor'},
      {id:'from',    label:'Sender Name/Role',   type:'input',    placeholder:'e.g. Rahul Verma, Marketing Intern'},
      {id:'tone',    label:'Tone',               type:'select',   options:['Formal & Professional','Friendly & Warm','Assertive & Direct','Apologetic','Persuasive','Follow-up']},
      {id:'points',  label:'Key Points to Include', type:'textarea', placeholder:'Main message, any specific details...', rows:3, required:true},
      {id:'length',  label:'Length',             type:'select',   options:['Concise (3-4 lines)','Standard (1 paragraph)','Detailed (2-3 paragraphs)']},
    ],
    build: f => `Write a ${f.tone} email.\n\nPurpose: ${f.purpose}\nTo: ${f.to||'recipient'}\nFrom: ${f.from||'sender'}\nKey Points: ${f.points}\nLength: ${f.length}\n\nInclude: subject line, proper greeting, clear body, professional sign-off.`
  },
  code: {
    icon:'💻', label:'CODE GENERATOR', cls:'code',
    desc:'Write clean, production-ready code',
    badge:'💻 CODE MODE',
    systemPrompt:'You are a senior software engineer and coding expert. Write clean, efficient, well-commented, production-ready code. Always use proper fenced code blocks with language tags. Include error handling, edge cases, and a brief explanation of the approach.',
    fields:[
      {id:'lang',    label:'Language',           type:'select',   options:['Python','JavaScript','TypeScript','Java','C++','C#','Go','Rust','SQL','Bash','HTML/CSS','React JSX'], required:true},
      {id:'task',    label:'What should it do?', type:'textarea', placeholder:'Describe the functionality in detail...', rows:3, required:true},
      {id:'input',   label:'Input / Parameters', type:'input',    placeholder:'e.g. list of integers, string, API response'},
      {id:'output',  label:'Expected Output',    type:'input',    placeholder:'e.g. sorted list, JSON object, boolean'},
      {id:'style',   label:'Code Style',         type:'select',   options:['Clean with comments','Minimal / No comments','Object-Oriented','Functional','With unit tests']},
      {id:'edge',    label:'Edge Cases to Handle', type:'input',  placeholder:'e.g. empty input, null values, large dataset'},
    ],
    build: f => `Write ${f.lang} code that does the following:\n\n${f.task}\n\nInput: ${f.input||'as needed'}\nOutput: ${f.output||'as needed'}\nStyle: ${f.style}\nEdge cases: ${f.edge||'standard'}\n\nUse fenced code blocks. Add brief comments. Explain the approach after the code.`
  },
  startup: {
    icon:'🚀', label:'STARTUP IDEA GENERATOR', cls:'startup',
    desc:'Generate validated startup concepts with GTM strategy',
    badge:'🚀 STARTUP MODE',
    systemPrompt:'You are a startup advisor and venture capitalist with 20 years experience. Generate detailed, realistic, and investable startup ideas with clear problem-solution fit, market sizing, revenue model, and growth strategy. Be specific and actionable.',
    fields:[
      {id:'industry',label:'Industry / Domain',  type:'select',   options:['SaaS / Software','EdTech','HealthTech','FinTech','E-Commerce','AgriTech','CleanTech','AI / ML','Gaming','Social Media','Logistics','Other'], required:true},
      {id:'problem', label:'Problem You Want to Solve', type:'textarea', placeholder:'Describe the pain point or gap you see...', rows:2, required:true},
      {id:'audience',label:'Target Audience',    type:'input',    placeholder:'e.g. College students, SMEs, Farmers'},
      {id:'budget',  label:'Startup Budget',     type:'select',   options:['Bootstrapped (<₹5L)','Seed Stage (₹5L–50L)','Series A (₹50L–5Cr)','Well-funded (>₹5Cr)']},
      {id:'country', label:'Target Market',      type:'input',    placeholder:'e.g. India, USA, Global'},
      {id:'model',   label:'Preferred Revenue Model', type:'select', options:['Subscription (SaaS)','Marketplace','Freemium','B2B Enterprise','D2C','Ads-based','Commission']},
    ],
    build: f => `Generate a detailed startup idea for the ${f.industry} space.\n\nProblem: ${f.problem}\nAudience: ${f.audience||'general'}\nBudget: ${f.budget}\nMarket: ${f.country||'India'}\nRevenue Model: ${f.model}\n\nInclude: Idea name, tagline, problem-solution fit, MVP features, revenue model, go-to-market strategy, competitive advantage, 12-month roadmap.`
  },
  sql: {
    icon:'🗄', label:'SQL QUERY BUILDER', cls:'sql',
    desc:'Generate optimised SQL for any database',
    badge:'🗄 SQL MODE',
    systemPrompt:'You are a senior database architect and SQL expert. Write optimized, production-ready SQL queries with proper indexing hints, explain the query logic, and mention performance considerations. Always use fenced ```sql code blocks.',
    fields:[
      {id:'db',      label:'Database Type',      type:'select',   options:['MySQL','PostgreSQL','SQLite','Microsoft SQL Server','Oracle','BigQuery','Snowflake'], required:true},
      {id:'tables',  label:'Table Structure',    type:'textarea', placeholder:'users(id, name, email, created_at)\norders(id, user_id, amount, status)', rows:3, required:true},
      {id:'goal',    label:'What query should do?', type:'textarea', placeholder:'Get all users who placed >3 orders in last 30 days...', rows:2, required:true},
      {id:'perf',    label:'Performance Focus',  type:'select',   options:['Standard','Optimised for large datasets','With indexes','With pagination','With aggregations']},
      {id:'extra',   label:'Extra Requirements', type:'input',    placeholder:'e.g. JOIN with another table, handle NULLs, add WHERE clause'},
    ],
    build: f => `Write an optimised ${f.db} SQL query.\n\nTable Structure:\n${f.tables}\n\nGoal: ${f.goal}\nPerformance: ${f.perf}\nExtra: ${f.extra||'none'}\n\nProvide: the SQL query in a fenced block, explanation of each clause, any index recommendations.`
  },
  prompt: {
    icon:'✨', label:'PROMPT ENHANCER', cls:'prompt',
    desc:'Transform weak prompts into AI-optimised masterpieces',
    badge:'✨ PROMPT MODE',
    systemPrompt:'You are an expert prompt engineer who has mastered prompting techniques for LLMs. Rewrite and enhance prompts to be clearer, more specific, and more effective. Use techniques like role assignment, chain-of-thought, few-shot examples, output format specification, and constraint setting. Show the original vs enhanced version.',
    fields:[
      {id:'raw',     label:'Your Original Prompt', type:'textarea', placeholder:'Paste your prompt here...', rows:4, required:true},
      {id:'goal',    label:'What do you want the AI to do?', type:'input', placeholder:'e.g. write code, explain a concept, generate ideas'},
      {id:'model',   label:'Target AI Model',    type:'select',   options:['General (any model)','GPT-4 / Claude','Code-focused model','Creative writing model','Data analysis model']},
      {id:'style',   label:'Enhancement Style',  type:'select',   options:['Add role + context','Chain-of-thought','Few-shot examples','Structured output format','All techniques combined']},
      {id:'extra',   label:'Specific Constraints', type:'input',  placeholder:'e.g. keep it under 100 words, output as JSON, use Hindi'},
    ],
    build: f => `Enhance this AI prompt:\n\n"${f.raw}"\n\nGoal: ${f.goal||'as described in prompt'}\nTarget model: ${f.model}\nEnhancement style: ${f.style}\nConstraints: ${f.extra||'none'}\n\nShow: 1) Analysis of original prompt's weaknesses 2) Enhanced version 3) Why each change improves it.`
  }
};

// Tool accent colours for header badge
const TOOL_COLORS = {
  resume:'#f4a261', email:'#64c8ff', code:'#2ecc71',
  startup:'#ffc83c', sql:'#a782ff', prompt:'#e63946'
};

function openTool(type){
  const def = TOOL_DEFS[type];
  if(!def) return;
  currentTool = type;

  // Populate modal header
  $('tm-icon').textContent  = def.icon;
  $('tm-title').textContent = def.label;
  $('tm-desc').textContent  = def.desc;

  // Badge
  const badge = $('tm-badge');
  badge.textContent = def.badge;
  badge.className   = 'tm-mode-badge ' + def.cls;

  // Use count
  const uses = (S.toolAnalytics[type] && S.toolAnalytics[type].uses) || 0;
  $('tm-use-count').textContent = uses > 0 ? `Used ${uses}× by you` : 'First time using this tool';

  // Render form fields
  $('tm-body').innerHTML = def.fields.map(f => {
    const req = f.required ? '<span class="tm-req">*</span>' : '';
    let input = '';
    if(f.type === 'input'){
      input = `<input class="tm-input" id="tf-${f.id}" placeholder="${escH(f.placeholder||'')}" autocomplete="off">`;
    } else if(f.type === 'textarea'){
      const rows = f.rows || 3;
      input = `<textarea class="tm-textarea" id="tf-${f.id}" placeholder="${escH(f.placeholder||'')}" rows="${rows}"></textarea>`;
    } else if(f.type === 'select'){
      const opts = f.options.map(o=>`<option value="${escH(o)}">${escH(o)}</option>`).join('');
      input = `<select class="tm-select" id="tf-${f.id}">${opts}</select>`;
    }
    const hint = f.hint ? `<div class="tm-hint">${escH(f.hint)}</div>` : '';
    return `<div class="tm-field"><label class="tm-label">${escH(f.label)} ${req}</label>${input}${hint}</div>`;
  }).join('');

  $('tool-overlay').classList.add('open');
  // Focus first required input
  setTimeout(()=>{
    const first = $('tool-overlay').querySelector('.tm-input, .tm-textarea');
    if(first) first.focus();
  }, 120);
}

function closeTool(){
  $('tool-overlay').classList.remove('open');
}

function launchTool(){
  const def = TOOL_DEFS[currentTool];
  if(!def) return;

  // Collect field values, validate required
  const vals = {};
  let missing = [];
  for(const f of def.fields){
    const el = $('tf-'+f.id);
    if(!el) continue;
    vals[f.id] = el.value.trim();
    if(f.required && !vals[f.id]) missing.push(f.label);
  }
  if(missing.length){
    toast('⚠ Please fill: ' + missing.join(', '));
    // Highlight missing
    missing.forEach(lbl => {
      const field = def.fields.find(f=>f.label===lbl);
      if(field){ const el=$('tf-'+field.id); if(el){ el.style.borderColor='var(--r)'; setTimeout(()=>el.style.borderColor='',2000); } }
    });
    return;
  }

  // Track analytics
  if(!S.toolAnalytics[currentTool]) S.toolAnalytics[currentTool] = {uses:0, lastUsed:null};
  S.toolAnalytics[currentTool].uses++;
  S.toolAnalytics[currentTool].lastUsed = new Date().toISOString();
  saveS();

  // Build prompt
  const prompt = def.build(vals);

  // Set Tool Mode badge in header
  setToolModeBadge(currentTool, def);

  // Store active tool system prompt
  window._activeToolSystemPrompt = def.systemPrompt;
  window._activeToolType = currentTool;

  closeTool();

  // Send to chat
  $('mi').value = prompt;
  autoR($('mi'));
  send();

  toast(`${def.icon} ${def.label} activated — generating with FRIDAY!`);
}

function setToolModeBadge(type, def){
  const pill = $('toolmode-hdr');
  const col  = TOOL_COLORS[type] || '#e63946';
  pill.style.cssText = `display:flex;background:${col}18;border-color:${col}55;color:${col}`;
  $('toolmode-hdr-icon').textContent = def.icon;
  $('toolmode-hdr-label').textContent = def.label.replace(/ GENERATOR| BUILDER| ENHANCER/,'') + ' MODE';
}

function clearToolMode(){
  window._activeToolSystemPrompt = null;
  window._activeToolType = null;
  const pill = $('toolmode-hdr');
  if(pill) pill.style.display = 'none';
  currentTool = null;
}

// Analytics modal
function openAnalytics(){
  const tools = Object.entries(TOOL_DEFS);
  const totalUses = tools.reduce((s,[k])=> s + ((S.toolAnalytics[k]&&S.toolAnalytics[k].uses)||0), 0);
  const mostUsed  = tools.reduce((best,[k]) => {
    const u=(S.toolAnalytics[k]&&S.toolAnalytics[k].uses)||0;
    return u > (best[1]||0) ? [k,u] : best;
  }, ['—',0]);

  $('an-summary').innerHTML = `
    <div class="an-card"><div class="an-val">${totalUses}</div><div class="an-lbl">TOTAL USES</div></div>
    <div class="an-card"><div class="an-val">${tools.filter(([k])=>(S.toolAnalytics[k]&&S.toolAnalytics[k].uses)>0).length}</div><div class="an-lbl">TOOLS USED</div></div>
    <div class="an-card"><div class="an-val">${mostUsed[0]!=='—'?(TOOL_DEFS[mostUsed[0]].icon+' '+mostUsed[1]+'×'):'—'}</div><div class="an-lbl">MOST USED</div></div>`;

  const maxUse = Math.max(1, ...tools.map(([k])=>(S.toolAnalytics[k]&&S.toolAnalytics[k].uses)||0));
  $('an-list').innerHTML = tools.map(([k, def]) => {
    const uses = (S.toolAnalytics[k]&&S.toolAnalytics[k].uses)||0;
    const last = S.toolAnalytics[k]&&S.toolAnalytics[k].lastUsed
      ? new Date(S.toolAnalytics[k].lastUsed).toLocaleDateString() : 'Never';
    const col  = TOOL_COLORS[k] || '#e63946';
    const pct  = Math.round((uses/maxUse)*100);
    return `<div class="an-row">
      <span class="an-tool-icon">${def.icon}</span>
      <div style="flex:1;min-width:0">
        <div class="an-tool-name">${def.label}</div>
        <div style="font-family:'Share Tech Mono',monospace;font-size:.48rem;color:rgba(255,255,255,.2);margin-top:2px">Last: ${last}</div>
      </div>
      <div class="an-bar-wrap"><div class="an-bar" style="width:${pct}%;background:${col}"></div></div>
      <span class="an-count">${uses}×</span>
    </div>`;
  }).join('');

  $('analytics-modal').classList.add('open');
}
function closeAnalytics(){ $('analytics-modal').classList.remove('open'); }

// Close modals on Escape
document.addEventListener('keydown', e=>{
  if(e.key==='Escape'){ closeTool(); closeAnalytics(); }
});

// ══════════════════════════════════════════════
//  STATS
// ══════════════════════════════════════════════
function updStats(){
  let wc=0; history.forEach(x=>{ wc+=x.content.split(/\s+/).length; });
  $('stm').textContent = history.length;
  $('sts').textContent = Object.keys(S.sessions).length;
  $('stw').textContent = wc>999?(wc/1000).toFixed(1)+'k':wc;
  $('stt').textContent = Math.floor((Date.now()-t0)/60000)+'m';
  updBadge();
}

// ══════════════════════════════════════════════
//  DEVELOPER MODE STATE
// ══════════════════════════════════════════════
let devMode = false;

function setMode(m){
  devMode = (m === 'dev');
  $('dtnorm').classList.toggle('on', !devMode);
  $('dtdev').classList.toggle('on', devMode);
  const badge = $('modebdg');
  badge.textContent = devMode ? '⚡ DEV MODE' : 'NORMAL';
  badge.classList.toggle('dev', devMode);
  const area = $('miarea');
  if(area){
    area.placeholder = devMode
      ? '💻 Dev Mode: Ask me to write Python, JS, SQL, bash...'
      : 'Type in any language... हिंदी, English, தமிழ், বাংলா...';
  }
  renderMsgs();
  toast(devMode ? '🧠 Developer Mode ON — syntax highlighting & copy active' : '⬜ Normal Mode');
}

function copyCode(id){
  const code = _codeStore[id] || '';
  function markCopied(){
    const btn = $('cp-'+id);
    if(btn){
      btn.textContent = '✓ COPIED';
      btn.classList.add('ok');
      setTimeout(()=>{ btn.textContent='⎘ COPY'; btn.classList.remove('ok'); }, 2000);
    }
    toast('✅ Code copied to clipboard!');
  }

  // Method 1: modern async clipboard API
  if(navigator.clipboard && typeof navigator.clipboard.writeText === 'function'){
    navigator.clipboard.writeText(code).then(markCopied).catch(tryExecCommand);
    return;
  }
  tryExecCommand();

  function tryExecCommand(){
    // Method 2: execCommand with a persistent offscreen textarea
    let ta = document.getElementById('_copy_helper');
    if(!ta){
      ta = document.createElement('textarea');
      ta.id = '_copy_helper';
      ta.setAttribute('readonly', '');
      ta.style.cssText = 'position:fixed;top:-9999px;left:-9999px;width:1px;height:1px;opacity:0;';
      document.body.appendChild(ta);
    }
    ta.value = code;
    ta.removeAttribute('readonly');
    ta.focus();
    ta.select();
    ta.setSelectionRange(0, ta.value.length);
    let ok = false;
    try{ ok = document.execCommand('copy'); } catch(e){}
    ta.setAttribute('readonly', '');
    if(ok){ markCopied(); return; }

    // Method 3: ClipboardItem API
    if(window.ClipboardItem && navigator.clipboard && navigator.clipboard.write){
      const blob = new Blob([code], {type:'text/plain'});
      navigator.clipboard.write([new ClipboardItem({'text/plain': blob})])
        .then(markCopied).catch(showManual);
      return;
    }
    showManual();
  }

  function showManual(){
    // Method 4: prompt dialog — always accessible, user presses Ctrl+C
    window.prompt('Press Ctrl+C / Cmd+C to copy:', code);
    markCopied();
  }
}

// ══════════════════════════════════════════════
//  CODE STORE — avoids HTML-attribute escaping bugs
// ══════════════════════════════════════════════
const _codeStore = {};

// ══════════════════════════════════════════════
//  MARKDOWN → HTML  (with Dev Mode code blocks)
// ══════════════════════════════════════════════
let _cbId = 0;

function md2h(raw){
  // Step 1: extract fenced code blocks first, replace with unique placeholders
  const blocks = [];
  const withPlaceholders = raw.replace(/```(\w*)\n([\s\S]*?)```/g, (_, lang, code) => {
    const id = 'PH' + (_cbId++) + 'PH';
    blocks.push({ id, lang: lang||'', code: code.trim() });
    return id;
  });

  // Step 2: process inline markdown on the non-code text
  function processInline(text){
    const lines = text.split('\n');
    const out = []; let io=false, iu=false;
    for(const ln of lines){
      const mo = ln.match(/^(\d+)\.\s+(.*)/);
      const mu = ln.match(/^[-*]\s+(.*)/);
      if(mo){
        if(iu){out.push('</ul>');iu=false;}
        if(!io){out.push('<ol style="margin:5px 0 5px 18px">');io=true;}
        out.push('<li>'+processSpan(mo[2])+'</li>');
      } else if(mu){
        if(io){out.push('</ol>');io=false;}
        if(!iu){out.push('<ul style="margin:5px 0 5px 18px">');iu=true;}
        out.push('<li>'+processSpan(mu[1])+'</li>');
      } else {
        if(io){out.push('</ol>');io=false;}
        if(iu){out.push('</ul>');iu=false;}
        out.push(processSpan(ln));
      }
    }
    if(io) out.push('</ol>');
    if(iu) out.push('</ul>');
    return out.join('\n').replace(/\n{2,}/g,'<br><br>').replace(/\n/g,'<br>');
  }

  function processSpan(s){
    s = escH(s);
    s = s.replace(/`([^`]+)`/g, '<code>$1</code>');
    s = s.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
    s = s.replace(/__(.+?)__/g, '<strong>$1</strong>');
    s = s.replace(/\*(.+?)\*/g, '<em>$1</em>');
    return s;
  }

  // Step 3: process inline text between placeholders
  const parts = withPlaceholders.split(/(PH\d+PH)/);
  const result = parts.map(part => {
    // If this part is a placeholder, replace with code block HTML
    const block = blocks.find(b => b.id === part);
    if(block){
      if(devMode){
        const cbId = 'cb' + (_cbId++);
        _codeStore[cbId] = block.code;   // store raw code — no escaping issues
        const escaped = escH(block.code);
        const langAttr = block.lang || 'plaintext';
        return `<div class="dev-pre">
  <div class="dev-hdr">
    <span class="dev-lang">◈ ${block.lang || 'code'}</span>
    <button class="dev-btn dev-copy" id="cp-${cbId}" onclick="copyCode('${cbId}')">⎘ COPY</button>
  </div>
  <pre><code class="language-${langAttr}">${escaped}</code></pre>
</div>`;
      } else {
        return `<pre><code>${escH(block.code)}</code></pre>`;
      }
    }
    // Otherwise process as inline markdown
    return processInline(part);
  });

  return result.join('');
}

function applyHighlight(){
  if(!devMode || typeof hljs === 'undefined') return;
  document.querySelectorAll('.dev-pre pre code:not([data-highlighted])').forEach(el=>{
    hljs.highlightElement(el);
  });
}

// ══════════════════════════════════════════════
//  RENDER MESSAGES
// ══════════════════════════════════════════════
function renderMsgs(){
  const c = $('msgs');
  if (!history.length){
    c.innerHTML = `<div id="emp">
      <div class="ei">
        <span class="e">🤖</span>
        <div class="rg" style="position:absolute;inset:0;border-radius:50%;
          border:1px dashed rgba(230,57,70,0.18);animation:spin 12s linear infinite"></div>
      </div>
      <p class="el">AWAITING INPUT</p>
      <p class="es2">Start a conversation with FRIDAY</p>
    </div>`;
    return;
  }
  c.innerHTML = history.map((m,i) => {
    const u = m.role==='user';
    const content = u
      ? `<p style="margin:0;white-space:pre-wrap">${escH(m.content)}</p>`
      : md2h(m.content);
    return `<div class="mw ${u?'u':'ai'}" style="animation-delay:${Math.min(i*.025,.18)}s">
      <div class="mav">${u?'👤':'🤖'}</div>
      <div class="mbd">
        <div class="mb">${content}</div>
        <div class="mt">${u ? m.time : 'FRIDAY · '+m.time}</div>
      </div>
    </div>`;
  }).join('');
  requestAnimationFrame(()=>{ c.scrollTop = c.scrollHeight; applyHighlight(); });
}

// ══════════════════════════════════════════════
//  SEND
// ══════════════════════════════════════════════
function hKey(e){ if(e.key==='Enter'&&!e.shiftKey){ e.preventDefault(); send(); } }
function autoR(el){ el.style.height='auto'; el.style.height=Math.min(el.scrollHeight,136)+'px'; }

async function send(){
  const inp=$('mi'), msg=inp.value.trim(); if(!msg) return;
  inp.value=''; autoR(inp); showQ(false);
  // ── Auto-memory detection ──
  const wasMemory = tryAutoMemory(msg);
  console.log("History length before push:", history.length);
  history.push({role:'user', content:msg, time:nowT()});
  if(S.sessions[S.curSid]){
    S.sessions[S.curSid].messages = history;
    if(S.sessions[S.curSid].title==='New Session'){
      S.sessions[S.curSid].title = msg.slice(0,40);
      setHdr(msg.slice(0,40).toUpperCase(), false);
      renderSess();
    }
  }
  saveS(); renderMsgs(); updStats();
  $('typ').style.display  = 'block';
  $('sndb').disabled      = true;
  $('msgs').scrollTop     = $('msgs').scrollHeight;

  const reply = await callAI(msg);
  $('typ').style.display  = 'none';
  $('sndb').disabled      = false;
  if(reply){
    history.push({role:'assistant', content:reply, time:nowT()});
    if(S.sessions[S.curSid]) S.sessions[S.curSid].messages = history;
    saveS(); renderMsgs(); updStats();
  }
}

// ══════════════════════════════════════════════
//  MEMORY MODE — Persistent AI Personality
// ══════════════════════════════════════════════

// Tag classifier — auto-labels what kind of memory it is
const MEM_TAGS = [
  { tag:'NAME',    rx:/\b(?:my name is|i(?:'m| am) called|call me)\s+(\w+)/i },
  { tag:'GOAL',    rx:/\b(?:preparing for|studying for|working towards|my goal is|i want to become|aiming for)\b/i },
  { tag:'STYLE',   rx:/\b(?:always (?:reply|respond|write|answer)|prefer|formal|casual|brief|detailed|in (?:bullet|points|hindi|english|short))\b/i },
  { tag:'TOPIC',   rx:/\b(?:interested in|learning about|focused on|working on|my project|my startup|my topic)\b/i },
  { tag:'ABOUT',   rx:/\b(?:i am|i'm|i work|i study|my job|my profession|i live|my age|i have)\b/i },
];

function classifyMem(text){
  for(const {tag, rx} of MEM_TAGS) if(rx.test(text)) return tag;
  return 'NOTE';
}

// Auto-detect "remember" intent in user messages
const REMEMBER_RX = /\b(?:remember(?: that)?|don't forget(?: that)?|keep in mind(?: that)?|note that|i want you to know(?: that)?|please remember)\b/i;

function tryAutoMemory(msg){
  if(!REMEMBER_RX.test(msg)) return false;
  // Strip the trigger phrase and save the rest
  const clean = msg
    .replace(REMEMBER_RX,'')
    .replace(/^[\s,.:;-]+/,'')
    .replace(/[.!]+$/,'')
    .trim();
  if(clean.length < 4) return false;
  _saveMemory(clean);
  return true;
}

function _saveMemory(text){
  const tag  = classifyMem(text);
  const id   = Date.now().toString(36);
  const mem  = { id, tag, text, ts: new Date().toISOString() };
  // Avoid near-duplicates (80% similarity check by first 40 chars)
  const key = text.toLowerCase().slice(0,40);
  if(S.memories.some(m => m.text.toLowerCase().slice(0,40) === key)) return false;
  S.memories.unshift(mem);
  if(S.memories.length > 40) S.memories = S.memories.slice(0,40); // cap at 40
  saveS();
  renderMemories();
  return true;
}

function addMemory(){
  const inp = $('mem-inp');
  const text = inp.value.trim();
  if(!text){ inp.focus(); return; }
  const added = _saveMemory(text);
  if(added){
    inp.value = '';
    toast('🧠 Memory saved — FRIDAY will remember this!');
  } else {
    toast('⚠ Already remembered something similar!');
  }
}

function delMemory(id){
  S.memories = S.memories.filter(m => m.id !== id);
  saveS();
  renderMemories();
  toast('🗑 Memory removed');
}

function clearMemories(){
  if(!confirm('Clear all memories? FRIDAY will forget everything.')) return;
  S.memories = [];
  saveS();
  renderMemories();
  toast('🧠 All memories cleared');
}

// Tag colour map
const TAG_COLORS = {
  NAME:'#f4a261', GOAL:'#e63946', STYLE:'#a8dadc',
  TOPIC:'#2ecc71', ABOUT:'#c77dff', NOTE:'rgba(255,255,255,.4)'
};

function renderMemories(){
  const list = $('mem-list');
  if(!list) return;
  const pill = $('mem-hdr-pill');
  const cnt  = $('mem-hdr-count');
  if(!S.memories.length){
    list.innerHTML = '<div class="mem-empty">No memories yet — tell me something!</div>';
    if(pill){ pill.style.display='none'; }
    return;
  }
  // Show header pill
  if(pill){ pill.style.display='flex'; }
  if(cnt){ cnt.textContent = S.memories.length; }

  list.innerHTML = S.memories.map(m => {
    const col = TAG_COLORS[m.tag] || TAG_COLORS.NOTE;
    return `<div class="mem-item" id="mi-${m.id}">
      <span class="mem-tag" style="color:${col};border-color:${col}40;background:${col}18">${m.tag}</span>
      <span class="mem-text">${escH(m.text)}</span>
      <button class="mem-del" onclick="delMemory('${m.id}')" title="Forget this">✕</button>
    </div>`;
  }).join('');

  // Add clear-all button if >1 memory
  if(S.memories.length > 1){
    list.innerHTML += `<div style="text-align:right;margin-top:3px">
      <button onclick="clearMemories()" style="background:transparent;border:none;
        font-family:'Share Tech Mono',monospace;font-size:.55rem;
        color:rgba(255,100,100,.4);cursor:pointer;letter-spacing:.06em"
        onmouseover="this.style.color='rgba(255,100,100,.85)'"
        onmouseout="this.style.color='rgba(255,100,100,.4)'">✕ clear all</button></div>`;
  }
}

// Build the memory context string injected into system prompt
function buildMemoryContext(){
  if(!S.memories.length) return '';
  const lines = S.memories.map(m => `[${m.tag}] ${m.text}`).join('\n');
  return `\n\n━━ USER MEMORY (always use this context) ━━\n${lines}\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━`;
}

// ══════════════════════════════════════════════
//  GROQ API  — key lives in Python backend only
// ══════════════════════════════════════════════
async function callAI(msg){
  if (!GROQ_KEY || GROQ_KEY === 'YOUR_GROQ_KEY_HERE'){
    toast('⚠ Open friday.py and set GROQ_API_KEY on line 5');
    return null;
  }
  const model  = $('mdl').value;
  const lparts = $('lng').value.split('|');
  const langP  = lparts[2] || 'Respond in English.';
  const devExtra = devMode ? ' You are in DEVELOPER MODE. Always use fenced code blocks with language tags (e.g. ```python). Write clean, well-commented code.' : '';
  const memCtx   = buildMemoryContext();
  // Tool-specific system prompt overrides when a tool is active
  const toolSys  = window._activeToolSystemPrompt || null;
  const baseSys  = toolSys
    ? `${toolSys}${memCtx}`
    : `You are FRIDAY, a brilliant AI assistant. ${langP}${devExtra}${memCtx}`;
  const msgs   = [
    {role:'system', content: baseSys},
    ...history.slice(-40).map(m=>({role:m.role, content:m.content}))
  ];
  // Clear tool system prompt after first use (one-shot mode)
  if(window._activeToolSystemPrompt) window._activeToolSystemPrompt = null;
  try{
    const r = await fetch('https://api.groq.com/openai/v1/chat/completions',{
      method:'POST',
      headers:{'Content-Type':'application/json','Authorization':'Bearer '+GROQ_KEY},
      body: JSON.stringify({model, messages:msgs, temperature:0.7, max_tokens:2048})
    });
    if(!r.ok){
      const e=await r.json().catch(()=>({}));
      toast('⚠ API Error: '+(e.error?.message||r.statusText));
      return null;
    }
    return (await r.json()).choices?.[0]?.message?.content || null;
  }catch(e){
    toast('⚠ Network error — check internet connection');
    return null;
  }
}

// ══════════════════════════════════════════════
//  VOICE
// ══════════════════════════════════════════════
let vR=null, vOn=false, vFin='';
function buildWaves(){
  const w=$('wvb'); w.innerHTML='';
  for(let i=0;i<14;i++){
    const d=document.createElement('div'); d.className='wb';
    d.style.animationDelay=(i*.08).toFixed(2)+'s'; w.appendChild(d);
  }
}
function vTog(){
  if(vOn){ vR&&vR.stop(); return; }
  const SR=window.SpeechRecognition||window.webkitSpeechRecognition;
  if(!SR){ $('vst').textContent='⚠ Chrome/Edge only'; return; }
  vR=new SR(); vR.lang=$('lng').value.split('|')[0];
  vR.continuous=true; vR.interimResults=true; vFin='';
  vR.onstart=()=>{ vOn=true; setVUI(true); };
  vR.onresult=e=>{
    let f='',it='';
    for(let i=0;i<e.results.length;i++){
      if(e.results[i].isFinal)f+=e.results[i][0].transcript+' ';
      else it+=e.results[i][0].transcript;
    }
    vFin=f; $('vtx').style.display='block';
    $('vtx').innerHTML=(f?`<span style="color:#fff">${f}</span>`:'')+
      (it?`<span style="color:rgba(230,57,70,.4)">${it}</span>`:'');
  };
  vR.onend=()=>{
    vOn=false; setVUI(false); const res=vFin.trim();
    if(res){ $('mi').value=res; autoR($('mi')); $('vst').textContent='✓ TRANSFERRED';
      $('vclr').style.display='inline-block';
      setTimeout(()=>$('vst').textContent='',3000); }
    else{ $('vtx').style.display='none'; $('vst').textContent='— no signal';
      setTimeout(()=>$('vst').textContent='',3000); }
  };
  vR.onerror=e=>{ vOn=false; setVUI(false); $('vst').textContent='ERR:'+e.error; };
  vR.start();
}
function setVUI(on){
  $('vbtn').classList.toggle('rc',on);
  $('wvb').style.display=on?'flex':'none';
  $('vic').textContent=on?'⏹':'🎤';
  $('vtx2').textContent=on?'STOP REC':'VOICE INPUT';
  $('vst').textContent=on?'● REC':'';
  $('vst').style.animation=on?'pulse 1.2s infinite':'none';
}
function vClr(){
  vFin=''; $('vtx').innerHTML=''; $('vtx').style.display='none';
  $('vclr').style.display='none'; $('vst').textContent='';
  $('mi').value=''; autoR($('mi'));
}

// ══════════════════════════════════════════════
//  BOOT  — runs after DOM is ready
// ══════════════════════════════════════════════
window.addEventListener('DOMContentLoaded', function(){
  loadS();

  // Wire up login button + Enter keys
  $('lbtn').addEventListener('click', doLogin);
  $('lp').addEventListener('keydown', e=>{ if(e.key==='Enter') doLogin(); });
  $('lu').addEventListener('keydown', e=>{ if(e.key==='Enter') $('lp').focus(); });

  // Auto-login if valid session exists in localStorage
  if (S.user && USERS[S.user]) {
    showChat();
  } else {
    $('lgn').style.display = 'flex';
    $('app').style.display = 'none';
    if (S.user) $('lu').value = S.user;
  }
});
</script>

</body>
</html>"""

# Replace the API key placeholder with the actual key
secure_html = _HTML.replace(
    'const GROQ_KEY = "";',
    f'const GROQ_KEY = "{GROQ_API_KEY}";'
)

components.html(
    secure_html,
    height=800,
    scrolling=True
)

st.markdown("""<style>
iframe[title="streamlit_components_v1.html"]{
  position:fixed!important;top:0!important;left:0!important;
  width:100vw!important;height:100vh!important;
  border:none!important;z-index:9999!important;
}
</style>
<script>
// Grant clipboard-write permission to the embedded iframe
(function(){
  function patchIframe(){
    var frames = document.querySelectorAll('iframe[title="streamlit_components_v1.html"]');
    frames.forEach(function(f){
      if(!f.getAttribute('allow') || !f.getAttribute('allow').includes('clipboard-write')){
        var cur = f.getAttribute('allow') || '';
        f.setAttribute('allow', (cur ? cur + '; ' : '') + 'clipboard-write');
      }
    });
  }
  // Run now and keep watching for the iframe to appear
  patchIframe();
  var obs = new MutationObserver(patchIframe);
  obs.observe(document.body, {childList:true, subtree:true});
})();
</script>""", unsafe_allow_html=True)