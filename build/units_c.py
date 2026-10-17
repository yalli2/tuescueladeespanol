from lib import *
UNITS=[]

UNITS.append(U(19,'A1','Artículos, género y plural','관사·명사의 성·복수형',
 '정관사·부정관사의 쓰임, 남성/여성 명사 구별법, 복수형 만드는 규칙을 익힙니다.',
 VS(4,37,32),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. 관사</h3>'''+tbl(['','남성','여성'],[['정관사 단수','el','la'],['정관사 복수','los','las'],['부정관사 단수','un','una'],['부정관사 복수','unos','unas']])+rules(['<b>정관사</b>: 이미 알고 있거나 하나뿐인 것 — '+E('El libro está en la mesa')+'.','<b>부정관사</b>: 처음 언급하거나 불특정한 것 — '+E('Tengo un libro')+'.','<b>a- 로 시작하는 강세 여성 명사</b>는 단수에서 el을 써요: '+E('el agua')+', '+E('el águila')+' (복수 las aguas).','<b>a + el = al</b>, <b>de + el = del</b>.'])+'''
<h3>2. 성</h3>'''+tbl(['규칙','예'],[['대부분 <b>-o</b> → 남성','el libro, el vaso'],['대부분 <b>-a</b> → 여성','la mesa, la casa'],['<b>-ción, -sión, -dad, -tad, -tud</b> → 여성','la canción, la ciudad, la libertad'],['<b>-aje, -or, -án</b> → 남성','el viaje, el amor'],['예외','el día, el mapa, el problema, el idioma, la mano, la foto'],['사람 명사','el estudiante / la estudiante (형태가 같은 경우도 있음)']])+'''
<h3>3. 복수형</h3>'''+tbl(['어미','복수 규칙','예'],[['모음','+ <b>s</b>','casa → casas'],['자음','+ <b>es</b>','ciudad → ciudades'],['<b>-z</b>','z → <b>c</b> + es','lápiz → lápices'],['<b>-s</b> (끝 음절 강세 없음)','그대로','el lunes → los lunes']])+warn('복수가 되면 강세 위치가 바뀔 수 있어요: <b>examen → exámenes</b>, <b>joven → jóvenes</b>, <b>canción → canciones</b>(강세 부호 사라짐).'),
 [X('연습 1. 관사','알맞은 관사를 고르세요.','정관사 el/la/los/las, 부정관사 un/una/unos/unas.',
   P(['el','la','los'],[['___ libro está en la mesa.','el','libro는 남성 단수.']])+
   P(['la','el','las'],[['___ casa es grande.','la','casa는 여성 단수.']])+
   P(['los','las','el'],[['___ zapatos son nuevos.','los','zapatos 남성 복수.']])+
   P(['una','un','unas'],[['Tengo ___ hermana.','una','hermana 여성 단수.']])+
   P(['unos','unas','un'],[['Hay ___ libros en la mesa.','unos','libros 남성 복수.']])+
   P(['el','la','un'],[['___ agua está fría.','el','a- 강세 여성 명사 단수 → el agua.']])+
   P(['al','a el','del'],[['Voy ___ cine.','al','a + el = al.']])+
   P(['del','de el','al'],[['Es el coche ___ profesor.','del','de + el = del.']])),
  X('연습 2. 성과 복수','알맞은 형태를 고르세요.','어미로 성 구별, 복수형 규칙.',
   P(['la','el'],[['___ canción','la','-ción → 여성.'],['___ ciudad','la','-dad → 여성.'],['___ viaje','el','-aje → 남성.'],['___ problema','el','예외: 남성.'],['___ mano','la','예외: 여성.'],['___ día','el','예외: 남성.']])+
   P(['lápices','lápizes','lápizs'],[['lápiz의 복수: ___.','lápices','z → c + es.']])+
   P(['ciudades','ciudads','ciudadas'],[['ciudad의 복수: ___.','ciudades','자음 + es.']])),
  X('연습 3. 직접 쓰기','알맞은 단어를 쓰세요.','관사와 복수형.',
   T([['casa의 복수: las ___','casas','모음 + s.'],['canción의 복수: las ___','canciones','-ción → -ciones.'],['examen의 복수: los ___ (강세 주의)','exámenes','강세 부호 필요.'],['joven의 복수: los ___','jóvenes','강세 부호 필요.'],['___ agua (el/la)','el','a- 강세 여성 명사.'],['Voy ___ banco. (a+el)','al','a + el = al.'],['Es la casa ___ profesor. (de+el)','del','de + el = del.'],['pared의 복수: las ___','paredes','자음 + es.']]))]
))

UNITS.append(U(20,'A1','Posesivos y demostrativos','소유사·지시사',
 'mi·tu·su 형태와 용법, este·ese·aquel 구분, bueno/buen·grande/gran의 줄임을 익힙니다.',
 VS(41,42,46,75),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. 소유사 (명사 앞)</h3>'''+tbl(['인칭','단수 명사','복수 명사'],[['yo','mi','mis'],['tú','tu','tus'],['él / ella / usted','su','sus'],['nosotros/as','nuestro / nuestra','nuestros / nuestras'],['vosotros/as','vuestro / vuestra','vuestros / vuestras'],['ellos / ustedes','su','sus']])+rules(['소유사는 <b>소유자가 아니라 소유되는 물건의 수</b>에 일치해요: '+E('mi libro')+', '+E('mis libros')+'.','nuestro/vuestro는 물건의 성에도 일치: '+E('nuestra casa')+'.','<b>tú(너)</b>와 <b>tu(너의)</b>, <b>él</b>과 <b>el</b>은 악센트로 구분해요.','<b>su</b>는 él/ella/usted/ellos 모두의 것이라 애매할 수 있어요: su casa de él → '+E('la casa de Juan')+'.','신체 부위·옷에는 소유사 대신 관사: '+E('Me lavo las manos')+'.'])+'''
<h3>2. 지시사</h3>'''+tbl(['거리','남성','여성','중성'],[['가까움 (이)','este / estos','esta / estas','esto'],['중간 (그)','ese / esos','esa / esas','eso'],['멀리 (저)','aquel / aquellos','aquella / aquellas','aquello']])+rules(['<b>este</b>: 말하는 사람 가까이 — '+E('este libro')+'.','<b>ese</b>: 듣는 사람 가까이 — '+E('ese libro')+'.','<b>aquel</b>: 둘 다에게서 멀리 — '+E('aquel edificio')+'.','중성 <b>esto/eso/aquello</b>는 정체를 모르는 것 — '+E('¿Qué es esto?')+'.'])+'''
<h3>3. 줄어드는 형용사</h3>'''+tbl(['형용사','남성 단수 명사 앞','나머지'],[['bueno','<b>buen</b> día','buena, buenos, buenas'],['malo','<b>mal</b> día','mala, malos'],['grande','<b>gran</b> amigo (훌륭한)','grandes'],['primero / tercero','<b>primer</b> / <b>tercer</b> piso','primera']])+warn('gran은 남성·여성 <b>단수 명사 앞</b>에서 쓰고 ‘크다’ 외에 ‘훌륭한’ 뜻이 돼요: un gran hombre(위대한 사람) vs un hombre grande(덩치 큰 사람).'),
 [X('연습 1. 소유사','알맞은 소유사를 고르세요.','소유되는 물건의 수와 성에 일치.',
   P(['mi','mis','mío'],[['Este es ___ libro.','mi','libro 단수 → mi.']])+
   P(['mis','mi','mías'],[['Estos son ___ libros.','mis','libros 복수 → mis.']])+
   P(['tu','tú','tus'],[['¿Dónde está ___ casa?','tu','casa 단수 → tu (악센트 없음).']])+
   P(['nuestra','nuestro','nuestras'],[['___ casa es grande.','nuestra','casa 여성 단수.']])+
   P(['vuestros','vuestro','vuestras'],[['¿Dónde están ___ libros?','vuestros','libros 남성 복수.']])+
   P(['sus','su','suyos'],[['Ellos viven con ___ padres.','sus','padres 복수 → sus.']])+
   P(['las','mis','sus'],[['Me lavo ___ manos.','las','신체 부위는 관사.']])+
   P(['su','sus','tu'],[['María y ___ marido viven aquí.','su','marido 단수 → su.']])),
  X('연습 2. 지시사와 buen/gran','알맞은 단어를 고르세요.','este/ese/aquel, 줄임형.',
   P(['este','ese','aquel'],[['(내 손에 있는 책) ___ libro es mío.','este','가까이 있으면 este.']])+
   P(['esa','esta','aquella'],[['(상대방 옆의 가방) ___ bolsa es tuya.','esa','듣는 사람 가까이 → ese/esa.']])+
   P(['aquel','este','ese'],[['(저 멀리 있는 산) ___ monte es muy alto.','aquel','멀리 → aquel.']])+
   P(['esto','este','esta'],[['¿Qué es ___?','esto','정체를 모르는 것 → 중성 esto.']])+
   P(['buen','bueno','buena'],[['Hace un ___ día.','buen','남성 단수 명사 앞 → buen.']])+
   P(['mala','mal','malo'],[['Es una ___ idea.','mala','여성 명사 앞에는 줄지 않음.']])+
   P(['gran','grande','grandes'],[['Es un ___ amigo. (훌륭한)','gran','단수 명사 앞 → gran.']])+
   P(['primer','primero','primera'],[['Vivo en el ___ piso.','primer','남성 단수 명사 앞.']])),
  X('연습 3. 직접 쓰기','알맞은 단어를 쓰세요.','소유사·지시사.',
   T([['(나의 책들) ___ libros','mis','복수 → mis.'],['(우리의 집) ___ casa','nuestra','여성 → nuestra.'],['(너의 친구) ___ amigo','tu','단수 → tu.'],['(이것) ¿Qué es ___?','esto','중성.'],['(저 건물들) ___ edificios','aquellos','멀리 + 복수.'],['(그 가방, 가까이) ___ bolsa','esa','ese/esa.'],['(좋은 아침) ___ día','buen','단수 남성 명사 앞.'],['(위대한 사람) un ___ hombre','gran','gran = 훌륭한.']]))]
))

