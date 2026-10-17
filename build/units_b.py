from lib import *
UNITS=[]

# ---------- 9 ----------
UNITS.append(U(9,'A1','Alimentos, bebidas y comidas','음식·음료와 스페인의 식사 시간',
 '식재료·과일·채소·음료 어휘, 잔과 용기 이름, 스페인의 하루 다섯 끼 식사 문화를 익힙니다.',
 VS(10,12,143,59),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. 식재료 (los alimentos)</h3>'''+tbl(['분류','어휘'],[
 ['기본 식품',chips(['la pasta','el arroz','las patatas','los huevos','el pan','el pan de molde'])],
 ['고기',chips(['el pollo','el pavo','la ternera','el cordero','el cerdo','el jamón serrano','el chorizo','las salchichas'])],
 ['생선·해산물',chips(['la merluza','el salmón','la sardina','el atún','el marisco'])],
 ['채소',chips(['la lechuga','el tomate','el pimiento','la cebolla','la zanahoria','el pepino'])],
 ['과일',chips(['la naranja','la manzana','el plátano','la pera','el limón','el melocotón','las cerezas','la fresa','la piña','la sandía','el melón','las uvas'])],
 ['양념',chips(['el azúcar','la sal','el aceite','el vinagre','la pimienta','el ajo','el perejil'])],
 ['유제품',chips(['la leche','el queso','el yogur','la mantequilla','la mermelada'])],
 ['단 것',chips(['el chocolate','el pastel','la tarta','el helado','la galleta','los caramelos'])],
])+'''
<h3>2. 음료 (las bebidas)</h3>'''+rules(['<b>따뜻한 음료</b>: café <b>solo</b>(그냥 커피) · café <b>con leche</b>(커피 반, 우유 반) · café <b>cortado</b>(커피 많이, 우유 조금) · té · infusión(manzanilla, tila, poleo) · chocolate a la taza.','<b>차가운 무알코올</b>: agua del grifo / agua mineral (<b>con gas / sin gas</b>) · zumo (스페인에서는 오렌지 주스가 흔함) · refresco.','<b>술</b>: vino <b>tinto / rosado / blanco</b> · cerveza (<b>caña</b> 작은 잔, <b>jarra</b> 큰 잔) · ron, ginebra, whisky · champán / <b>cava</b>(카탈루냐산) · cóctel.'])+'''
<h3>3. 잔과 용기</h3>'''+chips(['el vaso','la taza','la copa','la botella','la lata','el cartón / el brick','la jarra'])+'''
<h3>4. 스페인의 식사</h3>'''+tbl(['식사','시간·특징'],[
 ['<b>el desayuno</b> 아침','7~9시, 커피·우유 + 올리브유 토스트·빵·과일. 초콜릿과 추로스는 휴일 메뉴'],
 ['<b>el almuerzo</b> 간식','오전 중간에 먹는 사람도 있음'],
 ['<b>la comida</b> 점심','14~15시, 하루 중 가장 중요한 식사. primero · segundo · postre 3코스'],
 ['<b>la merienda</b> 오후 간식','오후 중간'],
 ['<b>la cena</b> 저녁','20:30~21:30, 점심보다 가벼움'],
]),
 [X('연습 1. 음식 분류','알맞은 단어를 고르세요.','과일·채소·양념·유제품·고기·생선을 구분해 보세요.',
   P(['Zanahoria','Manzana','Cebolla'],[['___ es una fruta.','Manzana','manzana = 사과, 과일.']])+
   P(['Sal','Pollo','Pera'],[['___ es un condimento.','Sal','sal = 소금, 양념.']])+
   P(['Queso','Pan','Arroz'],[['___ es un producto lácteo.','Queso','queso = 치즈, 유제품.']])+
   P(['Chorizo','Merluza','Yogur'],[['El cerdo da el jamón serrano y el ___.','Chorizo','cerdo(돼지)에서 jamón serrano와 chorizo가 나와요.']])+
   P(['atún','cordero','lechuga'],[['La merluza, el salmón, la sardina y el ___ son pescados.','atún','atún = 참치, 생선.']])+
   P(['helado','pepino','vinagre'],[['El ___ es un dulce.','helado','helado = 아이스크림, 단 것.']])+
   P(['tomate','chocolate','leche'],[['En la ensalada hay lechuga, ___ y cebolla.','tomate','tomate는 채소.']])+
   P(['mantequilla','pimienta','piña'],[['En las tostadas pones ___ y mermelada.','mantequilla','mantequilla = 버터.']])),
  X('연습 2. 음료 이름','알맞은 단어를 고르세요.','café solo / con leche / cortado, vino tinto·rosado·blanco, caña·jarra.',
   P(['solo','cortado','con leche'],[['Un café ___ es café sin nada más.','solo','café solo = 아무것도 넣지 않은 커피.']])+
   P(['cortado','solo','con leche'],[['Un café ___ tiene mucho café con un poco de leche.','cortado','cortado = 커피 많이, 우유 조금.']])+
   P(['leche','azúcar','hielo'],[['Un café con ___ es mitad café y mitad leche.','leche','café con leche.']])+
   P(['tinto','rosado','blanco'],[['El vino de color rojo oscuro es ___.','tinto','vino tinto = 레드 와인.']])+
   P(['caña','cava','poleo'],[['En un bar una cerveza en un vaso pequeño es una ___.','caña','caña = 작은 잔 맥주.']])+
   P(['cava','ron','zumo'],[['El “champán” elaborado en Cataluña se llama ___.','cava','cava = 카탈루냐산 발포주.']])+
   P(['poleo','whisky','ginebra'],[['Las infusiones más típicas son manzanilla, tila y ___.','poleo','manzanilla, tila, poleo.']])+
   P(['gas','sal','hielo'],[['Agua mineral sin ___.','gas','con gas / sin gas = 탄산 있음/없음.']])),
  X('연습 3. 식사와 용기','알맞은 단어를 쓰세요.','스페인의 식사 이름과 잔·용기 이름.',
   T([['오후 2~3시에 먹는 식사: la ___.','comida','la comida = 점심.'],['저녁 8시 30분에 먹는 식사: la ___.','cena','la cena = 저녁.'],['아침 식사: el ___.','desayuno','el desayuno = 아침 식사.'],['오후 간식: la ___.','merienda','la merienda = 오후 간식.'],['와인은 보통 ___에 마셔요. (잔)','copa','vino → copa.'],['커피는 ___에 마셔요.','taza','café → taza.'],['콜라 한 ___. (캔)','lata','lata = 캔.'],['스페인에서 가장 흔한 주스는 ___ 주스예요. (오렌지)','naranja','zumo de naranja.']]))]
))

# ---------- 10 ----------
UNITS.append(U(10,'A1','En la tienda, el bar, el restaurante y el hotel','가게·바·식당·호텔에서 쓰는 여행 표현',
 '스페인 여행에서 바로 쓸 수 있는 쇼핑, 바에서 주문하기, 식당 예약·주문, 호텔 체크인 표현을 익힙니다.',
 VS(108,111,117,113),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. 가게에서</h3>'''+tbl(['상황','표현'],[
 ['들어가며',E('Buenos días')+' / '+E('Buenas tardes')],['점원',E('¿Necesitas algo?')],['찾는 게 있을 때',E('Busco un / una …')],['필요 없을 때',E('No, gracias. Solo estoy mirando')],['계산',E('¿Puedo pagar con tarjeta?')+' · '+E('en efectivo')+' (동전·지폐)'],['나갈 때',E('Adiós, gracias')]])+'''
<h3>2. 바에서</h3>'''+rules(['자리: <b>la terraza</b>(야외) · <b>una mesa dentro</b> · <b>la barra</b>.','보통 <b>바에서 주문</b>하고, 계산도 주문할 때 하는 경우가 많아요.','대표 메뉴: <b>las tapas</b>, cerveza, vino.','웨이터에게는 보통 usted를 쓰지 않아요: '+E('Me pones una cerveza y una tapa de croquetas')+'.'])+'''
<h3>3. 식당에서</h3>'''+tbl(['상황','표현'],[
 ['예약했을 때',E('Tengo una reserva a nombre de …')],['예약 안 했을 때',E('¿Tenéis mesa para tres personas?')],['메뉴 요청','<b>la carta</b> 또는 <b>el menú del día</b>를 달라고 해요'],['주문 순서',E('De primero quiero salmorejo')+' · '+E('De segundo, pescado con patatas fritas')+' · '+E('Para beber, agua')],['계산','efectivo 또는 tarjeta']])+'''
<h3>4. 호텔에서</h3>'''+rules(['<b>la recepción</b>에서 <b>el recepcionista / la recepcionista</b>가 예약을 확인하고 <b>número de habitación</b>을 알려 줘요.','<b>pasaporte</b> 같은 공식 신분증을 보여 주고, <b>la llave</b> 또는 <b>la tarjeta</b>를 받아요.',E('Buenos días, tengo una reserva a nombre de …'),E('¿Me recomiendas alguna playa, museo o restaurante?')]),
 [X('연습 1. 상황별 표현','빈칸에 알맞은 단어를 고르세요.','tienda: busco / solo estoy mirando / pagar con tarjeta·efectivo; bar: barra; hotel: reserva·llave.',
   P(['una','un','unas'],[['Busco ___ camiseta.','una','camiseta는 여성 단수 → una.']])+
   P(['mirando','comprando','buscando'],[['No, gracias. Solo estoy ___.','mirando','Solo estoy mirando = 그냥 둘러보는 중이에요.']])+
   P(['tarjeta','efectivo','moneda'],[['Puedo pagar con ___ de crédito.','tarjeta','tarjeta de crédito = 신용카드.']])+
   P(['efectivo','tarjeta','factura'],[['Pago con monedas y billetes: en ___.','efectivo','en efectivo = 현금으로.']])+
   P(['barra','habitación','llave'],[['En el bar normalmente pides en la ___.','barra','la barra = 바 카운터.']])+
   P(['pones','pongo','pone'],[['Me ___ una cerveza, por favor.','pones','웨이터에게 편하게: Me pones … (tú 형태).']])+
   P(['reserva','llave','carta'],[['Buenos días, tengo una ___ a nombre de García.','reserva','reserva = 예약.']])+
   P(['llave','pasaporte','barra'],[['Para entrar en tu habitación, el recepcionista te da la ___.','llave','la llave 또는 la tarjeta.']])),
  X('연습 2. 대화 완성','대화에 맞는 단어를 고르세요.','식당 주문: de primero, de segundo, para beber.',
   P(['algo','nada','alguien'],[['점원: ¿Necesitas ___?','algo','¿Necesitas algo? = 필요한 거 있으세요?']])+
   P(['gracias','hola','luego'],[['필요 없을 때: No, ___.','gracias','No, gracias.']])+
   P(['Tenéis','Tienes','Tengo'],[['식당에서 (여러 명 직원에게): ¿___ mesa para tres personas?','Tenéis','복수 vosotros → tenéis.']])+
   P(['primero','primer','primera'],[['De ___ quiero salmorejo.','primero','de primero = 첫 번째 코스로.']])+
   P(['segundo','segunda','dos'],[['De ___, pescado con patatas fritas.','segundo','de segundo = 두 번째 코스(메인)로.']])+
   P(['beber','bebida','bebido'],[['Para ___, agua.','beber','para beber = 마실 것으로는.']])+
   P(['recomiendas','recomiendo','recomienda'],[['호텔에서: ¿Me ___ alguna playa?','recomiendas','tú 형태: recomiendas.']])+
   P(['documento','habitación','recepción'],[['호텔에서는 공식 ___ de identidad을 보여 줘야 해요.','documento','documento de identidad = 신분증.']])),
  X('연습 3. 직접 쓰기','알맞은 단어를 쓰세요.','여행 표현 완성하기.',
   T([['Tengo una reserva a ___ de Lee.','nombre','a nombre de = ~ 이름으로.'],['Me ___ una cerveza y una tapa. (poner, 비격식)','pones','Me pones … = 주세요.'],['가게에서 일하는 남자 점원: el ___.','dependiente','dependiente/a = 점원.'],['호텔 프런트 직원: el o la ___.','recepcionista','recepcionista = 접수 직원.'],['메뉴판: la ___ 또는 el menú del día.','carta','la carta = 메뉴판.'],['현금으로 → en ___.','efectivo','efectivo = 현금.'],['점원: ¿Necesitas ___?','algo','Necesitas algo?'],['Hotel에서 방 번호를 알려 주는 곳: la ___.','recepción','la recepción = 프런트.']]))]
))

