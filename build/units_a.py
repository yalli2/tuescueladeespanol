from lib import *
UNITS=[]

# ---------- 1 ----------
UNITS.append(U(1,'A1','Saludos y presentaciones','인사하기와 자기소개',
 '시간대별 인사말, 헤어질 때 인사, 이름·출신·나이·직업 소개하기, 비격식/격식 대화의 기본 표현을 익힙니다.',
 VS(69,123,80,89,95),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. 인사말 (스페인 기준)</h3>'''+tbl(['표현','언제 쓰나요?'],[
 [E('Hola'),'하루 종일, 친구·가족 사이의 편한 인사'],
 [E('Buenos días'),'아침~대략 14시까지 (스페인은 점심이 늦어서 오전이 길어요)'],
 [E('Buenas tardes'),'대략 14시~21시'],
 [E('Buenas noches'),'대략 21시 이후 · 잠자리에 들 때도 사용'],
])+warn('día는 <b>남성</b>이라 <b>Buenos</b> días, tarde와 noche는 <b>여성</b>이라 <b>Buenas</b> tardes / noches 입니다. 항상 복수형으로 말해요.')+'''
<h3>2. 헤어질 때</h3>'''+chips(['Adiós','Hasta luego','Chao','Hasta mañana','Hasta pronto','Hasta el lunes'])+rules([
 '<b>Adiós</b>: 한동안 볼 일이 없을 때','<b>Hasta luego</b>: 곧(같은 날 나중에) 다시 볼 때','<b>Hasta</b> + 날짜/요일: Hasta mañana, Hasta el sábado','<b>Chao</b>: 가족·친구 사이의 편한 작별 인사','<b>Buenas noches</b>는 잠자리에 들 때만 헤어짐 인사로 써요'])+'''
<h3>3. 자기소개 순서</h3>'''+tbl(['내용','표현'],[
 ['이름',E('Me llamo Elena')+' / '+E('Soy Elena')],
 ['출신','<b>ser</b> + 도시·나라·국적 → '+E('Soy de España')+' / '+E('Soy española')],
 ['사는 곳','<b>vivir</b> + en + 도시 → '+E('Vivo en Zamora')],
 ['나이','<b>tener</b> + 숫자 + años → '+E('Tengo 46 años')],
 ['결혼 여부','스페인은 <b>estar</b>, 중남미는 <b>ser</b> → '+E('Estoy casada')],
 ['직업','<b>ser</b> + 직업 → '+E('Soy profesora de español')],
 ['일하는 곳','<b>trabajar como</b> + 직책 / <b>trabajar en·para</b> + 회사 → '+E('Trabajo como profesora online')+' · '+E('Trabajo en Tu escuela de español')],
])+'''
<h3>4. 간단한 대화 (비격식 vs 격식)</h3>'''+tbl(['','비격식 (친구·가족)','격식 (<b>usted</b>)'],[
 ['안부 묻기',E('¿Qué tal?')+' / '+E('¿Qué tal estás?'),E('¿Cómo está usted?')],
 ['대답',E('Estoy bien')+' · '+E('Estoy mal')+' · '+E('Estoy regular'),E('Estoy bien, gracias')],
 ['인사',E('Hola'),E('Buenos días')+' / '+E('Buenas tardes')],
 ['작별',E('Chao')+' / '+E('Adiós'),E('Adiós')+' / '+E('Buenas tardes')],
])+pero('<b>usted</b>는 “당신”이지만 동사는 <b>3인칭(él, ella)</b> 형태로 씁니다. 복수는 <b>ustedes</b>.'),
 [X('연습 1. 인사말 고르기','상황에 맞는 표현을 고르세요.','아침·낮 = Buenos días / 오후 = Buenas tardes / 밤 = Buenas noches. 곧 다시 볼 사이 = Hasta luego.',
   P(['Buenos','Buenas'],[
    ['오전 10시 → ___ días.','Buenos','día는 남성 명사 → Buenos días.'],
    ['오후 5시 → ___ tardes.','Buenas','tarde는 여성 명사 → Buenas tardes.'],
    ['밤 11시 → ___ noches.','Buenas','noche는 여성 명사 → Buenas noches.'],
   ])+P(['Hola','Adiós','Hasta luego'],[
    ['친구에게 가볍게 인사할 때: ___, ¿qué tal?','Hola','Hola는 하루 종일 쓸 수 있는 편한 인사.'],
    ['오늘 나중에 다시 볼 사람에게: ___.','Hasta luego','같은 날 곧 볼 때는 Hasta luego.'],
    ['한동안 볼 일이 없는 사람에게: ___.','Adiós','Adiós는 곧 만날 계획이 없을 때 쓰는 작별 인사.'],
   ])+P(['Buenas noches','Buenos días'],[
    ['잠자리에 들기 전에: ___.','Buenas noches','잠자리에 들 때는 Buenas noches라고 말해요.'],
   ])+P(['mañana','luego','pronto'],[
    ['내일 볼 친구에게: Hasta ___.','mañana','Hasta mañana = 내일 봐요.'],
   ])),
  X('연습 2. 자기소개 동사','빈칸에 알맞은 단어를 고르세요.','이름 Me llamo/Soy · 출신 Soy · 거주 Vivo · 나이 Tengo · 직업 Soy · 회사 trabajo en.',
   P(['Me','Soy','Estoy'],[['___ llamo Marta.','Me','llamarse는 재귀동사: Me llamo.']])+
   P(['Soy','Estoy','Tengo'],[['___ de España.','Soy','출신은 ser 동사: Soy de España.'],['___ profesora de español.','Soy','직업은 ser + 직업.']])+
   P(['Vivo','Soy','Tengo'],[['___ en Zamora.','Vivo','사는 곳은 vivir + en.']])+
   P(['Tengo','Soy','Estoy'],[['___ 46 años.','Tengo','나이는 tener + años. (Soy 46 años ✘)']])+
   P(['como','en','de'],[['Trabajo ___ profesora online.','como','직책은 trabajar como + 직업.']])+
   P(['en','como','con'],[['Trabajo ___ Tu escuela de español. (회사)','en','회사는 trabajar en (또는 para) + 회사.']])+
   P(['Estoy','Soy','Tengo'],[['스페인에서 결혼했다고 말할 때(여성): ___ casada.','Estoy','스페인에서는 결혼 여부에 estar를 써요. (중남미는 ser)']])),
  X('연습 3. 써 보기','빈칸에 알맞은 한 단어를 쓰세요.','격식 = usted. 나이 = tener. 출신 국적(여성) = española.',
   T([['¿Cómo está ___? (격식, “당신”)','usted','격식 대화에서는 usted를 써요.'],
    ['— ¿Qué tal? — Estoy ___. (좋아요)','bien','Estoy bien = 잘 지내요.'],
    ['아침의 격식 있는 인사: Buenos ___.','días','Buenos días.'],
    ['스페인 여성이 말해요: Soy ___. (국적)','española','국적 형용사는 소문자, 여성형은 -a.'],
    ['Me ___ Pablo. (이름)','llamo','Me llamo Pablo.'],
    ['___ 20 años. (나는 20살입니다)','Tengo','나이는 tener 동사.'],
    ['Vivo ___ Madrid.','en','거주지 앞에는 전치사 en.'],
    ['Hasta ___. (곧 봐요, p로 시작)','pronto','Hasta pronto = 곧 다시 만나요.']]))]
))

# ---------- 2 ----------
UNITS.append(U(2,'A1','Pronombres y verbos básicos','인칭대명사와 기본 동사(ser·estar·tener·ir)',
 '주어 인칭대명사 6인칭, usted/ustedes 쓰임, 그리고 가장 많이 쓰는 불규칙 동사 4개의 현재형을 익힙니다.',
 VS(58,137,81,88,83,91),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. 주어 인칭대명사</h3>'''+tbl(['인칭','단수','복수'],[
 ['1인칭',E('yo'),E('nosotros')+' / '+E('nosotras')],
 ['2인칭',E('tú'),E('vosotros')+' / '+E('vosotras')],
 ['3인칭',E('él')+' / '+E('ella'),E('ellos')+' / '+E('ellas')],
 ['존칭 (동사는 3인칭)',E('usted'),E('ustedes')],
])+rules(['남녀가 섞인 그룹은 <b>남성 복수</b>(nosotros, vosotros, ellos)를 써요.','스페인 대부분 지역: 친한 사이 <b>tú / vosotros</b>, 격식 <b>usted / ustedes</b>.','스페인 남부·카나리아 제도·중남미: <b>vosotros를 쓰지 않고 ustedes</b>를 써요.','동사 형태만 봐도 주어를 알 수 있어서 <b>보통 주어 대명사를 생략</b>합니다: '+E('Estudias mucho')+'.','<b>쓰는 경우</b>: 누구인지 알려 줄 때(¿Quién sabe? — Yo), 강조·대조할 때(Ella está enfadada, yo no).'])+'''
<h3>2. 기본 동사 4개 (현재)</h3>'''+tbl(['','ser (이다)','estar (있다·~상태이다)','tener (가지고 있다)','ir (가다)'],[
 ['yo','soy','estoy','tengo','voy'],['tú','eres','estás','tienes','vas'],['él/ella/usted','es','está','tiene','va'],
 ['nosotros/as','somos','estamos','tenemos','vamos'],['vosotros/as','sois','estáis','tenéis','vais'],['ellos/ellas/ustedes','son','están','tienen','van']])+
 chips(['Yo soy Elena','Yo estoy en mi despacho','Tengo un lápiz','Yo voy a trabajar','Yo voy en coche']),
 [X('연습 1. ser와 estar 활용','주어에 맞는 동사 형태를 고르세요.','ser: soy·eres·es·somos·sois·son / estar: estoy·estás·está·estamos·estáis·están.',
   P(['soy','eres','es','somos','sois','son'],[['Yo ___ profesora.','soy','yo → soy.'],['Tú ___ de Corea.','eres','tú → eres.'],['Usted ___ muy amable.','es','usted는 3인칭 단수 → es.'],['Nosotros ___ amigos.','somos','nosotros → somos.'],['Vosotros ___ estudiantes.','sois','vosotros → sois.'],['Ustedes ___ de México.','son','ustedes는 3인칭 복수 → son.']])+
   P(['está','están','estoy'],[['Ella ___ en la oficina.','está','ella → está.'],['Ellos ___ en casa.','están','ellos → están.']])),
  X('연습 2. tener와 ir 활용','알맞은 형태를 고르세요.','tener: tengo·tienes·tiene·tenemos·tenéis·tienen / ir: voy·vas·va·vamos·vais·van.',
   P(['tengo','tienes','tiene','tenemos','tenéis','tienen'],[['Yo ___ un lápiz.','tengo','yo → tengo.'],['Tú ___ 20 años.','tienes','tú → tienes.'],['Ella ___ un coche.','tiene','ella → tiene.'],['Nosotros ___ hambre.','tenemos','nosotros → tenemos.'],['Vosotros ___ clase hoy.','tenéis','vosotros → tenéis.']])+
   P(['voy','vas','vamos'],[['Yo ___ a trabajar.','voy','yo → voy.'],['Tú ___ al cine.','vas','tú → vas.'],['Nosotros ___ en coche.','vamos','nosotros → vamos.']])),
  X('연습 3. 직접 쓰기','괄호 안 동사를 알맞은 형태로 쓰세요.','불규칙 동사의 현재형 표를 떠올려 보세요.',
   T([['Ellos ___ al colegio. (ir)','van','ellos → van.'],['Vosotros ___ al parque. (ir)','vais','vosotros → vais.'],['Ella ___ en el despacho. (estar)','está','ella → está.'],['Yo ___ en mi despacho. (estar)','estoy','yo → estoy.'],['Vosotras ___ muy simpáticas. (ser)','sois','vosotras → sois.'],['Ellas ___ tres hermanos. (tener)','tienen','ellas → tienen.'],['Tú ___ en casa. (estar)','estás','tú → estás (악센트 주의).'],['Nosotras ___ de Madrid. (ser)','somos','nosotras → somos.']]))]
))

