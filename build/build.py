import glob, importlib.util, json, os, sys, re
sys.path.insert(0,os.path.dirname(__file__))
OUT='/home/claude/tee-site'
units=[]
for f in sorted(glob.glob(os.path.join(os.path.dirname(__file__),'units_*.py'))):
    spec=importlib.util.spec_from_file_location(os.path.basename(f)[:-3],f); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); units+=m.UNITS
units.sort(key=lambda u:u['id'])
ids=[u['id'] for u in units]; assert len(set(ids))==len(ids),'dup ids'
# validation
errs=[]
for u in units:
    n=sum(len(e['items']) for e in u['ex'])
    for ei,e in enumerate(u['ex']):
        for ii,it in enumerate(e['items']):
            w=f"T{u['id']} ex{ei+1} q{ii+1}"
            if it['t']=='pick':
                if it['a'] not in it['o']: errs.append(w+' answer not in options')
                if len(set(it['o']))!=len(it['o']): errs.append(w+' dup options')
                if '___' not in it['q']: errs.append(w+' no blank')
            else:
                if '___' not in it['q']: errs.append(w+' no blank')
            if not it.get('why'): errs.append(w+' no why')
    if n<18: errs.append(f"T{u['id']} only {n} items")
if errs: print('\n'.join(errs)); sys.exit(1)
css=open(os.path.join(os.path.dirname(__file__),'part_css.html'),encoding='utf8').read()
fonts=open(os.path.join(os.path.dirname(__file__),'part_fonts.html'),encoding='utf8').read()
eng=open(os.path.join(os.path.dirname(__file__),'part_engine.js'),encoding='utf8').read()
LV={'A1':'입문 A1','A2':'초급 A2'}
eng=eng.replace('<div class="no">TEMA ${n}</div>','<div class="no">TEMA ${n}<span class="lv">${LVN[c.lv]}</span></div>')
def folder(u): return f"tema{u['id']:02d}"
def shortname(u): return f"Tema {u['id']}"
for k,u in enumerate(units):
    prev=units[k-1] if k>0 else None; nxt=units[k+1] if k+1<len(units) else None
    nav={'prev':[folder(prev),f"Tema {prev['id']}"] if prev else None,'next':[folder(nxt),f"Tema {nxt['id']}"] if nxt else None}
    nav={'prev':[folder(prev),shortname(prev)] if prev else None,'next':[folder(nxt),shortname(nxt)] if nxt else None}
    page=f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Español paso a paso · Tema {u['id']} {u['es']}</title>
{fonts}{css}</head><body>
<div id="app"></div>
<script>
const LVN={json.dumps(LV,ensure_ascii=False)};
const CH=[{json.dumps(u,ensure_ascii=False)}];
const SINGLE={u['id']};
const NAV={json.dumps(nav,ensure_ascii=False)};
{eng}
</script></body></html>'''
    d=os.path.join(OUT,folder(u)); os.makedirs(d,exist_ok=True)
    open(os.path.join(d,'index.html'),'w',encoding='utf8').write(page)
# index
cards=[]
for u in units:
    n=sum(len(e['items']) for e in u['ex'])
    cards.append(dict(id=u['id'],f=folder(u),lv=u['lv'],es=u['es'],ko=u['ko'],desc=u['desc'],n=n,v=len(u['vids'])))
idx=open(os.path.join(os.path.dirname(__file__),'index_tpl.html'),encoding='utf8').read()
idx=idx.replace('__FONTS__',fonts).replace('__CSS__',css).replace('__CARDS__',json.dumps(cards,ensure_ascii=False))
open(os.path.join(OUT,'index.html'),'w',encoding='utf8').write(idx)
tot=sum(c['n'] for c in cards)
print(len(units),'units',tot,'questions; videos referenced',len({v[0] for u in units for v in u['vids']}))
