import pygame
from random import randint

pygame.init()

# kolory
CZARNY = (0, 0, 0)
BIALY = (255, 255, 255)

try:
    with open("rekord.txt", "r") as f:
        rekord = int(f.read())
except:
    rekord = 0

class Rakietka(pygame.sprite.Sprite):
    # klasa Rakietka dziedziczy z klasy "Sprite" w Pygame.

    def __init__(self, color, width, height):
        # wołamy najpierw konstruktor klasy bazowej (Sprite)
        # dzięki metodzie super() dziedziczymy wszystkie elementy klasy bazowej
        super().__init__()

        # przekazanie koloru Rakietka oraz szerokości i wysokości, kolor tła i ustawienie go na przezroczyste
        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)

        # rysuję Rakietka jako prostokąt
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # pobieramy prostokąt (jego rozmiary) z obiektu image
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        # sprawdzanie położenia brzegowego
        if self.rect.x < 0:
           self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        # sprawdzanie położenia brzegowego
        if self.rect.x > 580:
           self.rect.x = 580



class Pilka(pygame.sprite.Sprite):
    # klasa Pilka dziedziczy ze "Sprite" w Pygame.

    def __init__(self, color, width, height):
        # wołamy konstruktor klasy bazowej
        super().__init__()

        # przekazujemy rozmiary, kolor, przezroczystość
        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)

        # rysowanie piłki (jako prostokącika)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # pobieramy prostokąt (jego rozmiary) z obiektu image
        self.rect = self.image.get_rect()

        self.reset()

    def reset(self):
        self.rect.x = randint(0, 690)
        self.rect.y = 0
        self.velocity = [randint(-5, 5), randint(4, 8)]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]



# definiujemy rozmiary i otwieramy nowe okno
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong - Solo")

clock = pygame.time.Clock()

font = pygame.font.Font(None, 48)

def koniec_gry(score, rekord):
    running = True
    while running:
        screen.fill(CZARNY)

        end_text = font.render("KONIEC GRY", True, BIALY)
        score_text = font.render(f"Wynik: {score}", True, BIALY)
        rekord_text = font.render(f"Rekord: {rekord}", True, BIALY)
        retry_text = font.render("Naciśnij R aby zagrać ponownie", True, BIALY)
        quit_text = font.render("Naciśnij Q aby wyjść", True, BIALY)

        screen.blit(end_text, (240, 150))
        screen.blit(score_text, (240, 200))
        screen.blit(rekord_text, (240, 250))
        screen.blit(retry_text, (120, 320))
        screen.blit(quit_text, (180, 370))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                if event.key == pygame.K_q:
                    return False

def start_game():
    global rekord

    rakietka = Rakietka(BIALY, 120, 12)
    rakietka.rect.x = 290
    rakietka.rect.y = 470

    pileczka = Pilka(BIALY,10,10)

    # lista wszystkich widzalnych obiektów potomnych z klasy Sprite
    all_sprites_list = pygame.sprite.Group()

    # dodanie obu rakietek i piłeczki do listy
    all_sprites_list.add(rakietka)
    all_sprites_list.add(pileczka)

    score = 0

    # zaczynamy właściwy blok programu
    kontynuuj = True


    # -------- GLÓWNA PĘTLA PROGRAMU -----------
    while kontynuuj:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # zamknięcie okienka
                kontynuuj = False

        # ruchy obiektów Rakietkas klawisze strzałka góra dół lub klawisz w s
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rakietka.moveLeft(7)
        if keys[pygame.K_RIGHT]:
            rakietka.moveRight(7)

        # aktualizacja listy duszków
        all_sprites_list.update()

        if pileczka.rect.left <= 0 or pileczka.rect.right >= 700:
            pileczka.velocity[0] *= -1

        if pileczka.rect.top <= 0:
            pileczka.velocity[1] *= -1

        if pygame.sprite.collide_rect(pileczka, rakietka):
            pileczka.velocity[1] *= -1
            score += 1

        if pileczka.rect.top > 500:
            kontynuuj = False

        # RYSOWANIE
        # czarny ekran
        screen.fill(CZARNY)

        # narysowanie obiektów
        all_sprites_list.draw(screen)

        # wyświetlanie wyniku
        text = font.render(f"Wynik: {score}", True, BIALY)
        screen.blit(text, (10, 10))

        # odświeżenie / przerysowanie całego ekranu
        pygame.display.flip()

        # 60 klatek na sekundę
        clock.tick(60)

    if score > rekord:
        rekord = score
        with open("rekord.txt", "w") as f:
            f.write(str(rekord))

    return koniec_gry(score, rekord)

gra = True
while gra:
    gra = start_game()

# koniec
pygame.quit()