# ---------- 3 ----------
UNITS.append(U(3,'A1','SER, ESTAR y errores frecuentes','ser와 estar 구분, 자주 하는 실수',
 'ser(본질·정체성)와 estar(상태·위치)의 쓰임을 비교하고, 나이·거주 기간·날씨 표현에서 학습자가 자주 틀리는 문장을 바로잡습니다.',
 VS(1,85,84,94,110),
 TIP+'''<h2>핵심 정리</h2>
<p>기본 원리: <b>ser</b>는 변하지 않는 특징·정체, <b>estar</b>는 일시적 상태·위치입니다.</p>'''+tbl(['쓰임','ser','estar'],[
 ['사람','정체·정의: '+E('Es María. Es mi hermana pequeña'),'신체 상태: '+E('María está delgada')],
 ['특징 vs 기분','외모·성격: '+E('María es morena y guapa'),'기분: '+E('Está contenta')+' · '+E('Está cansada')],
 ['출신·결혼','국적·출신: '+E('Soy española')+' · '+E('Soy de Madrid'),'결혼 여부(스페인): '+E('Estoy soltera')],
 ['사물','재료·소유: '+E('Es una camiseta de algodón')+' · '+E('Es de mi hijo'),'상태: '+E('La camiseta está sucia')],
 ['직업','직업: '+E('Antonio es médico'),'임시 일자리 estar de: '+E('Ahora está de obrero en una fábrica')],
 ['시간','시각·요일·날짜: '+E('Son las tres')+' · '+E('Hoy es lunes'),'날짜·계절 말하기: '+E('Estamos a 16 de junio')+' · '+E('Estamos en primavera')],
 ['위치','<b>행사·사건</b>의 장소: '+E('El concierto es en el Teatro Real'),'사람·사물의 위치: '+E('El gato está dentro de la bolsa')+' · '+E('El niño está en el parque')],
 ['자세','','자세: '+E('La niña está sentada')],
])+'''
<h3>자주 하는 실수 4가지</h3>'''+tbl(['✘ 틀린 문장','✔ 올바른 문장','이유'],[
 ['Yo soy 46 años',E('Yo tengo 46 años'),'나이는 <b>tener</b>'],
 ['Yo tengo 2 años en Valencia',E('Yo llevo dos años en Valencia'),'~에서 지낸 기간은 <b>llevar</b> (tengo 2 años = 내 나이가 2살)'],
 ['Hoy es mucho calor',E('Hoy hace mucho calor'),'추위·더위·날씨는 <b>hacer</b>'],
 ['Dónde es el libro?',E('¿Dónde está el libro?'),'장소를 물을 때 <b>¿Dónde está + 관사 + 명사?</b>'],
])+chips(['¿Dónde está Madrid?','¿Dónde está la cocina?','¿Dónde está Mario?']),
 [X('연습 1. ser / estar 고르기','알맞은 동사를 고르세요.','정체·특징·시간·재료 → ser / 상태·기분·위치 → estar (행사 장소는 ser).',
   P(['es','está'],[['María ___ mi hermana pequeña.','es','정체(누구인지)는 ser.'],['María ___ contenta hoy.','está','기분은 estar.'],['La camiseta ___ sucia.','está','일시적 상태는 estar.'],['Antonio ___ médico.','es','직업은 ser.'],['Hoy ___ lunes.','es','요일은 ser.'],['El gato ___ dentro de la bolsa.','está','사물의 위치는 estar.'],['El concierto ___ en el Teatro Real.','es','행사·사건의 장소는 ser.']])+
   P(['soy','estoy'],[['Yo ___ de Madrid.','soy','출신은 ser.']])),
  X('연습 2. 실수 바로잡기','올바른 표현을 고르세요.','나이 tener / 거주 기간 llevar / 날씨 hacer / 위치 질문 ¿Dónde está?',
   P(['tengo','soy','estoy'],[['나는 46살이다: Yo ___ 46 años.','tengo','나이는 tener.']])+
   P(['hace','es','está'],[['Hoy ___ mucho calor.','hace','날씨는 hacer: hace calor, hace frío.']])+
   P(['llevo','tengo','soy'],[['발렌시아에 2년째 살고 있다: Yo ___ dos años en Valencia.','llevo','지낸 기간은 llevar + 기간.']])+
   P(['Dónde','Cómo','Quién'],[['¿___ está el libro?','Dónde','위치를 물을 때 dónde.']])+
   P(['de','en','con'],[['Es una camiseta ___ algodón.','de','재료는 de.']])+
   P(['en','a','de'],[['Estamos ___ primavera.','en','계절을 말할 때 estar en + 계절.'],['Estamos ___ 16 de junio.','a','날짜를 말할 때 estar a + 날짜.']])),
  X('연습 3. 직접 쓰기','괄호 안 동사를 알맞게 활용해 쓰세요.','tener, hacer, estar, ser, llevar의 현재형.',
   T([['Yo ___ 30 años. (tener)','tengo','나이 → tener.'],['Hoy ___ mucho frío. (hacer)','hace','날씨 → hacer의 3인칭 단수.'],['Ella ___ soltera. (estar, 스페인)','está','스페인에서 결혼 여부는 estar.'],['Las jirafas ___ muy altas. (ser)','son','특징 → ser, 주어가 복수.'],['Ahora él ___ de obrero en una fábrica. (estar)','está','임시 일자리 → estar de.'],['La niña ___ sentada. (estar)','está','자세 → estar.'],['Yo ___ tres años en Seúl. (llevar)','llevo','지낸 기간 → llevar.'],['¿Dónde ___ Madrid? (estar)','está','위치 질문 → estar.']]))]
))

