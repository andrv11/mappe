from sys import exit
from random import randint
from o45 import Scene, Engine, Dead
                
class Roma(Scene): #første scene som blir utspilt

    def enter(self):
        print "Du er kommet til Rome for å kjempe mot de store"
        print "gladiatorene, du har blitt utfordret av Goliat"
        print "Hvis du klarer å bekjempe mot alle de onde"
        print "vil du få prinsessen av Roma"
        print "\n"
        print "Du er spent, du gruer deg"
        print "Du vet du er svakere og midre enn dem"
        print "Men du må klare det"
        print "Du må være smart"
                


        action = raw_input("> ") #Her kan du velge angrep mot gladiatorene"

        if action == "spark": #død
            print "Du står i ringen mot Goliat"
            print "Du venter til det rette øyeblikk"
            print "Før du skal utføre dit angrep"
            print "Men da du skal utføre angrepet faller du"
            print "Du blir liggene på bakken, og Goliat kommer"
            print "Du har ingen sjanse mot han, du dør"
            return 'dead'

        elif action == "slå":#vinner
            print "Du ser på han med store øyne"
            print "Du frykter ingen, ingen kan slå deg"
            print "Goliat prøver å slå den ned, du hindrer det"
            print "Du slår hardt tilbake og treffer godt"
            print "Du slår mer, helt til du ikke orker mer"
            print "Men det holder, du klarer og overvinne Goliat"
            return 'win'

        elif action == "løp":#velger du denne kommer du videre
            print "Du kommer ut i ringen"
            print "Men er redd for å slåss"
            print "Du finner ut at dette kommer du til å tape"
            print "Så du velger å flykte, du løper bort"
            print "Men du er ikke rask nok, Goliat kommer"
            print "Og slår deg ned, du dør"
            return 'dead'

        else:
            print "Du må fullføre angrepe for å komme videre!"
            return 'Roma' #obligatorisk valg, må utføres
                        
class win(Scene):#neste kamp

    def enter(self):
        print "Du klarte det, du vant din første kamå"
        print "Men motstanden blir vanskeligere"
        print "Du trenger fortsatt å vinne fler ganger"
        print "Får å overleve"
        print "Men du er kommet videre, du innser at du kan klare det"
        print ""
        print "Her skal du velge motstander for neste kamp"
		print "Det kan være lurt å velge riktig, får du"
		print "for vanskelig motstander dør du"
        code = "%d%d" % (randint(1,3), randint(1,3)) #Du velger motstander med denne
        guess = raw_input("[keypad]> ") 
        guesses = 0 #

        while guess != code and guesses < 5: #Du har 5 sjanser
            print "wrong!"
            guesses += 1 #teller
            guess = raw_input("[keypad]> ")

        if guess == code: #riktig
            print "Du velger en bra motstander"
            print "Dette blir krevende, men du fikk"
            print "Den letteste motstanderen"
            return 'level2'
        else: #feil
            print "Du får en alt for stor motstander"
            print "du blir nektet å starte i fare for å dø"
            print "Du kunne vært mer heldigere i trekningen"
            return 'dead'



class level2(Scene): #Neste kamp begynner

    def enter(self):
        print "Etter første kamp er ferdig går det fort videre til neste"
        print "Du har valgt en krevende motstander"
        print "Men hvis du klarer å forsvare og angripe riktig kan du klare det"
        print "Motstanderen heter Ali"
        print "Han er en av de største gladiatorene i byen"
        print "Her må du velge hvilke metoder du skal bekjeme Ali"

        action = raw_input("> ")

		    if action == "kniv":
            print "Du bestemmer deg"
            print "Du innser at motstanderen er tøffere"
            print "Etter forrige kamp var du redd"
            print "Så du stjal med en kniv inn i ringen"
            print "Du reiser den mot Ali for å trua han"
            print "Dette var ikke lurt, publikum kommer løpene for å ta deg"
			print "Våpen er ikke lov i ringen, du blir tatt"
            return 'dead '
		
				
		
        if action == "spark og forsvar":
            print "Du bestemmer deg"
            print "for å prøve å få til det første sparket"
            print "Du skal overaske han, du er tøff!"
            print "Men da du utføre sparket er Ali våken"
            print "Han tar tak i beinet og kaster deg bortover bakken"
            print "Han holder deg med jerngrep, du slipper ikke ut"
			print "Du klarer ikke rive deg løs, du taper"
            return 'dead '

        elif action == "forsvar":
            print "Du bestemmer deg"
            print "Ali er en krevende motstander"
            print "Men du tror at du kan holde ut lengre"
            print "Du bestemmer deg for å legge deg bakpå"
            print "Du forsvarer deg godt"
            print "Ali begynner å bli merktbart sliten"
            print "Han orker ikke mer"
            print "Du avslutter med et hardt spark, du klarte det!"
            return 'level3'
        else:
            print "Du må svare for å komme gjennom kampen!"
            return "level2"



    class level3(Scene): #Du vant

    def enter(self):
        print "Du har klart det, du overvant alle gladiatorene"
        print "Ingen kunne slå deg"
        print "Alle hedrer deg, du er kongen av Roma"
        print "Nå gjennstår det bare å møte prinsessen"
        

        action = raw_input("> ")

		    if action == "Hils":
            print "Du hilser på prinsessen hyggelig"
            print "Hun virker snill"
            print "Du kommer på at du ikke har vasket hendene"
            print "Du har fortsatt blod på fingrene fra kampen"
            print "Prinsessen hyler på vaktene"
            print "Dem kommer for å ta deg, du blir kastet ut"
			print "Du var uheldig, du mistet alt"
            return 'dead '
		
				
		
        if action == "Si hei":
            print "Du sier et høffelig hei til prinsessen"
            print "og presenterer deg "
            print "Du innser at du fortsatt har blod på hendene"
            print "Men velger å ikke vise det"
            print "Du tørker det bort, og ingen så det"
            print "Du har klart det, du slå gladiatorene og fikk prinsessen"
			print "Gratulerer, du vant spillet!"
            return 'finished '

        
        else:
            print "Du må svare for å komme gjennom kampen!"
            return "level3"

            return 'finished'
                        
class Map(object):#Her vises en oversikt over alle nivåene du har vært gjennom

        scenes = {
                'Roma': Roma(),
                'win': win(),
                'level1': level1(),
                'level2': level2(),
                'dead': Død()
        }
        
        def __init__(self, start_scene):
                self.start_scene = start_scene
                
        def next_scene(self, scene_name):
                return Map.scenes.get(scene_name)
                
        def opening_scene(self):
                return self.next_scene(self.start_scene)
                
a_map = Map('Roma')
a_game = Engine(a_map)
a_game.play()
