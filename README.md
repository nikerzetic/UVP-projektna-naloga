# UVP-projektna-naloga

Spominske škatle


Uporaba programa

Program poženete preko datoteke spominske \skatle.py. Avomatsko bo ustvarjena datoteka boxes_main_file.txt, v kateri bodo shranjena imena "škatel", in Praskatla.txt, ki služi za zgled. 

Hkrati se bo na zaslonu prikazalo glavno okno. V levem stolpcu lahko izberete eno od obstoječih "škatel", v srednjem enega ali več izmed odprtih "listkov", na desni pa so nanizani mogoči ukazi, razdeljeni v razdelka "Škatle" in "Listki".

Kot pove že ime, se prve nanašajo na "škatle". Med njimi so: 
- Nova škatla: ob kliku na ta gumb, se na zaslonu prikaže novo okno, v katero uporabnik vnese željeno ime nove škatle. Ta se potem prikaže na seznamu škatel v levem stolpcu
- Izbriši škatlo: ukaz izbriše izbrano škatlo
- Preimenuj škatlo: ob kliku na ta gumb, se na zaslonu prikaže novo okno, v katero uporabnik vnese željeno novo ime škatle.
- Odpri škatlo: ob kliku na ta gumb, se v srednje stolpcu izpišejo vsi lističi znotraj izbrane škatle

Ukazi iz drugega razdelka se nanašajo na "listke". Ti so:
- Nov listek: na zaslonu se prikaže novo okno, v katero uporabnik vnese vsebino novega listka in določi ciljno škatlo za nov listek. Pri tem se srednji stolpec ne osveži.
- Izbriši listke: ukaz izbriše vse izbrane listke (listke se izbere s klikom na njihovo ime v srednjem stolpcu)
- Uredi listek: odpre se oknov, v katerem uporabnik uredi vsebino listka
- Premakni listke: na zaslonu se prikaže novo okno, v katerem uporabnik izbere želeno destinacijo premika izbranih listkov. Po potrditvi, program listke premakne v novo škatlo.


Delovanje programa

Po zagonu datoteke spominske \skatle.py, ta zažene razred App iz user_interface.py. Slednja se po potrebi sklicuje na preostale datoteke, predvsem na model.py, ki se ukvarja z odpiranjem in zapiranje datotek, ter hranjenjem podatkov. Je ogrodje programa, ki vsebuje funkcije, s katerimi je mogoče program upravljati tudi skozi konzolo. Preostale datotek so namenjene predvsem grafičnemu umesniku.


Znane težave

Ko uporabnik izbriše "škatlo", je njeno ime odstranjeno s seznama boxes_main_file.py. Funkcija remmove iz zbirke os naj bi odstranila tudi .txt datoteko, v katerim je bila shranjena vsebina "škatle" z istim imenom. To je sprva delovalo, v poznejših verzijah programa, pa ta izbriše pot do datoteke in njeno vsebino, prazna datoteka .txt z istim imenom pa je še vedno vidna v mapi.
