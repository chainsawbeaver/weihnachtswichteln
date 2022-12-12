#!/usr/bin/python3

import copy
import random
import base64
import uuid

wichtler_liste = ["A", "B", "C", "D", "E", "F", "G"]

forbidden = [
             ("A", "G"),
             ("B", "D"),
             ("C", "E"),
             ]
             
             
print("Wichtler:\n", wichtler_liste)
print("Verbotene Kombinationen:\n", forbidden, "\n\n\n")

part_one = """<!doctype html>

<html lang="de">
<head>
    <title>Weichnachtswichteln</title>
    <meta name="robots" content="noindex, nofollow" />
    <meta charset='utf-8' />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel='stylesheet' type='text/css' href='../style/hfstyle.css' />
    </head>

<body>

<div id='start' class='content'>
    <h1><span lang=de>Weichnachtswichteln</span></h1></div>

<div id='one' class='content'>
    <h2>Hallo """

part_three = """!</h2>
    <p>Du sollst <b>"""

part_five = """</b> bewichteln!</p>
    <p>Diese Seite ist so erstellt worden, dass nur Du weißt wen Du bewichteln sollst (auch der Autor weiß es nicht).</p>
    </div>

<div id='two' class='content'>
    <h2>Alle Teilnehmer</h2>
    <p>Wer macht alles mit:</p>
    <ul>"""

part_six = """"""
for person in wichtler_liste:
    part_six += "<li>" + person + "</li>\n"

part_seven = """</ul>
    <h3>Verbotene Kombinationen waren:</h3>
    <p>(Können sich also gegenseitig nicht ziehen)</p>
    <ul>
    """

for kombi in forbidden:
    part_seven += f"<li> {kombi[0]} ⇋ {kombi[1]} </li>\n"

part_eight = """
    </ul>
    
    <p>Der Quellcode ist hier abgelegt <a href="https://github.com/chainsawbeaver/weihnachtswichteln/blob/main/wichteln_2022_public.py">github.com</a></p>
    </div>


<div id='footer'>
&bull; 2022-12-12 &bull;
</div>

</body>
</html>
"""

def function2(wichtler_liste):
    liste = copy.deepcopy(wichtler_liste)
    random.shuffle(liste)
    geheime_liste = []
    for i in range(len(liste)):
        if i == len(liste)-1:
            geheime_liste.append([liste[i],liste[0]])
            #print(liste[i], "beschenkt", liste[0])
        else:
            geheime_liste.append([liste[i],liste[i+1]])
            #print(liste[i], "beschenkt", liste[i+1])
    random.shuffle(geheime_liste)
    #print(geheime_liste)
    return(geheime_liste)


def check_forbidden(forbidden, liste):
    listeok = False
    checkliste = [0] * (len(liste))
    #print(checkliste)
    for index in range(len(liste)):
        test = tuple(liste[index])
        #print("Test", index, test, "und", test[::-1])
        if (test not in forbidden) and (test[::-1] not in forbidden):
            checkliste[index] = 1
    print(checkliste)
    if 0 not in checkliste:
        listeok = True
    return listeok

def encode_liste(liste):
    for i in liste:
        i[1] = base64.b85encode(i[1].encode()).decode()
        print(i)
    return liste

def decode_liste(liste):
    for i in liste:
        i[1] = base64.b85decode(i[1]).decode()
        #print(i)
    return liste

def make_html(liste):
    for i in liste:
        html = part_one + i[0] + part_three + i[1] + part_five + part_six + part_seven + part_eight
        with open(i[0]+"-"+str(uuid.uuid4())+".html", "w", encoding="utf-8") as save_file:
            save_file.write(html)

try_ = 0
while True:
    try_ += 1
    print("Versuch Nummer", try_)
    geheime_liste = function2(wichtler_liste)

    if check_forbidden(forbidden, geheime_liste):
        break
    
#encode_liste(geheime_liste)
#decode_liste(geheime_liste)

make_html(geheime_liste)

if __name__ == "__main__":
    print("Press Enter to continue ...")
    input()