# ---------- 4 ----------
UNITS.append(U(4,'A1','Describir personas','사람 묘사하기: 외모·성격·감정',
 'ser·estar·tener·llevar의 역할을 구분하고, 외모·머리카락·성격·감정 어휘로 사람을 묘사합니다.',
 VS(30,43,77,44,142),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. 사람 묘사에 쓰는 동사 4개</h3>'''+tbl(['동사','쓰임','예문'],[
 ['<b>ser</b>','본질·영구적 특징, 외모, 성격, 직업, 국적',E('Mi hermano es alto, delgado y guapo')],
 ['<b>estar</b>','일시적 상태, 기분, 자세, 위치',E('Está contento')+' · '+E('Está sentada')],
 ['<b>tener</b>','소유, 신체 부위, 나이, 신체 감각',E('Tiene la nariz grande')+' · '+E('Tiene 20 años')+' · '+E('Tiene sueño')],
 ['<b>llevar</b>','입고 걸친 것(옷·액세서리)',E('Lleva un pantalón y una camisa')],
])+rules(['머리카락·수염처럼 바뀔 수 있는 부분은 <b>본질적·지속적</b>이면 tener, <b>인위적·일시적</b>이면 llevar: '+E('Tiene barba')+' / '+E('Lleva el pelo rosa')+'.','결혼 상태는 스페인은 estar, 중남미는 ser.'])+'''
<h3>2. 외모 어휘</h3>'''+chips(['alto / alta','bajo / baja','gordo / gorda','delgado / delgada','guapo / guapa','feo / fea','joven','mayor','viejo / vieja'])+'''
<p><b>머리카락</b>: ser rubio·castaño·moreno·pelirrojo, 또는 <b>tener el pelo</b> + 색/모양 → '''+E('Tiene el pelo gris')+' · '+E('Tiene el pelo largo, liso y rizado')+'''</p>'''+chips(['largo','corto','liso','rizado','calvo / calva'])+warn('색은 <b>rubio, castaño</b>를 쓰고 amarillo, marrón은 쓰지 않아요. 부정적인 형용사는 <b>un poco</b>로 부드럽게: Es un poco feo. <b>barba, bigote, gafas</b>는 관사 없이 씁니다: Tiene gafas.')+'''
<h3>3. 성격 (ser + 형용사)</h3>'''+tbl(['긍정','반대'],[
 ['simpático 호감 가는','antipático 비호감인'],['alegre 명랑한','serio 진지한'],['sociable 사교적인','tímido 수줍은'],['abierto 개방적인','reservado 내성적인'],['hablador 말 많은','callado 말 없는'],['trabajador 부지런한','vago 게으른'],['tranquilo 차분한','nervioso 초조한'],['sincero 솔직한','mentiroso 거짓말쟁이'],['generoso 너그러운','egoísta 이기적인'],['cariñoso 다정한 · amable 친절한 · agradable 편안한 · inteligente 똑똑한','']])+'''
<h3>4. 감정 (estar + 형용사)</h3>'''+chips(['contento','feliz','triste','deprimido','tranquilo','relajado','nervioso','preocupado','cansado','agotado','estresado','enfadado','asustado','sorprendido','aburrido','enamorado'])+
 '<p>또 다른 표현: <b>estar de buen / mal humor</b>, <b>tener miedo</b>, <b>tener vergüenza</b>. 남성은 -o, 여성은 -a (feliz, relajado처럼 남녀 같은 것도 있어요).</p>',
 [X('연습 1. 알맞은 동사 고르기','ser, estar, tener, llevar 중 알맞은 것을 고르세요.','본질=ser / 상태=estar / 소유·나이·감각=tener / 입은 것=llevar.',
   P(['es','está','tiene','lleva'],[['Mi hermano ___ alto y delgado.','es','외모는 ser.'],['Ella ___ el pelo largo.','tiene','신체 부위·머리는 tener.'],['Hoy María ___ muy cansada.','está','일시적 상태는 estar.'],['Él ___ una camisa blanca.','lleva','입은 옷은 llevar.'],['Mi madre ___ 50 años.','tiene','나이는 tener.'],['Elena ___ simpática.','es','성격은 ser.']])+
   P(['están','tienen','son'],[['Los niños ___ sueño.','tienen','졸린 감각은 tener sueño.']])+
   P(['está','es','tiene'],[['Pablo ___ de mal humor.','está','기분은 estar de mal humor.']])),
  X('연습 2. 어휘 고르기','상황에 맞는 단어를 고르세요.','성격은 ser, 감정은 estar. 형용사의 성·수를 맞추세요.',
   P(['habladora','callada','seria'],[['내 이웃(여성)은 말이 많아요. Es ___.','habladora','hablador/a = 말이 많은.']])+
   P(['liso','rizado','calvo'],[['할아버지는 곱슬머리예요. Tiene el pelo ___.','rizado','rizado = 곱슬.']])+
   P(['sincero','mentiroso','vago'],[['Pedro는 항상 진실을 말해요. Es ___.','sincero','sincero = 솔직한.']])+
   P(['cansado','contento','enamorado'],[['많이 일한 뒤에 (남성): Estoy ___.','cansado','cansado = 피곤한.']])+
   P(['aburrido','enfadado','estresado'],[['할 일이 없을 때 (남성): Estoy ___.','aburrido','aburrido = 지루한.']])+
   P(['sorprendido','tranquilo','cansado'],[['예상 못한 일이 생기면 (남성) ___.','sorprendido','sorprendido = 놀란.']])+
   P(['generosa','egoísta','tímida'],[['Ana comparte lo que tiene. Es ___.','generosa','generoso/a = 너그러운, 나눠 주는.']])+
   P(['miedo','nervioso','mucho'],[['Yo tengo ___ de las arañas.','miedo','tener miedo de = ~을 무서워하다.']])),
  X('연습 3. 직접 쓰기','알맞은 단어를 쓰세요.','tener/llevar/estar/ser의 현재형과 감정·외모 어휘.',
   T([['Él ___ un pantalón y una camisa. (llevar)','lleva','입은 옷 → llevar.'],['Sí, ___ mucha sed. (tener, yo)','tengo','sed(갈증)는 tener.'],['Mi amigo es muy ___. (수줍은, 남성)','tímido','tímido/a = 수줍은.'],['María ___ embarazada. (estar)','está','임신 상태는 estar.'],['El hombre no tiene pelo. Es ___.','calvo','calvo/a = 대머리.'],['Ellos ___ de buen humor. (estar)','están','estar de buen humor.'],['Mi hermana ___ el pelo rosa. (염색, llevar)','lleva','인위적·일시적 → llevar.'],['Estoy muy ___ por el examen. (걱정되는, 남성)','preocupado','preocupado/a = 걱정하는.']]))]
))

# ---------- 5 ----------
UNITS.append(U(5,'A1','Los números','숫자: 기수와 서수',
 '0부터 백만 단위까지 숫자를 말하는 규칙과 uno/un/una, cien/ciento, 서수 primero~décimo를 익힙니다.',
 VS(6,5,56),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. 0~99</h3>'''+chips(['cero','uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve','diez'])+chips(['once','doce','trece','catorce','quince'])+chips(['dieciséis','diecisiete','dieciocho','diecinueve','veinte'])+chips(['veintiuno','veintidós','veintitrés','veinticuatro','veinticinco','veintiséis','veintisiete','veintiocho','veintinueve'])+chips(['treinta','cuarenta','cincuenta','sesenta','setenta','ochenta','noventa'])+
 rules(['11~29는 한 단어: 16~19는 <b>dieci-</b>, 21~29는 <b>veinti-</b>.','31~99는 <b>십의 자리 + y + 일의 자리</b>: '+E('treinta y ocho')+' · '+E('noventa y nueve')+' (y를 꼭 넣어요).','<b>uno</b>로 끝나는 수는 남·여 형태가 있어요: una, veintiuna, treinta y una. 남성 명사 앞이나 mil·millón 앞에서는 <b>un</b>: '+E('Solo hay un coche')+' · '+E('Son sesenta y un euros')+'.'])+'''
<h3>2. 100 이상</h3>'''+tbl(['수','표현'],[
 ['100',E('cien')+' (단독, 명사·mil·millones 앞) / '+E('ciento')+' (다른 수 앞: ciento dos)'],
 ['200~900',E('doscientos')+', '+E('trescientos')+', '+E('cuatrocientos')+', <b>'+E('quinientos')+'</b>, '+E('seiscientos')+', <b>'+E('setecientos')+'</b>, '+E('ochocientos')+', <b>'+E('novecientos')+'</b> (굵은 글씨는 불규칙)'],
 ['1,000','<b>mil</b> (✘ un mil). 2,000 → '+E('dos mil')],
 ['1,000,000',E('un millón')+' (un을 붙임) · 2,000,000 → '+E('dos millones')],
])+rules(['100 단위와 10 단위 사이에는 아무것도 넣지 않아요: '+E('doscientos cuarenta y ocho')+'.','200~900은 여성 명사 앞에서 <b>-as</b>: '+E('setecientas cincuenta libras')+'.','큰 수는 3자리씩 끊어 읽어요: '+E('un millón ochocientos tres mil ciento cuarenta y cuatro')+'.'])+'''
<h3>3. 서수</h3>'''+tbl(['번호','남성','여성'],[['1º / 1ª','primero','primera'],['2º','segundo','segunda'],['3º','tercero','tercera'],['4º','cuarto','cuarta'],['5º','quinto','quinta'],['6º','sexto','sexta'],['7º','séptimo','séptima'],['8º','octavo','octava'],['9º','noveno','novena'],['10º','décimo','décima']])+
 warn('남성 단수 명사 <b>앞</b>에서는 primero → <b>primer</b>, tercero → <b>tercer</b>: '+E('Vivo en el tercer piso')+'. 여성형(primera, tercera)은 그대로예요. 11번째 이상은 undécimo, duodécimo, decimotercero…'),
 [X('연습 1. 숫자 고르기','알맞은 표현을 고르세요.','16~19 dieci- / 21~29 veinti- / 31~99 y / cien·ciento / 200~900 -cientos.',
   P(['dieciséis','diecisiete','dieciocho'],[['16 → ___','dieciséis','16은 dieciséis.']])+
   P(['veintiuno','veintidós','treinta y uno'],[['21 → ___','veintiuno','21은 veintiuno.']])+
   P(['y','e','de'],[['45 → cuarenta ___ cinco','y','31~99에서는 십의 자리와 일의 자리 사이에 y.']])+
   P(['cien','ciento'],[['100 (단독) → ___','cien','단독일 때는 cien.'],['102 → ___ dos','ciento','다른 수가 이어지면 ciento.']])+
   P(['quinientos','cincocientos','quinientas'],[['500 → ___','quinientos','500은 불규칙: quinientos.']])+
   P(['setecientos','sietecientos'],[['700 → ___','setecientos','700은 불규칙: setecientos.']])+
   P(['mil','un mil'],[['1,000 → ___','mil','1,000은 mil. (un mil ✘)']])),
  X('연습 2. 성·수와 서수','알맞은 형태를 고르세요.','uno → un/una, 200~900 → -os/-as, 서수는 명사의 성·수에 맞춰요.',
   P(['mesas','coches'],[['Hay veintiuna ___.','mesas','una는 여성 명사와 → mesas.']])+
   P(['millón','millones','mil'],[['Tiene un ___ de euros.','millón','1,000,000은 un millón (복수는 millones).']])+
   P(['tercero','tercer','tercera'],[['Vivo en el ___ piso.','tercer','남성 단수 명사 앞 → tercer.']])+
   P(['segundo','segunda','segundas'],[['Es la ___ puerta.','segunda','puerta는 여성 → segunda.']])+
   P(['cuarto','cuarta','cuatro'],[['Vivo en el ___ piso. (4번째)','cuarto','서수 4번째 남성 → cuarto.']])+
   P(['libras','euros'],[['Cuesta trescientas ___. ','libras','trescientas가 여성형이므로 여성 명사 libras.']])+
   P(['primero','primer','primera'],[['Es el ___ examen.','primer','남성 단수 명사 앞 → primer.']])),
  X('연습 3. 숫자 쓰기','숫자를 스페인어로 쓰세요.','소문자로, 필요하면 악센트를 넣으세요.',
   T([['12 → ___','doce','12는 doce.'],['19 → ___','diecinueve','19는 diecinueve.'],['28 → ___','veintiocho','28은 veintiocho (한 단어).'],['37 → ___','treinta y siete','37은 treinta y siete.'],['90 → ___','noventa','90은 noventa.'],['1,500 → mil ___','quinientos','500은 quinientos.'],['9번째(남성): el ___','noveno','9번째 남성 → noveno.'],['10번째(여성): la ___','décima','10번째 여성 → décima (악센트).']]))]
))

