import easygui
import random

weapons=["Schwert","Zauberstab","Bogen","Buch"]

#Bilder,Waffen: bow.gif,sword.gif,staff.gif
#Bilder,Personen: archer/f.gif,magic/f.gif,warrior/f.gif
#(Bilder,Items:)

easygui.msgbox("Hallo Spieler!","Titel","Weiter","archerf.gif")
while True:
    waffe=easygui.buttonbox("Wähle eine Waffe.","Waffe wählen",weapons)
    if waffe=="Buch":
        easygui.msgbox("Option nicht verfügbar. Wie ist das bloß hier hinein geraten?",
                       "Option nicht verfügbar","Weiter","book.gif")
        continue
    else:
        break

if waffe=="Schwert":
    w_pic="sword.gif"
if waffe=="Bogen":
    w_pic="bow.gif"
if waffe=="Zauberstab":
    w_pic="staff.gif"

antwort=easygui.buttonbox("Ist das deine Wahl?",waffe,("Ja","Nein"),w_pic)
if antwort=="Nein":
    easygui.msgbox("Tja, jetzt ist es zu spät. Du wirst damit leben müssen.","Pech.","Weiter",w_pic)

if waffe=="Schwert":
    easygui.msgbox("Du hast das Schwert gewählt. Gute Wahl!","Auswahl","Weiter",w_pic)

if waffe=="Zauberstab":
    easygui.msgbox("Du hast den Zauberstab gewählt. Gute Wahl!","Auswahl","Weiter",w_pic)

if waffe=="Bogen":
    easygui.msgbox("Du hast den Bogen gewählt. Gute Wahl!","Auswahl","Weiter",w_pic)

easygui.msgbox("Das ist im Moment alles. Danke fürs spielen!","Ende","Beenden")
    
    
