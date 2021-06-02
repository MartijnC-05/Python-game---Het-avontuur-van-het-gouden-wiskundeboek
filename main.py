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
        self.inventory = ['']
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

rooms = {
  #level 1
  'schoolplein': {
    DESCRIPTION: 'Daar sta je dan, het oude, verlaten gebouw wat ooit het Sint-Maartenscollege was. \nJe kijkt nog even naar de brief. Je moet toch echt hier zijn, het staat er, \nhandgeschreven door ene Jopie hemzelf. “Het gouden wiskundeboek ligt verborgen \nin de ruïnes van het Maartens.” ‘Waarom doe ik dit?’ vraag je jezelf af, \nmaar het is te laat om terug te gaan.',
    ITEMS : "",
    DIRECTIONS : "Je kunt: \nA. Door de fietsenstalling de school in \nB. Via de achteringang de school in \nC. of naar KJ, wat sinds de grote bruggeroorlogen van ‘21 niet meer hetzelfde is.",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'fietsenstalling',
    B : 'achteringang',
    C : 'KJ plein',
    D : 'schoolplein'
  },

  'fietsenstalling' : {
    DESCRIPTION : "Je loopt de trap op om de fietsenstalling binnen te gaan. Je vestigt je aandacht op \neen eenzame roze fiets, maar wordt door iemand anders aangesproken... \n‘Mensen? Hier?’ denk je, maar je wordt uit je gedachten getrokken door de persoon. \n‘Wat zoek je hier?’ Vraagt hij. Je kijkt naar zijn naambordje, \nhet is Andy, een van de conciërges.",  
    ITEMS : "",
    DIRECTIONS : "Wat zeg je tegen Andy? \nA: ‘Wat doe JIJ hier?’ \nB: ‘Ik kom mijn fiets ophalen, die roze daar.’ \nC: ‘Ene Jopie heeft me gestuurd.’",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'Wat doe JIJ hier?',
    B : 'Ik kom mijn fiets ophalen, die roze daar',
    C : 'Ene Jopie heeft me gestuurd',
    D : 'fietsenstalling'
  },

  'Wat doe JIJ hier?' : {
    DESCRIPTION : "Andy stelt deze grap niet op prijs. Hij stuurt je meteen de fietsenstalling uit. \n“En niet meer terugkomen!” Schreeuwt hij je nog na. Nou, daar gaan je kansen om binnen te komen.",  
    ITEMS : "",
    DIRECTIONS : "",
    DEATH : 'ja',
    WIN : 'nee',
  },

  'Ik kom mijn fiets ophalen, die roze daar' : {
    DESCRIPTION : "“Eindelijk, de eigenaar!” Het lijkt haast alsof Andy blij is dat die fiets eindelijk wordt opgehaald. \nHij haalt de sleutels uit zijn broekzak en overhandigt ze aan je. \nHet is misschien niet echt jouw fiets, maar hij is zo blij, dat ga je toch niet verpesten? ",  
    ITEMS : "fiets",
    DIRECTIONS : "Je kunt: \nA: alleen maar naar de hal",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'hal',
    B : 'Ik kom mijn fiets ophalen, die roze daar',
    C : 'Ik kom mijn fiets ophalen, die roze daar',
    D : 'Ik kom mijn fiets ophalen, die roze daar',
  },

  'Ene Jopie heeft me gestuurd': {
    DESCRIPTION : "“Die naam heb ik al in tijden niet gehoord zeg. Kom verder, snel, voordat je gesnapt wordt.” \nJe vraagt je af wie jou zal snappen, maar goed, je volgt Andy snel.",  
    ITEMS : "",
    DIRECTIONS : "Je kunt: \nA: alleen maar naar de hal",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'hal',
    B : 'Ene Jopie heeft me gestuurd',
    C : 'Ene Jopie heeft me gestuurd',
    D : 'Ene Jopie heeft me gestuurd',
  },

  'achteringang' : {
    DESCRIPTION : "Je loopt langs het gebouw en gaat het achterplein op. Er zitten alleen \n2 mensen heel dichtbij elkaar op een bankje. ‘Nou ja, moet kunnen toch?’ \ndenk je. Lichtelijk walgend loop je naar de deur toe. ‘Huh? Niet op slot? Apart.’ \nDenk je, maar je loopt snel naar binnen.",
    ITEMS : "",
    DIRECTIONS: "Je kunt: \nA: alleen maar naar de hal",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'hal',
    B : 'achteringang',
    C : 'achteringang',
    D : 'achteringang',
  },

  'KJ plein' : {
    DESCRIPTION : "Je draait je om om naar KJ te gaan, maar meteen betwijfel je of dat een goed idee is. \nAlleen vanaf de ruïnes kan je al zien dat het er wemelt van de bruggers, \nzij hadden de oorlog gewonnen, en sindsdien is het hun basis. \n‘Is het wel zo handig om te gaan?’ vraag je je af. Er komt een jochie op een step langs. \n‘Ik zou t niet doen vriend.’ Hij stept verder.",  
    ITEMS : "",
    DIRECTIONS : "Wat doe je?: \nA: ‘Ik moet niet al te veel afdwalen, ik sla KJ wel over’ \nB: ‘Hoe erg kan het zijn? Het zijn ook maar bruggers.’",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'schoolplein',
    B : 'KJ centrum',
    C : 'KJ plein',
    D : 'KJ plein',
  },

  'KJ centrum' : {
    DESCRIPTION : "Je zet 1 stap in het centrum, en wordt meteen overvallen door de bruggers. \nJe doet je best om terug te vechten, maar voor elke brugger die je neerslaat \nkomen er 3 meer uit de Albert Heijn lopen. Na een langdurige strijd overleef je het niet.",  
    ITEMS : "",
    DIRECTIONS : "",
    DEATH : 'ja',
    WIN : 'nee',
  },

  #level 2
  'hal' : {
    DESCRIPTION : "Je bent nu binnen. Je staat in de hal en kijkt om je heen, \nje slikt je angst weg en besluit waar je heen gaat: De trap op richting de eerste verdieping, \nnaar de aula, naar de vleugel NT en G, of terug naar buiten.",  
    ITEMS : "",
    DIRECTIONS : "Je kunt naar: \nA: De trap \nB: De aula \nC: De vleugel NT en G \nD: Naar buiten",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'trap',
    B : 'aula',
    C : 'vleugel NT en G',
    D : 'schoolplein',
  },

  'trap' : {
    DESCRIPTION : "Er zijn twee trappen die je kan nemen: de trap die richting lokalen gaat, \nof de trap die richting de mediatheek gaat.",  
    ITEMS : "",
    DIRECTIONS : "Welke trap neem je? \nA: Naar de lokalen \nB: Naar de mediatheek",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'lokalen',
    B : 'mediatheek',
    C : 'trap',
    D : 'trap',
  },

  'mediatheek' : {
    DESCRIPTION : "Je gaat de trap op richting de mediatheek. Je loopt nog langs lokaal 126, \nwaar een man met donkerblond haar achter een computer zit te klooien met google meet. \n‘Rare eend.’ Denk je. Je loopt door naar de mediatheek, waar je een zacht geluid \nvan een printer hoort. Het geluid wordt luider en luider, \ntotdat je de mediatheek zelf binnenloopt. Er is een enkele vrouw aanwezig, \nbezig met de printer. Ze draait zich direct om bij je eerste stap. \n‘Dus jij wilt hulp met printen?’ Vraagt ze. Je kan geen antwoord geven \nvoordat ze je al naar de printer heeft geleid. Vervolgens moet je printen \ntotdat je je laatste adem hebt gegeven.",  
    ITEMS : "",
    DIRECTIONS : "",
    DEATH : 'ja',
    WIN : 'nee',
    },  

  'aula' : {
    DESCRIPTION : "Je loopt de aula binnen. Het is helemaal leeg, behalve 2 oude mannen \ndie bingo zitten te spelen. ‘Ach ja, beetje bingo moet kunnen.’ Denk je. \nJe kan de oude mannen benaderen of naar de kantine toe.",  
    ITEMS : "",
    DIRECTIONS : "Wat ga je doen? \nA: Naar de kantine \nB: Benader de oude mannen \nC: terug naar de hal",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'kantine',
    B : 'oude mannen',
    C : 'hal',
    D : 'aula'
  },

  'kantine' : {
    DESCRIPTION : "Het is misschien een doodlopend einde, maar je kan toch een beetje rondkijken \nzonder lastig te worden gevallen. Er zijn een paar dingen die je opvallen, \nzoals een hendeltje van de kapotte panini machine, \nen een heerlijke wafel die bijna aan de datum is.",  
    ITEMS : "zijn een hendeltje en een wafel te vinden",
    DIRECTIONS : "je kunt: \nA: alleen terug naar de aula",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'aula',
    B: 'kantine',
    C : 'kantine',
    D : 'kantine',
  },

  'oude mannen' : {
    DESCRIPTION : "Je loopt naar de oude mannen toe. Op het moment dat je aan komt lopen, \nklinkt er een krak. “Alle bingoballen nog aan toe!” Roept een van de twee uit. \nJe ziet dat de hendel van het bingorad is afgebroken. Een van de twee ziet je aan komen lopen, \nen begint meteen met praten. “Zeg, makker, jij daar, kun je ons even helpen?” \nJe hebt niet echt een keuze, dus je knikt ja. “Komt dat eens goed uit zeg! \nWij zijn Ome Henk en Ome Willem, en we houden van bingo. \nZoals je kunt zien hebben we een nieuw hendeltje nodig, kan je die voor ons zoeken?” \nJe knikt weer, je kan natuurlijk geen nee zeggen tegen zulke aardige mensen.",  
    ITEMS : "",
    DIRECTIONS : "je kunt: \nA: alleen naar de aula toe",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'aula',
    B : 'oude mannen',
    C : 'oude mannen',
    D : 'oude mannen',
  },

  'vleugel NT en G': {
    DESCRIPTION : "Je loopt richting de vleugel van NT en G, maar voordat je er goed kan komen \nhoor je een explosie. Er komen 2 andere mensen uit een lokaal gerend, \ngevolgd door een derde man met een honkbalknuppel. De gewapende gek keert zich tot jou. \n‘Ga jij eens even ergens anders kletsen.’ Zegt hij, met een simpelweg enge glimlach op zijn gezicht. \nJe probeert weg te rennen, maar voordat je het weet heeft hij je knieschijven ingetimmerd. \nJe overleeft het niet. ",  
    ITEMS : "",
    DIRECTIONS : "",
    DEATH : 'ja',
    WIN : 'nee',
  },

  #level 3
  'lokalen' : {
    DESCRIPTION : "Je bent nu de trap opgegaan richting de lokalen. Je kan verder op de eerste verdieping, \nnaar de tweede verdieping of helemaal naar de derde verdieping. \nJe kan natuurlijk ook weer terug naar beneden.",  
    ITEMS : "",
    DIRECTIONS : "Je kunt naar: \nA: De eerste verdieping \nB: De tweede verdieping \nC: De derde verdieping \nD:Naar beneden",
    DEATH : 'nee',
    WIN : 'win',
    A : 'verdieping 1',
    B : 'verdieping 2',
    C : 'verdieping 3',
    D : 'hal',
  },

  'verdieping 1' : {
    DESCRIPTION : "Je staat nu op de eerste verdieping. Je ziet 2 mensen in een lokaal zitten, en in de verte hoor je gestamp. Je kan de mensen benaderen, of verder naar het gestamp kijken.",  
    ITEMS : "",
    DIRECTIONS : "Wat ga je doen?: \nA: Benader de mensen \nB: Ga naar het gestamp",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'de mensen',
    B : 'het gestamp',
    C : 'verdieping 1',
    D : 'verdieping 1',
  },

   'de mensen' : {
    DESCRIPTION : "Je nadert de deuropening, en hoort een zacht gebabbel over God, Jezus en de 		Heilige Geest, amen. Je stapt het lokaal in, en de vrouw kijkt direct jouw kant op. 		'Verdwijn, brugger! U bent hier niet welkom!'' Ze duwt een kruis in je gezicht. 'De 		kracht van God houdt u tegen!'' Je wordt teruggebracht naar de hal.",  
    ITEMS : "",
    DIRECTIONS : "",
    DEATH : '',
    WIN : '',
    A : '',
    B : '',
    C : '',
    D : '',
  },

  '' : {
    DESCRIPTION : "",  
    ITEMS : "",
    DIRECTIONS : "",
    DEATH : '',
    WIN : '',
    A : '',
    B : '',
    C : '',
    D : '',
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
  player.location='schoolplein'
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
  option = input ("> ")
  if option.lower() == ("ja"):
    title_screen()
  elif option.lower() == ("nee"):
    stop_menu()
  else:
    print("vul aub ja of nee in.")
    win_menu_selections

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


### print location ###
def print_location():
  os.system('clear')
  print('+=' * 45)
  print(player.location.upper())

  if player.animations == 'lang':
    for x in ('\n' + rooms[player.location][DESCRIPTION] + '\n'):
      sleep(0.03)
      print(x, end='', flush=True)
  else:
    print('\n' + rooms[player.location][DESCRIPTION])
  

  if rooms[player.location][DEATH] == ('ja'):
    print('\n' + '+=' * 45)
    print('Game over')
    time.sleep(10)
    death_menu()
  elif rooms[player.location][WIN] == ('ja'):
    print('\n' + '+=' * 45)
    time.sleep(10)
    win_menu()
  else:
    if rooms[player.location][ITEMS] == (''):
      if player.animations == 'lang':
        for x in ('\n' + rooms[player.location][DIRECTIONS] + '\n \n'):
          sleep(0.03) 
          print(x, end='', flush=True)
      else:
        print('\n' + rooms[player.location][DIRECTIONS] + '\n')
      
    else:
      if player.animations == 'lang':
        for x in ('\nOp deze locatie zijn de volgende items te vinden: \n' + rooms[player.location][ITEMS] + '\n'):
          sleep(0.03) 
          print(x, end='', flush=True)
        for x in ('\n' + rooms[player.location][DIRECTIONS] + '\n \n'):
          sleep(0.03) 
          print(x, end='', flush=True)
      else:
        print('Op deze locatie zijn de volgende items te vinden: \n' + rooms[player.location][ITEMS])
        print('\n' + rooms[player.location][DIRECTIONS] + '\n')
        
    print('+=' * 45)
    options()

### GET OPTION ###
def get_menu():
  os.system('clear')
  print('+=' * 45)
  print('In deze kamer liggen deze items:')
  print('-=-' + rooms[player.location][ITEMS])
  print('\nWil je dit item oppakken?')
  print('+=' * 45)
  print('typ: y(yes), n(no), of b(back)')
  get_options()

def get_options():
  option = input('> ')
  if option.lower() == ('y'):
    rooms[player.location][ITEMS].remove(ITEMS)
    player.inventory.append(ITEMS)
  elif option.lower() == ('n'):
    print_location()
  elif option.lower() == ('b'):
    print_location()
  else:
    print('vul aub een geldig antwoord in')
    get_options()


def drop_item():
  os.system('clear')
  print('+=' * 45)
  print('Je hebt deze items:')
  print('-=-' + player.inventory)
  print('\nWelk item wil je laten vallen?')
  print('+=' * 45)
  print('typ de naam van het item dat je wilt laten vallen, of typ b(back) om terug te gaan')
  drop_options()

def drop_options():
  option = input('> ')
  if option.lower() == (''):
    player.inventory.remove()
    rooms[player.location][ITEMS].append()
  elif option.lower() == ('b'):
    print_location()
  else:
    print('vul aub een geldig antwoord in')
    drop_options()

def inventory():
  os.system('clear')
  print('+=' * 45)
  print('Je hebt de volgende items bij je:')
  print(player.inventory)
  print('\nWat wil je doen')
  print('+=' * 45)
  print('typ: d(drop item), b(back)')
  inventory_options()

def inventory_options():
  option = input('> ')
  if option.lower() == ('d'):
    drop_item()
  elif option.lower() == ('b'):
    print_location()
  else:
    print('vul aub een geldig antwoord in')
    inventory_options()


### OPTIONS ###
def options():
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
    print('dit wordt de inventory')
    options()
  elif option.lower() == ('i'):
    print('dit wordt de inventory')
    options()
  elif option.lower() == ('get'):
    print('dit wordt de item get function')
    get_menu()
  elif option.lower() == ('g'):
    print('dit wordt de item get function')
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
    print('vul aub een geldig antwoord in')
    options()

def move_player(move_dest):
	player.location = move_dest
	print_location()



title_screen()


### NOG DOEN! ###
# - alle kamers toevoegen
# - inventory tonen
# - inventory item laten vallen
# - items toevoegen
# - item oppakken
# - item nodig om verder te komen
# - health system???
# - als optie wel in abcd zit maar niet mogelijk is komt er een error