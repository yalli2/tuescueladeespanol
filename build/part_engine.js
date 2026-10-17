const vidsHTML = c => !c.vids||!c.vids.length ? '' : `<section class="vids"><div class="eyebrow">이 단원의 출처 영상 · Tu escuela de español</div><ul>${c.vids.map(v=>`<li><a href="https://www.youtube.com/watch?v=${v[0]}" target="_blank" rel="noopener"><span class="play">▶</span><span>${v[1]}${v[2]?`<small>${v[2]}</small>`:''}</span></a></li>`).join('')}</ul></section>`;
const pagerHTML = () => `<div class="pager">${NAV.prev?`<a href="../${NAV.prev[0]}/">← ${NAV.prev[1]}</a>`:'<span></span>'}${NAV.next?`<a href="../${NAV.next[0]}/">${NAV.next[1]} →</a>`:'<span></span>'}</div>`;
/* ---------- state ---------- */
const $ = s => document.querySelector(s);
const state = {}; // state[ch][key] = value
const marks = {}; // marks[ch][key] = 'ok'|'half'|'bad'
let focusedInput = null;
const store = {
  get(k){ try{ return JSON.parse(localStorage.getItem(k)); }catch(e){ return null; } },
  set(k,v){ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(e){} }
};
const progress = () => store.get('tee-progress') || {};
const total = ch => ch.ex.reduce((n,e)=>n+e.items.length,0);
const fmt = n => (Math.round(n*10)/10).toString();

function speak(t){
  try{ speechSynthesis.cancel(); const u=new SpeechSynthesisUtterance(t); u.lang='es-ES'; u.rate=.9; speechSynthesis.speak(u);}catch(e){}
}
document.addEventListener('click',e=>{ const s=e.target.closest('.es'); if(s) speak(s.dataset.say); });
document.addEventListener('keydown',e=>{ if((e.key==='Enter'||e.key===' ') && e.target.classList && e.target.classList.contains('es')){ e.preventDefault(); speak(e.target.dataset.say);} });

/* ---------- chapter page ---------- */
function chapter(n){
  const c = CH[0]; state[n]=state[n]||{}; marks[n]=marks[n]||{};
  const T = total(c);
    $('#app').innerHTML = `
  <div class="studybar"><div class="wrap">
    <div class="sb-row">
      <a class="home" href="../">← 전체 단원</a><span class="unit-tag lvtag">TEMA ${n}</span>
      <span class="sb-spacer"></span>
      <span class="count" id="count">답한 문제 0 / ${T}</span>
      <button class="btn" id="gradeBtn">채점하기</button>
    </div>
    <div class="keys" aria-label="스페인어 특수문자 입력"><span>입력 도우미</span>${['á','é','í','ó','ú','ñ','ü','¿','¡'].map(k=>`<button type="button" data-k="${k}">${k}</button>`).join('')}</div>
  </div></div>
  <header class="col ch-head"><div class="no">TEMA ${n}</div><h1>${c.es}<small>${c.ko}</small></h1></header>
  <main class="col">
    ${vidsHTML(c)}<section class="theory">${fmtTheory(c.theory)}</section>
    ${c.ex.map((e,ei)=>exHTML(n,e,ei)).join('')}
    <section class="result" id="result" hidden aria-live="polite"></section>
    ${pagerHTML()}
  </main>`;
  // restore state
  c.ex.forEach((e,ei)=>e.items.forEach((it,ii)=>{
    const k=`${ei}-${ii}`, v=state[n][k]; const li=document.getElementById(`i-${k}`);
    if(v!==undefined && v!==''){ if(it.t==='text') li.querySelector('input').value=v; else setPick(li,it,v); }
    if(marks[n][k]) showMark(n,ei,ii);
  }));
  updateCount(n);
  $('#gradeBtn').addEventListener('click',()=>grade(n));
  document.querySelector('.keys').addEventListener('mousedown',e=>{ if(e.target.dataset.k) e.preventDefault(); });
  document.querySelector('.keys').addEventListener('click',e=>{
    const k=e.target.dataset.k; if(!k) return;
    const inp = focusedInput && document.body.contains(focusedInput) ? focusedInput : null;
    if(!inp) return;
    const s=inp.selectionStart??inp.value.length, en=inp.selectionEnd??s;
    inp.value=inp.value.slice(0,s)+k+inp.value.slice(en); inp.setSelectionRange(s+1,s+1); inp.focus();
    inp.dispatchEvent(new Event('input',{bubbles:true}));
  });
  if(Object.keys(lastResult[n]||{}).length) renderResult(n,false);
}
const lastResult = {};


