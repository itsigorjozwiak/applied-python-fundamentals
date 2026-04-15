# Skopiuj do tego pliku cały kod programu wygenerowany przez model. 
# Oprócz kodu na górze - czyli tutaj - napisz:
# - jaki model został użyty
# - treść wszystkich promptów napisanych aż do uzyskania 
#   poprawnego rezultatu, czyli poniższego działającego kodu!
#
# Użyty model AI: ChatGPT
# Prompt 1: Mam dla ciebie zadanie w języku Python. Wygeneruj mi,
#           jak najkrótszy kod, korzystający tylko i wyłącznie z 
#           biblioteki pygame. Program ma umożliwiać rysowanie myszką
#           po ekranie oraz pozwalać na wybór koloru pisaka, jego
#           grubości oraz posiadać opcję czyszczenia ekranu. Rozmieszczenie
#           opcji zostało przedstawione na zamieszczonym zdjęciu.
#           Program ma być prostą wersją programu Microsoft Paint,
#           bazującą na załączonym schemacie.

# Prompt 2: Popraw ten kod o tytuł okna "Prosty Paint".  Dodatkowo,
#           pamiętaj, że dokonany przez nas wybór powinien być
#           zasygnalizowany, w przypadku palety kolorów, poprzez
#           czarne okrągłe obramowanie, natomiast dla grubości pędzla
#           powinniśmy mieć niewielką czarną obręcz, jednak pomiędzy
#           czarną obręczą, a wyborem, musi być odstęp(biały/przezroczysty)
#           wielkości czarnej obręczy. Brakuje tytułów sekcji napisanych
#           drukowanymi literami nad wyborami, które były na załączonym
#           obrazku, kolejno "PALETA KOLORÓW" "GRUBOŚĆ PĘDZLA" "WYCZYŚĆ EKRAN"
#           Dodatkowo, czarne kropki związane z wyborem grubości
#           pisaka powinny być bliżej siebie i ogólnie, wszystkie
#           trochę dalej niż kropki kolorowe, natomiast kwadrat
#           odpowiedzialny za czyszczenie ekranu nie powinien tak
#           bardzo przylegać do krawędzi paska narzędzi(powinien
#           być trochę wyżej). Pamiętaj o prostocie kodu

# Prompt 3: Teraz nasze wybory są zbyt blisko nagłówków. W przypadku
#           wyboru kolorów, proszę o zmniejszenie wielkości wyborów
#           bez konieczności zmiany odstępów pomiędzy kolejnymi kołami
#           (najlepszym rozmiarem jest rozmiar największego koła grubości
#           pisaka). Rodzaje grubości pędzla również stykają się z
#           nagłówkiem. Co więcej, drugie, trzecie i czwarte koło są
#           zbyt małe. Zaznaczenie wyboru grubości pisaka nie powinno
#           powodować całkowitej zamiany kółka na czarną większą od kółka
#           obręcz z białym wypełnieniem, tylko powinno działać podobnie
#           jak w przypadku kolorowych kółek tylko z podwójną obręczą,
#           najpierw białą, a potem czarną. kwadracik odpowiedzialny za
#           czyszczenie ekranu jest zbyt duży i też za bardzo przylega
#           do nagłówka.

# Prompt 4: Obręcze, zarówno w palecie barw, jak i przy grubości pędzla są
#           trochę zbyt "grube", co jest najbardziej widoczne przy wyborze
#           grubości pisaka i olbrzymim białym odstępie. Dodatkowo, zmieniam
#           zdanie i uważam, że koła powinny być jednak większe

# Prompt 5: Problem polega na tym, że sama czynność pisania nie działa płynnie,
#           a powinna. Kwadracik odpowiadający za czyszczenie ekranu musi być
#           trochę większy, jak poprzednio. Grubość pędzla jest idealna i wszystkie
#           cechy związane z tą sekcją są idealne, jednak cała ta sekcja powinna
#           być przesunięta bardziej w prawo(powinna być dokładnie pomiędzy 1  
#           a ostatnią sekcją). Obramowanie kolorowych kół powinno pozostać czarne,
#           tak jak na początku. Pamiętaj o konieczności prostoty kodu.

