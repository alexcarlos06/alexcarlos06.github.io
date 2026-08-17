---
title: Paradigmas de programação: diferentes formas de pensar e construir software
date: 2026-08-17
slug: paradigmas-de-programacao
description: Uma visão prática dos principais paradigmas de programação, seus modelos mentais, diferenças e como eles se combinam na construção de software moderno.
tags:
  - MBA
  - Engenharia de Software
  - Paradigmas
  - Arquitetura
  - Programação
---

# Paradigmas de programação: diferentes formas de pensar e construir software

Quando começamos a programar, é comum concentrarmos o aprendizado em linguagens:

```text
Python
Java
JavaScript
C#
C
SQL
```

Com o tempo, porém, percebemos que aprender uma linguagem não significa apenas aprender sua sintaxe.

Por trás do código existe algo mais importante: **a maneira como pensamos sobre o problema e descrevemos sua solução**.

É nesse ponto que entram os **paradigmas de programação**.

Um paradigma de programação pode ser entendido como uma abordagem ou modelo de pensamento utilizado para estruturar programas e expressar computações.

Em vez de perguntar apenas:

```text
Qual linguagem devo utilizar?
```

podemos começar a perguntar:

```text
Como quero representar este problema?

Como os dados serão transformados?

Onde ficará o estado?

Quem será responsável pelo comportamento?

O programa reagirá a eventos?

Quero dizer ao computador como executar
ou apenas descrever o resultado esperado?
```

Essas perguntas nos levam aos diferentes paradigmas.

Uma observação importante é que não existe uma única classificação universal e rígida dos paradigmas. Peter Van Roy propõe uma visão especialmente útil: paradigmas podem ser entendidos como combinações de conceitos de programação, e linguagens modernas frequentemente suportam vários deles simultaneamente.

Isso explica por que linguagens como Python ou JavaScript não precisam ser classificadas dentro de apenas uma categoria.

Podemos utilizar diferentes formas de pensar dependendo do problema que estamos tentando resolver.

## Paradigma não é linguagem

Talvez essa seja a primeira distinção importante.

Uma linguagem é uma ferramenta.

Um paradigma é uma forma de estruturar a solução.

Por exemplo, Python possui recursos para:

- programação procedural;
- programação orientada a objetos;
- programação funcional;
- programação assíncrona;
- programação orientada a eventos em diferentes bibliotecas e aplicações.

Portanto:

```text
Linguagem
    ↓
oferece recursos
    ↓
que permitem utilizar
    ↓
diferentes paradigmas
```

O paradigma influencia **como pensamos o código**.

## 1. Programação imperativa

A programação imperativa provavelmente representa a forma mais intuitiva de começar a programar.

Nela descrevemos uma sequência de instruções que devem ser executadas.

Podemos pensar assim:

```text
Faça isso
↓
depois isso
↓
verifique aquilo
↓
altere uma variável
↓
continue o processamento
```

Um exemplo simples:

```python
valores = [100, 200, 300, 400]

total = 0

for valor in valores:
    total = total + valor

media = total / len(valores)

print(media)
```

Estamos dizendo explicitamente:

1. crie uma variável;
2. percorra os valores;
3. altere o estado da variável;
4. calcule a média;
5. mostre o resultado.

O foco está principalmente em:

```text
COMO executar
```

A programação imperativa possui forte relação histórica com a arquitetura tradicional dos computadores, baseada em memória, instruções e alteração de estado.

Em sua conhecida palestra associada ao Turing Award, John Backus questionou a forte dependência dos modelos tradicionais de programação em relação ao estilo de computação inspirado pela arquitetura de von Neumann e explorou alternativas funcionais para a composição de programas.

## 2. Programação procedural

A programação procedural pode ser vista como uma evolução natural da programação imperativa.

Continuamos descrevendo **como o programa executará as operações**, mas organizamos o código em procedimentos ou funções.

Em vez de:

```python
valores = [100, 200, 300]

total = 0

for valor in valores:
    total += valor

media = total / len(valores)
```

podemos organizar:

```python
def calcular_media(valores):
    total = 0

    for valor in valores:
        total += valor

    return total / len(valores)


valores = [100, 200, 300]

media = calcular_media(valores)
```

A principal mudança está na decomposição do problema.

```text
Programa
   ↓
Procedimentos
   ↓
Funções
   ↓
Instruções
```

Isso melhora aspectos como:

- organização;
- reutilização;
- legibilidade;
- separação de responsabilidades.

