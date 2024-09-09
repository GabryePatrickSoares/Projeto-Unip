import turtle
import random

lista_geral = []
lista_personagens = []
lista_objetos =[]
lista_obstaculos = []

dic_posicao_geral = {}
dic_posicao_personagens = {}
dic_posicao_objetos = {}
dic_posicao_obstaculo = {}

def criar_personagem(cor, forma = None):
    personagem = turtle.Turtle()
    personagem.shape(forma)
    personagem.color(cor)
    lista_personagens.append(personagem)
    lista_geral.append(personagem)
    personagem.penup()
    return personagem

def criar_objeto(cor, forma = None, largura = None, altura = None):
    objeto = turtle.Turtle()
    objeto.shape(forma)
    objeto.color(cor)
    objeto.shapesize(altura, largura)
    lista_objetos.append(objeto)
    lista_geral.append(objeto)
    objeto.penup()
    return objeto

def criar_obstaculo(cor, forma = None, largura = None, altura = None):
    obstaculo = turtle.Turtle()
    obstaculo.shape(forma)
    obstaculo.color(cor)
    obstaculo.shapesize(altura, largura)
    lista_obstaculos.append(obstaculo)
    lista_geral.append(obstaculo)
    obstaculo.penup()
    return obstaculo

def area_de_geração(x_max, y_max, x_min = None, y_min = None):
    global xmax, ymax, xmin, ymin
    if x_min == None and y_min == None:
        xmax = x_max
        ymax = y_max
        xmin = -x_max
        ymin = -y_max
        return xmax, ymax, xmin, ymin
    if x_min != None and y_min != None:
        xmax = x_max
        ymax = y_max
        xmin = x_min
        ymin = y_min
        return xmax, ymax, xmin, ymin
    if x_min != None and y_min == None:
        xmax = x_max
        ymax = y_max
        xmin = x_min
        ymin = -y_max
        return xmax, ymax, xmin, ymin
    if x_min == None and y_min != None:
        xmax = x_max
        ymax = y_max
        xmin = -x_max
        ymin = y_min
        return xmax, ymax, xmin, ymin
    
def virar_direita(entidade, velocidade = 10):
    entidade.setheading(0) #0 cabeça apontando para direita
    entidade.forward(velocidade)

def virar_esquerda(entidade, velocidade = 10):
    entidade.setheading(180) #180 cabeça apontando para esquerda
    entidade.forward(velocidade)

def virar_cima(entidade, velocidade = 10):
    entidade.setheading(90) #90 cabeça apontando para cima
    entidade.forward(velocidade)

def virar_baixo(entidade, velocidade = 10):
    entidade.setheading(270) #270 cabeça apontando para baixo
    entidade.forward(velocidade)
    
def posicionar_aleatoriamente(entidade):
    entidade.setposition(random.randrange(xmin, xmax, 10), random.randrange(ymin, ymax, 10))
    listar_posicao(entidade)

def listar_posicao(entidade):
    if entidade in lista_personagens:
        loc = entidade.position()
        xinicial = loc[0]+(entidade.shapesize()[1]*10)
        yinicial = loc[1]+(entidade.shapesize()[0]*10)
        xfinal = loc[0]-(entidade.shapesize()[1]*10)
        yfinal = loc[1]-(entidade.shapesize()[0]*10)
        dic = {entidade: [(xinicial, xfinal), (yinicial, yfinal)]}
        dic_posicao_personagens.update(dic)
        dic_posicao_geral.update(dic)
    if entidade in lista_objetos:
        loc = entidade.position()
        xinicial = loc[0]+(entidade.shapesize()[1]*10)
        yinicial = loc[1]+(entidade.shapesize()[0]*10)
        xfinal = loc[0]-(entidade.shapesize()[1]*10)
        yfinal = loc[1]-(entidade.shapesize()[0]*10)
        dic = {entidade: [(xinicial, xfinal), (yinicial, yfinal)]}
        dic_posicao_objetos.update(dic)
        dic_posicao_geral.update(dic)
    if entidade in lista_obstaculos:
        loc = entidade.position()
        xinicial = loc[0]-(entidade.shapesize()[0]*10)
        yinicial = loc[1]-(entidade.shapesize()[1]*10)
        xfinal = loc[0]+(entidade.shapesize()[0]*10)
        yfinal = loc[1]+(entidade.shapesize()[1]*10)
        dic = {entidade: [(xinicial, xfinal), (yinicial, yfinal)]}
        dic_posicao_obstaculo.update(dic)
        dic_posicao_geral.update(dic)