UNITS.append(U(21,'A1','Cómo hacer preguntas','의문문과 의문사',
 '예/아니오 질문, 의문사 qué·quién·dónde·cuándo·cómo·cuánto·por qué 사용법을 익힙니다.',
 VS(49,50),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. 예/아니오 질문</h3>'''+rules(['평서문에 <b>¿ ?</b>만 붙이고 억양을 올려요: '+E('¿Vives en Madrid?')+'.','<b>의문부호는 앞뒤 모두</b>: ¿ … ?','주어를 동사 뒤에 두기도 해요: '+E('¿Vive Juan en Madrid?')+'.'])+'''
<h3>2. 의문사</h3>'''+tbl(['의문사','의미','예'],[['¿Qué?','무엇','¿Qué haces?'],['¿Quién? / ¿Quiénes?','누구','¿Quién es?'],['¿Dónde?','어디','¿Dónde vives?'],['¿Adónde?','어디로','¿Adónde vas?'],['¿De dónde?','어디 출신','¿De dónde eres?'],['¿Cuándo?','언제','¿Cuándo llegas?'],['¿Cómo?','어떻게','¿Cómo estás?'],['¿Cuánto/a/os/as?','얼마나·몇','¿Cuántos años tienes?'],['¿Por qué?','왜 (두 단어)','¿Por qué estudias español?'],['¿Cuál / Cuáles?','어느 것','¿Cuál es tu número?'],['¿Qué + 명사?','무슨 ~','¿Qué hora es?']])+rules(['의문사에는 항상 <b>악센트</b>: qué, quién, dónde, cuándo, cómo, cuánto, cuál.','대답할 때 <b>porque</b>(한 단어, 악센트 없음, 왜냐하면) — '+E('Porque me gusta')+'.','<b>cuál</b>은 여러 개 중 선택, <b>qué</b>는 정의·설명: ¿Qué es esto? / ¿Cuál es tu casa?','<b>cuánto</b>는 명사의 성·수에 일치: ¿Cuántas personas hay?']),
 [X('연습 1. 의문사 고르기','알맞은 의문사를 고르세요.','대답에 맞는 의문사.',
   P(['Dónde','Cuándo','Cómo'],[['¿___ vives? — En Madrid.','Dónde','장소를 물어요.']])+
   P(['Cuándo','Dónde','Quién'],[['¿___ llegas? — A las ocho.','Cuándo','시간을 물어요.']])+
   P(['Quién','Qué','Cuál'],[['¿___ es ese chico? — Es mi hermano.','Quién','사람 → quién.']])+
   P(['Cómo','Cuánto','Por qué'],[['¿___ estás? — Muy bien.','Cómo','상태 → cómo.']])+
   P(['Cuántos','Cuánto','Cuántas'],[['¿___ años tienes? — Treinta.','Cuántos','años 남성 복수.']])+
   P(['Por qué','Porque','Qué'],[['¿___ estudias español? — Porque me gusta.','Por qué','질문은 두 단어 + 악센트.']])+
   P(['De dónde','Dónde','Adónde'],[['¿___ eres? — De Corea.','De dónde','출신 → de dónde.']])+
   P(['Adónde','Dónde','De dónde'],[['¿___ vas? — Al cine.','Adónde','방향 → adónde.']])),
  X('연습 2. 질문 만들기','알맞은 표현을 고르세요.','의문부호, 악센트, porque.',
   P(['¿Qué','Que','¿Que'],[['___ hora es?','¿Qué','의문부호와 악센트.']])+
   P(['Porque','Por qué','Porqué'],[['No voy ___ estoy cansado.','Porque','대답 → porque.']])+
   P(['Cuántas','Cuántos','Cuánto'],[['¿___ personas hay?','Cuántas','personas 여성 복수.']])+
   P(['Cuál','Qué','Quién'],[['¿___ es tu número de teléfono?','Cuál','여러 가능성 중 → cuál.']])+
   P(['Quiénes','Quién','Cuáles'],[['¿___ son esas chicas?','Quiénes','사람 복수.']])+
   P(['Cuánto','Cuántos','Cuánta'],[['¿___ cuesta el libro?','Cuánto','가격 → cuánto.']])+
   P(['Cómo','Como','Cuándo'],[['¿___ te llamas?','Cómo','이름을 물어요.']])+
   P(['Cuáles','Cuál','Qué'],[['¿___ son tus zapatos?','Cuáles','zapatos 복수.']])),
  X('연습 3. 직접 쓰기','알맞은 단어를 쓰세요.','의문사.',
   T([['¿___ vives? (어디)','Dónde','장소.'],['¿___ te llamas? (어떻게)','Cómo','이름.'],['¿___ años tienes? (몇)','Cuántos','años 남성 복수.'],['¿___ es tu número? (어느)','Cuál','번호 선택.'],['¿___ llegas? (언제)','Cuándo','시간.'],['¿___ es ese hombre? (누구)','Quién','사람.'],['¿___ estudias español? (왜)','Por qué','왜 = por qué.'],['No voy ___ estoy enfermo.','porque','왜냐하면.']]))]
))

UNITS.append(U(22,'A1','Gustar y dar tu opinión','gustar·의견 말하기·동의/반대',
 'gustar 구문, encantar의 올바른 용법, 의견을 말하고 동의·반대를 표현하는 법을 익힙니다.',
 VS(15,96,141,92,100),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. gustar의 구조</h3>
<p><b>(a mí) me / te / le / nos / os / les + gusta(n) + 주어</b> — 좋아하는 것이 주어입니다.</p>'''+tbl(['좋아하는 것','표현'],[['동사원형·단수','Me <b>gusta</b> bailar. / Me <b>gusta</b> el café.'],['복수','Me <b>gustan</b> los perros.'],['강조','<b>A mí</b> me gusta, <b>a ti</b> te gusta, <b>a Juan</b> le gusta.']])+rules(['맞장구: <b>A mí también</b> / <b>A mí tampoco</b> / <b>A mí sí</b> / <b>A mí no</b>.','<b>encantar</b>도 같은 구조이며 이미 ‘아주 좋아하다’이므로 <b>mucho를 붙이지 않아요</b>: '+E('Me encanta bailar')+'.'])+warn('✘ Me encanta mucho → ✔ <b>Me encanta</b> / <b>Me gusta mucho</b>. encantar에는 mucho를 쓰지 않아요.')+'''
<h3>2. 의견 표현</h3>'''+tbl(['의견','표현'],[['제 생각에는','Creo que… · Pienso que… · En mi opinión…'],['동의','Estoy de acuerdo · Tienes razón · Por supuesto'],['반대','No estoy de acuerdo · No creo que… · Yo no pienso lo mismo'],['부분 동의','Sí, pero… · Depende']])+rules(['<b>creo que + 직설법</b>: '+E('Creo que es una buena idea')+'.','<b>estar de acuerdo con</b> + 사람/의견: '+E('Estoy de acuerdo contigo')+'.']),
 [X('연습 1. gustar','알맞은 형태를 고르세요.','단수/동사원형 → gusta, 복수 → gustan.',
   P(['gusta','gustan','gusto'],[['Me ___ el chocolate.','gusta','chocolate 단수.']])+
   P(['gustan','gusta','gustas'],[['Me ___ los perros.','gustan','perros 복수.']])+
   P(['te','me','le'],[['A ti ___ gusta bailar.','te','a ti → te.']])+
   P(['le','les','lo'],[['A Juan ___ gusta el fútbol.','le','a Juan → le.']])+
   P(['nos','me','os'],[['A nosotros ___ gustan las películas.','nos','nosotros → nos.']])+
   P(['les','le','las'],[['A mis padres ___ gusta viajar.','les','복수 → les.']])+
   P(['gusta','gustan','gustamos'],[['No me ___ nadar.','gusta','동사원형 → gusta.']])+
   P(['encanta','encantan','encantas'],[['Me ___ el helado.','encanta','단수.']])),
  X('연습 2. 의견과 동의','알맞은 표현을 고르세요.','맞장구, creo que, estar de acuerdo.',
   P(['también','tampoco','sí'],[['Me gusta el café. — A mí ___.','también','긍정에 동의 → también.']])+
   P(['tampoco','también','no'],[['No me gusta el frío. — A mí ___.','tampoco','부정에 동의 → tampoco.']])+
   P(['de acuerdo','de verdad','de nada'],[['Estoy ___ contigo.','de acuerdo','estar de acuerdo = 동의하다.']])+
   P(['razón','verdad','opinión'],[['Tienes ___.','razón','tener razón = 네가 옳다.']])+
   P(['que','de','a'],[['Creo ___ es una buena idea.','que','creer que.']])+
   P(['mi','tu','su'],[['En ___ opinión, es difícil.','mi','내 의견으로는.']])+
   P(['mucho','–','muy'],[['Me gusta ___ el cine. (정도)','mucho','gustar + mucho.']])+
   P(['no estoy','no soy','no tengo'],[['Lo siento, ___ de acuerdo.','no estoy','estar de acuerdo.']])),
  X('연습 3. 직접 쓰기','알맞은 단어를 쓰세요.','gustar·의견.',
   T([['Me ___ las flores. (gustar)','gustan','복수 → gustan.'],['A él ___ gusta leer.','le','a él → le.'],['Me ___ bailar. (매우 좋아함, 한 단어)','encanta','encantar.'],['___ que es verdad. (creer, 1인칭)','Creo','creo que.'],['Estoy de ___ contigo.','acuerdo','acuerdo.'],['No me gusta. — A mí ___.','tampoco','부정 동의.'],['Me gusta. — A mí ___.','también','긍정 동의.'],['Tienes ___.','razón','tener razón.']]))]
))

