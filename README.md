# Projeto Turtle - Jogo com Obstáculos e Personagens

Este projeto é uma simulação em Python utilizando a biblioteca `turtle` para criar um jogo simples. O objetivo principal é mover um personagem até objetos específicos, evitando obstáculos e interagindo com eles.

## Descrição

O código implementa um jogo onde:
- **Personagens** e **objetos** são representados por tartarugas (turtles) com diferentes cores e formas.
- **Obstáculos** são adicionados ao ambiente para desafiar o movimento do personagem.
- O personagem deve interagir com um objeto (a chave) e um portão para avançar no jogo.

## Funcionalidades

1. **Criação de Personagens e Objetos**:
   - `criar_personagem(cor, forma)` - Cria um personagem com cor e forma especificada.
   - `criar_objeto(cor, forma, largura, altura)` - Cria um objeto com cor, forma, largura e altura especificadas.
   - `criar_obstaculo(cor, forma, largura, altura)` - Cria um obstáculo com cor, forma, largura e altura especificadas.

2. **Movimentação**:
   - Funções para movimentar a tartaruga para a direita, esquerda, cima e baixo.
   - `virar_direita(entidade, velocidade)` - Move a tartaruga para a direita.
   - `virar_esquerda(entidade, velocidade)` - Move a tartaruga para a esquerda.
   - `virar_cima(entidade, velocidade)` - Move a tartaruga para cima.
   - `virar_baixo(entidade, velocidade)` - Move a tartaruga para baixo.

3. **Posicionamento**:
   - `posicionar_aleatoriamente(entidade)` - Posiciona a tartaruga aleatoriamente dentro da área definida.
   - `aleatorizar_posicoes_geral()` - Aleatoriza a posição de todos os elementos no ambiente.

4. **Colisão e Movimento até Entidade**:
   - `col2(entidade, entidade2)` - Verifica a colisão entre duas entidades.
   - `mover_ate(entidade1, entidade2)` - Move a tartaruga `entidade1` até a `entidade2`, considerando colisões com obstáculos.

5. **Área de Geração**:
   - `area_de_geração(x_max, y_max, x_min, y_min)` - Define a área dentro da qual as tartarugas podem ser posicionadas.

## Instruções de Uso

1. **Configuração Inicial**:
   - Defina a área de geração com `area_de_geração(x_max, y_max)`.
   - Crie os obstáculos, objetos e personagens desejados usando as funções apropriadas.

2. **Execução do Jogo**:
   - O jogo inicia movendo o personagem para interagir com a chave e o portão.
   - O estado do jogo e a posição dos objetos são atualizados com base na interação do personagem.

3. **Interatividade**:
   - O personagem deve pegar a chave para abrir o portão.
   - O estado da chave e do portão é atualizado aleatoriamente para criar uma experiência dinâmica.

## Exemplo de Código

```python
import turtle
import random

# Criação de obstáculos e objetos
mesa = criar_obstaculo("red", "square", 1, 1)
porta = criar_objeto("black", "square", 1, 2)
chave = criar_objeto("yellow", "square", 1, 1)
prof = criar_personagem("blue", "triangle")

# Configuração da área de geração
area_de_geração(150, 150)
aleatorizar_posicoes_geral()

# Lógica do jogo
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
```

## Dependências

- Python 3.x
- Biblioteca `turtle` (incluída no Python Standard Library)

## Contribuições

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou sugestões. Faça um fork deste repositório e envie um pull request.