def col2(entidade, entidade2 = None):
    if entidade2 == None:
        for i in range(len(lista_obstaculos)):
            obs = dic_posicao_obstaculo[lista_obstaculos[i]]
            if obs[0][0] <= entidade.position()[0]+5 <= obs[0][1] and obs[1][0] <= entidade.position()[1]+5 <= obs[1][1]:#colisão canto superior direito
                return "col_cant_sup_dir"
            if obs[0][0] <= entidade.position()[0]-5 <= obs[0][1] and obs[1][0] <= entidade.position()[1]+5 <= obs[1][1]:#colisão canto superior esquerdo
                return "col_cant_sup_esq"
            if obs[0][0] <= entidade.position()[0]+5 <= obs[0][1] and obs[1][0] <= entidade.position()[1]-5 <= obs[1][1]:#colisão canto inferior direito
                return "col_cant_inf_dir"
            if obs[0][0] <= entidade.position()[0]-5 <= obs[0][1] and obs[1][0] <= entidade.position()[1]-5 <= obs[1][1]:#colisão canto inferior esquerdo
                return "col_cant_inf_esq"
    else:
        obs = dic_posicao_geral[entidade2]
        if obs[0][0] <= entidade.position()[0]+5 <= obs[0][1] and obs[1][0] <= entidade.position()[1]+5 <= obs[1][1]:#colisão canto superior direito
            return True
        if obs[0][0] <= entidade.position()[0]-5 <= obs[0][1] and obs[1][0] <= entidade.position()[1]+5 <= obs[1][1]:#colisão canto superior esquerdo
            return True
        if obs[0][0] <= entidade.position()[0]+5 <= obs[0][1] and obs[1][0] <= entidade.position()[1]-5 <= obs[1][1]:#colisão canto inferior direito
            return True
        if obs[0][0] <= entidade.position()[0]-5 <= obs[0][1] and obs[1][0] <= entidade.position()[1]-5 <= obs[1][1]:#colisão canto inferior esquerdo
            return True
 