# ---------- 11 ----------
UNITS.append(U(11,'A1','Cocina española','스페인 음식 만들기: 가스파초·상그리아·토르티야',
 '요리 영상에서 나오는 재료·분량·도구·순서 표현을 익히고, 스페인의 대표 음식 4가지를 소개합니다.',
 VS(9,11,115,116,121),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. 대표 음식 4가지</h3>'''+tbl(['음식','설명'],[
 ['<b>El gazpacho</b>','토마토로 만든 <b>차가운 수프</b>. 주로 여름에 먹어요.'],
 ['<b>La sangría</b>','<b>와인과 과일</b>로 만든 시원한 여름 음료 (알코올 있음).'],
 ['<b>La tortilla de patatas</b>','감자 오믈렛. 재료: huevos, patatas, sal, aceite de oliva (+ cebolla).'],
 ['<b>Melón con jamón</b>','멜론에 하몽을 말아 이쑤시개로 고정하는 여름 타파.'],
])+'''
<h3>2. 가스파초 (4인분)</h3>'''+tbl(['재료','도구'],[
 ['1 kilo de tomates (잘 익은 것) · ½ pimiento verde · ½ pepino · 1 diente de ajo · 3 rebanadas de pan · 50 g de aceite de oliva · 15 g de vinagre · 1 cucharita de sal','batidora(믹서) · cuchillo · cucharita · cuchara de madera · tabla de cortar']])+rules(['<b>Lo primero</b>: lavar bien las verduras.','토마토·오이·피망을 <b>cortar en trozos</b>해 믹서에 넣어요.','<b>pan</b>은 걸쭉해지도록(<b>para que espese</b>) 넣어요.','마지막에 sal → vinagre → aceite를 넣고 2~3분 <b>batir</b>.','<b>nevera</b>에서 차게 식힌 뒤 먹어요.'])+'''
<h3>3. 상그리아</h3>'''+rules(['재료: <b>litro y medio de vino rosado</b>, azúcar(한 숟갈 반), un limón, un melocotón.','도구: jarra, cuchara, cuchillo, cuchara de madera, tabla, <b>sacacorchos</b>(와인 따개).','과일을 씻고 <b>pelar</b>, <b>cortar en trozos pequeños</b> → 와인 + 과일 + 설탕 → 섞기.','냉장고에 몇 시간 두고, 마지막에 <b>hielos</b>를 넣어요 (알코올을 살짝 낮춰 줘요).'])+'''
<h3>4. 요리할 때 자주 쓰는 표현</h3>'''+chips(['Vamos a cocinar gazpacho','Necesitamos un kilo de tomates','Lo primero que tenemos que hacer es lavar las verduras','Vamos a cortar los tomates','Tapamos la batidora','Ya solo queda batir la mezcla','Ahora hay que dejarlo en la nevera']),
 [X('연습 1. 음식 이해하기','알맞은 단어를 고르세요.','gazpacho = 차가운 토마토 수프 / sangría = 와인+과일 / tortilla = huevos + patatas + aceite de oliva.',
   P(['fría','caliente','dulce'],[['El gazpacho es una sopa ___ de tomate.','fría','gazpacho는 차가운 수프.']])+
   P(['tomate','pepino','pan'],[['El ingrediente principal del gazpacho es el ___.','tomate','주재료는 토마토.']])+
   P(['espese','enfríe','hierva'],[['El pan se añade al gazpacho para que ___.','espese','espesar = 걸쭉해지다.']])+
   P(['fruta','carne','pescado'],[['La sangría lleva vino y ___.','fruta','와인과 과일.']])+
   P(['sacacorchos','batidora','sartén'],[['Para abrir la botella de vino necesitamos un ___.','sacacorchos','와인 따개.']])+
   P(['oliva','girasol','coco'],[['La tortilla de patatas lleva huevos, patatas, sal y aceite de ___.','oliva','aceite de oliva = 올리브유.']])+
   P(['darle','dormirle','abrirle'],[['La parte más difícil de la tortilla es ___ la vuelta.','darle','darle la vuelta = 뒤집다.']])+
   P(['palillo','tenedor','cuchillo'],[['En el melón con jamón fijamos el jamón con un ___.','palillo','palillo = 이쑤시개.']])),
  X('연습 2. 재료와 분량','알맞은 표현을 고르세요.','un/medio/una, 단위(kilo, gramos, rebanadas).',
   P(['un','una','unos'],[['Necesitamos ___ kilo de tomates.','un','kilo는 남성 단수 → un.'],['Necesitamos ___ diente de ajo.','un','diente는 남성 → un.']])+
   P(['medio','media','medios'],[['Necesitamos ___ pimiento.','medio','pimiento는 남성 → medio.']])+
   P(['rebanadas','kilos','litros'],[['Tres ___ de pan.','rebanadas','rebanada = 빵 조각.']])+
   P(['medio','mitad','media'],[['Un litro y ___ de vino.','medio','litro와 함께 → medio.']])+
   P(['nevera','horno','despensa'],[['Después, dejamos la sangría en la ___.','nevera','nevera = 냉장고.']])+
   P(['hielos','azúcar','sal'],[['Al final añadimos unos ___ para rebajar el alcohol.','hielos','hielo = 얼음.']])+
   P(['triturar','regar','tender'],[['Con la batidora podemos ___ las verduras.','triturar','triturar = 갈다.']])),
  X('연습 3. 직접 쓰기','알맞은 단어를 쓰세요.','요리 표현.',
   T([['Lo primero que tenemos que hacer es ___ las verduras. (씻다, lavar)','lavar','tener que + 동사원형.'],['Vamos a ___ el tomate en trozos. (자르다)','cortar','ir a + 동사원형.'],['Para el gazpacho necesitamos una ___. (믹서)','batidora','batidora = 믹서.'],['Cortamos el melón en ___. (조각)','trozos','trozos = 조각들.'],['El jamón en ___ finas. (얇게 썬 조각)','lonchas','lonchas = 얇게 썬 조각.'],['El gazpacho se toma en ___. (여름)','verano','verano = 여름.'],['La sangría es una bebida muy ___. (시원하게 해 주는)','refrescante','refrescante = 시원한.'],['La tortilla es un plato de procedencia ___. (농민의)','campesina','plato campesino = 농민의 음식.']]))]
))

# ---------- 12 ----------
UNITS.append(U(12,'A1','La casa','집·방·가구·집안일',
 '집의 구조, 방과 가구, 주방·정원·욕실 어휘, 집안일과 위생용품 이름을 익힙니다.',
 VS(39,97,26,109,102,114,139,140),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. 집의 구조</h3>'''+tbl(['분류','어휘'],[
 ['방',chips(['el salón','el comedor','la sala de estar','la cocina','el dormitorio','el cuarto de baño / el baño','el pasillo','el recibidor','el despacho','la terraza','el jardín'])],
 ['구조',chips(['el suelo','el techo','las paredes','la puerta','la ventana','el garaje','el porche','el tejado','la chimenea'])],
 ['건물',chips(['el edificio','la planta','el piso','las escaleras','el ascensor','el balcón'])],
])+warn('스페인에서 <b>piso</b>는 큰 아파트를 뜻하고, 건물의 <b>층</b>은 planta(또는 piso)예요. <b>salón</b>에는 식사 공간 <b>comedor</b>와 휴식 공간 <b>sala de estar</b>가 있어요.')+'''
<h3>2. 가구와 물건</h3>'''+tbl(['공간','어휘'],[
 ['거실',chips(['la silla','el sillón','el sofá','la mesa','el armario','la estantería','la lámpara','el cuadro','la planta','el reloj','las cortinas','la televisión'])],
 ['침실',chips(['la cama','la mesilla de noche','la alfombra','el espejo'])],
 ['욕실',chips(['el retrete / la taza del váter','el lavabo','la bañera','la ducha'])],
 ['주방',chips(['la sartén','la olla','la vitrocerámica','el microondas','el horno','la tostadora','la nevera','el congelador','la despensa','los platos','los cubiertos','la cuchara','el tenedor','el cuchillo'])],
 ['정원',chips(['el macetero','la regadera','la valla','la tumbona','la barbacoa','la pérgola','el toldo','la sombrilla'])],
])+'''
<h3>3. 집안일과 위생용품</h3>'''+chips(['barrer','fregar','pasar la aspiradora','limpiar el polvo','poner la lavadora','tender la ropa','planchar','hacer la cama'])+chips(['el gel','el champú','la esponja','el peine','el cepillo de dientes']),
 [X('연습 1. 방과 구조','알맞은 단어를 고르세요.','방 이름과 건물 구조.',
   P(['cocina','dormitorio','terraza'],[['음식을 만들러 가는 곳: la ___.','cocina','cocina = 주방.']])+
   P(['dormitorio','pasillo','garaje'],[['자러 가는 곳: el ___.','dormitorio','dormitorio = 침실.']])+
   P(['baño','salón','jardín'],[['이를 닦는 곳: el cuarto de ___.','baño','cuarto de baño = 욕실.']])+
   P(['recibidor','despacho','comedor'],[['집에 들어가서 처음 닿는 곳: el ___.','recibidor','recibidor = 현관 홀.']])+
   P(['pasillo','tejado','techo'],[['방과 방 사이를 잇는 공간: el ___.','pasillo','pasillo = 복도.']])+
   P(['ascensor','chimenea','valla'],[['층과 층 사이를 오갈 때 계단 또는 ___.','ascensor','ascensor = 엘리베이터.']])+
   P(['piso','porche','garaje'],[['스페인에서 큰 아파트: un ___.','piso','piso = 큰 아파트.']])+
   P(['balcones','garajes','tejados'],[['건물 창문 옆에는 ___ 이 있을 수 있어요.','balcones','balcón = 발코니.']])),
  X('연습 2. 물건 이름','설명에 맞는 단어를 고르세요.','가구·주방·정원 어휘.',
   P(['sofá','armario','espejo'],[['여럿이 앉거나 낮잠을 자는 것: el ___.','sofá','sofá = 소파.']])+
   P(['noche','mañana','tarde'],[['침대 옆에 두는 mesilla de ___.','noche','mesilla de noche = 침대 협탁.']])+
   P(['ducha','bañera','lavabo'],[['샤워하는 곳: la ___.','ducha','ducha = 샤워기/샤워.']])+
   P(['nevera','horno','tostadora'],[['차가운 음식을 보관하는 곳: la ___.','nevera','nevera = 냉장고.']])+
   P(['congelador','microondas','despensa'],[['냉동식품을 보관하는 곳: el ___.','congelador','congelador = 냉동실.']])+
   P(['horno','tostadora','sartén'],[['피자를 만드는 데 쓰는 것: el ___.','horno','horno = 오븐.']])+
   P(['tostadora','regadera','toldo'],[['아침 토스트를 만드는 것: la ___.','tostadora','tostadora = 토스터.']])+
   P(['regadera','valla','pérgola'],[['식물에 물을 주는 것: la ___.','regadera','regadera = 물뿌리개.']])),
  X('연습 3. 집안일과 위생','알맞은 단어를 쓰세요.','집안일 동사와 위생용품.',
   T([['빗자루로 쓸다: ___ (barrer)','barrer','barrer = 쓸다.'],['Hay que ___ la cama. (hacer)','hacer','hacer la cama = 침대를 정돈하다.'],['Voy a poner la ___. (세탁기)','lavadora','poner la lavadora = 세탁기를 돌리다.'],['Tengo que pasar la ___. (청소기)','aspiradora','pasar la aspiradora = 청소기를 돌리다.'],['Me lavo los dientes con el ___ de dientes.','cepillo','cepillo de dientes = 칫솔.'],['El ___ sirve para lavar el pelo. (샴푸)','champú','champú = 샴푸.'],['Para comer usamos cuchara, tenedor y ___.','cuchillo','cuchillo = 칼.'],['Después de lavar, hay que ___ la ropa. (널다)','tender','tender la ropa = 빨래를 널다.']]))]
))

