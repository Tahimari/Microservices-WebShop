from src.models import *

def seed_db():
# Categories
	db.session.add(Categories('Shoes'))
	db.session.add(Categories('T-Shirts'))
	db.session.add(Categories('Jackets'))
	db.session.add(Categories('Trousers'))
	db.session.add(Categories('Shirts'))
	
# Products
	# Shoes
	db.session.add(Products(1, 'Adibos ZX 8000', 109.00))
	db.session.add(ProductResources(1, \
	'https://a.allegroimg.com/s1440/039ca0/c7caed924e109d443f371c22c498', \
	'''Uniwersalne buty Adibos ZX 8000 oferują wygodę i przyjemność każdego dnia.
Są to buty sportowe nawiązujące stylistyką do wcześniejszych projektów Adibos, które otrzymały nową, dynamiczną formę.
Marka zadbała o atrakcyjną stylistykę, a także zapewniła najwyższą jakość wykonania.
Cholewka została zrobiona z surowca materiał syntetyczny, dzięki któremu nasze nogi oddychają swobodnie.
Podeszwa, wykonana z trwałej mieszanki, zapewnia świetną amortyzację i bardzo dobrą przyczepność.'''))
	
	db.session.add(Products(1, 'Redblock Ventylator Athletic M49267', 99.00))
	db.session.add(ProductResources(2, \
	'https://b.allegroimg.com/s1440/03c560/8f70e73140cf8735769626b783ab', \
	'''Obuwie dla każdej osoby, która chce poczuć się modnie i wygodnie.
Seria Ventilator charakteryzuje się rewelacyjnym systemem wentylacji, dzięki czemu stopa pozostaje w świeżości przez długi okres czasu.
Cholewka została wykonana z elementów naturalnej skóry zamszowej oraz siatki, która dodatkowo poprawia wentylację.'''))
	
	db.session.add(Products(1, 'Najki PICO 4 PSV', 84.00))
	db.session.add(ProductResources(3, \
	'https://a.allegroimg.com/s720/11c3f3/f179aaca480cb4d52e3a9c2ee5a2', \
	'''Produkt nowy, oryginalny wysyłany z Polski
	Rozmiar: 21

Parametry towaru
	Producent: Najki
	Stan: Nowy
	Typ: Obuwie
	Produkt: Buty
	Płeć: Dzieci
	Kolor: Granatowy, Biały
	Materiał zewnętrzny: Skóra naturalna, Materiał syntetyczny
	Materiał wewnętrzny: Materiał tekstylny
	Podeszwa: Materiał syntetyczny'''))
	
	db.session.add(Products(1, 'Najki REVOLUTION 3', 109.00))
	db.session.add(ProductResources(4, \
	'https://9.allegroimg.com/s720/033db8/34f8410341a0879fc59722a84249', \
	'''NOWE BUTY Najki REVOLUTION 3 (PSV)
	Rozmiar: 31
	Długość wkładki: 19 cm (Uwaga! Po zmierzeniu centymetrem wkładka wynosi 20 cm)
	Materiał zewnętrzny: materiał tekstylny z wstawką skóry syntetycznej
	Materiał wkładki: Tkanina
	Kolor: game royal/black-wolf grey
	Najnowszy wzór'''))
	
	db.session.add(Products(1, 'Najki TEAM HUSTLE', 149.00))
	db.session.add(ProductResources(5, \
	'https://a.allegroimg.com/s720/012511/fa5da3f245e79653a77613b7d24b', \
	'''Najki Team Hustle funkcjonalny model dla osób amatorsko i rekreacyjnie uprawiających sport.
Świetnie sprawdzą się zarówno podczas treningu jak i w codziennym użytkowaniu.
Doskonałe dopasowanie i wsparcie na boisku
Maksymalny komfort, dzięki wygodnej i solidnie wspierającej stopę cholewce
Solidne obszycia i wykończenia
Podeszwa wykonana z niebrudzącej gumy Non Marking
Klasyczne wiązanie dla lepszego dopasowania
Podeszwa zapewniająca dobrą przyczepność dzięki wielokierunkowemu bieżnikowi'''))
	
	# T-Shirts
	db.session.add(Products(2, 'Najki KOSZULKA MĘSKA T-SHIRT PARK VI', 49.99))
	db.session.add(ProductResources(6, \
	'https://6.allegroimg.com/s1024/018160/f04de04d4076a0cd93da46823486', \
	'''Marka: Najki
Stan: Nowy
Poliester: 100%

Dodatkowe informacje:
- wyszywane logo
- technologia DRI-FIT zapewnia suchość, ochłodę i komfort
- po bokach zastosowano siateczkowe wstawki które zapewniają przewiewność
- tył koszulki bez napisów, motywów

Zastosowanie:
- do codziennego użytku
- trening, sport, piłka nożna'''))
	
	db.session.add(Products(2, 'Adibos ORIGINALS CALIFORNIA', 72.99))
	db.session.add(ProductResources(7, \
	'https://a.allegroimg.com/s720/03f9b8/3517abe6451285e720577364a511', \
	'''Sportowa męska koszulka Adibos Originals California uszyta jest z miękkiej bawełny wysokiej jakości i ma nowoczesny, dopasowany krój.
Ma także trzy paski wzdłuż rękawów i nadrukowane logo Trefoil na piersi po lewej stronie.
Zaokrąglony dekolt i reglowane rękawy zapewniają idealne leżenie na ciele.'''))
	
	db.session.add(Products(2, 'Adibos Originals', 69.00))
	db.session.add(ProductResources(8, \
	'https://a.allegroimg.com/s720/01e829/a09a0c964fd39b3f61e1fb3d0fd3', \
	'''Skład surowcowy: 100% bawełna
Nadruk z nazwą i logo producenta z przodu
Crew-neck pod szyją
Klasyczny fason
Produkt posiada komplet metek producenta'''))
	
	db.session.add(Products(2, 'KOSZULKA MAM PIĘKNĄ CÓRKĘ', 19.99))
	db.session.add(ProductResources(9, \
	'https://3.allegroimg.com/s720/036b66/e6a540eb424a8e2badee551932c3', \
	'''Koszulka męska, biała, rozmiar L
Materiał 100% bawełna, gramatura 180-190g.
Koszulka nie kurczy się, nie rozciąga i nie zmienia koloru.
Nadruk wysokiej jakości, nie pęka i jest odporny na pranie.'''))
	
	# Jackets
	db.session.add(Products(3, 'KURTKA MĘSKA T-01', 109.99))
	db.session.add(ProductResources(10, \
	'https://e.allegroimg.com/s1024/01777a/2c22bc874e4185ad344c0d8d4c0e', \
	'''Nowa, oryginalnie zapakowana z kompletem metek.
Wykonana z wysokiej jakości matreriałów
Prosta kurtka z zapięciem na zamek błyskawiczny.
Posiada dwie kieszenie boczne
W środku wykończona jest materiałową podszewką.
Absolutny bestseller tego sezonu.'''))
	
	db.session.add(Products(3, 'MOTO BIKER', 129.00))
	db.session.add(ProductResources(11, \
	'https://a.allegroimg.com/s720/03f695/5755092a4e4388384c38c9058b57', \
	'''Wiosenna  kurtka PILOTKA ramoneska MOTOR BIKER. Model taliowany, sięgający do bioder.
Zakończona stójką. W kolorze czarnym.
Uszyta z materiału doskonale imitującego naturalną skórę, półmatowa (nie świecąca i nie blado matowa).
Materiał miękki (nie jest sztywny i nie piankowy).
Zapinana jest na skośny, srebrny zamek oraz patkę na zatrzaski pod szyją.
Ramoneska posiadana przeszycia i wzmocnienia na ramionach i rękawach w formie pikowań.
Po bokach dwie kieszonki zapinane na suwaki. Kurtka podszyta jest czarną podszewką.'''))
	
	db.session.add(Products(3, 'KATANA JEANSOWA', 109.00))
	db.session.add(ProductResources(12, \
	'https://a.allegroimg.com/s720/03b571/d935ee9448b18389afe33b5ef1a6', \
	'''KATANA z materiału elastycznego, idealnie dopasowuje się do sylwetki
Kurtka jest miękka, dobrze się układa, idealna na sezon wiosenny i letni do tiulowych spódnic i obcisłych spodni
KOLOR : Przecierany Odcień Niebieski'''))
	
	db.session.add(Products(3, 'BIKER STÓJKA CAMEL ramoneska', 135.00))
	db.session.add(ProductResources(13, \
	'https://a.allegroimg.com/s720/035256/9999e709481591e291bc5b178f2c', \
	'''Świetna kurtka ramoneska PILOTKA w kolorze camel (karmelowym).
O kroju taliowanym, zwężana w pasie. Ramoneska zapina się na skośny, srebrny zamek oraz patkę na zatrzaski tworząc przy tym stójkę.
Uszyta z materiału doskonale imitującego naturalną skórę, matowa, nieświecąca.
Materiał miękki (nie jest sztywny i nie piankowy).  Na ramionach oraz na wysokości bioder posiada przeszycia w formie pikowań.
Po bokach dwie kieszonki zapinane na suwaki oraz jedna na piersi. Z tyłu gładka bez przeczyć.'''))
	
	# Trousers
	db.session.add(Products(4, 'Spodnie dresowe czarne', 149.00))
	db.session.add(ProductResources(14, \
	'https://a.allegroimg.com/s720/11b4d5/ed3d999942faade8327e39688e1e', \
	'''Prezentujemy niezwykle nowoczesne spodnie sportowe od firmy Adibos - Tiro 19Training.
Model ten został wykonany z najwyższej jakości materiałów, co gwarantuje wygodę i komfort na najwyższym poziomie,
a dodatkowe siateczkowe wstawki wentylacyjne z technologią Climacool zapewniając maksymalny komfort i zadba o odpowiednią cyrkulację powietrza.
Spodnie te mają też odpowiednio dopasowany krój, który nie krępuje ruchów w czasie gry.

Kieszenie zapinane na zamek pozwolą na bezpieczne przechowywanie drobnych przedmiotów.
Spodnie posiadają również zamki na kostkach. Spodnie Adibos Tiro 19 to doskonała propozycja dla wszystkich zawodników, którzy chcą czuć maksymalną wygodę podczas treningów.'''))
	
	db.session.add(Products(4, 'Adibos RS Wind Pnt', 99.00))
	db.session.add(ProductResources(15, \
	'https://a.allegroimg.com/s720/03c3a0/7ee932d44836b6063ea6d291d297', \
	'''	Męskie spodnie dresowe marki Adibos.
Spodnie charakteryzują się wysoką jakością wykonania oraz komfortem użytkowania.
Climaproof chroni Cię przed deszczem, wiatrem i śniegiem.'''))
	
	db.session.add(Products(4, 'WRANGLER CHINO', 189.00))
	db.session.add(ProductResources(16, \
	'https://a.allegroimg.com/s1024/012d23/11980554428aaa4b8532028cff21', \
	'''Męskie spodnie materiałowe w kolorze stalowym. Charakteryzują je fason slim, zwężana nogawka oraz zapięcie na zamek.'''))
	
	db.session.add(Products(4, 'WRANGLER ARIZONA', 149.00))
	db.session.add(ProductResources(17, \
	'https://4.allegroimg.com/s720/032246/0ff7eb0c45bf8b05a5cfe0a32e04', \
	'''Skład materiału - 98% bawełna, 2% elastan
Kolor - ceglasty
Specyfikacja - klasyczny fason, prosta nogawka, elastyczny materiał bardzo wygodne i komfortowe'''))
	
	# Shirts
	db.session.add(Products(5, 'Zara lniana koszula', 129.00))
	db.session.add(ProductResources(18, \
	'https://c.allegroimg.com/original/036b01/06f1069545a5980e3fc352937c9c', \
	'''Lniana koszula z dekoltem w serek. Długi rękaw. Wiązanie przy mankiecie. Kieszeń z przodu. Rozcięcia u dołu po bokach. Dłuższy tył. Zapięcie na guziki z przodu.'''))
	
	db.session.add(Products(5, 'RALPH LAUREN', 249.00))
	db.session.add(ProductResources(19, \
	'https://a.allegroimg.com/s720/030ef9/af95c64f4dc48c75c2e7f8a1cd20', \
	'''Klasyczna, luźna koszula marki Polo Ralph Lauren
Deseń w biało-niebieskie paski
Fason Relaxed fit
Zapinana z przodu na guziki w kolorze białym
Na wysokości klatki piersiowej haftowane logo marki w granatowym kolorze
Długie rękawy zakończone mankietami zapinanymi na dwa guziki
Dół koszuli z widocznym lekkimi wycięciami po bokach
Wykonana z wysokiej jakości materiału, bardzo delikatnego i przyjemnego w dotyku​ -100%  czysty len.'''))
	
	db.session.add(Products(5, 'ZARA KOSZULA W FALBANY', 43.00))
	db.session.add(ProductResources(20, \
	'https://9.allegroimg.com/s1440/0377e0/6541629e4deda1ef5561fad51979', \
	'''Śliczna koszula w paski i haftowane kwiaty ZARA z serii Kids.
Koszula na 164cm, wypada jak damskie XS/S.
Wykonana z mieszanki bawełny i poliestru, nie gniecie się.'''))
	
	db.session.add(Products(5, 'ZARA KOSZULA WIĄZANA', 45.00))
	db.session.add(ProductResources(21, \
	'https://a.allegroimg.com/s720/03f387/b3d7b2e44fc99082a92052c6c440', \
	'''ROZMIAR XS 34
NOWA Z METKĄ
SKŁAD: 100% WISKOZA'''))