Linguagens como C são fortemente associadas a esse estilo, embora conceitos procedurais também apareçam em inúmeras linguagens modernas.

## 3. Programação Orientada a Objetos

Na Programação Orientada a Objetos, ou OOP, começamos a enxergar o software através de **objetos que combinam dados e comportamentos**.

Imagine um domínio financeiro.

Em uma solução procedural poderíamos ter:

```python
def pagar_titulo(titulo):
    titulo["status"] = "pago"
```

Na orientação a objetos poderíamos representar o próprio conceito:

```python
class Titulo:
    def __init__(self, valor):
        self.valor = valor
        self.status = "aberto"

    def pagar(self):
        self.status = "pago"
```

Agora temos:

```text
Titulo
├── dados
│   ├── valor
│   └── status
│
└── comportamento
    └── pagar()
```

Entre os conceitos normalmente associados à orientação a objetos estão:

- abstração;
- encapsulamento;
- herança;
- polimorfismo.

### Abstração

Representamos apenas aquilo que é relevante para determinado contexto.

```text
Titulo
valor
vencimento
fornecedor
status
```

Não precisamos representar todo o mundo real.

Apenas o necessário para resolver o problema.

### Encapsulamento

Tentamos proteger o estado interno de um objeto e controlar como ele poderá ser alterado.

Em vez de permitir:

```python
titulo.status = "qualquer coisa"
```

podemos disponibilizar comportamentos:

```python
titulo.pagar()
titulo.cancelar()
```

### Herança

Permite criar novas abstrações baseadas em outras existentes.

### Polimorfismo

Permite que diferentes implementações respondam ao mesmo tipo de operação.

Mas orientação a objetos não significa simplesmente:

```text
usar classes
```

O ponto mais importante é **modelar responsabilidades, estado e comportamento de maneira coerente**.

## 4. Programação funcional

A programação funcional muda significativamente a maneira como pensamos sobre o programa.

Em vez de colocar o foco principal em objetos alterando estado, colocamos grande ênfase em:

```text
dados
  ↓
funções
  ↓
transformações
  ↓
novos dados
```

Considere:

```python
valores = [100, 200, 300, 400]

valores_com_desconto = []

for valor in valores:
    valores_com_desconto.append(valor * 0.9)
```

Uma abordagem funcional poderia ser:

```python
def aplicar_desconto(valor):
    return valor * 0.9


valores = [100, 200, 300, 400]

valores_com_desconto = list(
    map(aplicar_desconto, valores)
)
```

Ou simplesmente:

```python
valores_com_desconto = [
    valor * 0.9
    for valor in valores
]
```

O objetivo não é utilizar `map()` em todo lugar.

O paradigma funcional envolve conceitos mais profundos como:

- funções como valores;
- funções de ordem superior;
- composição;
- redução de efeitos colaterais;
- preferência por imutabilidade;
- transformações de dados.

Python, embora não seja uma linguagem funcional pura, possui módulos e recursos destinados ao estilo funcional, incluindo `functools`, `itertools` e operações sobre funções.

Haskell representa um exemplo muito mais radical desse paradigma. O projeto oficial da linguagem a descreve como puramente funcional, com características como transparência referencial, imutabilidade e avaliação preguiçosa.

Podemos representar a ideia assim:

```text
Entrada
  ↓
função A
  ↓
resultado
  ↓
função B
  ↓
resultado
  ↓
função C
  ↓
Saída
```

Esse modelo aparece com bastante força em processamento de dados, pipelines e transformações.

## 5. Programação declarativa

Aqui acontece uma mudança importante.

Na programação imperativa normalmente descrevemos:

```text
COMO fazer
```

Na programação declarativa damos maior ênfase a:

```text
O QUE queremos
```

SQL é um excelente exemplo para entender essa ideia.

Considere:

```sql
SELECT
    fornecedor,
    SUM(valor)
FROM titulos
WHERE status = 'ABERTO'
GROUP BY fornecedor;
```

Não precisamos implementar manualmente:

```text
Abra o arquivo
↓
percorra cada registro
↓
verifique o status
↓
crie um agrupamento
↓
some os valores
↓
organize os resultados
```

Descrevemos o resultado desejado.

```text
Quero:

títulos abertos
agrupados por fornecedor
com seus valores somados
```

O banco de dados decide como executar essa consulta.

Essa mudança de perspectiva é extremamente importante:

```text
Imperativo

COMO fazer?


Declarativo

O QUE quero obter?
```

## 6. Programação lógica

