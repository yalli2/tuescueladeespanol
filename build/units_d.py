from lib import *
UNITS=[]

UNITS.append(U(26,'A2','Las preposiciones','전치사: 장소·시간·이동',
 'en/a/de/desde/hasta, 장소 위치 표현, hace·desde·desde hace를 익힙니다.',
 VS(25,24,22,21,31),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. 장소 전치사</h3>'''+tbl(['전치사','의미','예'],[['en','~에 (정지)','Estoy en casa.'],['sobre / encima de','~ 위에','El libro está sobre la mesa.'],['debajo de','~ 아래에','El gato está debajo de la silla.'],['delante de / detrás de','앞 / 뒤','delante de la casa'],['al lado de','옆','al lado del banco'],['entre','~ 사이','entre Madrid y Barcelona'],['cerca de / lejos de','가까이 / 멀리','cerca del parque'],['enfrente de','맞은편','enfrente de la farmacia']])+'''
<h3>2. 이동 전치사</h3>'''+tbl(['전치사','의미','예'],[['a','~로','Voy a Madrid.'],['de','~에서','Vengo de Madrid.'],['desde','~부터','desde mi casa'],['hasta','~까지','hasta la plaza'],['por','~을 지나 / 근처','Paso por el parque.'],['hacia','~쪽으로','Voy hacia el centro.'],['para','~를 향해 (목적지)','Salgo para el trabajo.']])+'''
<h3>3. 시간 전치사</h3>'''+rules(['<b>a</b> + 시각: '+E('a las ocho')+'.','<b>en</b> + 월·계절·연도: '+E('en enero')+', '+E('en verano')+', '+E('en 2025')+'.','<b>de … a …</b>: '+E('de lunes a viernes')+'.','<b>desde … hasta …</b>: '+E('desde las nueve hasta las cinco')+'.','<b>por</b> la mañana/tarde/noche.','<b>hace</b> + 기간 = ~ 전에: '+E('Llegué hace dos horas')+'.','<b>desde hace</b> + 기간 = ~ 동안 (지금까지): '+E('Vivo aquí desde hace tres años')+'.','<b>desde</b> + 시점: '+E('Vivo aquí desde 2020')+'.']),
 [X('연습 1. 장소','알맞은 전치사를 고르세요.','위치 표현.',
   P(['sobre','debajo de','entre'],[['El libro está ___ la mesa. (위)','sobre','sobre = 위.']])+
   P(['debajo de','sobre','detrás de'],[['El gato está ___ la silla. (아래)','debajo de','debajo de = 아래.']])+
   P(['entre','al lado de','cerca de'],[['España está ___ Francia y Portugal. (사이)','entre','entre = 사이.']])+
   P(['enfrente de','al lado de','sobre'],[['La farmacia está ___ banco. (맞은편)','enfrente de','enfrente de = 맞은편.']])+
   P(['en','a','de'],[['Estoy ___ casa.','en','정지 상태 → en.']])+
   P(['a','en','de'],[['Voy ___ Madrid.','a','이동 → a.']])+
   P(['de','a','en'],[['Soy ___ Corea.','de','출신 → de.']])+
   P(['lejos de','cerca de','entre'],[['Corea está ___ España. (멀리)','lejos de','lejos de = 멀리.']])),
  X('연습 2. 시간','알맞은 표현을 고르세요.','a las, en, de…a, desde…hasta, hace, desde hace.',
   P(['a','en','de'],[['Quedamos ___ las ocho.','a','시각 → a las.']])+
   P(['en','a','por'],[['Nací ___ junio.','en','월 → en.']])+
   P(['de','desde','hasta'],[['Trabajo ___ lunes a viernes.','de','de … a ….']])+
   P(['desde','de','hasta'],[['Estudio ___ las nueve hasta las doce.','desde','desde … hasta ….']])+
   P(['hace','desde','hasta'],[['Llegué ___ dos horas.','hace','과거 시점 → hace.']])+
   P(['desde hace','hace','desde'],[['Vivo aquí ___ tres años.','desde hace','지금까지 → desde hace.']])+
   P(['desde','desde hace','hace'],[['Vivo aquí ___ 2020.','desde','시점 → desde.']])+
   P(['hace','desde hace','en'],[['___ dos años que vivo aquí.','hace','Hace dos años que… 구문.']])),
  X('연습 3. 직접 쓰기','알맞은 전치사를 쓰세요.','전치사 선택.',
   T([['Voy ___ trabajo en autobús. (a + el)','al','a + el = al.'],['Vengo ___ la escuela. (~에서)','de','de = 출발.'],['Vivo ___ Madrid. (~에)','en','거주 → en.'],['Caminamos ___ el parque. (~까지)','hasta','hasta = ~까지.'],['Paso ___ el centro. (~를 지나)','por','por = 지나서.'],['Estudio ___ la mañana. (~에)','por','por la mañana.'],['Nos vemos ___ lunes. (요일 앞 관사)','el','요일 앞에는 el.'],['Soy profesor ___ hace diez años. (~동안)','desde','desde hace.']]))]
))

UNITS.append(U(27,'A2','Pronombres de objeto directo e indirecto','목적격 대명사: lo/la, le/les, se lo',
 '직접목적어(lo, la, los, las), 간접목적어(le, les), 두 대명사가 함께 올 때(se lo)를 익힙니다.',
 VS(64,67,68),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. 직접목적어 (무엇을/누구를)</h3>'''+tbl(['인칭','대명사'],[['yo / tú','me / te'],['él / usted (남)','lo'],['ella / usted (여)','la'],['nosotros / vosotros','nos / os'],['ellos / ustedes','los (남·혼합) / las (여)']])+rules(['<b>동사 앞</b>: '+E('Lo compro')+'.','<b>부정문</b>: no + 대명사 + 동사 — '+E('No lo compro')+'.','<b>동사원형</b> 뒤에 붙이거나 활용 동사 앞에: '+E('Voy a comprarlo')+' = '+E('Lo voy a comprar')+'.'])+'''
<h3>2. 간접목적어 (누구에게)</h3>'''+tbl(['인칭','대명사'],[['yo / tú','me / te'],['él / ella / usted','le'],['nosotros / vosotros','nos / os'],['ellos / ellas / ustedes','les']])+rules(['<b>le/les</b>는 성별 구분이 없어요: '+E('Le doy el libro a María')+'.','<b>강조·명확화</b>: '+E('Le doy el libro a ella')+'.','간접목적어 + 직접목적어가 함께 올 때: <b>간접 → 직접</b> 순서 — '+E('Me lo das')+'.'])+warn('<b>le/les + lo/la/los/las → se lo / se la / se los / se las</b>. “le lo”는 틀려요! '+E('Se lo doy')+' (그에게 그것을 줍니다). 의미가 모호하면 <b>a él / a ella / a ustedes</b>를 덧붙여요.'),
 [X('연습 1. 직접목적어','알맞은 대명사를 고르세요.','lo/la/los/las, me/te/nos/os.',
   P(['lo','la','los'],[['¿Compras el pan? — Sí, ___ compro.','lo','el pan → lo.']])+
   P(['la','lo','las'],[['¿Ves la película? — Sí, ___ veo.','la','película 여성 단수.']])+
   P(['los','las','lo'],[['¿Tienes los libros? — Sí, ___ tengo.','los','libros 남성 복수.']])+
   P(['las','los','la'],[['¿Lees las revistas? — Sí, ___ leo.','las','revistas 여성 복수.']])+
   P(['te','me','lo'],[['¿Me llamas mañana? — Sí, ___ llamo.','te','tú 질문 → 대답은 te.']])+
   P(['lo','la','los'],[['Voy a comprar el coche. → Voy a comprar-___.','lo','원형 뒤에 붙임 (comprarlo).']])+
   P(['lo','la','los'],[['No ___ conozco. (el hombre)','lo','남성 → lo.']])+
   P(['la','lo','las'],[['No ___ entiendo. (la lección)','la','여성 → la.']])),
  X('연습 2. 간접목적어와 se lo','알맞은 대명사를 고르세요.','le/les, se lo.',
   P(['Le','Lo','La'],[['___ doy un regalo a María.','Le','a María → le.']])+
   P(['Les','Le','Los'],[['___ escribo a mis padres.','Les','a mis padres → les.']])+
   P(['me','te','le'],[['Mi madre ___ da dinero. (a mí)','me','a mí → me.']])+
   P(['se lo','le lo','lo le'],[['¿El libro? Yo ___ doy a Juan.','se lo','le lo → se lo.']])+
   P(['me la','le la','la me'],[['¿La carta? Ella ___ envía a mí.','me la','a mí + la carta → me la.']])+
   P(['se los','les los','los se'],[['¿Los regalos? Yo ___ doy a ellos.','se los','les los → se los.']])+
   P(['te lo','lo te','le lo'],[['¿Me das el libro? — Sí, ___ doy.','te lo','a ti + el libro → te lo.']])+
   P(['se las','les las','las se'],[['¿Las flores? Yo ___ regalo a mi madre.','se las','le las → se las.']])),
  X('연습 3. 직접 쓰기','대명사를 쓰세요.','대명사 선택.',
   T([['¿Ves el coche? — Sí, ___ veo.','lo','el coche → lo.'],['¿Compras la leche? — Sí, ___ compro.','la','la leche → la.'],['¿Tienes las llaves? — Sí, ___ tengo.','las','las llaves → las.'],['Doy el libro a Ana → ___ doy el libro.','le','a Ana → le.'],['Doy el libro a mis amigos → ___ doy el libro.','les','a mis amigos → les.'],['Doy el libro a Ana → ___ doy. (두 대명사)','se lo','le lo → se lo.'],['Voy a comprar-___. (el pan)','lo','comprarlo.'],['¿Me ___ explicas? (la lección)','la','la lección → la.']]))]
))