UNITS.append(U(23,'A1','Muy, mucho, poco y adverbios','muy/mucho/poco · -mente 부사 · 흔한 실수',
 'muy와 mucho의 구분, poco, -mente 부사 만드는 법을 익힙니다.',
 VS(14,98,35),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. muy vs mucho</h3>'''+tbl(['','쓰임','예'],[['<b>muy</b>','형용사·부사 앞 (변하지 않음)',E('muy bonito')+' · '+E('muy bien')],['<b>mucho</b>','동사 뒤 (변하지 않음)',E('Trabajo mucho')],['<b>mucho/a/os/as</b>','명사 앞 (성·수 일치)',E('mucha gente')+' · '+E('muchos libros')],['<b>poco/a/os/as</b>','mucho의 반대 (거의 없는)',E('poco tiempo')+' · '+E('pocas personas')]])+warn('✘ Yo estoy mucho contenta → ✔ <b>Yo estoy muy contenta</b>. 형용사 앞에는 <b>muy</b>예요. ‘mucho + 형용사’는 틀린 표현!')+rules(['mejor, peor, mayor, menor 앞에는 <b>mucho</b>: '+E('mucho mejor')+'.','<b>un poco (de)</b> = 조금.'])+'''
<h3>2. -mente 부사</h3>'''+tbl(['규칙','예'],[['형용사 <b>여성형</b> + mente','rápido → rápida<b>mente</b>, lento → lenta<b>mente</b>'],['-e / 자음으로 끝나는 형용사 + mente','fácil → fácil<b>mente</b>, feliz → feliz<b>mente</b>'],['원래 악센트는 유지','fácil → fácilmente (악센트 유지)'],['두 개를 연달아 쓸 때','앞은 여성형만: lenta y cuidadosamente']]),
 [X('연습 1. muy / mucho / poco','알맞은 단어를 고르세요.','형용사 앞 muy, 동사 뒤 mucho, 명사 앞 mucho/a.',
   P(['muy','mucho','mucha'],[['Estoy ___ contento.','muy','형용사 앞.']])+
   P(['mucho','muy','mucha'],[['Trabajo ___.','mucho','동사 뒤.']])+
   P(['muchos','muy','mucho'],[['Hay ___ libros.','muchos','libros 남성 복수.']])+
   P(['mucha','mucho','muy'],[['Hay ___ gente.','mucha','gente 여성 단수.']])+
   P(['muy','mucho','poco'],[['Habla ___ bien.','muy','부사 앞.']])+
   P(['pocos','poco','pocas'],[['Tengo ___ amigos.','pocos','amigos 남성 복수.']])+
   P(['mucho','muy','más'],[['Hoy hace ___ mejor tiempo.','mucho','비교급 앞.']])+
   P(['poco','pocos','poca'],[['Tengo un ___ de tiempo.','poco','un poco de.']])),
  X('연습 2. -mente','알맞은 부사를 고르세요.','형용사 여성형 + mente.',
   P(['rápidamente','rápidomente','rápidamenta'],[['rápido → ___','rápidamente','여성형 rápida + mente.']])+
   P(['lentamente','lentomente','lentemente'],[['lento → ___','lentamente','lenta + mente.']])+
   P(['fácilmente','fácilamente','facilmente'],[['fácil → ___','fácilmente','악센트 유지.']])+
   P(['felizmente','felizamente','felizmente.'],[['feliz → ___','felizmente','feliz + mente.']])+
   P(['claramente','claromente','claramente.'],[['claro → ___','claramente','clara + mente.']])+
   P(['normalmente','normalamente','normalemente'],[['normal → ___','normalmente','normal + mente.']])+
   P(['muy','mucho','muchas'],[['Estoy ___ cansada.','muy','형용사 앞.']])+
   P(['mucho','muy','muchos'],[['Te quiero ___.','mucho','동사 뒤.']])),
  X('연습 3. 직접 쓰기','알맞은 단어를 쓰세요.','muy/mucho 및 -mente.',
   T([['Estoy ___ contenta. (매우)','muy','형용사 앞.'],['Como ___. (많이)','mucho','동사 뒤.'],['Hay ___ personas. (많은)','muchas','personas 여성 복수.'],['Tengo ___ tiempo. (거의 없는)','poco','남성 단수.'],['lento → ___','lentamente','lenta + mente.'],['fácil → ___','fácilmente','악센트 유지.'],['(조금) un ___ de agua','poco','un poco de.'],['Es ___ mejor así. (훨씬)','mucho','비교급 앞.']]))]
))

UNITS.append(U(24,'A1','Presente de indicativo','현재형: 규칙·불규칙 동사',
 '-ar/-er/-ir 규칙 활용과 불규칙(1인칭 변화, 어간 모음 변화, 특수 동사)을 익힙니다.',
 VS(70,71,101,103,105,106,112,99,125,132,144),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. 규칙 동사</h3>'''+tbl(['','hablar','comer','vivir'],[['yo','hablo','como','vivo'],['tú','hablas','comes','vives'],['él/ella/usted','habla','come','vive'],['nosotros','hablamos','comemos','vivimos'],['vosotros','habláis','coméis','vivís'],['ellos/ustedes','hablan','comen','viven']])+'''
<h3>2. 불규칙 동사</h3>'''+tbl(['유형','예'],[
 ['yo만 불규칙 (-go)','hacer → hago · poner → pongo · salir → salgo · traer → traigo · decir → digo · tener → tengo · venir → vengo'],
 ['yo만 불규칙 (기타)','saber → sé · conocer → conozco · dar → doy · ver → veo'],
 ['<b>e → ie</b>','pensar → pienso, piensas, piensa, pensamos, pensáis, piensan · querer · empezar · cerrar'],
 ['<b>o → ue</b>','volver → vuelvo · poder → puedo · dormir → duermo · encontrar · aprobar → apruebo'],
 ['<b>u → ue</b>','jugar → juego, juegas, juega, jugamos, jugáis, juegan'],
 ['<b>e → i</b>','pedir → pido, pides, pide, pedimos, pedís, piden · seguir · repetir'],
 ['완전 불규칙','ser · estar · ir (voy, vas, va, vamos, vais, van) · haber']])+warn('<b>nosotros/vosotros</b>는 어간 모음이 바뀌지 않아요: pensamos, volvemos, pedimos. (신발 모양 ‘botas’ 변화)'),
 [X('연습 1. 규칙 활용','알맞은 형태를 고르세요.','-ar/-er/-ir 어미.',
   P(['hablo','hablas','habla'],[['Yo ___ español.','hablo','yo → -o.']])+
   P(['comes','como','come'],[['Tú ___ mucho.','comes','tú → -es.']])+
   P(['vive','vives','vivo'],[['Ella ___ en Madrid.','vive','ella → -e.']])+
   P(['trabajamos','trabajáis','trabajan'],[['Nosotros ___ aquí.','trabajamos','nosotros → -amos.']])+
   P(['escribís','escribimos','escriben'],[['Vosotros ___ cartas.','escribís','vosotros -ir → -ís.']])+
   P(['beben','bebemos','bebes'],[['Ellos ___ agua.','beben','ellos → -en.']])+
   P(['estudio','estudias','estudia'],[['Yo ___ español.','estudio','yo → -o.']])+
   P(['aprenden','aprendéis','aprendemos'],[['Ustedes ___ rápido.','aprenden','ustedes → ellos형.']])),
  X('연습 2. 불규칙','알맞은 형태를 고르세요.','hago/pongo/salgo, e→ie, o→ue, u→ue, e→i.',
   P(['hago','hace','hacemos'],[['Yo ___ la tarea.','hago','hacer 1인칭.']])+
   P(['salgo','sale','salimos'],[['Yo ___ de casa a las ocho.','salgo','salir 1인칭.']])+
   P(['pienso','pensamos','pensáis'],[['Yo ___ que es verdad.','pienso','pensar e→ie.']])+
   P(['vuelvo','volvemos','volvéis'],[['Yo ___ a casa tarde.','vuelvo','volver o→ue.']])+
   P(['juega','jugamos','jugáis'],[['Ella ___ al tenis.','juega','jugar u→ue.']])+
   P(['pedimos','pido','piden'],[['Nosotros ___ una pizza.','pedimos','nosotros는 변화 없음.']])+
   P(['duermes','dormimos','duerme'],[['Tú ___ ocho horas.','duermes','dormir o→ue.']])+
   P(['puede','podemos','pueden'],[['Él no ___ venir.','puede','poder o→ue.']])),
  X('연습 3. 직접 쓰기','알맞은 형태를 쓰세요.','현재형 활용.',
   T([['Yo ___ (tener) hambre.','tengo','tener 1인칭.'],['Yo ___ (saber) la respuesta.','sé','saber 1인칭.'],['Tú ___ (querer) agua.','quieres','querer e→ie.'],['Nosotros ___ (poder) ir.','podemos','nosotros 변화 없음.'],['Ellos ___ (pedir) café.','piden','pedir e→i.'],['Yo ___ (conocer) a Ana.','conozco','conocer 1인칭.'],['Yo ___ (ir) al cine.','voy','ir 완전 불규칙.'],['Ella ___ (aprobar) el examen.','aprueba','aprobar o→ue.']]))]
))