A programação lógica leva a ideia declarativa ainda mais longe.

Em vez de escrevermos diretamente um algoritmo, podemos representar:

```text
fatos
+
regras
+
consultas
```

Prolog é provavelmente o exemplo mais conhecido.

Imagine:

```prolog
pai(joao, maria).
pai(joao, pedro).

irmaos(X, Y) :-
    pai(P, X),
    pai(P, Y),
    X \= Y.
```

Podemos então perguntar:

```prolog
irmaos(maria, pedro).
```

A lógica de inferência do ambiente tenta determinar se a relação pode ser satisfeita.

O modelo mental muda novamente:

```text
Imperativo
↓
Execute estes passos


Funcional
↓
Transforme estes dados


Orientado a objetos
↓
Estes objetos possuem estado e comportamento


Lógico
↓
Estes fatos e regras são verdadeiros;
descubra a solução
```

## 7. Programação orientada a eventos

Existem ainda paradigmas ou estilos de programação que tratam principalmente do **fluxo de execução**.

Na programação orientada a eventos, o programa reage à ocorrência de eventos.

Por exemplo:

```text
Usuário clicou
        ↓
evento
        ↓
executa função
```

Ou:

```text
Mensagem chegou
      ↓
evento
      ↓
processamento
```

Em JavaScript:

```javascript
botao.addEventListener("click", () => {
    console.log("Botão clicado");
});
```

Esse paradigma aparece bastante em:

- interfaces gráficas;
- aplicações web;
- sistemas assíncronos;
- mensageria;
- integrações;
- arquiteturas distribuídas.

Podemos imaginar:

```text
Evento A ──→ Handler A

Evento B ──→ Handler B

Evento C ──→ Handler C
```

O fluxo do sistema deixa de ser necessariamente uma grande sequência linear de instruções.

## 8. Programação concorrente

Outro eixo importante aparece quando precisamos executar várias atividades que podem progredir independentemente.

É o caso da programação concorrente.

Imagine um sistema processando simultaneamente:

```text
requisição A
requisição B
requisição C
mensagem D
arquivo E
```

Em vez de pensar apenas em uma sequência:

```text
A → B → C → D → E
```

podemos trabalhar com múltiplos fluxos de execução.

Erlang é um exemplo importante desse modelo. A linguagem foi projetada para cenários de concorrência massiva utilizando processos leves que podem executar e se comunicar independentemente.

Uma representação simplificada seria:

```text
               ┌── Processo A
Entrada ───────┼── Processo B
               ├── Processo C
               └── Processo D
```

Concorrência não significa necessariamente paralelismo.

Podemos ter várias tarefas progredindo concorrentemente mesmo quando não estão sendo executadas literalmente ao mesmo tempo em diferentes processadores.

## Os paradigmas não precisam competir

Talvez o erro mais comum seja pensar que precisamos escolher:

```text
OOP

OU

Funcional

OU

Procedural
```

Na prática, sistemas reais frequentemente combinam essas abordagens.

Imagine uma aplicação:

```text
API REST
   ↓
Orientação a objetos
para representar conceitos do domínio

   ↓
Programação funcional
para transformar conjuntos de dados

   ↓
SQL declarativo
para consultar informações

   ↓
Eventos
para processamento assíncrono

   ↓
Concorrência
para executar múltiplas tarefas
```

Essa combinação é extremamente natural.

É justamente por isso que a visão de programação multiparadigma é tão relevante.

O objetivo não deveria ser:

```text
Qual paradigma é o melhor?
```

Mas:

```text
Qual maneira de representar este problema
produz a solução mais clara?
```

## Um mesmo problema em diferentes paradigmas

Imagine a necessidade de aplicar 10% de desconto aos pedidos acima de R$ 1.000.

### Imperativo

```python
pedidos = [500, 1200, 2000]

resultado = []

for pedido in pedidos:
    if pedido > 1000:
        pedido = pedido * 0.9

    resultado.append(pedido)
```

Pensamos principalmente nos passos.

### Funcional

```python
def calcular_valor(valor):
    return valor * 0.9 if valor > 1000 else valor


resultado = list(map(calcular_valor, pedidos))
```

Pensamos principalmente na transformação.

### Orientado a objetos

```python
class Pedido:
    def __init__(self, valor):
        self.valor = valor

    def aplicar_desconto(self):
        if self.valor > 1000:
            self.valor *= 0.9
```

Pensamos principalmente no objeto e em seu comportamento.

### Declarativo