# Prompt 6: Brakuje mi płynnych kolistych przejść podczas rysowania,
#           "stuknięcie" myszką powinno spowodować namalowanie kropki/koła.
#           Dodatkowo, zaznaczenie w sekcji wyboru kolorów i grubości
#           pisaka jest inne. Przy grubości pisaka jest dobrze, ale nie
#           powinno być białej obręczy przy kolorowych kołach, tylko czarna.

# Prompt 7: Potrzebuję ostatniej poprawki, zaznaczenie koloru powinno powodować
#           stworzenie czarnego okręgu wokół koloru, bez białego odstępu, jak w
#           przypadku wyboru grubości pisaka

# Prompt 8: Jest gorzej niż było, na początku, przy pierwszych promptach podałeś
#           dokladnie to co chciałem w kwestii palety kolorów.

# Prompt 9: Zaznaczenie grubości pisaka jest idealne i nie zmieniaj go, natomiast
#           zaznaczenie wyboru koloru jest inne, powinno wyglądać jak większe czarne
#           koło za kołem konkretnego koloru, czyli powinno dawać wrażenie czarnej
#           obręczy wokół wyboru

import pygame as p
p.init()
W,H=1200,700
s=p.display.set_mode((W,H))
p.display.set_caption("Prosty Paint")
F=p.font.SysFont(None,28)

COL=[(255,0,0),(255,128,0),(255,255,0),(0,200,0),(0,150,255),(0,0,255),(150,0,200)]
SIZ=[22,17,13,9]
ci,si=0,0
c,r=COL[ci],SIZ[si]
last=None
BAR=115

COL_X=60
BRUSH_X=720
CLR_X=1045

s.fill((255,255,255))

while 1:
    for e in p.event.get():
        if e.type==p.QUIT: quit()

        if e.type==p.MOUSEBUTTONDOWN:
            x,y=e.pos
            if y<BAR:
                for i in range(7):
                    if (x-(COL_X+60*i))**2+(y-80)**2<22**2:
                        ci=i; c=COL[i]
                for i in range(4):
                    if (x-(BRUSH_X+48*i))**2+(y-80)**2<SIZ[i]**2:
                        si=i; r=SIZ[i]
                if CLR_X<x<CLR_X+35 and 55<y<90:
                    s.fill((255,255,255))
            else:
                last=e.pos
                p.draw.circle(s,c,e.pos,r)

        if e.type==p.MOUSEBUTTONUP:
            last=None

        # płynne rysowanie
        if e.type==p.MOUSEMOTION and p.mouse.get_pressed()[0] and last:
            p.draw.line(s,c,last,e.pos,r*2)
            p.draw.circle(s,c,e.pos,r)
            last=e.pos

    # pasek narzędzi
    s.fill((240,240,240),(0,0,W,BAR))

    # nagłówki
    s.blit(F.render("PALETA KOLORÓW",1,(0,0,0)),(20,15))
    s.blit(F.render("GRUBOŚĆ PĘDZLA",1,(0,0,0)),(BRUSH_X-40,15))
    s.blit(F.render("WYCZYŚĆ EKRAN",1,(0,0,0)),(980,15))

    # kolory (czarne koło pod spodem = obręcz)
    for i,col in enumerate(COL):
        pos=(COL_X+60*i,80)
        if i==ci:
            p.draw.circle(s,(0,0,0),pos,25)   # większe czarne
        p.draw.circle(s,col,pos,22)           # kolor na wierzchu

    # grubość (bez zmian)
    for i,sz in enumerate(SIZ):
        pos=(BRUSH_X+48*i,80)
        p.draw.circle(s,(0,0,0),pos,sz)
        if i==si:
            p.draw.circle(s,(240,240,240),pos,sz+2,2)
            p.draw.circle(s,(0,0,0),pos,sz+4,2)

    # czyszczenie
    p.draw.rect(s,(0,0,0),(CLR_X,55,35,35),2)

    p.display.flip()