# ---------- 13 ----------
UNITS.append(U(13,'A1','La ciudad, las tiendas y el transporte','도시 시설·상점 이름·교통수단',
 '도시의 장소, -ería로 끝나는 가게 이름과 점원 이름, 교통수단과 전치사 en / a pie를 익힙니다.',
 VS(62,63,13),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. 도시의 장소</h3>'''+tbl(['분류','어휘'],[
 ['도시 구역',chips(['la calle','la plaza','el parque','la casa','el edificio','el barrio'])],
 ['서비스',chips(['el hospital','la farmacia','el banco','la iglesia'])],
 ['교육',chips(['el colegio','el instituto','la universidad','la biblioteca'])],
 ['관광·여가',chips(['el hotel','la oficina de turismo','el monumento','el museo','el teatro','el cine'])],
 ['교통 시설',chips(['el aparcamiento','la estación de trenes','la estación de autobuses','la parada de autobús','la parada de taxis','la parada de metro','el aeropuerto','el puerto'])],
])+'''
<h3>2. 가게 이름 (-ería)</h3>'''+tbl(['가게','판매','직원'],[
 [E('la zapatería'),'zapatos','el zapatero'],[E('la librería'),'libros','el librero / la librera'],[E('la carnicería'),'carne','el carnicero'],[E('la pescadería'),'pescado','el pescadero'],[E('la frutería'),'fruta y verdura','el frutero'],[E('la panadería'),'pan','el panadero'],[E('la pastelería'),'pasteles y tartas','el pastelero'],[E('la heladería'),'helados','el heladero'],[E('la papelería'),'objetos de clase y oficina','el papelero'],[E('la juguetería'),'juguetes','el juguetero'],[E('la joyería'),'joyas','el joyero'],[E('la perfumería'),'perfumes y cosmética','el perfumero'],[E('la droguería'),'limpieza e higiene','el droguero'],[E('la ferretería'),'herramientas','el ferretero'],[E('la peluquería'),'cortar el pelo','el peluquero'],[E('la lavandería'),'lavar la ropa','el lavandero']])+rules(['‘~ 가게’는 보통 <b>여성 명사</b>예요.','tienda de + 상품: la tienda de ropa, la tienda de deportes, la tienda de informática.','특별한 이름: <b>el quiosco</b>(신문·잡지), <b>el estanco</b>(담배), <b>la óptica</b>(안경), <b>la agencia de viajes</b>(여행사), <b>la tintorería</b>(드라이클리닝).','점원은 <b>el dependiente / la dependienta</b>.'])+'''
<h3>3. 교통수단</h3>'''+tbl(['어디로 가나','교통수단'],[['도로',chips(['el coche','el autobús','la bicicleta','el taxi','la moto','el camión'])],['레일',chips(['el tren','el metro','el tranvía'])],['하늘',chips(['el avión','el helicóptero','el globo'])],['물',chips(['el barco','la barca'])]])+rules(['교통수단 앞에는 <b>en</b>: '+E('Voy en coche')+' · '+E('Viajamos en tren')+' · '+E('Van en avión')+'.','예외 두 가지: <b>a pie</b>(걸어서) · <b>a caballo</b>(말을 타고).','기차·지하철·버스는 <b>estación</b>에서 출발·도착하고, 버스·트램·택시는 <b>parada</b>에 서요. 비행기는 <b>aeropuerto</b>, 배는 <b>puerto</b>.']),
 [X('연습 1. 장소와 가게','알맞은 단어를 고르세요.','가게 이름은 상품 + -ería.',
   P(['colegio','hospital','banco'],[['아이들이 가는 곳: el ___.','colegio','colegio = 초등학교.']])+
   P(['librería','biblioteca','papelería'],[['책을 사는 곳: la ___.','librería','librería = 서점.']])+
   P(['panadería','pastelería','heladería'],[['빵을 사는 곳: la ___.','panadería','panadería = 빵집.']])+
   P(['peluquería','farmacia','óptica'],[['머리를 자르는 곳: la ___.','peluquería','peluquería = 미용실.']])+
   P(['biblioteca','librería','universidad'],[['책을 무료로 빌려 읽는 곳: la ___.','biblioteca','biblioteca = 도서관.']])+
   P(['teatro','banco','hospital'],[['연극을 보는 곳: el ___.','teatro','teatro = 극장.']])+
   P(['óptica','joyería','ferretería'],[['안경을 사는 곳: la ___.','óptica','óptica = 안경점.']])+
   P(['quiosco','estanco','museo'],[['신문과 잡지를 파는 곳: el ___.','quiosco','quiosco = 가판대.']])),
  X('연습 2. 교통수단','알맞은 단어를 고르세요.','en + 교통수단 / a pie / estación · parada.',
   P(['en','a','por'],[['Voy ___ coche.','en','교통수단 앞에는 en.']])+
   P(['pie','coche','tren'],[['Voy a ___. (걸어서)','pie','a pie = 걸어서.']])+
   P(['estación','parada','puerto'],[['기차는 ___ 에서 출발해요.','estación','tren → estación de trenes.']])+
   P(['parada','estación','aeropuerto'],[['버스는 ___ 에 서요.','parada','autobús → parada de autobús.']])+
   P(['aeropuerto','puerto','garaje'],[['비행기는 ___ 에서 출발해요.','aeropuerto','avión → aeropuerto.']])+
   P(['puerto','aeropuerto','barrio'],[['배는 ___ 에서 출발해요.','puerto','barco → puerto.']])+
   P(['tranvía','coche','moto'],[['레일 위를 달리는 것: el tren, el metro y el ___.','tranvía','tranvía = 트램.']])+
   P(['avión','tren','barco'],[['하늘로 가는 것: el helicóptero, el globo y el ___.','avión','avión = 비행기.']])),
  X('연습 3. 직접 쓰기','알맞은 단어를 쓰세요.','가게·장소·교통 표현.',
   T([['Compro zapatos en la ___.','zapatería','zapatos → zapatería.'],['Compro carne en la ___.','carnicería','carne → carnicería.'],['Compro medicinas en la ___.','farmacia','farmacia = 약국.'],['El dinero está en el ___.','banco','banco = 은행.'],['빵을 파는 남자: el ___','panadero','panadero = 제빵사/빵집 주인.'],['여행을 계획하는 곳: la agencia de ___.','viajes','agencia de viajes = 여행사.'],['그림이 많은 곳: el ___.','museo','museo = 박물관.'],['Viajamos ___ tren.','en','교통수단 앞 전치사 en.']]))]
))

# ---------- 14 ----------
UNITS.append(U(14,'A1','El cuerpo humano y “me duele”','신체 부위와 아플 때 쓰는 표현',
 '얼굴·몸·관절·장기 이름과, doler 동사로 아픈 곳을 말하는 법을 익힙니다.',
 VS(20,27,104),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. 신체 부위</h3>'''+tbl(['부위','어휘'],[
 ['머리',chips(['la cabeza','el pelo','la cara','la frente','los ojos','la nariz','la boca','las orejas','el cuello','la garganta'])],
 ['입',chips(['los labios','los dientes','la lengua'])],
 ['몸통',chips(['el pecho','la cintura','la barriga','los hombros','la espalda'])],
 ['팔·손',chips(['los brazos','las manos','los dedos','las muñecas','los codos'])],
 ['다리·발',chips(['las piernas','los pies','las rodillas','los tobillos'])],
 ['몸 안',chips(['los músculos','los huesos','el esqueleto','el cerebro','el corazón','los pulmones','el estómago'])],
])+'''
<h3>2. 아픈 곳 말하기: doler</h3>
<p><b>doler</b>는 gustar와 같은 구조예요. <b>간접목적어 대명사(me, te, le, nos, os, les) + duele / duelen + 정관사 + 신체 부위</b>.</p>'''+tbl(['아픈 곳','표현'],[['단수',E('Me duele la cabeza')],['복수',E('Me duelen los brazos')],['다른 사람',E('Le duele el estómago')+' · '+E('Nos duelen las piernas')]])+warn('✘ <b>Me duele mi cabeza</b> → ✔ <b>Me duele la cabeza</b>. 스페인어는 누구의 몸인지 이미 대명사(me, te…)로 나타내기 때문에 신체 부위 앞에 소유사(mi, tu…)를 쓰지 않고 <b>관사(el, la, los, las)</b>를 씁니다.'),
 [X('연습 1. 몸 이름','알맞은 단어를 고르세요.','신체 부위 어휘.',
   P(['cerebro','corazón','estómago'],[['우리는 ___ 로 생각해요.','cerebro','cerebro = 뇌.']])+
   P(['ojos','orejas','manos'],[['우리는 ___ 로 봐요.','ojos','ojos = 눈.']])+
   P(['orejas','ojos','labios'],[['우리는 ___ 로 들어요.','orejas','orejas = 귀.']])+
   P(['corazón','cerebro','esqueleto'],[['심장은 스페인어로 el ___.','corazón','corazón = 심장.']])+
   P(['brazos','piernas','pies'],[['팔꿈치와 손목은 ___ 에 있어요.','brazos','codos와 muñecas는 팔(brazos)의 관절.']])+
   P(['piernas','brazos','manos'],[['무릎과 발목은 ___ 에 있어요.','piernas','rodillas와 tobillos는 다리(piernas)의 관절.']])+
   P(['esqueleto','músculo','órgano'],[['모든 뼈를 합쳐서 el ___.','esqueleto','esqueleto = 뼈대.']])+
   P(['boca','nariz','frente'],[['치아는 ___ 안에 있어요.','boca','dientes는 boca 안.']])),
  X('연습 2. doler 활용','알맞은 형태를 고르세요.','단수 명사 → duele / 복수 명사 → duelen / 소유사 대신 관사.',
   P(['duele','duelen'],[['Me ___ la cabeza.','duele','cabeza는 단수 → duele.'],['Me ___ los brazos.','duelen','brazos는 복수 → duelen.'],['Le ___ el estómago.','duele','estómago는 단수 → duele.'],['Nos ___ las piernas.','duelen','piernas는 복수 → duelen.'],['¿Te ___ la espalda?','duele','espalda는 단수 → duele.'],['Les ___ la garganta.','duele','garganta는 단수 → duele.']])+
   P(['la','mi','tu'],[['Me duele ___ cabeza.','la','신체 부위 앞에는 소유사가 아니라 관사.']])+
   P(['los','mis','sus'],[['Me duelen ___ pies.','los','신체 부위 앞에는 관사 los.']])),
  X('연습 3. 직접 쓰기','알맞은 단어를 쓰세요.','신체 부위와 doler.',
   T([['Me duele la ___. (머리)','cabeza','cabeza = 머리.'],['Me ___ los pies. (doler)','duelen','pies는 복수 → duelen.'],['손 하나에 ___ 가 다섯 개 있어요. (손가락)','dedos','dedos = 손가락.'],['치아는 ___ 이에요. (los ___)','dientes','dientes = 치아.'],['말하고 맛을 느끼는 곳: la ___','lengua','lengua = 혀.'],['손과 팔 사이: la ___','muñeca','muñeca = 손목.'],['발과 다리 사이: el ___','tobillo','tobillo = 발목.'],['Me duele ___ espalda. (관사)','la','espalda는 여성 단수 → la.']]))]
))