Imagine que os pedidos estejam no banco:

```sql
SELECT
    CASE
        WHEN valor > 1000
        THEN valor * 0.9
        ELSE valor
    END AS valor_final
FROM pedidos;
```

Descrevemos o resultado que queremos obter.

O problema é praticamente o mesmo.

O **modelo mental utilizado para resolvê-lo é diferente**.

## Paradigma, arquitetura e Design Patterns são a mesma coisa?

Não.

Essa distinção também é importante.

Podemos imaginar diferentes níveis:

```text
Paradigma
↓
forma de pensar o código


Design Pattern
↓
solução recorrente para um problema de design


Arquitetura
↓
organização estrutural do sistema
```

Por exemplo:

```text
Paradigma
Orientação a Objetos

        ↓

Design Pattern
Strategy

        ↓

Arquitetura
Clean Architecture
```

Esses conceitos podem coexistir.

DDD também não é um paradigma de programação. Ele atua principalmente na forma como compreendemos e modelamos um domínio complexo.

Portanto:

```text
Paradigma
        ↓
influencia como escrevemos


Patterns
        ↓
ajudam a organizar soluções recorrentes


DDD
        ↓
ajuda a modelar o domínio


Arquitetura
        ↓
organiza o sistema e suas dependências
```

São níveis diferentes de decisão dentro da Engenharia de Software.

## Qual paradigma devo aprender?

Talvez a melhor resposta seja:

```text
mais de um.
```

Cada paradigma treina uma maneira diferente de pensar.

A programação procedural ensina a decompor algoritmos.

A orientação a objetos ensina a pensar em responsabilidades, estado e comportamento.

A programação funcional fortalece o pensamento baseado em transformações, composição e redução de efeitos colaterais.

A programação declarativa ensina a expressar **o resultado desejado** sem controlar cada detalhe da execução.

A programação lógica mostra como representar conhecimento através de fatos e regras.

Programação orientada a eventos ajuda a compreender sistemas reativos e assíncronos.

Concorrência ensina a pensar em múltiplos fluxos de execução.

Aprender paradigmas, portanto, não significa decorar definições.

Significa aumentar o número de ferramentas mentais disponíveis para resolver problemas.

## Uma forma simples de lembrar

```text
IMPERATIVO
"Como executar?"

        ↓

PROCEDURAL
"Quais procedimentos executar?"

        ↓

ORIENTADO A OBJETOS
"Quem possui esse comportamento?"

        ↓

FUNCIONAL
"Como transformar esses dados?"

        ↓

DECLARATIVO
"O que eu quero obter?"

        ↓

LÓGICO
"Quais fatos e regras definem a solução?"

        ↓

ORIENTADO A EVENTOS
"O que deve acontecer quando algo ocorrer?"

        ↓

CONCORRENTE
"Quais tarefas podem progredir independentemente?"
```

O ponto mais importante talvez seja perceber que programação não é apenas escrever instruções.

É **modelar problemas**.

Quanto mais paradigmas conhecemos, mais maneiras temos de observar o mesmo problema.

E essa é uma das diferenças entre simplesmente conhecer uma linguagem e desenvolver uma visão mais ampla de Engenharia de Software.

Uma linguagem nos fornece a sintaxe.

Os paradigmas ampliam nossa forma de pensar.

## Referências

- Peter Van Roy — Programming Paradigms for Dummies: What Every Programmer Should Know: https://webperso.info.ucl.ac.be/~pvr/VanRoyChapter.pdf
- John Backus — Can Programming Be Liberated from the von Neumann Style?: https://research.ibm.com/publications/can-programming-be-liberated-from-the-von-neumann-style-a-functional-style-and-its-algebra-of-programs
- Python Software Foundation — Functional Programming HOWTO: https://docs.python.org/3/howto/functional.html
- Python Software Foundation — Classes: https://docs.python.org/3/tutorial/classes.html
- Python Software Foundation — Functional Programming Modules: https://docs.python.org/3/library/functional.html
- Haskell — documentação oficial: https://www.haskell.org/
- Microsoft Learn — Object-Oriented Programming em C#: https://learn.microsoft.com/dotnet/csharp/fundamentals/tutorials/oop
- PostgreSQL — SELECT: https://www.postgresql.org/docs/current/sql-select.html
- SWI-Prolog — documentação oficial: https://www.swi-prolog.org/
- Node.js — Events: https://nodejs.org/api/events.html
- Erlang — Concurrent Programming: https://www.erlang.org/doc/system/conc_prog.html
