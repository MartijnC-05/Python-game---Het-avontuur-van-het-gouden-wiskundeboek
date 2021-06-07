import sys
import os
import time
from time import sleep


### PLAYER ###
class player:
    def __init__(self):
        self.name = ''
        self.health = 1 
        self.location = 'schoolplein'
        self.inventory = []
        self.animations = 'kort'
player = player()

### ROOMS ###
LOCATION = 'location'
DESCRIPTION = 'description'
ITEMS = 'items'
DIRECTIONS = 'directions'
DEATH = 'death'
WIN = 'win'
A = 'a'
B = 'b'
C = 'c'
D = 'd'
VISITED = 'visited'
REQUIRED = 'required'

rooms = {
#level 1
  'schoolplein': {
    DESCRIPTION: 'Daar sta je dan, het oude, verlaten gebouw wat ooit het Sint-Maartenscollege was. \nJe kijkt nog even naar de brief. Je moet toch echt hier zijn, het staat er, \nhandgeschreven door ene Jopie hemzelf. “Het gouden wiskundeboek ligt verborgen \nin de ruïnes van het Maartens.” ‘Waarom doe ik dit?’ vraag je jezelf af, \nmaar het is te laat om terug te gaan.',
    ITEMS : [],
    DIRECTIONS : "Je kunt: \nA. Door de fietsenstalling de school in \nB. Via de achteringang de school in \nC. of naar KJ, wat sinds de grote bruggeroorlogen van ‘21 niet meer hetzelfde is.",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'fietsenstalling',
    B : 'achteringang',
    C : 'KJ plein',
    D : 'schoolplein',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'fietsenstalling' : {
    DESCRIPTION : "Je loopt de trap op om de fietsenstalling binnen te gaan. Je vestigt je aandacht op \neen eenzame roze fiets, maar wordt door iemand anders aangesproken... \n‘Mensen? Hier?’ denk je, maar je wordt uit je gedachten getrokken door de persoon. \n‘Wat zoek je hier?’ Vraagt hij. Je kijkt naar zijn naambordje, \nhet is Andy, een van de conciërges.",  
    ITEMS : [],
    DIRECTIONS : "Wat zeg je tegen Andy? \nA: ‘Wat doe JIJ hier?’ \nB: ‘Ik kom mijn fiets ophalen, die roze daar.’ \nC: ‘Ene Jopie heeft me gestuurd.’",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'Wat doe JIJ hier?',
    B : 'Ik kom mijn fiets ophalen, die roze daar',
    C : 'Ene Jopie heeft me gestuurd',
    D : 'fietsenstalling',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'Wat doe JIJ hier?' : {
    DESCRIPTION : "Andy stelt deze grap niet op prijs. Hij stuurt je meteen de fietsenstalling uit. \n“En niet meer terugkomen!” Schreeuwt hij je nog na. Nou, daar gaan je kansen om binnen te komen.",  
    DEATH : 'ja',
    WIN : 'nee',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'Ik kom mijn fiets ophalen, die roze daar' : {
    DESCRIPTION : "“Eindelijk, de eigenaar!” Het lijkt haast alsof Andy blij is dat die fiets eindelijk wordt opgehaald. \nHij haalt de sleutels uit zijn broekzak en overhandigt ze aan je. \nHet is misschien niet echt jouw fiets, maar hij is zo blij, dat ga je toch niet verpesten? ",  
    ITEMS : ["fiets"],
    DIRECTIONS : "Je kunt: \nA: alleen maar naar de hal",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'hal',
    B : 'Ik kom mijn fiets ophalen, die roze daar',
    C : 'Ik kom mijn fiets ophalen, die roze daar',
    D : 'Ik kom mijn fiets ophalen, die roze daar',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'Ene Jopie heeft me gestuurd': {
    DESCRIPTION : "“Die naam heb ik al in tijden niet gehoord zeg. Kom verder, snel, voordat je gesnapt wordt.” \nJe vraagt je af wie jou zal snappen, maar goed, je volgt Andy snel.",  
    ITEMS : [],
    DIRECTIONS : "Je kunt: \nA: alleen maar naar de hal",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'hal',
    B : 'Ene Jopie heeft me gestuurd',
    C : 'Ene Jopie heeft me gestuurd',
    D : 'Ene Jopie heeft me gestuurd',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'achteringang' : {
    DESCRIPTION : "Je loopt langs het gebouw en gaat het achterplein op. Er zitten alleen \n2 mensen heel dichtbij elkaar op een bankje. ‘Nou ja, moet kunnen toch?’ \ndenk je. Lichtelijk walgend loop je naar de deur toe. ‘Huh? Niet op slot? Apart.’ \nDenk je, maar je loopt snel naar binnen.",
    ITEMS : [],
    DIRECTIONS: "Je kunt: \nA: alleen maar naar de hal",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'hal',
    B : 'achteringang',
    C : 'achteringang',
    D : 'achteringang',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'KJ plein' : {
    DESCRIPTION : "Je draait je om om naar KJ te gaan, maar meteen betwijfel je of dat een goed idee is. \nAlleen vanaf de ruïnes kan je al zien dat het er wemelt van de bruggers, \nzij hadden de oorlog gewonnen, en sindsdien is het hun basis. \n‘Is het wel zo handig om te gaan?’ vraag je je af. Er komt een jochie op een step langs. \n‘Ik zou t niet doen vriend.’ Hij stept verder.",  
    ITEMS : [],
    DIRECTIONS : "Wat doe je?: \nA: ‘Ik moet niet al te veel afdwalen, ik sla KJ wel over’ \nB: ‘Hoe erg kan het zijn? Het zijn ook maar bruggers.’",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'schoolplein',
    B : 'KJ centrum',
    C : 'KJ plein',
    D : 'KJ plein',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'KJ centrum' : {
    DESCRIPTION : "Je zet 1 stap in het centrum, en wordt meteen overvallen door de bruggers. \nJe doet je best om terug te vechten, maar voor elke brugger die je neerslaat \nkomen er 3 meer uit de Albert Heijn lopen. Na een langdurige strijd overleef je het niet.",  
    DEATH : 'ja',
    WIN : 'nee',
    VISITED : 'nee',
    REQUIRED : ''
  },

#level 2
  'hal' : {
    DESCRIPTION : "Je bent nu binnen. Je staat in de hal en kijkt om je heen, \nje slikt je angst weg en besluit waar je heen gaat: De trap op richting de eerste verdieping, \nnaar de aula, naar de vleugel NT en G, of terug naar buiten.",  
    ITEMS : [],
    DIRECTIONS : "Je kunt naar: \nA: De trap \nB: De aula \nC: De vleugel NT en G \nD: Naar buiten",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'trap',
    B : 'aula',
    C : 'vleugel NT en G',
    D : 'schoolplein',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'trap' : {
    DESCRIPTION : "Er zijn twee trappen die je kan nemen: de trap die richting lokalen gaat, \nof de trap die richting de mediatheek gaat.",  
    ITEMS : [],
    DIRECTIONS : "Welke trap neem je? \nA: Naar de lokalen \nB: Naar de mediatheek",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'lokalen',
    B : 'mediatheek',
    C : 'trap',
    D : 'trap',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'mediatheek' : {
    DESCRIPTION : "Je gaat de trap op richting de mediatheek. Je loopt nog langs lokaal 126, \nwaar een man met donkerblond haar achter een computer zit te klooien met google meet. \n‘Rare eend.’ Denk je. Je loopt door naar de mediatheek, waar je een zacht geluid \nvan een printer hoort. Het geluid wordt luider en luider, \ntotdat je de mediatheek zelf binnenloopt. Er is een enkele vrouw aanwezig, \nbezig met de printer. Ze draait zich direct om bij je eerste stap. \n‘Dus jij wilt hulp met printen?’ Vraagt ze. Je kan geen antwoord geven \nvoordat ze je al naar de printer heeft geleid. Vervolgens moet je printen \ntotdat je je laatste adem hebt gegeven.",  
    DEATH : 'ja',
    WIN : 'nee',
    VISITED : 'nee',
    REQUIRED : ''
    },  

  'aula' : {
    DESCRIPTION : "Je loopt de aula binnen. Het is helemaal leeg, behalve 2 oude mannen \ndie bingo zitten te spelen. ‘Ach ja, beetje bingo moet kunnen.’ Denk je. \nJe kan de oude mannen benaderen of naar de kantine toe.",  
    ITEMS : [],
    DIRECTIONS : "Wat ga je doen? \nA: Naar de kantine \nB: Benader de oude mannen \nC: terug naar de hal",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'kantine',
    B : 'oude mannen',
    C : 'hal',
    D : 'aula',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'kantine' : {
    DESCRIPTION : "Er zijn een paar dingen die je opvallen, zoals een hendeltje van de kapotte panini machine, \nen een heerlijke wafel die bijna aan de datum is.",  
    ITEMS : ["hendeltje", "wafel"],
    DIRECTIONS : "je kunt: \nA: alleen terug naar de aula",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'aula',
    B: 'kantine',
    C : 'kantine',
    D : 'kantine',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'oude mannen' : {
    DESCRIPTION : "Je loopt naar de oude mannen toe. Op het moment dat je aan komt lopen, \nklinkt er een krak. “Alle bingoballen nog aan toe!” Roept een van de twee uit. \nJe ziet dat de hendel van het bingorad is afgebroken. Een van de twee ziet je aan komen lopen, \nen begint meteen met praten. “Zeg, makker, jij daar, kun je ons even helpen?” \nJe hebt niet echt een keuze, dus je knikt ja. “Komt dat eens goed uit zeg! \nWij zijn Ome Henk en Ome Willem, en we houden van bingo. \nZoals je kunt zien hebben we een nieuw hendeltje nodig, kan je die voor ons zoeken?” \nJe knikt weer, je kan natuurlijk geen nee zeggen tegen zulke aardige mensen.",  
    ITEMS : [],
    DIRECTIONS : "Wat zeg je tegen Ome Henk en Ome Willem? \nA: Ik ga voor jullie op zoek \nB: Hier heb je de hendel",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'aula',
    B : 'hier heb je de hendel',
    C : 'oude mannen',
    D : 'oude mannen',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'hier heb je de hendel' : {
    DESCRIPTION : "Daar heb je hem hoor! Geef hem, alsjeblieft, dan kunnen we weer verder.” \nJe overhandigt de hendel aan de oude mannen. Nadat je een gezellig potje bingo hebt gespeeld, \ngeeft Ome Willem je een legoblokje. “Die krijg je van ons cadeau, \nje kan altijd terugkomen om nog een potje te spelen!” ",
    ITEMS : ["legoblokje"],
    DIRECTIONS : "Je kunt: \nA: alleen naar de aula",
    DEATH : 'nee',
    WIN : "nee",
    A : 'aula',
    B : 'hier heb je de hendel',
    C : 'hier heb je de hendel',
    D : 'hier heb je de hendel',
    VISITED : 'nee',
    REQUIRED : 'hendeltje'
  },

  'vleugel NT en G': {
    DESCRIPTION : "Je loopt richting de vleugel van NT en G, maar voordat je er goed kan komen \nhoor je een explosie. Er komen 2 andere mensen uit een lokaal gerend, \ngevolgd door een derde man met een honkbalknuppel. De gewapende gek keert zich tot jou. \n‘Ga jij eens even ergens anders kletsen.’ Zegt hij, met een simpelweg enge glimlach op zijn gezicht. \nJe probeert weg te rennen, maar voordat je het weet heeft hij je knieschijven ingetimmerd. \nJe overleeft het niet. ",  
    DEATH : 'ja',
    WIN : 'nee',
    VISITED : 'nee',
    REQUIRED : ''
  },

#level 3
  'lokalen' : {
    DESCRIPTION : "Je bent nu de trap opgegaan richting de lokalen. Je kan verder op de eerste verdieping, \nnaar de tweede verdieping of helemaal naar de derde verdieping. \nJe kan natuurlijk ook weer terug naar beneden.",  
    ITEMS : [],
    DIRECTIONS : "Je kunt naar: \nA: De eerste verdieping \nB: De tweede verdieping \nC: De derde verdieping \nD: Naar beneden",
    DEATH : 'nee',
    WIN : 'win',
    A : 'verdieping 1',
    B : 'verdieping 2',
    C : 'verdieping 3',
    D : 'hal',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'verdieping 1' : {
    DESCRIPTION : "Je staat nu op de eerste verdieping. Je ziet 2 mensen in een lokaal zitten, en in de verte hoor je gestamp. \nJe kan de mensen benaderen, of verder naar het gestamp kijken.",  
    ITEMS : [],
    DIRECTIONS : "Wat ga je doen?: \nA: Benader de mensen \nB: Ga naar het gestamp",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'benader de mensen',
    B : 'ga naar het gestamp',
    C : 'verdieping 1',
    D : 'verdieping 1',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'benader de mensen' : {
    DESCRIPTION : "Je nadert de deuropening, en hoort een zacht gebabbel over God, Jezus en de Heilige Geest, amen. \nJe stapt het lokaal in, en de vrouw kijkt direct jouw kant op. 'Verdwijn, brugger! \nU bent hier niet welkom!' Ze duwt een kruis in je gezicht. 'De kracht van God houdt u tegen!' \nJe wordt teruggebracht naar de hal.",  
    ITEMS : [],
    DIRECTIONS : "Je kunt: \nA: alleen maar naar de hal",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'hal',
    B : 'benader de mensen',
    C : 'benader de mensen',
    D : 'benader de mensen',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'ga naar het gestamp' : {
    DESCRIPTION : "Je loopt op het gestamp af. Je ziet in een lokaal een man die bruggers aan het hypnotiseren is \nmet groene koffiebonen. Uiteindelijk kom je aan bij een ander lokaal, waar je een man met korte broek ziet. \nJe herinnert je ineens een oude tegeltjes wijsheid van je oom Mark. \n'Een man zonder baard is als Deegens zonder beenhaar.' Je ziet dat zijn benen glad geschoren zijn. \nJe valt flauw van de shock, en wordt wakker bij de trap. Je ziet een briefje liggen met een code.",  
    ITEMS : ["briefje met code"],
    DIRECTIONS : "Je kunt: \nA: alleen maar naar de hal",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'hal',
    B : 'ga naar het gestamp',
    C : 'ga naar het gestamp',
    D : 'ga naar het gestamp',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'verdieping 2' : {
    DESCRIPTION : "Je komt aan op de tweede verdieping. Ergens in de verte ruik je een vreemde geur \ndie erg kenmerkend is voor het vak wiskunde, je weet dus dat je in de buurt bent, maar moet je er wel heen gaan?",  
    ITEMS : [],
    DIRECTIONS : "Je kunt: \nA: verder de gang in \nB: terug gaan",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'verder de gang in',
    B : 'terug gaan',
    C : 'verdieping 2',
    D : 'verdieping 2',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'verder de gang in' : {
    DESCRIPTION : "je loopt verder de gang in, hoe verder je loopt hoe sterker de geur wordt. Je komt aan bij het lokaal van Jopie.",  
    ITEMS : [],
    DIRECTIONS : "Je kunt: \nA: alleen naar de ingang van het lokaal van jopie",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'ingang van het lokaal van jopie',
    B : 'verder de gang in',
    C : 'verder de gang in',
    D : 'verder de gang in',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'terug gaan' : {
    DESCRIPTION : "Je wilt terug gaan, maar de geur is zo sterk dat je niet meer kan nadenken, \nje loopt vanzelf naar het wiskundelokaal van jopie, je kunt niet eens meer tegenstribbelen.",  
    ITEMS : [],
    DIRECTIONS : "je kunt: \nA: alleen maar naar het lokaal van jopie",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'ingang van het lokaal van jopie',
    B : 'terug gaan',
    C : 'terug gaan',
    D : 'terug gaan',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'verdieping 3' : {
    DESCRIPTION : "Helemaal uitgeput kom je aan op de derde verdieping. Je hoort uit de gang een oorverdovend geschreeuw komen, \nje vraagt je af of je wel verder de gang in moet lopen of dat je terug zal gaan. ",  
    ITEMS : [],
    DIRECTIONS : "Waar ga je heen: \nA: verder in de gang \nB: terug",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'verder in de gang',
    B : 'lokalen',
    C : 'verdieping 3',
    D : 'verdieping 3',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'verder in de gang' : {
    DESCRIPTION : "Je besluit om verder de gang in te lopen. Je loopt eerst langs een lokaal waar allemaal mensen \ncroissants en baguettes aan het eten zijn met een zeer arelaxend muziekje op de achtergrond. \nAls je dan verder de gang in loopt zie je een dame die heel aandachtig aan het kijken is \nnaar naakte beelden. 'Vreemd.' Denk je, maar je loopt toch door. \nTenslotte kom je aan bij het lokaal waar het geluid vandaan kwam. Je probeert het lokaal in te kijken, \nmaar er sprint een huilende brugger uit het lokaal, gevolgd door een schreeuwende man. \nHet geluid is werkelijk oorverdovend, maar veel tijd voor zeuren heb je niet. \nDe man kijkt direct jouw kant op. 'Vertaal jij eens een gerundivum!' \nHij knijpt zijn ogen tot spleetjes, dit is wel echt serieus.",  
    ITEMS : [],
    DIRECTIONS : "Wat zeg je? \nA: 'Uh… Servus? \nB: gebruik legoblokje (alleen beschikbaar als je een legoblokje hebt)	",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'Uh… Servus?',
    B : 'gebruik legoblokje',
    C : 'verder in de gang',
    D : 'verder in de gang',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'Uh… Servus?' : {
    DESCRIPTION : "De gezichtsuitdrukking van de man verandert in eens. \nHet lijkt alsof hij gaat huilen, maar ineens start hij met opera zingen. \nNa een tijdje pakt hij je bij je kraag. 'Ik ga jou necare.' Ik spaar je de details, maar het laatste wat je hoorde was 'slaven en doden is echt mijn ding.' Het loopt niet goed af.",  
    DEATH : 'ja',
    WIN : 'nee',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'gebruik legoblokje' : {
    DESCRIPTION : "Je legt het legoblokje op de grond en rent zo snel mogelijk weg. \nDe man kan zijn aandacht alleen vestigen op het blokje. \nJe bent weer veilig, ook al is het volledig uitgeput, bij de trap.",  
    ITEMS : [],
    DIRECTIONS : "Je kunt: \nA: alleen maar naar de trap",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'trap',
    B : 'gebruik legoblokje',
    C : 'gebruik legoblokje',
    D : 'gebruik legoblokje',
    VISITED : 'nee',
    REQUIRED : 'legoblokje'
  },

# level 4
  'ingang van het lokaal van jopie' : {
    DESCRIPTION : "Je staat nu bij de ingang van het lokaal waar de geur vandaan komt. \nEr staat een zeer lange en brede man in de deuropening. \nHij kijkt niet naar beneden, hij bromt alleen iets van “Geef mij de code.”",  
    ITEMS : [],
    DIRECTIONS : "Wat doe je? \nA: Welke code? \nB: gebruik code",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'welke code?',
    B : 'gebruik code',
    C : 'ingang van het lokaal van jopie',
    D : 'ingang van het lokaal van jopie',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'welke code?' : {
    DESCRIPTION : "Welke code? Ik moet hier waarschijnlijk later terugkomen.",  
    ITEMS : [],
    DIRECTIONS : "Je kunt: \nA: alleen maar naar de trap",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'trap',
    B : 'welke code?',
    C : 'welke code?',
    D : 'welke code?',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'gebruik code' : {
    DESCRIPTION : "Je noemt de code op, namelijk 69420. De man kijkt ineens omlaag, en gaat als een soort deur aan de kant. ",  
    ITEMS : [],
    DIRECTIONS : "Je kunt: \nA: alleen maar naar het lokaal van Jopie",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'lokaal van Jopie',
    B : 'gebruik code',
    C : 'gebruik code',
    D : 'gebruik code',
    VISITED : 'nee',
    REQUIRED : 'briefje met code'
  },

  'lokaal van Jopie' : {
    DESCRIPTION : "Je stapt het lokaal in, waar een half kale man op een troon van wiskundeboeken zit. \n“Gegroet! Ik zie dat je mijn brief hebt ontvangen. Wist je al dat je de haakjes bent vergeten?” \nJe kijkt een beetje verward. ‘Waar heeft hij het over?’ denk je. “Ik zal mezelf even voorstellen. \nIk ben Jopie, heer van lokaal 211 en meester van de wiskunde.” Achter hem staat een groot krijtbord \nmet een grote scheur erin. \nhet gerucht gaat dat Jopie eens een leerling met zijn hoofd tegen het bord aan heeft gegooid. \nJopie gaat verder met zijn verhaal, van alles over zijn meesterplan, hoeveel succes hij al heeft geboekt \nen hoe hij hier zo vorstelijk voor betaald wordt. ",  
    ITEMS : [],
    DIRECTIONS : "Wat doe je? \nA: “Hij heeft wel een boeiend verhaal, dat wil ik wel afluisteren.” \nB: “Ik kom hier voor het gouden boek, ik heb geen tijd voor dit verhaal.”",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'verhaal afluisteren',
    B : 'ik heb geen tijd voor dit verhaal',
    C : 'lokaal van Jopie',
    D : 'lokaal van Jopie',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'verhaal afluisteren' : {
    DESCRIPTION : "Je wacht netjes Jopie zijn verhaal af. Nadat hij is afgesloten met zijn keuze om van vorstelijke salaris \neen gouden wiskundeboek te kopen, bedankt hij je voor het luisteren. Vervolgens drukt hij op een knopje, \nwaardoor je in de kelder van de ruïnes valt. Je kan wel mooi een gesprek voeren met een andere jongen \ndie heel erg van Feyenoord houdt, maar vervolgens ga je dood van de verveling.",  
    DEATH : 'ja',
    WIN : 'nee',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'ik heb geen tijd voor dit verhaal' : {
    DESCRIPTION : "“Ik kom hier voor het gouden boek, ik heb geen tijd voor dit verhaal.” Je blik dwaalt af naar 2 glimmende boeken achter hem, \neen gouden boek wat erg lijkt op wiskunde, en een zilveren boek wat lijkt op Frans. Je schraapt met je nagels over het krijtbord \nom jopie tijdelijk uit te schakelen, het geluid is zo scherp dat je zelf ook bijna was uitgeschakeld. \nJe kunt nu snel naar het boek lopen, maar welk boek pak je?",  
    ITEMS : [],
    DIRECTIONS : "Wat doe je? \nA: “Ik kwam hier voor het gouden boek, ik pak het gouden boek!” \nB: “Eigenlijk is dat zilveren boek leuker...”",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'gouden boek',
    B : 'zilveren boek',
    C : 'ik heb geen tijd voor dit verhaal',
    D : 'ik heb geen tijd voor dit verhaal',
    VISITED : 'nee',
    REQUIRED : ''
  },

##### nog aanpassen ####
  'zilveren boek' : {
    DESCRIPTION : "“Eigenlijk is dat zilveren boek leuker...”Je rent langs de troon van Jopie en pakt het boek. \nHet moment dat je het boek aanraakt voel je de kracht van de Fransen in je opkomen.",  
    ITEMS : ['zilveren boek'],
    DIRECTIONS : "Wat doe je? \nA: Je gaat naar de gang \nB: Je gaat via het raam naar buiten \nC: Je kijkt nog even rond in het lokaal",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'naar de gang',
    B : 'via het raam naar buiten',
    C : 'nog even rondkijken in het lokaal',
    D : 'zilveren boek',
    VISITED : 'nee',
    REQUIRED : ''
  },

#level 5
  'gouden boek' : {
    DESCRIPTION : "Je rent langs de troon van Jopie en pakt het boek. Het boek is best zwaar, dus je weet meteen dat het boek van puur goud is gemaakt \n Je hebt nu het boek te pakken, maar je moet nu nog zien te ontsnappen \nvoordat Jopie weer wakker wordt. Welke kant ga je op?",  
    ITEMS : ['gouden wiskundeboek'],
    DIRECTIONS : "Wat doe je? \nA: Je gaat naar de gang \nB: Je gaat via het raam naar buiten \nC: Je kijkt nog even rond in het lokaal",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'naar de gang',
    B : 'via het raam naar buiten',
    C : 'nog even rondkijken in het lokaal',
    D : 'gouden boek',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'via het raam naar buiten' : {
    DESCRIPTION : "De snelste weg naar buiten is natuurlijk via het raam. Je doet het raam open en kijkt even, \n‘Het valt wel mee hoe hoog dit is.’ Denk je, je tuurt iets te ver over het randje en kukelt naar beneden. \nJe komt met je bips terecht op een legoblokje. Je schreeuwt het uit van de pijn, en door de schreeuw wordt Jopie weer wakker, \nwaarna hij zelf ook springt. Uiteindelijk heeft hij je toch te pakken.",  
    DEATH : 'ja',
    WIN : 'nee',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'nog even rondkijken in het lokaal' : {
    DESCRIPTION : "Je besluit om nog even rond te kijken in het rommelige lokaal van jopie. \n“Misschien liggen er nog wel waardevolle spullen die ik kan meenemen.” Denk je. \nJe ziet nog een paar wiskunde uitwerkingen liggen. Je denkt: “die kan ik nog wel voor wat geld aan bruggers verkopen.” \nOp dat moment wordt Jopie wakker, hij ziet dat zijn gouden boek weg is en dat jij in zijn lokaal \naan het rondkijken bent. Hij drukt op een knopje en je valt naar beneden. \n“En waag het niet om nog eens te komen!” roept hij je nog na. ",  
    DEATH : 'ja',
    WIN : 'nee',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'naar de gang' : {
    DESCRIPTION : "Je rent snel het lokaal uit, maar Jopie wordt net wakker. Hij ziet dat zijn boek weg is en dat jij in de deuropening staat. \n“Nou ja, dat had ik niet verwacht!” Zegt hij. “Maar goed, ik wil dat boek wel terug.” \nHij schraapt zijn keel. “MAAAAAARCEEEEEEEEEEEEL!” Schreeuwt hij. \nPlots komt een zeer brede man uit een ander lokaal gestormd. Je slikt puur van de schrik, \nen zet het op een rennen.",  
    ITEMS : [],
    DIRECTIONS : "Wat doe je? \nA: “Oh jeetje, snel weg hier.” \nB: gebruik fiets \nC: gebruik wafel",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'oh jeetje, snel weg hier',
    B : 'gebruik fiets',
    C : 'gebruik wafel',
    D : 'naar de gang',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'oh jeetje, snel weg hier' : {
    DESCRIPTION : "Het maakt niet uit hoe snel je rent, Marcel is gewoon sneller. Op een gegeven moment haalt hij je in. \nHij grijpt het boek uit je handen en vervolgens gooit hij je terug naar de hal. Volgende keer beter dan maar",  
    ITEMS : [],
    DIRECTIONS : "Je kunt: \nA: aleen maar naar hal",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'hal',
    B : 'oh jeetje, snel weg hier',
    C : 'oh jeetje, snel weg hier',
    D : 'oh jeetje, snel weg hier',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'gebruik fiets' : {
    DESCRIPTION : "Je merkt dat Marcel simpelweg sneller is, maar je herinnert ineens dat Andy je een fiets had gegeven. \nJe tovert de fiets uit je broekzak en start met door de gangen fietsen. Je gaat de trap af, \nen komt dan weer Andy tegen. Hij blokkeert het pad en kijkt je heel boos aan. \n“Niet fietsen door de gangen!” Schreeuwt hij. Hij trapt je de school uit. “En niet meer terugkomen!” \nSchreeuwt hij. helaas heb je het boek niet kunnen redden. ",  
    DEATH : 'ja',
    WIN : 'nee',
    VISITED : 'nee',
    REQUIRED : 'fiets'
  },

  'gebruik wafel' : {
    DESCRIPTION : "Marcel nadert steeds, maar dan herinner je ineens dat je nog een wafel had gevonden. \nJe gooit hem naar achteren, en kijkt niet om totdat je bij de trap bent. Marcel is blijkbaar \nheel geïnteresseerd door de wafel, aangezien je bent ontsnapt.",  
    ITEMS : [],
    DIRECTIONS : "je kunt: \nA: alleen maar naar de ontsnapping",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'ontsnapping',
    B : 'gebruik wafel',
    C : 'gebruik wafel',
    D : 'gebruik wafel',
    VISITED : 'nee',
    REQUIRED : 'wafel'
  },

  'ontsnapping' : {
    DESCRIPTION : "Je rent snel via de trap naar beneden, maar als je naar buiten wilt rennen komt de rector om de hoek lopen.",  
    ITEMS : [],
    DIRECTIONS : "Wat doe je? \nA: Als je het gouden wiskundeboek hebt \nB: als je het zilveren wiskundeboek hebt",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'ontsnapping gouden wiskundeboek',
    B : 'ontsnapping zilveren wiskundeboek',
    C : 'ontsnapping',
    D : 'ontsnapping',
    VISITED : 'nee',
    REQUIRED : ''
  },

  'ontsnapping zilveren wiskundeboek' : {
    DESCRIPTION : "De rector probeert zich nog voor te stellen. Je hoort alleen maar “...Ajolt...“ \nen “Ik hou van stroopwafels.” Maar je rent ontzettend snel langs hem. Je nadert de uitgang, \nmaar plotseling komt er een groepje mensen gewapend met baguettes en berets om de hoek kijken. \n“Prenez son noix!” Zegt een van hen. Ze komen op je afgerend en steken je neer met hun baguettes. \nHet is een zeer onprettige, arelaxende ervaring. ",  
    DEATH : 'ja',
    WIN : 'nee',
    VISITED : 'nee',
    REQUIRED : 'zilveren boek'
  },

  'ontsnapping gouden wiskundeboek' : {
    DESCRIPTION : "De rector probeert zich nog voor te stellen. Je hoort alleen maar “...Ajolt...“ en “Ik hou van stroopwafels.” \nMaar je rent ontzettend snel langs hem. Je nadert de uitgang, maar plotseling staat Jopie in de weg. \n“Dus jij denkt dat je snel weg kan komen?! Nou nou zeg, je lijkt echt op David. \nWat ben ik toch ont-zet-tend blij met jou. Helaas stopt het hier echt, \nhierna ga ik denk ik wel genieten van mijn pensioen op een mooi strand, al hou ik helemaal niet van het strand.” \nJopie maakt zijn verhaal af, maar je was al langs hem gerend. Je rent door de fietsenstalling, \nzegt Andy even gedag en rent weg naar de horizon, met het gouden wiskundeboek onder je arm.",  
    DEATH : 'nee',
    WIN : 'ja',
    VISITED : 'nee',
    REQUIRED : 'gouden wiskundeboek'
  },
}

### MENU SELECTIONS ### 
def title_screen_selections(): 
  option = input("> ")
  if option.lower() == ("start"):
    start_game()
  elif option.lower() == ("help"):
    help_menu()
  elif option.lower() == ('settings'):
    settings_menu()
  elif option.lower() == ("stop"):
    stop_menu()
  else:
    print("vul aub een geldig antwoord in.")
    title_screen_selections()

### HELP MENU SELECTIONS ###
def help_menu_selections():
  option = input("> ")
  if option.lower() == ("menu"):
    title_screen()
  elif option.lower() == ("stop"):
      stop_menu()
  elif option.lower() == ("quit"):
      stop_menu()
  elif option.lower() == ("q"):
      stop_menu()
  elif option.lower() == ("help"):
      help_menu()
  elif option.lower() == ("h"):
      help_menu()
  else:
    print("vul aub een geldig antwoord in.")
    help_menu_selections()

### GAME HELP MENU SELECTIONS ###
def game_help_menu_selections():
  option = input("> ")
  if option.lower() == ("back"):
    print_location()
  elif option.lower() == ("b"):
    print_location()
  else:
    print("vul aub een geldig antwoord in.")
    game_help_menu_selections()

### SETTINGS OPTIONS ####
def settings_options():
  option = input('> ')
  if option.lower() == ('k'):
    player.animations = 'kort'
    settings_menu()
  elif option.lower() == ('kort'):
    player.animations = 'kort'
    settings_menu()
  elif option.lower() == ('l'):
    player.animations = 'lang'
    settings_menu()
  elif option.lower() == ('lang'):
    player.animations = 'lang'
    settings_menu()
  elif option.lower() == ('back'):
    title_screen()
  elif option.lower() == ('b'):
    title_screen()
  elif option.lower() == ('menu'):
    title_screen()
  elif option.lower() == ('m'):
    title_screen()
  else:
    print('vul aub een geldig antwoord in')
    settings_options()

### GAME SETTINGS OPTIONS ####
def game_settings_options():
  option = input('> ')
  if option.lower() == ('k'):
    player.animations = 'kort'
    game_settings_menu()
  elif option.lower() == ('kort'):
    player.animations = 'kort'
    game_settings_menu()
  elif option.lower() == ('l'):
    player.animations = 'lang'
    game_settings_menu()
  elif option.lower() == ('lang'):
    player.animations = 'lang'
    game_settings_menu()
  elif option.lower() == ('back'):
    print_location()
  elif option.lower() == ('b'):
    print_location()
  else:
    print('vul aub een geldig antwoord in')
    game_settings_options()


### STOP MENU SELECTIONS ###
def stop_menu_selections():
  option = input("> ")
  if option.lower() == ("ja"):
    os.system('clear')
    sys.exit
  elif option.lower() == ("nee"):
      title_screen()
  else:
    print("vul aub ja of nee in.")
    stop_menu_selections()

### GAME STOP MENU SELECTIONS ###
def game_stop_menu_selections():
  option = input("> ")
  if option.lower() == ("ja"):
    os.system('clear')
    sys.exit
  elif option.lower() == ("nee"):
    print_location()
  else:
    print("vul aub ja of nee in.")
    game_stop_menu_selections()

### DEATH MENU SELECTIONS ###
def death_menu_selections():
  player.location = 'schoolplein'
  player.inventory = ''
  option = input ("> ")
  if option.lower() == ("ja"):
    print_location()
  elif option.lower() == ("nee"):
    stop_menu()
  else:
    print("vul aub ja of nee in.")
    death_menu_selections()

### WIN MENU SELECTIONS ###
def win_menu_selections():
  player.location='schoolplein'
  player.inventory = ''
  option = input ("> ")
  if option.lower() == ("ja"):
    title_screen()
  elif option.lower() == ("nee"):
    stop_menu()
  else:
    print("vul aub ja of nee in.")
    win_menu_selections

### GET OPTIONS ###
def get_options():
  option = input('> ')
  if option.lower() in (rooms[player.location][ITEMS]):
      player.inventory.append(option.lower())
      print(f'{option} is toegevoegd aan je inventory')
      rooms[player.location][ITEMS].remove(option.lower())
      time.sleep(1)
      get_menu()
  elif option.lower() == ('b'):
    print_location()
  elif option.lower() == ('back'):
    print_location()
  elif option.lower() == ('i'):
    inventory()
  elif option.lower() == ('inventory'):
    inventory()
  else:
    print('Dit is geen geldig antwoord. Probeer opnieuw.')
    time.sleep(1)
    get_menu()

### DROP OPTIONS ###
def drop_options():
  option = input('> ')
  if option.lower() in player.inventory:
    player.inventory.remove(option.lower())
    print(f'{option} is verwijderd uit je inventory')
    rooms[player.location][ITEMS].append(option.lower())
    time.sleep(1)
    drop_item()
  elif option.lower() == ('b'):
    print_location()
  elif option.lower() == ('back'):
    print_location()
  else:
    print('Dit is niet een geldig antwoord. Probeer opnieuw.')
    drop_options()

### INVENTORY OPTIONS ###
def inventory_options():
  option = input('> ')
  if option.lower() == ('d'):
    drop_item()
  elif option.lower() == ('b'):
    print_location()
  else:
    print('vul aub een geldig antwoord in')
    inventory_options()


### MENU'S ###
def title_screen():
  os.system('clear')
  print('############################################################')
  print('#                   -=- Text adventure -=-                 #')
  print('#     -=- Het avontuur van het gouden wiskundeboek -=-     #')
  print('############################################################')
  print('#                                                          #')
  print('#               -=-=-=-o  Start     o-=-=-=-               #')
  print('#               -=-=-=-o  Help      o-=-=-=-               #')
  print('#               -=-=-=-o  Settings  o-=-=-=-               #')
  print('#               -=-=-=-o  Stop      o-=-=-=-               #')
  print('#                                                          #')
  print('#             Typ Start, Help, Settings of stop            #')
  print('############################################################')
  print('#          -=- gemaakt door Brendan en Martijn -=-         #')
  print('############################################################')
  title_screen_selections() 

def help_menu():
  os.system('clear')
  print('############################################################')
  print('#                      -=- Help -=-                        #')
  print('############################################################')
  print('#                                                          #')
  print('# -=- Als er een optie komt om ergens heen te gaan         #')
  print('#        typ dan de letter in die bij die optie hoort      #')
  print('#                                                          #')
  print('# -=- Als je de mogelijkheid hebt om een item op te pakken #')
  print('#        typ dan g (get) om het item op te pakken          #')
  print('#        typ d (drop) om het item te laten vallen          #')
  print('#        en typ i (inventory) om je inventory te bekijken  #')
  print('#                                                          #')
  print('# -=- Je kunt altijd tijdens het spelen q (quit)           #')
  print('#        en h (help) typen om te stoppen                   #')
  print('#        of dit menu opnieuw te tonen                      #')
  print('#                                                          #')
  print('# -=- Veel plezier met het spelen!                         #')
  print('#                                                          #')
  print('#        Typ Menu om terug naar het menu te gaan           #')
  print('############################################################')
  print('#         -=- gemaakt door Brendan en Martijn -=-          #')
  print('############################################################')
  help_menu_selections() 

def settings_menu():
  os.system('clear')
  print('############################################################')
  print('#                    -=- Settings -=-                      #')
  print('############################################################')
  print('#                                                          #')
  print('# -=- Animations                                           #')
  print('#                                                          #')
  print('# -=- Op dit moment zijn animaties ' + player.animations + '                    #')
  print('#     Als je dit wilt aanpassen typ: k(kort) of l(lang)    #')
  print('#                                                          #')
  print('#        Typ Menu om terug naar het menu te gaan           #')
  print('############################################################')
  print('#         -=- gemaakt door Brendan en Martijn -=-          #')
  print('############################################################')
  settings_options()

def game_settings_menu():
  os.system('clear')
  print('############################################################')
  print('#                    -=- Settings -=-                      #')
  print('############################################################')
  print('#                                                          #')
  print('# -=- Animations                                           #')
  print('#                                                          #')
  print('# -=- Op dit moment zijn animaties ' + player.animations + '                    #')
  print('#     Als je dit wilt aanpassen typ: k(kort) of l(lang)    #')
  print('#                                                          #')
  print('#               Typ b(back) om terug te gaan               #')
  print('############################################################')
  print('#         -=- gemaakt door Brendan en Martijn -=-          #')
  print('############################################################')
  game_settings_options()

def game_help_menu():
  os.system('clear')
  print('############################################################')
  print('#                      -=- Help -=-                        #')
  print('############################################################')
  print('#                                                          #')
  print('# -=- Als er een optie komt om ergens heen te gaan         #')
  print('#        typ dan de letter in die bij die optie hoort      #')
  print('#                                                          #')
  print('# -=- Als je de mogelijkheid hebt om een item op te pakken #')
  print('#        typ dan g (get) om het item op te pakken          #')
  print('#        typ d (drop) om het item te laten vallen          #')
  print('#        en typ i (inventory) om je inventory te bekijken  #')
  print('#                                                          #')
  print('# -=- Je kunt altijd tijdens het spelen q (quit)           #')
  print('#        en h (help) typen om te stoppen                   #')
  print('#        of dit menu opnieuw te tonen                      #')
  print('#                                                          #')
  print('# -=- Veel plezier met het spelen!                         #')
  print('#                                                          #')
  print('#        Typ b(back) om terug naar het menu te gaan        #')
  print('############################################################')
  print('#         -=- gemaakt door Brendan en Martijn -=-          #')
  print('############################################################')
  game_help_menu_selections() 

def stop_menu():
  os.system('clear')
  print('############################################################')
  print('#                      -=- Stop -=-                        #')
  print('############################################################')
  print('#                                                          #')
  print('# -=- Weet je zeker dat je wilt stoppen?                   #')
  print('# -=- Ja/ Nee                                              #')
  print('#                                                          #')
  print('############################################################')
  print('#         -=- gemaakt door Brendan en Martijn -=-          #')
  print('############################################################')
  stop_menu_selections()

def game_stop_menu():
  os.system('clear')
  print('############################################################')
  print('#                      -=- Stop -=-                        #')
  print('############################################################')
  print('#                                                          #')
  print('# -=- Weet je zeker dat je wilt stoppen?                   #')
  print('# -=- Ja/ Nee                                              #')
  print('#                                                          #')
  print('############################################################')
  print('#         -=- gemaakt door Brendan en Martijn -=-          #')
  print('############################################################')
  game_stop_menu_selections()

def death_menu():
  os.system('clear')
  print('############################################################')
  print('#                    -=- Game Over -=-                     #')
  print('############################################################')
  print('#                                                          #')
  print('# -=- Helaas, je hebt het niet gered. Game over            #')
  print('# -=- Wil je het opnieuw proberen?                         #')
  print('#                                                          #')
  print('############################################################')
  print('#         -=- gemaakt door Brendan en Martijn -=-          #')
  print('############################################################')
  death_menu_selections()

def win_menu():
  os.system('clear')
  print('############################################################')
  print('#                    -=- Gewonnen! -=-                     #')
  print('############################################################')
  print('#                                                          #')
  print('# -=- Gefeliciteerd je hebt gewonnen!                      #')
  print('# -=- Wil je het spel opnieuw spelen?                      #')
  print('#                                                          #')
  print('############################################################')
  print('#         -=- gemaakt door Brendan en Martijn -=-          #')
  print('############################################################')
  win_menu_selections()

### GET MENU ###
def get_menu():
  os.system('clear')
  print('+=' * 45)
  print('GET ITEM')
  print('+=' * 45)
  print('')
  if rooms[player.location][ITEMS] == []:
    print('In deze kamer bevinden zich geen items')
    print('typ b(back) om terug te gaan')
    print('')
    print('+=' * 45)
    option = input('> ')
    if option.lower() == ('b'):
      print_location()
    elif option.lower() == ('back'):
      print_location()
    else:
      print('vul aub een geldig antwoord in')
      time.sleep(1)
      get_menu()
  else:
    print('In deze kamer liggen deze items:')
    for x in rooms[player.location][ITEMS]:
      print ('-=- ' + x)
    print('')
    print('+=' * 45)
    print('typ de naam van het item dat je wilt oppakken, typ i(inventory) om je inventory te tonen \nof typ b(back) om terug te gaan')
    get_options()

### DROP ITEM ###
def drop_item():
  os.system('clear')
  print('+=' * 45)
  print('DROP ITEM')
  print('+=' * 45)
  print('')
  if player.inventory == []:
    print('Je hebt geen items in je inventory')
    print('typ b(back) om terug te gaan')
    print('')
    print('+=' * 45)
    option = input('> ')
    if option.lower() == ('b'):
      print_location()
    elif option.lower() == ('back'):
      print_location()
    else:
      print('vul aub een geldig antwoord in')
      drop_item()
  else:
    print('Je hebt deze items:')
    for x in player.inventory:
      print ('-=- ' + x)
    print('')
    print('+=' * 45)
    print('typ de naam van het item dat je wilt laten vallen, of typ b(back) om terug te gaan')
    drop_options()

### INVENTORY ###
def inventory():
  os.system('clear')
  print('+=' * 45)
  print('INVENTORY')
  print('+=' * 45)
  print('')
  if player.inventory == []:
    print ('Je inventory is nog leeg, ga naar een kamer en typ g(get) om een item op te pakken')
    print ('typ b(back) om terug te gaan')
    print('')
    print('+=' * 45)
    option = input("> ")
    if option.lower() == ('b'):
      print_location()
    elif option.lower() == ('back'):
      print_location()
    else:
      print('vul aub een geldig antwoord in')
      inventory()
  else:
    print('Je hebt de volgende items bij je:')
    for x in player.inventory:
      print ('-=- ' + x)
    print('')
    print('Wat wil je doen')
    print('')
    print('+=' * 45)
    print('typ: d(drop item), b(back)')
    inventory_options()

def start_game():
  os.system('clear')
  print('############################################################')
  print('#                   -=- Text adventure -=-                 #')
  print('#     -=- Het avontuur van het gouden wiskundeboek -=-     #')
  print('############################################################')
  print('#                                                          #')
  print('# -=- Wat is uw naam?                                      #')
  print('#                                                          #')
  print('############################################################')
  print('#         -=- gemaakt door Brendan en Martijn -=-          #')
  print('############################################################')
  player_name = input("> ")
  player.name = player_name

  format_string = "Hallo %s, leuk dat je dit spel speelt!"
  print(format_string % player.name)

### loading game ###
  print("\nLoading:")
  animation = ["10% [■□□□□□□□□□]","20% [■■□□□□□□□□]", "30% [■■■□□□□□□□]", "40% [■■■■□□□□□□]", "50% [■■■■■□□□□□]", "60% [■■■■■■□□□□]", "70% [■■■■■■■□□□]", "80% [■■■■■■■■□□]", "90% [■■■■■■■■■□]", "100%[■■■■■■■■■■]"]

  for x in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[x % len(animation)])
    sys.stdout.flush()

  print_location()

benodigdheden = rooms[player.location][REQUIRED]

### print location ###
def print_location():
  os.system('clear')
  print('+=' * 55)
  print(player.location.upper())

  if rooms[player.location][REQUIRED] == (''):
    opties1()
  elif rooms[player.location][REQUIRED] in player.inventory:
    opties1()
  else:
    print('\nJe hebt nog niet de benodigde items om verder te gaan')
    print('je hebt nodig: ' + rooms[player.location][REQUIRED])
    print('\nGa terug naar de hal om het juiste item te vinden')
    print('')
    print('+=' * 55)
    time.sleep(5)
    player.location = 'hal'
    print_location()
    
def opties1():
  if rooms[player.location][VISITED] == ('ja'):
    print('\n' + rooms[player.location][DESCRIPTION])
  elif player.animations == 'lang':
    for x in ('\n' + rooms[player.location][DESCRIPTION] + '\n'):
      sleep(0.03)
      print(x, end='', flush=True)
  else:
    print('\n' + rooms[player.location][DESCRIPTION])
  

  if rooms[player.location][DEATH] == ('ja'):
    print('\n' + '+=' * 55)
    print('Game over')
    time.sleep(10) 
    death_menu()
  elif rooms[player.location][WIN] == ('ja'):
    print('\n' + '+=' * 55)
    time.sleep(10)
    win_menu()
  else:
    if rooms[player.location][ITEMS] == []:
      if rooms[player.location][VISITED] == ('ja'):
        print('\n' + rooms[player.location][DIRECTIONS] + '\n')
      elif player.animations == 'lang':
        for x in ('\n' + rooms[player.location][DIRECTIONS] + '\n \n'):
          sleep(0.03) 
          print(x, end='', flush=True)
      else:
        print('\n' + rooms[player.location][DIRECTIONS] + '\n')
      
    else:
      if rooms[player.location][VISITED] == ('ja'):
        print('\nOp deze locatie zijn de volgende items te vinden: ') 
        for x in rooms[player.location][ITEMS]:
          print ('-=- ' + x)
        print('\n' + rooms[player.location][DIRECTIONS] + '\n')
      elif player.animations == 'lang':
        for x in ('\nOp deze locatie zijn de volgende items te vinden: '):
          sleep(0.03) 
          print(x, end='', flush=True)
        for y in (rooms[player.location][ITEMS]):
          print ('\n-=- ' + y)
        for x in ('\n' + rooms[player.location][DIRECTIONS] + '\n \n'):
          sleep(0.03) 
          print(x, end='', flush=True)
          
      else:
        print('\nOp deze locatie zijn de volgende items te vinden: ') 
        for x in rooms[player.location][ITEMS]:
          print ('-=- ' + x)
        print('\n' + rooms[player.location][DIRECTIONS] + '\n')
        
    print('+=' * 55)
    options()

### OPTIONS ###
def options():
  rooms[player.location][VISITED] = 'ja'
  print('Mogelijke acties: ')
  print('- a, b, c, d, g(get item), i(inventory), h(help), s(settings) en q(quit) ')
  print('\nWat wil je doen?')
  option = input('> ')
  if option.lower() == ('quit'):
    game_stop_menu()
  elif option.lower() == ('q'):
    game_stop_menu()
  elif option.lower() == ('help'):
    game_help_menu()
  elif option.lower() == ('h'):
    game_help_menu()
  elif option.lower() == ('settigns'):
    game_settings_menu()
  elif option.lower() == ('s'):
    game_settings_menu()
  elif option.lower() == ('inventory'):
    inventory()
  elif option.lower() == ('i'):
    inventory()
  elif option.lower() == ('get'):
    get_menu()
  elif option.lower() == ('g'):
    get_menu()
  elif option.lower() == 'a':
    move_dest = rooms[player.location][A]
    move_player(move_dest)
  elif option.lower() == 'b':
    move_dest = rooms[player.location][B]
    move_player(move_dest)
  elif option.lower() == 'c':
    move_dest = rooms[player.location][C]
    move_player(move_dest)
  elif option.lower() == 'd':
    move_dest = rooms[player.location][D]
    move_player(move_dest)
  else:
    print('\nvul aub een geldig antwoord in')
    options()

def move_player(move_dest):
	player.location = move_dest
	print_location()
    


title_screen()

### NOG DOEN! ###

# ITEMS
# - als je in een item nodig kamer item niet oppakt kun je dat item niet meer krijgen
# - items in kamer als je dood gaat zijn weg # misschien droppen in de kamer waar je dood bent gegaan of in de hal --> mijn voorkeur is hal

# EXTRA
# - zinuitlijning tekst verbeteren !
# - aangepaste tijd voordat deathmenu getoont wordt !
# - rooms in aparte file ?
# - code naar VAA + geboortejaar ?

# WAT DOEN WE?
# - items uit inventory halen als gebruikt --> kamer niet meer in dus als daar items zijn ben je die kwijt, maar item is wel gebruikt
# - gaan we de rooms in een aparte file doen, ik weet hoe het werkt, maar de code moet dan helemaal worden aangepast
# - doen we het einde met rooms of toch gewoon programmeren --> programmeren is makkelijker, maar het neemt wel veel meer regels in beslag
# - 