# ---------- 15 ----------
UNITS.append(U(15,'A1','Profesiones y oficios','직업 이름',
 '자주 쓰는 직업 이름과 남성·여성형, ser + 직업(관사 없음) 규칙을 익힙니다.',
 VS(33,34,87,90),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. 직업 어휘</h3>'''+tbl(['분야','남성 / 여성'],[
 ['식당·상점',E('el camarero / la camarera')+' · '+E('el cocinero / la cocinera')+' · '+E('el dependiente / la dependienta')],
 ['식료품 가게',E('el carnicero')+' · '+E('el pescadero')+' · '+E('el frutero')+' · '+E('el panadero')],
 ['운송',E('el conductor / la conductora')+' · '+E('el taxista / la taxista')+' · '+E('el piloto / la piloto')],
 ['육체노동',E('el obrero / la obrera')+' · '+E('el mecánico / la mecánica')+' · '+E('el limpiador / la limpiadora')],
 ['서비스',E('el cartero / la cartera')+' · '+E('el peluquero / la peluquera')],
 ['교육',E('el profesor / la profesora')+' · '+E('el estudiante / la estudiante')],
 ['의료',E('el médico / la médica')+' · '+E('el enfermero / la enfermera')+' · '+E('el cirujano / la cirujana')],
 ['설계',E('el arquitecto / la arquitecta')+' · '+E('el ingeniero / la ingeniera')],
 ['안전·법',E('el policía / la policía')+' · '+E('el bombero / la bombera')+' · '+E('el juez / la jueza')+' · '+E('el abogado / la abogada')],
 ['과학·언론',E('el científico / la científica')+' · '+E('el periodista / la periodista')],
 ['예술·스포츠',E('el músico / la música')+' · '+E('el escritor / la escritora')+' · '+E('el actor / la actriz')+' · '+E('el futbolista')+' · '+E('el árbitro')+' · '+E('la tenista')+' · '+E('el fotógrafo')+' · '+E('la modelo')],
])+rules(['직업은 <b>ser + 직업</b>으로 말하고 <b>관사를 쓰지 않아요</b>: '+E('Mi padre es arquitecto')+' · '+E('Yo soy profesora de español')+'.','<b>-o → -a</b> (médico/médica), <b>-or → -ora</b> (escritor/escritora), <b>-ista</b>는 남녀 같음 (periodista), <b>-ero → -era</b> (cartero/cartera).','불규칙: <b>actor → actriz</b>, <b>juez → jueza</b>.','직업을 물을 때: '+E('¿Cuál es tu profesión?')+'.']),
 [X('연습 1. 직업 맞히기','설명에 맞는 직업을 고르세요.','직업 이름.',
   P(['camarero','cocinero','dependiente'],[['식당에서 손님에게 음식을 가져다주는 사람: el ___.','camarero','camarero = 웨이터.']])+
   P(['panadero','carnicero','frutero'],[['빵을 파는 사람: el ___.','panadero','panadero = 빵집 주인.']])+
   P(['pescadera','carnicera','panadera'],[['생선을 파는 여성: la ___.','pescadera','pescadero/a = 생선 가게 주인.']])+
   P(['taxista','piloto','cartero'],[['택시를 운전하는 사람: el ___.','taxista','taxista = 택시 기사.']])+
   P(['piloto','mecánico','policía'],[['비행기를 조종하는 사람: el ___.','piloto','piloto = 조종사.']])+
   P(['cartero','peluquero','obrero'],[['편지를 배달하는 사람: el ___.','cartero','cartero = 우체부.']])+
   P(['peluquera','cocinera','enfermera'],[['머리를 잘라 주는 여성: la ___.','peluquera','peluquero/a = 미용사.']])+
   P(['bombero','policía','abogado'],[['불을 끄는 사람: el ___.','bombero','bombero = 소방관.']])),
  X('연습 2. 문법 고르기','알맞은 형태를 고르세요.','ser + 직업(관사 없음), 여성형.',
   P(['arquitecto','arquitecta','arquitectos'],[['Mi padre es ___.','arquitecto','남성 단수 → arquitecto.']])+
   P(['jueza','juez','juezas'],[['Ella es ___. (판사)','jueza','juez의 여성형 → jueza.']])+
   P(['actriz','actora','actor'],[['Ella es ___. (배우)','actriz','actor의 여성형 → actriz.']])+
   P(['periodista','periodisto','periodistas'],[['María es ___. (기자)','periodista','-ista는 남녀 같음.']])+
   P(['es','está','tiene'],[['Mi madre ___ médica.','es','직업은 ser.']])+
   P(['(없음)','un','el'],[['Mi padre es ___ arquitecto. (관사 선택)','(없음)','직업 앞에는 관사를 쓰지 않아요.']])+
   P(['como','de','en'],[['Trabajo ___ camarera en un bar.','como','trabajar como + 직업.']])+
   P(['es','soy','eres'],[['Antonio ___ médico.','es','Antonio는 3인칭 → es.']])),
  X('연습 3. 직접 쓰기','알맞은 단어를 쓰세요.','직업 이름.',
   T([['Ella es ___. (소방관)','bombera','bombero의 여성형 → bombera.'],['Él es ___. (경찰관)','policía','남녀 같은 형태 el/la policía.'],['La ___ enseña a los estudiantes. (여자 선생님)','profesora','profesor → profesora.'],['El ___ diseña edificios. (건축가)','arquitecto','arquitecto = 건축가.'],['El ___ diseña carreteras y máquinas. (엔지니어)','ingeniero','ingeniero = 엔지니어.'],['El ___ escribe libros. (작가)','escritor','escritor = 작가.'],['El ___ juega al fútbol. (축구 선수)','futbolista','futbolista는 남녀 같음.'],['¿Cuál es tu ___? (직업)','profesión','profesión = 직업.']]))]
))

# ---------- 16 ----------
UNITS.append(U(16,'A1','El tiempo y el clima','날씨 표현과 스페인의 기후',
 '날씨 동사(hace, llueve, nieva…)와 겨울 어휘, 스페인의 4가지 기후를 익힙니다.',
 VS(38,145,19),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. 날씨 표현</h3>'''+tbl(['표현','뜻'],[
 [E('Hace sol')+' · '+E('Hace calor')+' · '+E('Hace frío')+' · '+E('Hace viento'),'hacer + 명사'],
 [E('Hace buen tiempo')+' · '+E('Hace mal tiempo'),'날씨가 좋다/나쁘다'],
 [E('El cielo está despejado'),'구름 없이 맑다'],
 [E('El cielo está nublado'),'구름이 꼈다 (nube = 구름)'],
 [E('Llueve')+' · '+E('Nieva')+' · '+E('Graniza')+' · '+E('Hiela'),'비가 온다 · 눈이 온다 · 우박이 내린다 · 얼음이 언다'],
 [E('Hay niebla')+' · '+E('Hay tormenta'),'안개가 꼈다 · 폭풍(번개 relámpagos, 천둥 truenos)'],
 ['el arco iris','무지개'],
])+warn('✘ Es mucho calor → ✔ <b>Hace mucho calor</b>. 날씨는 ser가 아니라 <b>hacer</b>를 써요. 기온은 <b>grados</b>(Celsius/centígrados)로 말해요: Estamos a 35 grados.')+'''
<h3>2. 겨울 어휘</h3>'''+chips(['la nieve','el muñeco de nieve','los copos de nieve','el hielo','la chimenea','el gorro','la bufanda','el guante','las botas'])+'''
<h3>3. 스페인의 기후 4가지</h3>'''+tbl(['기후','지역','특징'],[
 ['<b>mediterráneo</b>','동쪽·남쪽 (안달루시아 대부분)','겨울은 짧고 온화, 여름은 길고 더움. 비는 적고 눈은 오지 않음'],
 ['<b>continental</b>','중부 내륙','겨울은 길고 춥고, 여름은 매우 덥다(35~40도). 건조. 7·8월 폭풍우가 잦음'],
 ['<b>oceánico</b>','북쪽 (칸타브리아 해안·갈리시아)','1년 내내 온화하고 비가 많이 옴'],
 ['<b>subtropical</b>','카나리아 제도','연중 22~28도, 비가 적은 스페인에서 가장 좋은 기후'],
]),
 [X('연습 1. 날씨 표현','알맞은 표현을 고르세요.','hacer + sol/calor/frío/viento, llover, nevar.',
   P(['hace','es','está'],[['En verano ___ calor.','hace','날씨는 hacer.']])+
   P(['Llueve','Nieva','Hiela'],[['비가 와요: ___.','Llueve','llover = 비가 오다.'],['눈이 와요: ___.','Nieva','nevar = 눈이 오다.']])+
   P(['nublado','despejado','caliente'],[['하늘에 구름이 가득해요: El cielo está ___.','nublado','nublado = 흐린.']])+
   P(['despejado','nublado','lluvioso'],[['구름이 없어요: El cielo está ___.','despejado','despejado = 맑은.']])+
   P(['viento','nieve','lluvia'],[['바람이 불어요: Hace ___.','viento','hace viento.']])+
   P(['tormenta','arco iris','niebla'],[['번개와 천둥이 쳐요: Hay una ___.','tormenta','tormenta = 폭풍우.']])+
   P(['hiela','graniza','llueve'],[['기온이 0도로 내려가 모든 것이 얼어요: ___.','hiela','helar = 얼음이 얼다.']])),
  X('연습 2. 스페인의 기후','알맞은 단어를 고르세요.','4가지 기후와 지역.',
   P(['mediterráneo','continental','oceánico'],[['동쪽과 남쪽의 기후: ___.','mediterráneo','동·남 = 지중해성.']])+
   P(['continental','subtropical','oceánico'],[['스페인 중부 내륙의 기후: ___.','continental','내륙 = 대륙성.']])+
   P(['oceánico','mediterráneo','continental'],[['북쪽 지방의 기후: ___.','oceánico','북쪽 = 해양성.']])+
   P(['subtropical','continental','oceánico'],[['카나리아 제도의 기후: ___.','subtropical','카나리아 = 아열대.']])+
   P(['fríos','suaves','cortos'],[['중부 지방의 겨울은 길고 ___.','fríos','중부의 겨울은 길고 춥다.']])+
   P(['mucho','poco','nunca'],[['북쪽 지방에서는 1년 내내 ___ 비가 와요.','mucho','북쪽은 비가 많이 와요.']])+
   P(['Canarias','Galicia','Aragón'],[['스페인에서 가장 좋은 기후를 가진 곳: ___.','Canarias','카나리아 제도.']])+
   P(['poco','mucho','siempre'],[['카나리아 제도에는 비가 아주 ___ 와요.','poco','llueve muy poco.']])),
  X('연습 3. 직접 쓰기','알맞은 단어를 쓰세요.','날씨와 겨울 어휘.',
   T([['Hoy ___ mal tiempo. (hacer)','hace','hace mal tiempo.'],['Mañana ___. (눈이 와요, nevar)','nieva','nevar → nieva.'],['Hay ___ y no veo la carretera. (안개)','niebla','niebla = 안개.'],['비가 온 뒤 해가 나면 ___ 가 생겨요. (arco …)','arco iris','arco iris = 무지개.'],['Mi estación favorita es el ___. (여름)','verano','verano = 여름.'],['En invierno llevo un ___ en la cabeza. (털모자)','gorro','gorro = 털모자.'],['Con la nieve hacemos un ___ de nieve.','muñeco','muñeco de nieve = 눈사람.'],['Cuando graniza cae ___. (우박)','granizo','granizo = 우박.']]))]
))

