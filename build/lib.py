import html, json
def E(t):
    t=t.replace('"','&quot;')
    return f'<span class="es" role="button" tabindex="0" data-say="{t}">{t}</span>'
def chips(arr): return '<div class="chips">'+''.join(E(a) for a in arr)+'</div>'
def tbl(head, rows):
    return '<div class="tw"><table><thead><tr>'+''.join(f'<th>{h}</th>' for h in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)+'</tbody></table></div>'
def warn(h): return f'<div class="note warn"><b class="lab">ATENCIÓN</b>{h}</div>'
def pero(h): return f'<div class="note pero"><b class="lab">PERO</b>{h}</div>'
def rules(items): return '<ul class="rules">'+''.join(f'<li>{i}</li>' for i in items)+'</ul>'
TIP='<p class="tip">🔊 스페인어 표현을 누르면 발음을 들을 수 있어요.</p>'
def pk(q,o,a,why=''): return {'t':'pick','q':q,'o':o,'a':a,'why':why}
def tx(q,a,why=''): return {'t':'text','q':q,'a':a if isinstance(a,list) else [a],'why':why}
def X(title,instr,rule,items): return {'title':title,'instr':instr,'rule':rule,'items':items}
def U(id,lv,es,ko,desc,vids,theory,ex): return dict(id=id,lv=lv,es=es,ko=ko,desc=desc,vids=vids,theory=theory,ex=ex)
def V(vid,title,note=''): return [vid,title,note]
def P(o,rows): return [pk(r[0],o,r[1],r[2] if len(r)>2 else '') for r in rows]
def T(rows): return [tx(r[0],r[1],r[2] if len(r)>2 else '') for r in rows]

_VI={}
for _l in open(__import__('os').path.join(__import__('os').path.dirname(__file__),'vids_raw.txt'),encoding='utf8'):
    _p=_l.rstrip('\n').split('|')
    if len(_p)>=3: _VI[int(_p[0])]=[_p[1],_p[2],_p[3] if len(_p)>3 else '']
def VS(*idx): return [_VI[i] for i in idx]
