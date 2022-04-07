class Game:
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y

    def direita(self):
        if (self.x+1,self.y) in Bloco.coordenadas:
            evento('Você não pode ir para onde tem um bloco')
            return
        if self.x+1 > 4:
            evento('Você não pode sair do mapa')
            return
        self.x += 1
        evento('Você foi para a direita')

    def esquerda(self):
        if (self.x-1,self.y) in Bloco.coordenadas:
            evento('Você não pode ir para onde tem um bloco')
            return
        if self.x-1 < 0:
            evento('Você não pode sair do mapa')
            return
        self.x -= 1
        evento('Você foi para a esquerda')

    def baixo(self):
        if (self.x,self.y-1) in Bloco.coordenadas:
            evento('Você não pode ir para onde tem um bloco')
            return
        if self.y-1 < 0:
            evento('Você não pode sair do mapa')
            return
        self.y -= 1
        evento('Você foi para baixo')
    
    def cima(self):
        if (self.x,self.y+1) in Bloco.coordenadas:
            evento('Você não pode ir para onde tem um bloco')
            return
        if self.y+1 < 0:
            evento('Você não pode sair do mapa')
            return
        self.y += 1
        evento('Você foi para cima')

class Destino:
    def __init__(self,x=4,y=0):
        self.x = x
        self.y = y

class Bloco:
    coordenadas = []
    def __init__(self,x,y):
        self.x = x
        self.y = y
        Bloco.coordenadas.append((self.x,self.y))
    

def evento(txt):
    print('-='*15)
    print(f'{txt:^30}')
    print('-='*15)

def bloco():
    print('|||', end = '')

player = Game(0,0)
b1 = Bloco(1,0)
b2 = Bloco(1,1)
b3 = Bloco(3,0)
b4 = Bloco(2,3)
b5 = Bloco(2,4)
b6 = Bloco(0,4)
b7 = Bloco(4,3)
b8 = Bloco(4,2)
d = Destino(4,4)

while True:
    for y in range(4,-1,-1):
        for x in range(0,5):
            if (x,y) not in [(d.x,d.y),(player.x,player.y)] and (x,y) not in Bloco.coordenadas:
                print('   ',end = '')
            elif (x,y) == (player.x,player.y) and (player.x,player.y) != (d.x,d.y):
                print(f'{"😳":^2}',end = '')
            elif (x,y) == (d.x,d.y) and (player.x,player.y) != (d.x,d.y):
                print(f'{"🥇":^2}',end = '')
            elif (x,y) == (d.x,d.y) == (d.x,d.y):
                print(f'{"😁":^2}',end = '')
            else:
                bloco()
        print('')

    if (player.x,player.y) == (d.x,d.y):
        evento('GG izi fih')
        break
    
    print('''
[ W ] Cima
[ S ] Baixo
[ A ] Esquerda
[ D ] Direita
''')
    n = input('Para onde ir agora? ').lower()
    while n not in ['w','a','s','d']:
        print('Escolha inválida')
        n = input('Para onde ir agora? ')

    if n == 'd':
        player.direita()
    if n == 's':
        player.baixo()
    if n == 'a':
        player.esquerda()
    if n == 'w':
        player.cima()