UNITS.append(U(28,'A2','Comparativos y negaciones','비교급·부정 표현',
 'más…que, menos…que, tan…como, mejor/peor 등 비교급과 no, nunca, nada, tampoco 등 부정어를 익힙니다.',
 VS(8,76),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. 비교급</h3>'''+tbl(['유형','구조','예'],[['우등','más + 형용사/부사/명사 + <b>que</b>',E('Ana es más alta que Pedro')],['열등','menos + … + que',E('Pedro es menos alto que Ana')],['동등','tan + 형용사/부사 + <b>como</b>',E('Soy tan alto como tú')],['동등 (명사)','tanto/a/os/as + 명사 + como',E('Tengo tantos libros como tú')],['동등 (동사)','동사 + tanto como',E('Trabajo tanto como tú')]])+'''
<h3>2. 불규칙 비교급</h3>'''+tbl(['원급','비교급'],[['bueno / bien','<b>mejor</b>'],['malo / mal','<b>peor</b>'],['grande','<b>mayor</b> (나이·중요도) / más grande (크기)'],['pequeño','<b>menor</b> / más pequeño']])+'''
<h3>3. 부정 표현</h3>'''+tbl(['긍정','부정'],[['algo','<b>nada</b>'],['alguien','<b>nadie</b>'],['siempre','<b>nunca</b>'],['también','<b>tampoco</b>'],['algún / alguno','<b>ningún / ninguno</b>']])+rules(['부정어가 <b>동사 뒤</b>에 오면 앞에 no를 붙여요: '+E('No tengo nada')+'. 부정어가 <b>동사 앞</b>이면 no를 쓰지 않아요: '+E('Nunca como carne')+'.','이중 부정이 가능: '+E('No como nunca nada')+'.','<b>ningún</b>은 단수 명사 앞: '+E('No tengo ningún libro')+'.']),
 [X('연습 1. 비교급','알맞은 단어를 고르세요.','más/menos…que, tan…como, mejor/peor.',
   P(['que','como','de'],[['Ana es más alta ___ Pedro.','que','más … que.']])+
   P(['como','que','de'],[['Soy tan alto ___ tú.','como','tan … como.']])+
   P(['tantos','tanto','tantas'],[['Tengo ___ libros como tú.','tantos','libros 남성 복수.']])+
   P(['mejor','más bueno','más bien'],[['Este restaurante es ___ que el otro.','mejor','bueno → mejor.']])+
   P(['peor','más malo','menos mal'],[['Hoy el tiempo es ___ que ayer.','peor','malo → peor.']])+
   P(['mayor','más grande','más mayor'],[['Mi hermano es ___ que yo. (나이)','mayor','나이 → mayor.']])+
   P(['menos','más','tan'],[['Pedro es ___ alto que Ana. (더 작다)','menos','menos … que.']])+
   P(['tan','tanto','más'],[['No es ___ difícil como parece.','tan','tan + 형용사.']])),
  X('연습 2. 부정어','알맞은 부정어를 고르세요.','nada, nadie, nunca, tampoco, ningún.',
   P(['nada','nadie','nunca'],[['No tengo ___. (아무것도)','nada','nada = 아무것도.']])+
   P(['nadie','nada','nunca'],[['No conozco a ___. (아무도)','nadie','nadie = 아무도.']])+
   P(['Nunca','Nadie','Tampoco'],[['___ como carne. (결코)','Nunca','동사 앞이므로 no 불필요.']])+
   P(['tampoco','también','nunca'],[['No me gusta el té. — A mí ___.','tampoco','부정 동의.']])+
   P(['ningún','ninguno','nada'],[['No tengo ___ problema.','ningún','단수 남성 명사 앞.']])+
   P(['No','Nunca','Nada'],[['___ tengo nada.','No','nada가 동사 뒤 → no 필요.']])+
   P(['también','tampoco','nunca'],[['Me gusta el café. — A mí ___.','también','긍정 동의.']])+
   P(['algo','nada','alguien'],[['¿Quieres ___ de beber?','algo','긍정 의문 → algo.']])),
  X('연습 3. 직접 쓰기','알맞은 단어를 쓰세요.','비교·부정.',
   T([['Es más caro ___ el otro.','que','más … que.'],['Es tan bonito ___ el otro.','como','tan … como.'],['Mi madre es ___ que yo. (나이 많은)','mayor','mayor.'],['No hay ___ en casa. (아무도)','nadie','nadie.'],['___ voy al gimnasio. (결코)','Nunca','nunca.'],['No tengo ___ hermano. (한 명도)','ningún','ningún.'],['No fumo y mi hermano ___. (도 안 해요)','tampoco','tampoco.'],['Es el ___ de todos. (가장 좋은)','mejor','mejor.']]))]
))

UNITS.append(U(29,'A2','El imperativo, ir/venir y llevar/traer','명령형·ir/venir·llevar/traer',
 '긍정 명령(tú/usted), 부정 명령, ir·venir·llevar·traer의 구분을 익힙니다.',
 VS(86,45),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. 긍정 명령형</h3>'''+rules(['<b>규칙형 tú</b> 명령 = 현재 3인칭 단수형: '+E('Habla más despacio')+', '+E('Come más fruta')+', '+E('Escribe tu nombre')+'.','<b>불규칙 8개</b>: decir → <b>di</b>, hacer → <b>haz</b>, ir → <b>ve</b>, poner → <b>pon</b>, salir → <b>sal</b>, ser → <b>sé</b>, tener → <b>ten</b>, venir → <b>ven</b>.','<b>usted</b>: 현재 접속법 3인칭 — '+E('Hable más despacio, por favor')+'.'])+'''
<h3>2. 부정 명령형</h3>'''+rules(['<b>no + 접속법</b>: '+E('No hables tan rápido')+', '+E('No comas eso')+', '+E('No salgas')+'.','대명사: 긍정은 동사 뒤에 붙이고, 부정은 동사 앞에: '+E('Dímelo')+' / '+E('No me lo digas')+'.'])+'''
<h3>3. ir / venir, llevar / traer</h3>'''+tbl(['동사','방향'],[['<b>ir</b>','말하는 곳에서 <b>멀어짐</b> (가다)'],['<b>venir</b>','말하는 곳으로 <b>가까워짐</b> (오다)'],['<b>llevar</b>','화자(또는 현재 장소)에서 <b>멀리 가져가다</b>'],['<b>traer</b>','화자(또는 현재 장소) <b>쪽으로 가져오다</b>']])+warn('상대방이 있는 곳으로 갈 때 한국어는 “갈게”라고 하지만 스페인어에서는 <b>Voy</b> (ir)를 써요. 반대로 상대가 내 쪽으로 오면 <b>vienes</b> (venir)를 써요.'),
 [X('연습 1. 명령형','알맞은 형태를 고르세요.','tú 명령, 불규칙, usted, 부정.',
   P(['Habla','Hablas','Hable'],[['(tú) ___ más despacio.','Habla','tú 명령 = 3인칭 단수.']])+
   P(['Haz','Hace','Hago'],[['(tú) ___ la tarea.','Haz','hacer → haz.']])+
   P(['Di','Dice','Diga'],[['(tú) ___ la verdad.','Di','decir → di.']])+
   P(['Ven','Viene','Vengo'],[['(tú) ___ aquí.','Ven','venir → ven.']])+
   P(['Hable','Habla','Hablas'],[['(usted) ___ más despacio, por favor.','Hable','usted 긍정 명령.']])+
   P(['hables','hablas','hable'],[['No ___ tan rápido. (tú)','hables','부정 명령 = 접속법.']])+
   P(['comas','comes','come'],[['No ___ eso. (tú)','comas','부정 명령.']])+
   P(['Pon','Pone','Pongo'],[['(tú) ___ la mesa.','Pon','poner → pon.']])),
  X('연습 2. ir/venir, llevar/traer','알맞은 동사를 고르세요.','방향 구분.',
   P(['venir','ir','traer'],[['(전화로) ¿Puedes ___ a mi casa?','venir','내 쪽으로 오다 → venir.']])+
   P(['vienes','vas','van'],[['(친구가 내 파티에 올 때) ¿___ a mi fiesta?','vienes','내 쪽으로 오다 → venir.']])+
   P(['voy','vengo','traigo'],[['(너의 집으로) Mañana ___ a tu casa.','voy','멀어짐 → ir.']])+
   P(['traigo','llevo','voy'],[['(여기로) Mañana te ___ el libro.','traigo','화자 쪽으로 가져오다 → traer.']])+
   P(['llevo','traigo','vengo'],[['(너의 집으로) Mañana te ___ el libro.','llevo','멀리 가져가다 → llevar.']])+
   P(['traer','llevar','ir'],[['¿Puedes ___ la botella aquí? (이쪽으로)','traer','traer.']])+
   P(['Lleva','Trae','Viene'],[['___ tu paraguas cuando salgas.','Lleva','가지고 나가다 → llevar.']])+
   P(['ve','ven','va'],[['Ahora no puedo ir, ___ tú. (너 가)','ve','ir → ve.']])),
  X('연습 3. 직접 쓰기','알맞은 형태를 쓰세요.','명령형.',
   T([['(tú, hacer) ___ la cama.','haz','hacer → haz.'],['(tú, decir) ___ la verdad.','di','decir → di.'],['(tú, salir) ___ de aquí.','sal','salir → sal.'],['(tú, ser) ___ bueno.','sé','ser → sé.'],['(tú, tener) ___ cuidado.','ten','tener → ten.'],['(tú, hablar) No ___ tan rápido.','hables','부정 명령.'],['(tú, ir) ___ a casa.','ve','ir → ve.'],['(usted, escribir) ___ su nombre.','Escriba','usted 명령 = 접속법.']]))]
))