# ---------- 6 ----------
UNITS.append(U(6,'A1','Días, meses, fechas y horas','요일·월·계절·날짜·시각',
 '요일·월·계절 이름, 날짜 읽는 순서, 시각을 말하고 묻는 법을 익힙니다.',
 VS(28,93,29,36),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. 요일·월·계절</h3>'''+chips(['lunes','martes','miércoles','jueves','viernes','sábado','domingo'])+chips(['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'])+chips(['la primavera','el verano','el otoño','el invierno'])+rules(['요일·월·계절은 <b>소문자</b>로 써요 (영어와 달라요).','모두 <b>남성</b>이고, 월 이름 앞에는 el을 붙이지 않아요: '+E('En España enero es un mes muy frío')+'.','요일은 lunes~viernes가 단·복수 같고, sábado·domingo만 복수형이 있어요: '+E('Odio los lunes y me encantan los sábados')+'. fin de semana → los fines de semana.','스페인의 주는 lunes에 시작하고 sábado·domingo가 주말이에요.','북반구 계절: 봄 3월 21일경~6월 21일경, 여름 ~9월 21일경, 가을 ~12월 21일경, 겨울 ~3월 21일경.'])+'''
<h3>2. 날짜</h3>'''+rules(['순서는 <b>일 + de + 월 + de + 연도</b>: 10/1/2010 → '+E('diez de enero de 2010')+'.','일은 기수(uno, dos…)로 읽고 서수는 쓰지 않아요.','날짜 앞에는 <b>el</b>: '+E('Se casaron el 5 de junio de 2013')+'. hoy, ayer, mañana 뒤에는 관사 없이: '+E('Hoy es 6 de febrero de 2017')+'.','요일을 함께 말하면 요일이 먼저: '+E('Nos vamos al Caribe el viernes 14 de abril')+'.','연도는 점 없이 2017 (✘ 2.017).'])+'''
<h3>3. 시각</h3>'''+tbl(['시각','표현','규칙'],[
 ['1:00',E('Es la una'),'1시만 단수 <b>Es la</b>'],['3:00',E('Son las tres en punto'),'나머지는 <b>Son las</b>'],['3:05',E('Son las tres y cinco'),'1~30분: 시 + y + 분'],['3:15',E('Son las tres y cuarto'),'15분 = cuarto'],['3:30',E('Son las tres y media'),'30분 = media'],['3:35 / 4:45',E('Son las cuatro menos veinticinco')+' · '+E('Son las cinco menos cuarto'),'31~59분: <b>다음 시 + menos + 남은 분</b>']])+rules(['12시간제로 말하고 필요하면 <b>de la mañana / de la tarde / de la noche</b>를 붙여요: '+E('las diez y media de la noche')+'.','시각을 물을 땐 '+E('¿Qué hora es?')+', 몇 시에 하는지 물을 땐 <b>a</b>를 써요: '+E('¿A qué hora comes?')+' — '+E('A las dos y media')+'.']),
 [X('연습 1. 요일·월·날짜','알맞은 답을 고르세요.','요일·월·계절은 소문자 / 날짜는 el + 일 + de + 월 + de + 연도.',
   P(['minúscula','mayúscula'],[['스페인어에서 요일 이름은 ___로 씁니다.','minúscula','요일·월·계절·국적은 소문자.']])+
   P(['lunes','domingo','sábado'],[['스페인에서 한 주의 첫날은 ___.','lunes','스페인의 주는 lunes에 시작.']])+
   P(['domingo','viernes','lunes'],[['주말은 sábado와 ___.','domingo','fin de semana = sábado + domingo.']])+
   P(['febrero','enero','diciembre'],[['일 수가 가장 적은 달은 ___.','febrero','2월 febrero.']])+
   P(['de','en','a'],[['10/1/2010 → diez ___ enero de dos mil diez.','de','일과 월 사이에는 de.']])+
   P(['el','la','en'],[['Se casaron ___ 5 de junio de 2013.','el','날짜 앞에는 el.']])+
   P(['primavera','verano','otoño'],[['3월 21일에 시작하는 계절은 ___.','primavera','봄 = primavera.']])),
  X('연습 2. 시각 말하기','알맞은 표현을 고르세요.','1시 Es la una / 나머지 Son las / 15분 cuarto / 30분 media / 31분 이후 menos.',
   P(['Es la','Son las'],[['1:00 → ___ una.','Es la','1시만 단수: Es la una.'],['3:00 → ___ tres en punto.','Son las','2시 이후 → Son las.']])+
   P(['cuarto','media','cinco'],[['3:15 → Son las tres y ___.','cuarto','15분 = y cuarto.']])+
   P(['media','cuarto','diez'],[['3:30 → Son las tres y ___.','media','30분 = y media.']])+
   P(['menos','y','con'],[['4:45 → Son las cinco ___ cuarto.','menos','45분은 다음 시 menos cuarto.']])+
   P(['veinticinco','treinta y cinco','veinte'],[['4:35 → Son las cinco menos ___.','veinticinco','다음 시까지 남은 분 25분.']])+
   P(['Qué','Cuál','Cuándo'],[['¿___ hora es?','Qué','시각을 물을 땐 ¿Qué hora es?']])+
   P(['A','En','De'],[['¿___ qué hora comes?','A','몇 시에 하는지 물을 때 a qué hora.']])),
  X('연습 3. 직접 쓰기','알맞은 단어를 쓰세요.','소문자로 쓰고 악센트를 확인하세요.',
   T([['9월 → ___','septiembre','septiembre (p 하나, 소문자).'],['7:00 → Son las siete en ___.','punto','정각 = en punto.'],['2:10 → Son las dos y ___.','diez','분 단위는 y + 숫자.'],['오후 1:20 → Es la una y veinte de la ___.','tarde','오후 = de la tarde.'],['Odio los lunes y me encantan los ___. (토요일 복수)','sábados','sábado의 복수는 sábados.'],['16/8/2000 → dieciséis de ___ de dos mil','agosto','8월 = agosto.'],['Estamos en ___. (가을)','otoño','가을 = otoño (ñ 주의).'],['주말 → los fines de ___','semana','fin de semana의 복수 → los fines de semana.']]))]
))

# ---------- 7 ----------
UNITS.append(U(7,'A1','Países y nacionalidades','국가와 국적',
 '스페인어를 쓰는 나라들과 세계 주요 국가의 이름·국적 형용사, 국적 형용사의 성·수 변화를 익힙니다.',
 VS(51,52,53,54),
 TIP+'''<h2>핵심 정리</h2>
<p>스페인어는 21개 나라(유럽 1, 아프리카 1, 아메리카 19)에서 공용어 또는 공동 공용어입니다. 국적 형용사는 <b>소문자</b>로 씁니다.</p>
<h3>1. 스페인어권 국가</h3>'''+tbl(['국가','남 / 여'],[
 ['España',E('español')+' / '+E('española')],['Guinea Ecuatorial',E('ecuatoguineano')+' / '+E('ecuatoguineana')],['México',E('mexicano')+' / '+E('mexicana')],['Cuba',E('cubano')+' / '+E('cubana')],['República Dominicana',E('dominicano')+' / '+E('dominicana')],['Puerto Rico',E('puertorriqueño')+' / '+E('puertorriqueña')],['Guatemala',E('guatemalteco')+' / '+E('guatemalteca')],['Honduras',E('hondureño')+' / '+E('hondureña')],['El Salvador',E('salvadoreño')+' / '+E('salvadoreña')],['Nicaragua',E('nicaragüense')+' (남녀 같음)'],['Costa Rica',E('costarricense')+' (남녀 같음)'],['Panamá',E('panameño')+' / '+E('panameña')],['Colombia',E('colombiano')+' / '+E('colombiana')],['Venezuela',E('venezolano')+' / '+E('venezolana')],['Ecuador',E('ecuatoriano')+' / '+E('ecuatoriana')],['Perú',E('peruano')+' / '+E('peruana')],['Bolivia',E('boliviano')+' / '+E('boliviana')],['Paraguay',E('paraguayo')+' / '+E('paraguaya')]])+
 '<p class="tip">그 밖에 Uruguay(uruguayo), Argentina(argentino), Chile(chileno)도 스페인어권 국가예요.</p><h3>2. 세계의 나라</h3>'+tbl(['지역','국가 → 국적 (남 / 여)'],[
 ['유럽','Portugal → portugués / portuguesa · Italia → italiano / italiana · Francia → francés / francesa · Reino Unido → británico / británica · Alemania → alemán / alemana · Polonia → polaco · Rusia → ruso'],
 ['아메리카','Canadá → canadiense · Estados Unidos → estadounidense · Brasil → brasileño / brasileña'],
 ['아프리카','Marruecos → marroquí · Egipto → egipcio / egipcia · Nigeria → nigeriano · Sudáfrica → sudafricano'],
 ['아시아','Turquía → turco / turca · India → indio / india · China → chino / china · Japón → japonés / japonesa']])+'''
<h3>3. 성·수 규칙</h3>'''+rules(['<b>-o</b>로 끝나면 남성, 여성은 -o → <b>-a</b>: mexicano / mexicana.','<b>자음</b>으로 끝나면 남성, 여성은 <b>-a</b>를 붙여요: español / española, francés / francesa, alemán / alemana.','<b>-e, -í</b>로 끝나면 남녀 같아요: canadiense, marroquí.','복수: 모음 뒤 <b>-s</b> (mexicanos), 자음·í 뒤 <b>-es</b> (españoles, marroquíes).','악센트가 있던 -és, -án은 복수·여성형에서 악센트가 사라져요: francés → franceses, francesa / alemán → alemanes, alemana.','남녀 혼합 그룹은 <b>남성 복수</b>를 써요.']),
 [X('연습 1. 국적 형용사','알맞은 형태를 고르세요.','-o → -a / 자음 → +a / -e·-í 남녀 동일 / 복수 -s·-es.',
   P(['mexicano','mexicana','mexicanas'],[['Ella es de México. Es ___.','mexicana','여성형은 -a.']])+
   P(['francés','francesa','franceses'],[['Él es de Francia. Es ___.','francés','남성 단수는 악센트가 있는 francés.']])+
   P(['alemán','alemana','alemanas'],[['Ellas son de Alemania. Son ___.','alemanas','여성 복수 → alemanas.']])+
   P(['canadiense','canadienso','canadiensa'],[['Mi amiga es de Canadá. Es ___.','canadiense','-e로 끝나면 남녀 동일.']])+
   P(['estadounidenses','estadounidenseses','estadounidensos'],[['Ellos son de Estados Unidos. Son ___.','estadounidenses','-e로 끝나는 형용사의 복수는 -s.']])+
   P(['japonés','japonesa','japoneses'],[['Ella es de Japón. Es ___.','japonesa','여성형 -a를 붙이고 악센트 삭제.']])+
   P(['marroquí','marroquía','marroquío'],[['Él es de Marruecos. Es ___.','marroquí','-í로 끝나면 남녀 동일.']])+
   P(['colombianos','colombianas','colombiano'],[['Nosotros (남자들) somos ___.','colombianos','남성 복수 → colombianos.']])),
  X('연습 2. 국적에서 나라 찾기','알맞은 나라를 고르세요.','국적 형용사의 어근을 떠올려 보세요.',
   P(['Colombia','Ecuador','Venezuela'],[['Una persona colombiana es de ___.','Colombia','colombiano → Colombia.']])+
   P(['Perú','Bolivia','Paraguay'],[['Una persona peruana es de ___.','Perú','peruano → Perú.']])+
   P(['Costa Rica','Cuba','Honduras'],[['Una persona costarricense es de ___.','Costa Rica','costarricense → Costa Rica.']])+
   P(['Panamá','Paraguay','Perú'],[['Una persona panameña es de ___.','Panamá','panameño → Panamá.']])+
   P(['El Salvador','Honduras','Guatemala'],[['Una persona salvadoreña es de ___.','El Salvador','salvadoreño → El Salvador.']])+
   P(['Puerto Rico','República Dominicana','Cuba'],[['Una persona puertorriqueña es de ___.','Puerto Rico','puertorriqueño → Puerto Rico.']])+
   P(['Guinea Ecuatorial','Ecuador','México'],[['Una persona ecuatoguineana es de ___.','Guinea Ecuatorial','ecuatoguineano → Guinea Ecuatorial.']])+
   P(['República Dominicana','Puerto Rico','Panamá'],[['Una persona dominicana es de ___.','República Dominicana','dominicano → República Dominicana.']])),
  X('연습 3. 국적 쓰기','괄호의 성별에 맞게 국적 형용사를 쓰세요.','소문자로 쓰세요.',
   T([['Ella es de China. Es ___.','china','여성형 chino → china.'],['Él es de Italia. Es ___.','italiano','남성형 italiano.'],['Ellos son de Portugal. Son ___.','portugueses','portugués의 복수 → portugueses.'],['Ella es de Brasil. Es ___.','brasileña','brasileño의 여성형 → brasileña (ñ).'],['Él es de Argentina. Es ___.','argentino','남성형 argentino.'],['Ellas son de Rusia. Son ___.','rusas','ruso의 여성 복수 → rusas.'],['Soy ___. (스페인 여성)','española','국적은 소문자, 여성형 española.'],['Ella es de Reino Unido. Es ___.','británica','británico의 여성형 → británica (악센트 유지).']]))]
))

# ---------- 8 ----------
UNITS.append(U(8,'A1','Colores y ropa','색깔과 옷, 신발, 액세서리',
 '색 이름과 성·수 일치, 옷·신발·액세서리 어휘, 옷 가게에서 쓰는 표현을 익힙니다.',
 VS(65,82,18,17),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. 색깔</h3>'''+chips(['negro','blanco','gris','azul','verde','rojo','amarillo','naranja','marrón','rosa','morado','granate','violeta'])+rules(['<b>claro / oscuro</b>를 붙이면 더 구체적: azul claro, verde oscuro.','중남미 표현: naranja → anaranjado, marrón → café, rosa → rosado, azul claro → celeste.','색 이름 자체는 <b>남성 명사</b>: '+E('El amarillo es mi color favorito')+'.','명사를 꾸미는 형용사일 때는 명사와 <b>성·수 일치</b>: '+E('La camiseta es amarilla')+' · '+E('Tengo unas botas verdes')+'.','색을 물을 때: '+E('¿De qué color son las botas?')+' — '+E('Son verdes')+' / '+E('Son de color verde')+'.'])+'''
<h3>2. 옷 (la ropa)</h3>'''+chips(['la camisa','la camiseta','los pantalones','los vaqueros','la falda','la chaqueta','el jersey','la cazadora','el abrigo','el vestido','el traje','el pijama','el bañador','el biquini'])+'<p><b>속옷</b>: calzoncillos, bragas, sujetador, calcetines, medias · <b>탈의실</b>: el probador → '+E('¿Por qué no te los pruebas?')+'</p><h3>3. 신발과 액세서리</h3>'+tbl(['분류','어휘'],[
 ['신발 (zapatería에서 구입)','botas · sandalias (더울 때) · zapatos · zapatos de tacón · zapatillas de deporte (deportivas)'],
 ['머리','sombrero · gorra (햇빛) · gorro (추위)'],
 ['추위','bufanda (목) · guantes (손)'],
 ['날씨','gafas de sol · paraguas · pañuelo'],
 ['몸에 걸치는 것','reloj · cinturón · corbata'],
 ['가방','cartera (돈·카드) · bolso · mochila · maletín'],
 ['보석 (joyería)','pendientes (귀) · collar (목) · pulsera (손목) · anillo (손가락)']]),
 [X('연습 1. 색과 성·수 일치','알맞은 형태를 고르세요.','색 형용사는 명사의 성·수와 일치.',
   P(['amarillo','amarilla','amarillas'],[['La camiseta es ___.','amarilla','camiseta는 여성 단수 → amarilla.'],['El sol es ___.','amarillo','sol은 남성 단수 → amarillo.']])+
   P(['verde','verdes'],[['Tengo unas botas ___.','verdes','botas는 복수 → verdes.'],['El árbol es ___.','verde','verde는 남녀 동일, 단수.']])+
   P(['rojas','rojos','roja'],[['Las botas son ___.','rojas','botas는 여성 복수 → rojas.']])+
   P(['azul','azules'],[['La ballena es ___.','azul','단수 → azul.']])+
   P(['gris','grises'],[['El tiburón es ___.','gris','단수 → gris.']])+
   P(['blanco','blanca','blancos'],[['El coche es ___.','blanco','coche는 남성 단수 → blanco.']])),
  X('연습 2. 어휘 고르기','설명에 맞는 단어를 고르세요.','액세서리와 옷 이름.',
   P(['bufanda','corbata','gorra'],[['추울 때 목에 두르는 것: la ___.','bufanda','bufanda = 목도리.']])+
   P(['sol','lluvia','frío'],[['햇빛이 강할 때: las gafas de ___.','sol','gafas de sol = 선글라스.']])+
   P(['paraguas','sombrero','pañuelo'],[['비에 젖지 않게: el ___.','paraguas','paraguas = 우산.']])+
   P(['guantes','botas','pendientes'],[['손에 끼는 것: los ___.','guantes','guantes = 장갑.']])+
   P(['reloj','anillo','cinturón'],[['시간을 알려 주는 것: el ___.','reloj','reloj = 시계.']])+
   P(['corbata','bolso','collar'],[['정장에 남자들이 매는 것: la ___.','corbata','corbata = 넥타이.']])+
   P(['zapatos','guantes','pendientes'],[['zapatería에서 사는 것: los ___.','zapatos','zapatería = 신발 가게.']])+
   P(['pendientes','anillos','pulseras'],[['귀에 하는 장신구: los ___.','pendientes','pendientes = 귀걸이.']])),
  X('연습 3. 직접 쓰기','알맞은 단어를 쓰세요.','옷·액세서리 어휘와 색 질문.',
   T([['Cuando hace calor llevo ___. (샌들)','sandalias','sandalias = 샌들.'],['Necesito unos pantalones ___. (청바지)','vaqueros','pantalones vaqueros = 청바지.'],['Voy a probarme la camiseta en el ___.','probador','probador = 탈의실.'],['Para nadar necesito un ___.','bañador','bañador = 수영복.'],['En invierno llevo un ___. (코트)','abrigo','abrigo = 코트.'],['¿De ___ color son las botas?','qué','색을 물을 때 ¿De qué color…?'],['Las botas son de ___ rojo.','color','Son de color rojo.'],['Mi color favorito es el ___. (노란색)','amarillo','색 이름은 남성 명사.']]))]
))