const NOBREAK='(?<!\\bSra?)(?<!\\bDra?)(?<!\\bSrta)(?<!\\bUds?)(?<!\\bEE)';
function fmtQ(s){
  if(!s) return s;
  s=s.replace(/ (?=–)/g,'<br>');
  s=s.replace(new RegExp('(?<![A-Za-z]\\.[A-Z])'+NOBREAK+'([.!?…])\\s+(?=[¿¡A-ZÁÉÍÓÚÑ(\\[])','g'),'$1<br>');
  return s;
}
function fmtTheory(h){
  const ES='<span class="es"';
  h=h.replace(/<\/span>(?:\s*[·\/]\s*|\s+)(?=<span class=\"es\")/g,'</span><br>');
  h=h.replace(/(<span class="es"[^>]*>)([^<]*)(<\/span>)/g,(m,a,t,c)=>a+fmtQ(t)+c);
  h=h.replace(/(<br>)\s*(<br>)/g,'$1');
  h=h.replace(/(:\s*)(<span class="es"[^>]*>[^<]*<\/span><br><span class="es")/g,'$1<br>$2');
  return h;
}
function exHTML(n,e,ei){
  return `<section class="ex" id="ex${ei}">
    <div class="ex-head"><h2>${e.title}</h2><span class="ex-score" id="sc${ei}"></span></div>
    <p class="instr">${e.instr}</p>
    <ol class="items">${e.items.map((it,ii)=>{
      const k=`${ei}-${ii}`; const [a,b]=it.q.split('___').map(fmtQ);
      const body = it.t==='text'
        ? `${a}<input type="text" id="in-${n}-${k}" data-k="${k}" autocomplete="off" autocapitalize="none" spellcheck="false" aria-label="${ii+1}번 답">${b||''}`
        : `${a}<span class="blank" id="bl-${n}-${k}"></span>${b||''}<div class="opts" role="radiogroup" aria-label="${ii+1}번 선택지">${it.o.map(o=>`<button type="button" role="radio" aria-checked="false" data-k="${k}" data-v="${o.replace(/"/g,'&quot;')}">${o}</button>`).join('')}</div>`;
      return `<li class="item" id="i-${k}"><span class="n">${ii+1}</span><div class="q">${body}</div><div class="fb" id="fb-${k}"></div></li>`;
    }).join('')}</ol></section>`;
}

function setPick(li,it,v){
  li.querySelector('.blank').textContent=v;
  li.querySelectorAll('.opts button').forEach(b=>b.setAttribute('aria-checked',b.dataset.v===v?'true':'false'));
}
function clearMark(n,k){
  delete marks[n][k]; const li=document.getElementById('i-'+k); if(!li) return;
  li.classList.remove('ok','bad','half'); document.getElementById('fb-'+k).innerHTML='';
}
function updateCount(n){
  const c=CH[0]; let a=0; c.ex.forEach((e,ei)=>e.items.forEach((it,ii)=>{ const v=state[n][`${ei}-${ii}`]; if(v!==undefined&&v!=='') a++; }));
  const el=$('#count'); if(el) el.textContent=`답한 문제 ${a} / ${total(c)}`; return a;
}

document.addEventListener('focusin',e=>{ if(e.target.matches && e.target.matches('.q input')) focusedInput=e.target; });
document.addEventListener('input',e=>{
  const t=e.target; if(!t.matches||!t.matches('.q input')) return;
  const n=curChapter(); const k=t.dataset.k; state[n][k]=t.value; clearMark(n,k); updateCount(n);
});
document.addEventListener('click',e=>{
  const b=e.target.closest('.opts button'); if(!b) return;
  const n=curChapter(); const k=b.dataset.k; const [ei,ii]=k.split('-').map(Number); const it=CH[0].ex[ei].items[ii];
  state[n][k]=b.dataset.v; setPick(document.getElementById('i-'+k),it,b.dataset.v); clearMark(n,k); updateCount(n);
});
document.addEventListener('keydown',e=>{
  if(e.key==='Enter' && e.target.matches && e.target.matches('.q input')){
    const ins=[...document.querySelectorAll('.q input')]; const i=ins.indexOf(e.target); if(ins[i+1]) ins[i+1].focus();
  }
});
const curChapter = () => SINGLE;

/* ---------- grading ---------- */
const strip = s => s.replace(/ñ/g,'\u0001').normalize('NFD').replace(/[̀-ͯ]/g,'');
const norm = s => s.toLowerCase().trim().replace(/\s+/g,' ').replace(/[.!?]+$/,'');
function judge(it,v){
  if(v===undefined||v==='') return 'none';
  if(it.t==='pick') return v===it.a?'ok':'bad';
  const x=norm(v);
  if(it.a.some(a=>norm(a)===x)) return 'ok';
  if(it.a.some(a=>strip(norm(a))===strip(x))) return 'half';
  return 'bad';
}
function showMark(n,ei,ii){
  const k=`${ei}-${ii}`, it=CH[0].ex[ei].items[ii], m=marks[n][k], li=document.getElementById('i-'+k), fb=document.getElementById('fb-'+k);
  li.classList.remove('ok','bad','half'); if(!m) return; li.classList.add(m);
  const ans = it.t==='pick'?it.a:it.a[0]; const rule = CH[0].ex[ei].rule;
  const why = it.why||rule;
  const head = m==='ok'?'✔ 정답':m==='half'?`△ 악센트(´) 확인 · 정답 <b>${ans}</b> (0.5점)`:`✘ 오답 · 정답 <b>${ans}</b>`;
  fb.innerHTML = head + (why?`<span class="why"><b>해설</b> ${why}</span>`:'');
}
function grade(n){
  const c=CH[0]; const res={ex:[],score:0,total:0,blank:0};
  c.ex.forEach((e,ei)=>{
    let s=0;
    e.items.forEach((it,ii)=>{
      const k=`${ei}-${ii}`, j=judge(it,state[n][k]);
      if(j==='none'){ marks[n][k]='bad'; res.blank++; } else marks[n][k]=j;
      if(j==='ok') s+=1; else if(j==='half') s+=.5;
      showMark(n,ei,ii);
      if(j==='none'){ document.getElementById('fb-'+k).innerHTML='✘ 미응답 · 정답 <b>'+(it.t==='pick'?it.a:it.a[0])+'</b>'+`<span class="why"><b>해설</b> ${it.why||e.rule}</span>`; }
    });
    document.getElementById('sc'+ei).textContent=`${fmt(s)} / ${e.items.length}`;
    res.ex.push({title:e.title,s,t:e.items.length}); res.score+=s; res.total+=e.items.length;
  });
  lastResult[n]=res;
  const pr=progress(); const old=pr['ch'+n];
  if(!old||res.score>=old.score){ pr['ch'+n]={score:res.score,total:res.total}; store.set('tee-progress',pr); }
  renderResult(n,true);
}
function renderResult(n,scroll){
  const res=lastResult[n], pct=Math.round(res.score/res.total*100), name=(store.get('tee-name')||'').trim();
  const msg = pct>=90?['훌륭해요!','거의 완벽합니다. 다음 단원으로 넘어가도 좋아요.']:pct>=70?['잘했어요!','틀린 문제의 해설을 읽고 다시 도전해 보세요.']:pct>=50?['조금만 더!','문법 정리를 한 번 더 읽고 틀린 문제를 다시 풀어 보세요.']:['다시 도전해요','문법 정리를 천천히 읽고 예문을 소리 내어 따라 해 보세요.'];
  const R=54, C=2*Math.PI*R;
  const el=$('#result'); el.hidden=false;
  el.innerHTML=`
   <div class="r-top">
    <div class="ring"><svg viewBox="0 0 132 132" aria-hidden="true"><circle class="bg" cx="66" cy="66" r="${R}"/><circle class="fg" cx="66" cy="66" r="${R}" stroke-dasharray="${C*pct/100} ${C}"/></svg><b>${pct}%</b></div>
    <div class="r-txt"><div class="eyebrow">${name?name+' · ':''}TEMA ${n} 결과</div><h2>${fmt(res.score)} / ${res.total}점 · ${msg[0]}</h2><p>${msg[1]}</p>${res.blank?`<p>풀지 않은 문제가 ${res.blank}개 있어요. 오답으로 처리되었습니다.</p>`:''}</div>
   </div>
   <div class="brk">${res.ex.map(e=>`<div><span>${e.title}</span><span class="bar"><i style="width:${e.s/e.t*100}%"></i></span><span>${fmt(e.s)}/${e.t}</span></div>`).join('')}</div>
   <div class="r-act"><button class="btn" id="retryWrong">틀린 문제만 다시 풀기</button><button class="btn ghost" id="retryAll">처음부터 다시 풀기</button></div>`;
  $('#retryWrong').onclick=()=>retry(n,false); $('#retryAll').onclick=()=>retry(n,true);
  if(scroll) el.scrollIntoView({behavior:'smooth',block:'center'});
}
function retry(n,all){
  const c=CH[0];
  c.ex.forEach((e,ei)=>e.items.forEach((it,ii)=>{
    const k=`${ei}-${ii}`, m=marks[n][k];
    if(all || m!=='ok'){
      delete state[n][k]; clearMark(n,k); const li=document.getElementById('i-'+k);
      if(it.t==='text') li.querySelector('input').value=''; else { li.querySelector('.blank').textContent=''; li.querySelectorAll('.opts button').forEach(b=>b.setAttribute('aria-checked','false')); }
    }
  }));
  c.ex.forEach((e,ei)=>{ $('#sc'+ei).textContent=''; });
  delete lastResult[n]; $('#result').hidden=true; updateCount(n);
  const first=document.querySelector('li.item:not(.ok)'); if(first) first.scrollIntoView({behavior:'smooth',block:'center'}); else window.scrollTo({top:0,behavior:'smooth'});
}

/* ---------- router ---------- */
function route(){
  chapter(SINGLE);
  window.scrollTo(0,0);
}
route();