UNITS.append(U(30,'A2','Pretéritos: perfecto, indefinido e imperfecto','과거 시제 비교',
 'pretérito perfecto compuesto(he + 과거분사), indefinido, imperfecto의 용법과 선택 기준을 익힙니다.',
 VS(136,130,138,2,3),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. pretérito perfecto compuesto</h3>
<p><b>haber(he, has, ha, hemos, habéis, han) + 과거분사</b>. 과거분사: -ar → <b>-ado</b>, -er/-ir → <b>-ido</b>.</p>'''+tbl(['동사','과거분사'],[['hablar','hablado'],['comer','comido'],['vivir','vivido'],['escribir','<b>escrito</b>'],['ver','<b>visto</b>'],['hacer','<b>hecho</b>'],['decir','<b>dicho</b>'],['poner','<b>puesto</b>'],['volver','<b>vuelto</b>'],['abrir','<b>abierto</b>']])+warn('✘ He escribido → ✔ <b>He escrito</b>. 불규칙 과거분사를 조심하세요. 또한 ✘ He levantado pronto → ✔ <b>Me he levantado pronto</b> (재귀대명사 필요).')+rules(['쓰임: <b>지금과 연결된 과거</b> (오늘·이번 주·올해) — '+E('Hoy he comido paella')+'.','신호어: hoy, esta semana, este año, ya, todavía no, alguna vez.'])+'''
<h3>2. indefinido</h3>'''+rules(['<b>끝난 과거의 한 순간·사건</b>: '+E('Ayer comí paella')+'.','신호어: ayer, anoche, el año pasado, en 2010, hace dos días.','-ar: -é, -aste, -ó, -amos, -asteis, -aron / -er·-ir: -í, -iste, -ió, -imos, -isteis, -ieron.'])+'''
<h3>3. imperfecto</h3>'''+rules(['<b>과거의 배경·습관·묘사</b>: '+E('Cuando era niño, vivía en Seúl')+'.','-ar: -aba, -abas, -aba, -ábamos, -abais, -aban / -er·-ir: -ía, -ías, -ía, -íamos, -íais, -ían.','불규칙은 3개뿐: <b>ser</b> (era), <b>ir</b> (iba), <b>ver</b> (veía).','<b>indefinido = 사건</b>, <b>imperfecto = 배경</b>: '+E('Llovía cuando llegué')+'.']),
 [X('연습 1. 과거분사와 perfecto','알맞은 형태를 고르세요.','불규칙 과거분사.',
   P(['escrito','escribido','escribo'],[['He ___ una carta. (escribir)','escrito','escribir → escrito.']])+
   P(['hecho','hacido','hace'],[['Hoy he ___ la tarea. (hacer)','hecho','hacer → hecho.']])+
   P(['visto','vido','ver'],[['¿Has ___ esa película? (ver)','visto','ver → visto.']])+
   P(['dicho','decido','dice'],[['Me ha ___ la verdad. (decir)','dicho','decir → dicho.']])+
   P(['comido','comiendo','comer'],[['Hoy he ___ paella.','comido','-er → -ido.']])+
   P(['hablado','hablando','hablo'],[['He ___ con mi madre.','hablado','-ar → -ado.']])+
   P(['Me he','He','Me'],[['___ levantado pronto hoy.','Me he','재귀동사: me he levantado.']])+
   P(['abierto','abrido','abre'],[['Han ___ la tienda. (abrir)','abierto','abrir → abierto.']])),
  X('연습 2. 시제 고르기','알맞은 시제를 고르세요.','신호어와 용법.',
   P(['comí','he comido','comía'],[['Ayer ___ paella.','comí','ayer → indefinido.']])+
   P(['he comido','comí','comía'],[['Hoy ___ paella.','he comido','hoy → perfecto.']])+
   P(['vivía','viví','he vivido'],[['De niño, ___ en Seúl.','vivía','습관·배경 → imperfecto.']])+
   P(['era','fue','ha sido'],[['Cuando ___ niño, jugaba mucho.','era','배경 → imperfecto.']])+
   P(['llegué','llegaba','he llegado'],[['Llovía cuando ___.','llegué','사건 → indefinido.']])+
   P(['iba','fui','he ido'],[['Todos los veranos ___ a la playa.','iba','습관 → imperfecto.']])+
   P(['nació','nacía','ha nacido'],[['Picasso ___ en 1881.','nació','과거의 한 시점 → indefinido.']])+
   P(['estudié','estudiaba','he estudiado'],[['El año pasado ___ español.','estudié','el año pasado → indefinido.']])),
  X('연습 3. 직접 쓰기','알맞은 형태를 쓰세요.','과거 시제.',
   T([['Ayer yo ___ (hablar) con Ana.','hablé','hablar 1인칭 indefinido.'],['Ayer tú ___ (comer) pizza.','comiste','comer 2인칭.'],['Ella ___ (vivir) en Madrid en 2010.','vivió','vivir 3인칭.'],['Hoy he ___ (escribir) un email.','escrito','escribir.'],['De niño, yo ___ (jugar) mucho.','jugaba','jugar imperfecto.'],['Antes ellos ___ (ser) amigos.','eran','ser imperfecto.'],['Hoy he ___ (ver) esa película.','visto','ver → visto.'],['Esta semana ___ (trabajar, yo) mucho.','he trabajado','esta semana → perfecto.']]))]
))

UNITS.append(U(31,'A1','Ortografía y pronunciación','맞춤법·발음: B/V, R/RR, Z/C/Q/K, I/Y, U',
 '헷갈리기 쉬운 철자(b/v, r/rr, z/c/q/k, i/y)와 u의 특이한 철자를 익힙니다.',
 VS(40,47,60,61,66,134),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. B와 V</h3>'''+rules(['<b>발음이 같아요</b> (둘 다 [b]). 철자만 구분하면 돼요.','<b>b</b>: -ar 동사의 <b>imperfecto -aba</b>, <b>-bir</b> 동사(escribir, recibir… 예외: hervir, servir, vivir), <b>b + l/r</b> (blanco, brazo), <b>bu-, bus-</b> (buscar).','<b>v</b>: <b>servir, vivir, hervir</b>, <b>ad-</b> 뒤 (adverbio), -ivo (activo).'])+'''
<h3>2. R와 RR</h3>'''+rules(['<b>단어 첫머리 r</b> = 강한 r [rr]: '+E('rojo')+', '+E('ropa')+'.','<b>모음 사이 r</b> = 약한 r (혀를 한 번 튕김): '+E('pero')+', '+E('caro')+'.','<b>모음 사이의 강한 r</b>은 rr로 써요: '+E('perro')+', '+E('carro')+'. perro(개)와 pero(그러나)는 의미가 달라요.','<b>n, l, s 뒤</b> r = 강한 r: '+E('Enrique')+'.'])+'''
<h3>3. Z, C, Q, K</h3>'''+rules(['<b>[k] 소리</b>: ca, <b>que</b>, <b>qui</b>, co, cu — queso, quien. (ke, ki는 qu 사용)','<b>[θ] 소리</b>: za, ce, ci, zo, zu — zapato, cena, cine.','<b>k</b>는 외래어: kilo, kiwi, kárate.','<b>-z → -ces</b> (복수): lápiz → lápices.'])+'''
<h3>4. I와 Y, 그리고 U</h3>'''+rules(['<b>y</b>는 단어 끝(소리 [i]): rey, hoy, muy / 접속사 y(그리고).','<b>gue, gui</b>: g 뒤 u는 묵음 — guerra, guitarra. 소리를 내려면 <b>güe, güi</b> — pingüino, vergüenza.','<b>qu</b> 뒤 u는 항상 묵음.']),
 [X('연습 1. B/V, R/RR','알맞은 철자를 고르세요.','철자 규칙.',
   P(['perro','pero','pe_ro'],[['“개”는 ___.','perro','perro = 개.']])+
   P(['pero','perro','pe-ro'],[['“그러나”는 ___.','pero','pero = 그러나.']])+
   P(['rojo','roxo','rrojo'],[['“빨강”은 ___.','rojo','첫머리 r은 한 개.']])+
   P(['carro','caro','cáro'],[['“자동차(중남미)”는 ___.','carro','모음 사이 rr.']])+
   P(['escribir','escrivir','escribír'],[['“쓰다”는 ___.','escribir','-bir.']])+
   P(['vivir','bibir','vibir'],[['“살다”는 ___.','vivir','vivir 예외.']])+
   P(['blanco','vlanco','bblanco'],[['“하양”은 ___.','blanco','b + l.']])+
   P(['jugaba','jugava','jugába'],[['Yo ___ al fútbol. (imperfecto)','jugaba','-aba.']])),
  X('연습 2. Z/C/Q, G/GU','알맞은 철자를 고르세요.','za ce ci zo zu / que qui / gue gui / güe güi.',
   P(['zapato','sapato','capato'],[['“신발”은 ___.','zapato','za.']])+
   P(['cena','zena','sena'],[['“저녁”은 ___.','cena','ce.']])+
   P(['queso','keso','cueso'],[['“치즈”는 ___.','queso','que.']])+
   P(['quien','kien','cuien'],[['“누구”는 ___.','quien','qui.']])+
   P(['guitarra','gitarra','guittara'],[['“기타”는 ___.','guitarra','gui.']])+
   P(['pingüino','pinguino','pinguíno'],[['“펭귄”은 ___.','pingüino','güi.']])+
   P(['lápices','lápizes','lapíces'],[['lápiz의 복수: ___.','lápices','z → c.']])+
   P(['hoy','hoi','oy'],[['“오늘”은 ___.','hoy','끝 y.']])),
  X('연습 3. 직접 쓰기','알맞은 철자를 쓰세요.','철자 채우기.',
   T([['pe___o (개, rr/r)','rr','perro = 개.'],['___ojo (빨강, r/rr)','r','첫머리는 r 하나.'],['___ueso (치즈)','q','queso.'],['___itarra (기타)','gu','guitarra.'],['___erra (전쟁)','gu','guerra.'],['___ivir (살다, b/v)','v','vivir.'],['___uscar (찾다, b/v)','b','buscar.'],['rey와 hoy의 끝소리 [i]는 ___ 로 써요.','y','단어 끝 y.']]))]
))

