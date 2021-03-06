import sys
import os
import time
from time import sleep
from rooms import *
from logo import *

start_time = time.time()

### PLAYER ###
class player:
    def __init__(self):
        self.name = ''
        self.health = 1 
        self.location = 'schoolplein'
        self.inventory = ['brief van jopie']
        self.animations = 'kort'
player = player()


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
    logo()
  elif option.lower() == ("nee"):
    print_location()
  else:
    print("vul aub ja of nee in.")
    game_stop_menu_selections()

### DEATH MENU SELECTIONS ###
def death_menu_selections():
  player.location = 'schoolplein'
  rooms['hal'][ITEMS] = player.inventory
  player.inventory = []
  option = input("> ")
  if option.lower() == ("ja"):
    print('\nAndy vindt een dood lichaam en brengt alle spullen terug naar de hal.')
    time.sleep(5)
    print_location()
  elif option.lower() == ("nee"):
    stop_menu()
  else:
    print("vul aub ja of nee in.")
    death_menu_selections()


### WIN MENU SELECTIONS ###
def win_menu_selections():
  player.location='schoolplein'
  player.inventory = []
  rooms['Ik kom mijn fiets ophalen, die roze daar'][ITEMS] = ['fiets']
  rooms['kantine'][ITEMS] = ["hendeltje", "wafel"]
  rooms['hier heb je de hendel'][ITEMS] = ['legoblokje']
  rooms['ga naar het gestamp'][ITEMS] = ['briefje met code']
  rooms['zilveren boek'][ITEMS] = ['zilveren boek']
  rooms['gouden boek'][ITEMS] = ['gouden wiskundeboek']
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
  print('# -=- Typ s(settings) om animaties lang of                 #')
  print('#        kort af te spelen                                 #')
  print('#                                                          #')
  print('# -=- Veel plezier met het spelen!                         #')
  print('#                                                          #')
  print('#        Typ b(back) om terug naar het menu te gaan        #')
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
  print('# -=- Typ s(settings) om animaties lang of                 #')
  print('#        kort af te spelen                                 #')
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
  e = int(time.time() - start_time)
  os.system('clear')
  print('############################################################')
  print('#                    -=- Gewonnen! -=-                     #')
  print('############################################################')
  print('#                                                          #')
  print('# -=- Gefeliciteerd je hebt gewonnen!                      #')
  print('#                                                          #')
  print('# -=- Duur van jouw avontuur:                              #')
  print('#     {:02d}:{:02d}:{:02d}'.format(e // 3600, (e % 3600 // 60), e % 60) + '                                             #')
  print('#                                                          #')
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

# ONTSNAPPING #
def ontsnapping():
  os.system('clear')
  print('+=' * 55)
  print('ONTSNAPPING')
  print('+=' * 55)
  print("\nJe rent snel via de trap naar beneden, maar als je naar buiten wilt rennen komt de rector om de hoek lopen.") 
  if 'zilveren boek' in player.inventory:
    print("\nDe rector probeert zich nog voor te stellen. Je hoort alleen maar ???...Ajolt...??? \nen ???Ik hou van stroopwafels.??? Maar je rent ontzettend snel langs hem. Je nadert de uitgang, \nmaar plotseling komt er een groepje mensen gewapend met baguettes en berets om de hoek kijken. \n???Prenez son noix!??? Zegt een van hen. Ze komen op je afgerend en steken je neer met hun baguettes. \nHet is een zeer onprettige, arelaxende ervaring. ")
    print('')
    print('+=' * 55)
    print('game over, druk op enter om door te gaan')
    ontsnapping_death()

  elif 'gouden wiskundeboek' in player.inventory:
    print("\nDe rector probeert zich nog voor te stellen. Je hoort alleen maar ???...Ajolt...??? en ???Ik hou van stroopwafels.??? \nMaar je rent ontzettend snel langs hem. Je nadert de uitgang, maar plotseling staat Jopie in de weg. \n???Dus jij denkt dat je snel weg kan komen?! Nou nou zeg, je lijkt echt op David. \nWat ben ik toch ont-zet-tend blij met jou. Helaas stopt het hier echt, \nhierna ga ik denk ik wel genieten van mijn pensioen op een mooi strand, al hou ik helemaal niet van het strand.??? \nJopie maakt zijn verhaal af, maar je was al langs hem gerend. Je rent door de fietsenstalling, \nzegt Andy even gedag en rent weg naar de horizon, met het gouden wiskundeboek onder je arm.")
    print('')
    print('+=' * 55)
    print("druk op enter om verder te gaan")
    option = input()
    if option.lower() == (''):
      credits()
    else:
      print('vul aub een geldig antwoord in')
      time.sleep(1)
      ontsnapping()

  else:
    print('Je bent flink aan het rennen, maar ineens herriner je je dat je geen boek hebt gepakt. Terwijl je stil staat om je zonden te overdenken, ruikt het ineens naar wafel achter je. \nJe draait je om, en ziet dat Marcel je toch heeft ingehaald. Hij gooit je terug naar de hal.')
    print('')
    print('+=' * 55)
    print('druk op enter om verder te gaan')
    option = input()
    if option == (''):
      player.location = 'hal'
      print_location()
    else:
      print('vul aub een geldig antwoord in')
      ontsnapping()

# ontsnappings opties
def ontsnapping_win():
  option = input()
  if option.lower() == (""):
    win_menu()    
  else:
    print('vul aub een geldig antwoord in')
    ontsnapping_win()

def ontsnapping_death():
  option = input()
  if option.lower() == (""):
    death_menu()
  else:
    print('vul aub een geldig antwoord in')
    ontsnapping_death()

def credits():
  os.system('clear')
  time.sleep(0.5)
  print('############################################################')
  time.sleep(0.5)
  print('#                   -=- Text adventure -=-                 #')
  time.sleep(0.5)
  print('#     -=- Het avontuur van het gouden wiskundeboek -=-     #')
  time.sleep(0.5)
  print('############################################################')
  time.sleep(0.5)
  print('#                                                          #')
  time.sleep(0.5)
  print('# CREDITS                                                  #')
  time.sleep(0.5)
  print('#                                                          #')
  time.sleep(2)
  print('# -=- Verhaal naar idee van Brendan Darwinkel              #')
  time.sleep(2)
  print('# -=- Programmeren in python:                              #')
  print('#     Martijn met behulp van Brendan                       #')
  time.sleep(0.5)
  print('#                                                          #')
  time.sleep(2)
  print('#                                                          #')
  time.sleep(2)
  print('# ROLLEN                                                   #')
  time.sleep(0.5)
  print('#                                                          #')
  time.sleep(2)
  print('# -=- Jopie                      Joop van der Vaart        #')
  time.sleep(2)
  print('# -=- Conci??rge Andy             Andy Ganpat               #')
  time.sleep(2)
  print('# -=- Twee mensen op bankje      Brendan Darwinkel en      #')
  print('#                                Sannah Kuip               #')
  time.sleep(2)
  print('# -=- Bruggeraanvoerder          Vivian Speijer            #')
  time.sleep(2)
  print('# -=- Man in lokaal 126          Tim Logtenberg            #')
  time.sleep(2)
  print('# -=- Print mevrouw              Sandra Rossel             #')
  time.sleep(2)
  print('# -=- Ome Henk                   Ome Henk                  #')
  time.sleep(2)
  print('# -=- Ome Willem                 Martijn Carton            #')
  time.sleep(2)
  print('# -=- De mannen NT en G          Michel van der Mark en    #')
  print('#                                Stef Huizer               #')
  time.sleep(2)
  print('# -=- Gek met honkbalknuppel     Thijs de Jong             #')
  time.sleep(2)
  print('# -=- Over god pratende mensen   Vincent Rink en           #')
  print('#                                Marlijn Passchier-Storm   #')
  time.sleep(2)
  print('# -=- Hypnotiserende Man         Davy Stam                 #')
  time.sleep(2)
  print('# -=- Oom Mark                   Mark van Breda Vriesman   #')
  time.sleep(2)
  print('# -=- Man zonder beenhaar        Vincent Deegens           #')
  time.sleep(2)
  print('# -=- Sectie Frans               Simone Bakker, Luci G??tz  #')
  print('#                                en Krijn Oorschot         #')
  time.sleep(2)
  print('# -=- Beelden kijkende vrouw     Kim Roepert               #')
  time.sleep(2)
  print('# -=- Schreeuwende Gek           Albert Huisman            #')
  time.sleep(2)
  print('# -=- Deur van lokaal 211        Markus van Rest           #')
  time.sleep(2)
  print('# -=- Hoofd tegen bord leerling  Maja Kersten              #')
  time.sleep(2)
  print('# -=- Feyenoord fan in de kelder Quinten de Kort           #')
  time.sleep(2)
  print('# -=- Marcel                     Marcel Thoen              #')
  time.sleep(2)
  print('# -=- David                      David Houtzagers          #')
  time.sleep(2)
  print('# -=- Rector                     Ajolt Elsakkers           #')
  time.sleep(0.5)
  print('#                                                          #')
  time.sleep(0.5)
  print('#                                                          #')
  time.sleep(2)
  print('# MET EXTRA VEEL DANK AAN:                                 #')
  time.sleep(2)
  print('# -=- Avonturier                ' + player.name )
  time.sleep(2)
  print('# -=- Joop van der Vaart voor het vervullen van            #')
  print('#     de hoofdrol in ons verhaal                           #')
  time.sleep(2)
  print('# -=- Tim Logtenberg voor de aanleiding om spel te maken   #')
  time.sleep(0.5)
  print('#                                                          #')
  time.sleep(2)
  print('############################################################')
  time.sleep(0.5)
  print('#   -=- Het avontuur van het gouden wiskundeboekTM is -=-  #')
  time.sleep(0.5)
  print('#  -=- geschreven, geprogrammeerd en gepubliceerd door -=- #')
  time.sleep(0.5)
  print('# -=- Cool Kids Club BV. Alle rechten voorbehouden. -=-    #')
  time.sleep(0.5)
  print('#     -=- Voor vragen, opmerkingen of complimenten -=-     #')
  time.sleep(0.5)
  print('#        -=- mail 110816@st-maartenscollege.nl -=-         #')
  time.sleep(0.5)
  print('#         -=- of 110739@st-maartenscollege.nl -=-          #')
  time.sleep(0.5)
  print('############################################################')
  time.sleep(8)
  win_menu()

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
  animation = ["10% [??????????????????????????????]","20% [??????????????????????????????]", "30% [??????????????????????????????]", "40% [??????????????????????????????]", "50% [??????????????????????????????]", "60% [??????????????????????????????]", "70% [??????????????????????????????]", "80% [??????????????????????????????]", "90% [??????????????????????????????]", "100%[??????????????????????????????]"]

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
    print('Game over, druk op enter om verder te gaan')
    option = input()
    if option.lower() == (''):
      death_menu()
    else:
      opties2()
  elif rooms[player.location][WIN] == ('ja'):
    print('\n' + '+=' * 55)
    print('druk op enter om verder te gaan')
    option = input()
    if option.lower() == (''):
      ontsnapping()
    else:
      print('vul aub een geldig antwoord in')
      opties1()
      
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