def mover_ate(entidade1, entidade2):
    repeticao = 0
    while entidade1.position()[0] > entidade2.position()[0]:
        if repeticao < 2:
            if col2(entidade1) == "col_cant_sup_esq":
                entidade1.backward(20)
                entidade1.setheading(270)
                entidade1.forward(10)
                repeticao += 1
            if col2(entidade1) == "col_cant_inf_esq":
                entidade1.backward(20)
                entidade1.setheading(90)
                entidade1.forward(10)
                repeticao += 1
            virar_esquerda(entidade1)
        else:
            if col2(entidade1) == "col_cant_sup_esq":
                entidade1.backward(20)
                entidade1.setheading(random.choice([270,90]))
                entidade1.forward(10)
                repeticao += 1
            if col2(entidade1) == "col_cant_inf_esq":
                entidade1.backward(20)
                entidade1.setheading(random.choice([90,270]))
                entidade1.forward(10)
                repeticao += 1
            virar_esquerda(entidade1)
    while entidade1.position()[0] < entidade2.position()[0]:
        if repeticao < 2:
            if col2(entidade1) == "col_cant_sup_dir":
                entidade1.backward(20)
                entidade1.setheading(270)
                entidade1.forward(10)
                repeticao += 1
            if col2(entidade1) == "col_cant_inf_dir":
                entidade1.backward(20)
                entidade1.setheading(90)
                entidade1.forward(10)
                repeticao += 1
            virar_direita(entidade1)
        else:
            if col2(entidade1) == "col_cant_sup_dir":
                entidade1.backward(20)
                entidade1.setheading(random.choice([270,90]))
                entidade1.forward(10)
                repeticao += 1
            if col2(entidade1) == "col_cant_inf_dir":
                entidade1.backward(20)
                entidade1.setheading(random.choice([90,270]))
                entidade1.forward(10)
                repeticao += 1
            virar_direita(entidade1)
    while entidade1.position()[1] > entidade2.position()[1]:
        if repeticao < 2:
            if col2(entidade1) == "col_cant_inf_esq":
                entidade1.backward(20)
                entidade1.setheading(0)
                entidade1.forward(10)
                repeticao += 1
            if col2(entidade1) == "col_cant_inf_dir":
                entidade1.backward(20)
                entidade1.setheading(180)
                entidade1.forward(10)
                repeticao += 1
            virar_baixo(entidade1)
        else:
            if col2(entidade1) == "col_cant_inf_esq":
                entidade1.backward(20)
                entidade1.setheading(random.choice([0,180]))
                entidade1.forward(10)
                repeticao += 1
            if col2(entidade1) == "col_cant_inf_dir":
                entidade1.backward(20)
                entidade1.setheading(random.choice([180,0]))
                entidade1.forward(10)
                repeticao += 1
            virar_baixo(entidade1)
    while entidade1.position()[1] < entidade2.position()[1]:
        if repeticao < 2:
            if col2(entidade1) == "col_cant_sup_esq":
                entidade1.backward(20)
                entidade1.setheading(0)
                entidade1.forward(10)
                repeticao += 1
            if col2(entidade1) == "col_cant_sup_dir":
                entidade1.backward(20)
                entidade1.setheading(180)
                entidade1.forward(10)
                repeticao += 1
            virar_cima(entidade1)
        else:
            if col2(entidade1) == "col_cant_sup_esq":
                entidade1.backward(20)
                entidade1.setheading(random.choice([0,180]))
                entidade1.forward(10)
                repeticao += 1
            if col2(entidade1) == "col_cant_sup_dir":
                entidade1.backward(20)
                entidade1.setheading(random.choice([180,0]))
                entidade1.forward(10)
                repeticao += 1
            virar_cima(entidade1)

def aleatorizar_posicoes_geral():
    for i in range(len(lista_geral)):
        posicionar_aleatoriamente(lista_geral[i])  

#O PROGRAMA COMEÇA AQUI

esta_com_chave = random.choice([True, False])
mesa = criar_obstaculo("red","square", 1,1)
mesa2 = criar_obstaculo("red","square", 1,1)
mesa3 = criar_obstaculo("red","square", 1,1)
mesa4 = criar_obstaculo("red","square", 1,1)
mesa5 = criar_obstaculo("red","square", 1,1)
mesa6 = criar_obstaculo("red","square", 1,1)
mesa7 = criar_obstaculo("red","square", 1,1)
mesa8 = criar_obstaculo("red","square", 1,1)
mesa9 = criar_obstaculo("red","square", 1,1)
mesa10 = criar_obstaculo("red","square", 1,1)
mesa11 = criar_obstaculo("red","square", 1,1)
mesa12 = criar_obstaculo("red","square", 1,1)
mesa13 = criar_obstaculo("red","square", 1,1)
mesa14 = criar_obstaculo("red","square", 1,1)
porta = criar_objeto("black", "square",1,2)
chave = criar_objeto("yellow", "square",1,1)
prof = criar_personagem("blue", "triangle")

area_de_geração(150, 150)
aleatorizar_posicoes_geral()

while True:
    while col2(chave):
         posicionar_aleatoriamente(chave)

    while col2(porta):
         posicionar_aleatoriamente(porta)

    if esta_com_chave:
        porta.color("black")
        chave.hideturtle()
        mover_ate(prof, porta)
        if prof.distance(porta) <= 25:
            aleatorizar_posicoes_geral()
            esta_com_chave = random.choice([True, False])
            if esta_com_chave:
                chave.showturtle()
    else:
        porta.color("#522E31")
        chave.showturtle()
        mover_ate(prof, chave)
        if prof.distance(chave) <= 25:
            esta_com_chave = True
            chave.hideturtle()