UNITS.append(U(32,'A1','Falsos amigos español–inglés','영어와 헷갈리는 단어 (false friends)',
 '영어와 비슷하게 생겼지만 뜻이 다른 단어(balón, carpeta, librería, embarazada 등)를 익힙니다.',
 VS(57,107,122,135),
 TIP+'''<h2>핵심 정리</h2>
<p>영어를 아는 학습자라면 꼭 조심해야 하는 “거짓 친구”입니다.</p>'''+tbl(['스페인어','진짜 뜻','영어와 혼동'],[
 ['<b>balón</b>','(축구)공','balloon (풍선) = <b>globo</b>'],
 ['<b>carpeta</b>','서류철, 폴더','carpet (카펫) = <b>alfombra</b>'],
 ['<b>librería</b>','서점','library (도서관) = <b>biblioteca</b>'],
 ['<b>embarazada</b>','임신한','embarrassed (창피한) = <b>avergonzado/a</b>'],
 ['<b>éxito</b>','성공','exit (출구) = <b>salida</b>'],
 ['<b>actual</b>','현재의','actual (실제의) = <b>real</b>'],
 ['<b>asistir</b>','참석하다','assist (돕다) = <b>ayudar</b>'],
 ['<b>soportar</b>','견디다','support (지지하다) = <b>apoyar</b>'],
 ['<b>constipado</b>','감기 걸린','constipated (변비) = <b>estreñido</b>'],
 ['<b>sensible</b>','민감한','sensible (분별있는) = <b>sensato</b>'],
 ['<b>ropa</b>','옷','rope (밧줄) = <b>cuerda</b>'],
 ['<b>sopa</b>','수프','soap (비누) = <b>jabón</b>'],
 ['<b>campo</b>','시골, 들판','camp (캠프) = <b>campamento</b>']])+warn('가장 흔한 실수: ✘ Estoy embarazada(창피해서) → <b>Tengo vergüenza / Estoy avergonzado/a</b>. embarazada는 ‘임신 중’이에요!'),
 [X('연습 1. 뜻 고르기','알맞은 단어를 고르세요.','false friends.',
   P(['balón','globo','pelota'],[['축구공은 el ___. (풍선이 아님)','balón','balón = 축구공.']])+
   P(['globo','balón','carpeta'],[['생일 파티의 풍선은 el ___.','globo','globo = 풍선.']])+
   P(['alfombra','carpeta','librería'],[['바닥에 까는 것(카펫)은 la ___.','alfombra','alfombra = 카펫.']])+
   P(['carpeta','alfombra','biblioteca'],[['서류를 넣는 폴더는 la ___.','carpeta','carpeta = 폴더.']])+
   P(['librería','biblioteca','carpeta'],[['책을 사는 곳은 la ___.','librería','librería = 서점.']])+
   P(['biblioteca','librería','papelería'],[['책을 빌려 읽는 곳은 la ___.','biblioteca','biblioteca = 도서관.']])+
   P(['embarazada','avergonzada','constipada'],[['Estoy ___. (임신 중)','embarazada','embarazada = 임신한.']])+
   P(['avergonzado','embarazado','sensible'],[['Estoy muy ___. (창피해서)','avergonzado','avergonzado = 창피한.']])),
  X('연습 2. 문장에서 쓰기','알맞은 단어를 고르세요.','false friends 문맥.',
   P(['éxito','salida','real'],[['Tu película tiene mucho ___. (성공)','éxito','éxito = 성공.']])+
   P(['salida','éxito','entrada'],[['La ___ está a la derecha. (출구)','salida','salida = 출구.']])+
   P(['asisto','ayudo','apoyo'],[['Yo ___ a la clase todos los días. (참석)','asisto','asistir = 참석하다.']])+
   P(['ayudar','asistir','soportar'],[['¿Puedes ___ a mi hermano? (도와주다)','ayudar','ayudar = 돕다.']])+
   P(['constipado','estreñido','sensible'],[['Estoy ___; tengo tos y mocos. (감기)','constipado','constipado = 감기 든.']])+
   P(['ropa','cuerda','sopa'],[['Compro ___ en el centro comercial.','ropa','ropa = 옷.']])+
   P(['sopa','jabón','tarta'],[['Hoy comemos ___ de verduras.','sopa','sopa = 수프.']])+
   P(['jabón','sopa','ropa'],[['Me lavo las manos con ___.','jabón','jabón = 비누.']])),
  X('연습 3. 직접 쓰기','알맞은 스페인어를 쓰세요.','영어 단어에 해당하는 스페인어.',
   T([['balloon → el ___','globo','balloon = globo.'],['carpet → la ___','alfombra','carpet = alfombra.'],['library → la ___','biblioteca','library = biblioteca.'],['bookstore → la ___','librería','bookstore = librería.'],['pregnant → ___','embarazada','pregnant = embarazada.'],['embarrassed → ___ (m.)','avergonzado','embarrassed = avergonzado.'],['exit → la ___','salida','exit = salida.'],['soap → el ___','jabón','soap = jabón.']]))]
))