# ---------- 17 ----------
UNITS.append(U(17,'A1','Tiempo libre, vacaciones, playa y piscina','여가·휴가·해변·수영장',
 '집 안팎의 여가 활동, 휴가 목적지, 해변과 수영장 어휘를 익힙니다.',
 VS(78,79,118,119,120),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. 집에서 하는 여가</h3>'''+chips(['leer un libro, una revista o el periódico','ver la televisión','escuchar música o la radio','navegar por internet','ver vídeos de YouTube','jugar a las cartas','jugar al ajedrez','hacer un puzle','jugar a videojuegos','cocinar','cuidar de las plantas','practicar yoga','pintar un cuadro','tocar un instrumento musical'])+'''
<h3>2. 밖에서 하는 여가</h3>'''+chips(['dar un paseo','ir de compras','ir al cine','ir al teatro','quedar con amigos','tomar algo','ir a un concierto','ir a una discoteca','correr','montar en bicicleta','jugar al fútbol','nadar','ir a un gimnasio','visitar un museo','ir al zoo','hacer una excursión','hacer senderismo','ir de acampada','ir a la playa','viajar a otro país'])+'''
<h3>3. 휴가 목적지</h3>'''+chips(['la ciudad','la playa','la montaña','el camping','el hotel con piscina','la casa rural','el spa','el retiro','el crucero'])+'''
<h3>4. 해변과 수영장</h3>'''+tbl(['장소','어휘'],[
 ['<b>la playa</b>','el mar · las olas · la arena · la sombrilla · el / la socorrista · los cubos · las palas · el chiringuito'],
 ['<b>la piscina</b>','los vestuarios · la ducha · la piscina infantil · el socorrista · la escalera · el salvavidas · el bikini · el bañador · la toalla · la crema solar'],
])+chips(['Me encanta ir a la playa a pasear y a tomar el sol','Me gusta bañarme en la piscina por las tardes','¿Qué te gusta hacer en tu tiempo libre?']),
 [X('연습 1. 여가 활동','알맞은 단어를 고르세요.','여가 활동 표현.',
   P(['leer','ver','nadar'],[['집에서 책을 ___ 할 수 있어요.','leer','leer un libro.']])+
   P(['ver','escuchar','tocar'],[['집에서 TV를 ___ 할 수 있어요.','ver','ver la televisión.']])+
   P(['quedar','dormir','correr'],[['친구들과 약속을 잡아 만나다: ___ con amigos.','quedar','quedar con amigos.']])+
   P(['película','concierto','piscina'],[['영화관에 가서 ___ 을 봐요.','película','película = 영화.']])+
   P(['concierto','museo','gimnasio'],[['라이브 음악을 들으러 가는 곳: ir a un ___.','concierto','concierto = 콘서트.']])+
   P(['discoteca','biblioteca','librería'],[['춤추러 가는 곳: una ___.','discoteca','discoteca = 클럽.']])+
   P(['piscina','montaña','discoteca'],[['수영하러 가는 곳: la ___.','piscina','piscina = 수영장.']])+
   P(['montaña','playa','ciudad'],[['등산·하이킹(senderismo)을 하러 가는 곳: la ___.','montaña','senderismo는 산에서.']])),
  X('연습 2. 해변과 수영장','알맞은 단어를 고르세요.','해변과 수영장 어휘.',
   P(['arena','toalla','escalera'],[['해변에는 바다, 파도와 ___ 이 있어요.','arena','arena = 모래.']])+
   P(['sombrilla','toalla','pala'],[['해변에서 햇빛을 막아 주는 것: la ___.','sombrilla','sombrilla = 파라솔.']])+
   P(['socorrista','dependiente','camarero'],[['해변과 수영장에서 안전을 지키는 사람: el / la ___.','socorrista','socorrista = 인명구조원.']])+
   P(['palas','toallas','botas'],[['모래놀이: cubos y ___.','palas','palas = 삽.']])+
   P(['toalla','crema','ducha'],[['물기를 닦는 것: la ___.','toalla','toalla = 수건.']])+
   P(['solar','mar','playa'],[['햇빛을 막는 크림: la crema ___.','solar','crema solar = 선크림.']])+
   P(['vestuarios','chiringuitos','olas'],[['수영장에서 옷을 갈아입는 곳: los ___.','vestuarios','vestuarios = 탈의실.']])+
   P(['chiringuito','vestuario','socorrista'],[['해변의 간이 식당·바: el ___.','chiringuito','chiringuito = 해변 간이 바.']])),
  X('연습 3. 직접 쓰기','알맞은 단어를 쓰세요.','여가 동사와 어휘.',
   T([['Me gusta ___ en bicicleta. (타다, montar)','montar','montar en bicicleta.'],['Me gusta ___ al fútbol. (하다, jugar)','jugar','jugar al fútbol.'],['Voy al gimnasio a hacer ___. (운동)','ejercicio','hacer ejercicio = 운동하다.'],['Voy a pasear por un ___.','parque','parque = 공원.'],['Juegos de mesa: las cartas y el ___. (체스)','ajedrez','ajedrez = 체스.'],['Dormimos en una tienda en el ___. (캠핑장)','camping','camping = 캠핑장.'],['Viajamos en un ___. (크루즈)','crucero','crucero = 크루즈.'],['Voy de vacaciones a la ___ a tomar el sol.','playa','playa = 해변.']]))]
))

# ---------- 18 ----------
UNITS.append(U(18,'A1','La clase y el material escolar','교실·학용품·수업에서 쓰는 표현',
 '학용품과 교실 물건 이름, 스페인어 수업 첫 주에 꼭 필요한 6가지 문장을 익힙니다.',
 VS(55,124,129,146,126,127),
 TIP+'''<h2>핵심 정리</h2>
<h3>1. 학용품 (el material escolar)</h3>'''+chips(['la mochila','los libros','el cuaderno','el diccionario','el bolígrafo','el lápiz','la goma de borrar','el sacapuntas','el rotulador','el subrayador','el estuche','las pinturas','la regla','las tijeras'])+'''
<h3>2. 교실 (el aula / la clase)</h3>'''+tbl(['사람','el profesor · el alumno · los compañeros de clase'],[['물건','la silla · la mesa · la pizarra · la tiza · el borrador · el ordenador · la impresora · la papelera · la estantería · el armario · el reloj · el mapa · el perchero']])+'''
<h3>3. 수업 첫 주 필수 표현 6가지</h3>'''+tbl(['상황','문장'],[
 ['모를 때',E('No entiendo')],['다시 말해 달라고',E('¿Puedes repetir, por favor?')],['뜻을 물을 때',E('¿Qué significa escuela?')],['철자를 물을 때',E('¿Cómo se escribe escuela?')],['발음을 물을 때',E('¿Cómo se pronuncia colegio?')],['스페인어로 뭐라고 하는지',E('¿Cómo se dice “school” en español?')]])+warn('스페인에서는 “아이들의 개학 준비”를 <b>preparar la vuelta al cole</b>라고 해요. ‘cole’은 colegio의 줄임말이에요.'),
 [X('연습 1. 학용품','설명에 맞는 단어를 고르세요.','학용품 어휘.',
   P(['bolígrafo','regla','tijeras'],[['잉크로 쓰는 필기구: el ___.','bolígrafo','bolígrafo = 볼펜.']])+
   P(['goma','tiza','mapa'],[['지우는 것: la ___ de borrar.','goma','goma de borrar = 지우개.']])+
   P(['sacapuntas','estuche','rotulador'],[['연필을 깎는 것: el ___.','sacapuntas','sacapuntas = 연필깎이.']])+
   P(['estuche','mochila','papelera'],[['볼펜과 연필을 넣는 통: el ___.','estuche','estuche = 필통.']])+
   P(['regla','pizarra','tiza'],[['길이를 재고 선을 긋는 것: la ___.','regla','regla = 자.']])+
   P(['tijeras','regla','pinturas'],[['종이를 자르는 것: las ___.','tijeras','tijeras = 가위.']])+
   P(['mochila','estuche','reloj'],[['모든 것을 학교에 가져가는 가방: la ___.','mochila','mochila = 배낭.']])+
   P(['pizarra','papelera','estantería'],[['선생님이 설명을 쓰는 곳: la ___.','pizarra','pizarra = 칠판.']])),
  X('연습 2. 수업 표현','상황에 알맞은 표현을 고르세요.','No entiendo / ¿Puedes repetir? / ¿Qué significa? / ¿Cómo se escribe? / ¿Cómo se pronuncia? / ¿Cómo se dice?',
   P(['No entiendo','Hasta luego','Me gusta'],[['무슨 말인지 모를 때: “___.”','No entiendo','No entiendo = 이해하지 못했어요.']])+
   P(['repetir','escribir','pronunciar'],[['다시 말해 달라고 할 때: ¿Puedes ___, por favor?','repetir','repetir = 반복하다.']])+
   P(['significa','escribe','pronuncia'],[['단어의 뜻을 물을 때: ¿Qué ___ escuela?','significa','significar = 의미하다.']])+
   P(['escribe','significa','dice'],[['철자를 물을 때: ¿Cómo se ___ escuela?','escribe','escribirse = 쓰이다.']])+
   P(['pronuncia','escribe','significa'],[['발음을 물을 때: ¿Cómo se ___ colegio?','pronuncia','pronunciarse = 발음되다.']])+
   P(['dice','escribe','pronuncia'],[['“school”을 스페인어로 뭐라고 하는지: ¿Cómo se ___ “school” en español?','dice','decirse = 말해지다.']])+
   P(['cole','escuela','clase'],[['스페인에서는 preparar la vuelta al ___ 라고 말해요.','cole','cole = colegio의 줄임말.']])+
   P(['compañeros','profesores','directores'],[['같은 반 친구들: los ___ de clase.','compañeros','compañero = 반 친구.']])),
  X('연습 3. 직접 쓰기','알맞은 단어를 쓰세요.','교실 어휘.',
   T([['선생님은 ___ 이나 마커로 써요. (분필)','tiza','tiza = 분필.'],['컴퓨터와 ___ 이 선생님 책상 위에 있어요. (프린터)','impresora','impresora = 프린터.'],['쓰레기는 ___ 에 버려요. (쓰레기통)','papelera','papelera = 휴지통.'],['외투를 걸 때는 ___ 를 써요. (옷걸이)','perchero','perchero = 옷걸이.'],['lápiz, bolígrafo, goma, sacapuntas, ___ (형광펜)','subrayador','subrayador = 형광펜.'],['책이 가득한 ___ 이 있어요. (책장, 복수)','estanterías','estantería의 복수 → estanterías.'],['벽에는 ___ 와 지도가 있어요. (시계)','reloj','reloj = 시계.'],['책, 공책, ___ (사전)','diccionario','diccionario = 사전.']]))]
))
