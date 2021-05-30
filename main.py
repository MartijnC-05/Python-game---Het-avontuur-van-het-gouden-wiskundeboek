import sys
import os
import time
from time import sleep

### PLAYER ###
class player:
    def __init__(self):
        self.name = ''
        self.health = 1 
        self.location = 'Schoolplein'
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
  'Schoolplein': {
    LOCATION : "op het Schoolplein",
    DESCRIPTION: 'Daar sta je dan, het oude, verlaten gebouw wat ooit het Sint-Maartenscollege was. \nJe kijkt nog even naar de brief. Je moet toch echt hier zijn, het staat er, \nhandgeschreven door ene Jopie hemzelf. “Het gouden wiskundeboek ligt verborgen \nin de ruïnes van het Maartens.” ‘Waarom doe ik dit?’ vraag je jezelf af, \nmaar het is te laat om terug te gaan.',
    ITEMS : "zijn geen items te vinden",
    DIRECTIONS : "Je kunt: \nA. Door de fietsenstalling de school in \nB. Via de achteringang de school in \nC. of naar KJ, wat sinds de grote bruggeroorlogen van ‘21 niet meer hetzelfde is.",
    DEATH : 'nee',
    WIN : 'nee',
    A : 'fietsenstalling',
    B : 'achteringang',
    C : 'KJ plein'
  },

  'fietsenstalling' : {
    LOCATION : "bij de fietsenstalling",
    DESCRIPTION : "Je loopt de trap op om de fietsenstalling binnen te gaan. Je vestigt je aandacht op \neen eenzame roze fiets, maar wordt door iemand anders aangesproken... \n‘Mensen? Hier?’ denk je, maar je wordt uit je gedachten getrokken door de persoon. \n‘Wat zoek je hier?’ Vraagt hij. Je kijkt naar zijn naambordje, \nhet is Andy, een van de conciërges.",  
    ITEMS : "zijn geen items te vinden",
    DIRECTIONS : "Wat zeg je tegen Andy? \nA: ‘Wat doe JIJ hier?’ \nB: ‘Ik kom mijn fiets ophalen, die roze daar.’ \nC: ‘Ene Jopie heeft me gestuurd.’",
    DEATH : 'nee',
    WIN : 'nee',
  },

  'achteringang' : {
    LOCATION : "bij de achteringang",
    DESCRIPTION : "Je loopt langs het gebouw en gaat het achterplein op. Er zitten alleen \n2 mensen heel dichtbij elkaar op een bankje. ‘Nou ja, moet kunnen toch?’ \ndenk je. Lichtelijk walgend loop je naar de deur toe. ‘Huh? Niet op slot? Apart.’ \nDenk je, maar je loopt snel naar binnen.",
    ITEMS : "zijn geen items te vinden",
    DIRECTIONS: "Je kunt: \nA: alleen maar naar de hal",
    DEATH : 'nee',
    WIN : 'nee',
  },

  'KJ plein' : {
    LOCATION : "bij het KJ plein",
    DESCRIPTION : "Je draait je om om naar KJ te gaan, maar meteen betwijfel je of dat een goed idee is. \nAlleen vanaf de ruïnes kan je al zien dat het er wemelt van de bruggers, \nzij hadden de oorlog gewonnen, en sindsdien is het hun basis. \n‘Is het wel zo handig om te gaan?’ vraag je je af. Er komt een jochie op een step langs. \n‘Ik zou t niet doen vriend.’ Hij stept verder.",  
    ITEMS : "zijn geen items te vinden",
    DIRECTIONS : "Wat doe je?: \nA: ‘Ik moet niet al te veel afdwalen, ik sla KJ wel over’ \nB: ‘Hoe erg kan het zijn? Het zijn ook maar bruggers.’",
    DEATH : 'nee',
    WIN : 'nee',
  },

}


### MENU SELECTIONS ### 
def title_screen_selections(): 
  option = input("> ")
  if option.lower() == ("start"):
    start_game()
  elif option.lower() == ("help"):
    help_menu()
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

### DEATH MENU SELECTIONS ###
def death_menu_selections():
  option = input ("> ")
  if option.lower() == ("ja"):
    start_game()
  elif option.lower() == ("nee"):
    stop_menu()
  else:
    print("vul aub ja of nee in.")
    death_menu_selections()

### WIN MENU SELECTIONS ###
def win_menu_selections():
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
  print('#                  -=-=-=-o Start o-=-=-=-                 #')
  print('#                  -=-=-=-o Help  o-=-=-=-                 #')
  print('#                  -=-=-=-o Stop  o-=-=-=-                 #')
  print('#                                                          #')
  print('#                  Typ Start, Help of stop                 #')
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
  print('\n' + rooms[player.location][DESCRIPTION])
  print('\n' + 'op deze locatie ' + rooms[player.location][ITEMS])
  print('\n' + rooms[player.location][DIRECTIONS])
  print('\n Mogelijke acties: ')
  print('- d(directions), g(get item), i(inventory), h(help), q(quit) ')
  print('+=' * 45)

  if rooms[player.location][DEATH] == ('ja'):
    death_menu()
  elif rooms[player.location][WIN] == ('ja'):
    win_menu()
  else:
    options()

### OPTIONS ###
def options():
  print('Wat wil je doen?')
  option = input('> ')
  if option.lower() == ('quit'):
    stop_menu()
  elif option.lower() == ('q'):
    stop_menu()
  elif option.lower() == ('help'):
    help_menu()
  elif option.lower() == ('h'):
    help_menu()
  elif option.lower() == ('inventory'):
    print('dit wordt de inventory')
    options()
  elif option.lower() == ('i'):
    print('dit wordt de inventory')
    options()
  elif option.lower() == ('get'):
    print('dit wordt de item get function')
    options()
  elif option.lower() == ('g'):
    print('dit wordt de item get function')
    options()
  elif option.lower() == ('directions'):
    directions()
  elif option.lower() == ('d'):
    directions()
  else:
    print('vul aub een geldig antwoord in')
    options()

def directions():
  print ('Waar wil je heen gaan?')
  option = input('> ')
	
  if option.lower() == 'a':
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
    print("Vul aub alleen a, b, c of d in.")
    directions()

def move_player(move_dest):
	player.location = move_dest
	print_location()


  


title_screen()


### NOG DOEN! ###
# - alle kamers toevoegen
# - mogelijkheid om terug te gaan na tonen help/ stop menu
# - inventory tonen
# - inventory item laten vallen
# - item oppakken
# - health system