UNITS.append(U(33,'A1','España: regiones, geografía y tradiciones','스페인의 지역·지리·전통',
 '17개 자치지역, 스페인의 지리, 생일 전통을 통해 스페인 문화를 익힙니다.',
 VS(7,16,74,23),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. 스페인의 17개 자치지역 (comunidades autónomas)</h3>'''+chips(['Andalucía','Aragón','Asturias','Islas Baleares','Canarias','Cantabria','Castilla-La Mancha','Castilla y León','Cataluña','Comunidad Valenciana','Extremadura','Galicia','La Rioja','Comunidad de Madrid','Región de Murcia','Navarra','País Vasco'])+rules(['수도는 <b>Madrid</b>. 자치도시 2곳: <b>Ceuta</b>와 <b>Melilla</b>.','공용어: <b>castellano</b>(스페인어) + 일부 지역에서 catalán, gallego, euskera 등.'])+'''
<h3>2. 지리 어휘</h3>'''+tbl(['어휘','뜻'],[['la península ibérica','이베리아 반도'],['los Pirineos','피레네 산맥 (프랑스와 국경)'],['el río Ebro / Tajo / Guadalquivir','주요 강'],['el mar Mediterráneo / el océano Atlántico','지중해 / 대서양'],['las Islas Baleares / Canarias','발레아레스 / 카나리아 제도'],['el norte / el sur / el este / el oeste','북 / 남 / 동 / 서']])+'''
<h3>3. 생일 전통</h3>'''+rules(['생일 축하: '+E('¡Feliz cumpleaños!')+' / '+E('¡Felicidades!')+' 노래 “Cumpleaños feliz”.','케이크 촛불을 끄기 전에 소원을 빌어요 (pedir un deseo).','생일 아이의 귀를 나이만큼 살짝 잡아당기기도 해요 (tirón de orejas).','생일에 선물을 받고, 가족이 모여 식사해요.']),
 [X('연습 1. 지리','알맞은 단어를 고르세요.','스페인의 지리.',
   P(['Madrid','Barcelona','Sevilla'],[['스페인의 수도: ___.','Madrid','수도는 마드리드.']])+
   P(['Pirineos','Alpes','Andes'],[['프랑스와의 국경 산맥: los ___.','Pirineos','피레네.']])+
   P(['Mediterráneo','Atlántico','Pacífico'],[['동쪽 바다: el mar ___.','Mediterráneo','지중해.']])+
   P(['Canarias','Baleares','Galicia'],[['아프리카 가까운 섬들: las islas ___.','Canarias','카나리아 제도.']])+
   P(['Galicia','Andalucía','Cataluña'],[['북서쪽 자치지역: ___.','Galicia','갈리시아.']])+
   P(['Andalucía','Navarra','Aragón'],[['남쪽 자치지역: ___.','Andalucía','안달루시아.']])+
   P(['Cataluña','Galicia','Murcia'],[['도시 Barcelona가 있는 지역: ___.','Cataluña','카탈루냐.']])+
   P(['diecisiete','quince','veinte'],[['스페인에는 ___ 자치지역이 있어요.','diecisiete','17.']])),
  X('연습 2. 문화','알맞은 표현을 고르세요.','생일 전통.',
   P(['Feliz','Alegre','Bueno'],[['¡___ cumpleaños!','Feliz','Feliz cumpleaños.']])+
   P(['deseo','regalo','tirón'],[['촛불을 끄기 전에 ___ 를 빌어요.','deseo','pedir un deseo.']])+
   P(['orejas','manos','pies'],[['생일 아이의 ___ 를 살짝 잡아당겨요.','orejas','귀.']])+
   P(['castellano','inglés','francés'],[['스페인의 공용어는 ___ 와 지역 언어예요.','castellano','castellano = 스페인어.']])+
   P(['norte','sur','este'],[['Galicia는 스페인의 ___ 쪽에 있어요.','norte','북서쪽.']])+
   P(['sur','norte','oeste'],[['Andalucía는 ___ 쪽에 있어요.','sur','남쪽.']])+
   P(['felicidades','tristezas','gracias'],[['생일에는 ¡___!라고 말해요.','felicidades','felicidades = 축하해요.']])+
   P(['Ceuta','Madrid','Valencia'],[['북아프리카에 있는 스페인 자치도시: ___.','Ceuta','Ceuta와 Melilla.']])),
  X('연습 3. 직접 쓰기','알맞은 단어를 쓰세요.','스페인 문화.',
   T([['¡___ cumpleaños! (Feliz)','Feliz','Feliz cumpleaños.'],['스페인의 수도: ___','Madrid','수도.'],['El río ___ pasa por Zaragoza. (Ebro)','Ebro','Ebro.'],['Pedimos un ___ al apagar las velas. (소원)','deseo','deseo.'],['España y Portugal forman la península ___. (이베리아)','ibérica','ibérica.'],['스페인의 공용어: el ___','castellano','castellano.'],['스페인의 지역 수: ___','diecisiete','17.'],['북쪽: el ___','norte','norte.']]))]
))