UNITS.append(U(25,'A1','La rutina diaria y los verbos reflexivos','하루 일과와 재귀동사',
 '하루 일과 어휘와 순서 표현, 재귀동사(levantarse 등)를 익힙니다.',
 VS(72,48,131,133),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. 재귀동사</h3>
<p>동사원형 끝에 <b>-se</b>가 붙고, 주어와 같은 사람에게 행동이 돌아옵니다: <b>me, te, se, nos, os, se</b>를 동사 앞에.</p>'''+tbl(['인칭','levantarse'],[['yo','me levanto'],['tú','te levantas'],['él/ella/usted','se levanta'],['nosotros','nos levantamos'],['vosotros','os levantáis'],['ellos/ustedes','se levantan']])+rules(['<b>재귀대명사는 동사 앞</b>: '+E('Me levanto a las siete')+'.','동사원형 구문에서는 뒤에 붙이거나 앞에: '+E('Voy a levantarme')+' = '+E('Me voy a levantar')+'.','같은 동사라도 <b>재귀 / 비재귀</b> 뜻이 달라져요: '+E('Lavo el coche')+' (차를 씻다) vs '+E('Me lavo')+' (내 몸을 씻다).'])+'''
<h3>2. 하루 일과 어휘</h3>'''+chips(['despertarse','levantarse','ducharse','lavarse los dientes','vestirse','desayunar','ir al trabajo','comer','volver a casa','cenar','ver la tele','acostarse','dormirse'])+'''
<h3>3. 순서 표현</h3>'''+chips(['primero','luego / después','más tarde','por último','por la mañana','por la tarde','por la noche']),
 [X('연습 1. 재귀대명사','알맞은 재귀대명사를 고르세요.','me/te/se/nos/os/se.',
   P(['me','te','se'],[['Yo ___ levanto a las siete.','me','yo → me.']])+
   P(['te','me','se'],[['Tú ___ duchas por la mañana.','te','tú → te.']])+
   P(['se','me','te'],[['Ella ___ viste rápido.','se','ella → se.']])+
   P(['nos','os','se'],[['Nosotros ___ acostamos a las once.','nos','nosotros → nos.']])+
   P(['os','nos','se'],[['Vosotros ___ laváis las manos.','os','vosotros → os.']])+
   P(['se','nos','os'],[['Ellos ___ despiertan temprano.','se','ellos → se.']])+
   P(['Me','Te','Se'],[['___ lavo los dientes.','Me','yo → me.']])+
   P(['se','me','lo'],[['Mi hijo ___ llama Pablo.','se','llamarse 3인칭.']])),
  X('연습 2. 일과 순서','알맞은 단어를 고르세요.','순서 표현과 재귀/비재귀.',
   P(['Primero','Por último','Más tarde'],[['___ me despierto, y luego me levanto.','Primero','처음.']])+
   P(['Por último','Primero','Después'],[['___ me acuesto.','Por último','마지막.']])+
   P(['desayuno','me desayuno','desayunar'],[['Por la mañana ___ café y tostadas.','desayuno','desayunar는 재귀동사가 아님.']])+
   P(['me ducho','ducho','me duchas'],[['Yo ___ por la mañana.','me ducho','ducharse.']])+
   P(['Lavo','Me lavo','Se lava'],[['___ el coche los sábados.','Lavo','차를 씻음 → 비재귀.']])+
   P(['Me lavo','Lavo','Lava'],[['___ las manos antes de comer.','Me lavo','내 손 → 재귀.']])+
   P(['acostarme','acostar','acuesto'],[['Voy a ___ temprano.','acostarme','ir a + 재귀동사원형.']])+
   P(['noche','mañana','tarde'],[['Cenamos por la ___.','noche','저녁/밤 식사.']])),
  X('연습 3. 직접 쓰기','알맞은 형태를 쓰세요.','재귀동사.',
   T([['Yo ___ (levantarse) a las siete.','me levanto','yo형.'],['Tú ___ (ducharse) rápido.','te duchas','tú형.'],['Él ___ (vestirse) solo.','se viste','vestirse e→i.'],['Nosotros ___ (acostarse) tarde.','nos acostamos','nosotros형.'],['Ellos ___ (despertarse) pronto.','se despiertan','despertarse e→ie.'],['Me ___ los dientes. (lavar)','lavo','lavarse los dientes.'],['Voy a ___ (dormirse) en el sofá.','dormirme','ir a + 재귀.'],['¿A qué hora ___ (levantarse, tú)?','te levantas','tú형.']]))]
))
