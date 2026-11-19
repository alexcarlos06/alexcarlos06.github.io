---
title: "User Experience (UX): por que a experiência do usuário deve fazer parte da Engenharia de Software?"
date: 2026-11-19
slug: user-experience-ux-engenharia-de-software
description: "Reflexões do MBA em Engenharia de Software sobre UX, pesquisa com usuários, jornadas, arquitetura da informação, prototipagem e design emocional."
tags:
  - MBA
  - Engenharia de Software
  - UX
  - Design
---

# User Experience (UX): por que a experiência do usuário deve fazer parte da Engenharia de Software?

Quando pensamos em desenvolvimento de software, é natural direcionarmos nossa atenção para arquitetura, linguagens de programação, integrações, desempenho e segurança. Todos esses aspectos são fundamentais para construir soluções robustas.

Mas existe uma questão igualmente importante: **o usuário consegue utilizar aquilo que desenvolvemos de maneira simples, eficiente e satisfatória?**

Durante meus estudos no MBA em Engenharia de Software da USP/Esalq, na disciplina de User Experience (UX), ministrada pelo professor Daniel Furtado, aprofundei conceitos que mostram como a experiência do usuário vai muito além da aparência de uma interface.

Uma solução pode ser tecnicamente excelente e, ainda assim, oferecer uma experiência ruim. Isso acontece quando a tecnologia funciona conforme o esperado, mas não atende adequadamente às necessidades, expectativas ou características de quem a utiliza.

Neste artigo, compartilho os principais conceitos estudados e sua relação com a construção de soluções digitais.

## 1. O que é User Experience (UX)?

User Experience, ou Experiência do Usuário, envolve a percepção e as respostas das pessoas ao interagirem com um produto, sistema ou serviço.

O conceito ganhou destaque com Donald Norman, que defendia uma visão abrangente da experiência, envolvendo não apenas interfaces e usabilidade, mas também aspectos físicos, emocionais e contextuais da interação.

É importante distinguir três conceitos:

- **UI (User Interface):** elementos da interface pelos quais o usuário interage com o sistema.
- **Usabilidade:** facilidade, eficiência e satisfação ao realizar tarefas em determinado contexto.
- **UX (User Experience):** experiência mais ampla, incluindo expectativas, percepções e resultados da interação.

Pense em um sistema corporativo de aprovação de pedidos. Ele pode apresentar todas as informações necessárias, funcionar sem erros e processar as transações corretamente. Entretanto, se o usuário precisa navegar por diversas telas para concluir uma aprovação simples, existe uma oportunidade de melhoria na experiência.

A UX nos convida a avaliar não apenas se a funcionalidade existe, mas se ela realmente resolve o problema de quem a utiliza.

**Fundamentação:** Donald Norman e Jakob Nielsen, [The Definition of User Experience (UX)](https://www.nngroup.com/articles/definition-user-experience/).

## 2. Os sete elementos de uma boa experiência: UX Honeycomb

Peter Morville desenvolveu o modelo *UX Honeycomb*, representado por sete dimensões que ajudam a avaliar a qualidade de uma experiência.

| Dimensão | Significado |
| --- | --- |
| Útil | Resolve uma necessidade real |
| Utilizável | Permite realizar tarefas com facilidade |
| Desejável | Desperta interesse e percepção positiva |
| Encontrável | Facilita localizar informações e funcionalidades |
| Acessível | Considera pessoas com diferentes capacidades |
| Confiável | Transmite credibilidade e segurança |
| Valioso | Gera valor para usuários e organizações |

O aspecto interessante desse modelo é reconhecer que a qualidade de um produto não depende de uma única característica.

Um software pode ser extremamente útil, mas difícil de utilizar. Pode ter uma interface agradável, mas apresentar informações pouco confiáveis.

Na Engenharia de Software, essas dimensões podem orientar critérios de qualidade e decisões de produto desde o levantamento dos requisitos.

A acessibilidade, por exemplo, também deve ser considerada desde o início. As diretrizes WCAG do W3C estabelecem princípios para tornar conteúdos e interfaces perceptíveis, operáveis, compreensíveis e robustos.

**Fundamentação:** Peter Morville, UX Honeycomb; [User Experience Honeycomb](https://www.designatlas.org/en/disciplines/ux-design/user-experience-honeycomb/); [WCAG 2.2 — W3C](https://www.w3.org/TR/WCAG22/).

## 3. UX começa antes da interface: os cinco planos de experiência

Jesse James Garrett propôs um modelo que organiza a experiência do usuário em cinco planos, partindo de decisões abstratas até chegar aos elementos visuais.

1. **Estratégia:** compreender as necessidades dos usuários e os objetivos do negócio.
2. **Escopo:** definir funcionalidades e requisitos de conteúdo.
3. **Estrutura:** organizar fluxos de interação e informações.
4. **Esqueleto:** estabelecer a disposição dos elementos, navegação e interface.
5. **Superfície:** construir a apresentação visual e sensorial do produto.

O modelo demonstra que a interface visível representa apenas uma parte do trabalho necessário para proporcionar uma experiência satisfatória.

Por exemplo, ao desenvolver um portal de serviços internos, a definição das cores e dos botões pertence à superfície. Antes disso, precisamos entender quais serviços serão disponibilizados, quais informações são necessárias e como os usuários percorrerão os fluxos.

Esse raciocínio possui uma conexão direta com a Engenharia de Software: **decisões de interface não compensam requisitos mal compreendidos ou fluxos inadequadamente projetados.**

**Fundamentação:** Jesse James Garrett, [The Elements of User Experience](https://www.oreilly.com/library/view/the-elements-of/9780321684486/).

## 4. Conhecer o usuário: pesquisas, modelos mentais e personas

Um dos principais aprendizados de UX é que não devemos presumir que os usuários pensam ou utilizam os sistemas da mesma maneira que seus desenvolvedores.

Cada pessoa possui experiências anteriores, conhecimentos e expectativas que influenciam a forma como interpreta uma interface. Esses fatores estão relacionados aos chamados *modelos mentais*.

Para compreender melhor essas diferenças, podemos utilizar métodos de pesquisa complementares.

**Pesquisa quantitativa:** busca identificar padrões e medir comportamentos por meio de números, como taxas de conclusão, volume de acessos e tempo de execução.

**Pesquisa qualitativa:** procura compreender motivações, dificuldades e comportamentos por meio de entrevistas, observações e testes.

Os resultados dessas pesquisas podem contribuir para a construção de *personas*: representações de grupos de usuários com necessidades, objetivos e comportamentos relevantes para o produto.

Uma persona deve ser baseada em informações reais ou hipóteses explicitamente identificadas, e não apenas em características imaginadas pela equipe.

Em um sistema empresarial, podemos encontrar diferentes perfis: usuários operacionais que executam dezenas de transações diariamente, gestores que acessam indicadores eventualmente e profissionais que precisam consultar informações específicas.

Cada grupo pode apresentar expectativas distintas sobre navegação, velocidade e nível de detalhamento.

**Fundamentação:** Donald Norman e Alan Cooper sobre modelos mentais e design orientado a objetivos; [When to Use Which UX Research Methods — NN/g](https://www.nngroup.com/articles/which-ux-research-methods/); [Personas: Study Guide — NN/g](https://www.nngroup.com/articles/personas-study-guide/).

## 5. A jornada do usuário e os pontos de atrito

A jornada do usuário representa as etapas percorridas por uma pessoa para alcançar determinado objetivo, incluindo suas interações, expectativas, dificuldades e percepções.

Seu mapeamento permite identificar *pain points*, ou pontos de atrito: situações que dificultam, atrasam ou prejudicam a experiência.

Imagine o processo de solicitação de acesso a um sistema corporativo:

O colaborador identifica a necessidade, abre uma solicitação, preenche informações, aguarda aprovações, recebe a liberação e finalmente acessa o sistema.

Cada etapa representa uma oportunidade para avaliar a experiência.

Informações duplicadas, aprovações pouco transparentes, ausência de acompanhamento e comunicações confusas podem gerar frustração, mesmo que o fluxo esteja tecnicamente funcionando.

Dois conceitos apresentados na aula ajudam a aprofundar essa análise:

- **Regra do pico-fim:** associada aos estudos de Daniel Kahneman, indica que momentos emocionalmente intensos e o encerramento de uma experiência podem influenciar significativamente sua avaliação retrospectiva.
- **Reserva de boa vontade:** conceito trabalhado por Steve Krug que representa a disposição limitada do usuário para tolerar dificuldades durante uma interação.

Dessa forma, melhorar a experiência envolve analisar o processo completo, e não apenas uma tela isolada.

**Fundamentação:** [How to Conduct Research for Customer Journey Mapping — NN/g](https://www.nngroup.com/articles/research-journey-mapping/); Daniel Kahneman, *Rápido e Devagar: Duas Formas de Pensar*; Steve Krug, *Don't Make Me Think*.

## 6. Design Thinking e Double Diamond: compreender antes de construir

Outro aspecto importante estudado foi a estruturação dos processos de design.

O Design Thinking utiliza práticas de empatia, definição de problemas, ideação, prototipagem e testes para orientar a construção de soluções.

Já o modelo *Double Diamond*, desenvolvido pelo Design Council, organiza o processo em quatro momentos:

- **Discover (Descobrir):** investigar o problema e compreender o contexto.
- **Define (Definir):** sintetizar descobertas e delimitar o desafio.
- **Develop (Desenvolver):** explorar e testar alternativas.
- **Deliver (Entregar):** validar e disponibilizar a solução.

O modelo alterna momentos de pensamento divergente, quando exploramos diferentes possibilidades, e convergente, quando selecionamos caminhos.

Na Engenharia de Software, isso reforça a importância de validar o problema antes de investir esforços na implementação.

Uma equipe pode desenvolver uma funcionalidade corretamente e ainda assim descobrir, depois da entrega, que ela não resolve a necessidade original.

**Fundamentação:** [Design Council — The Double Diamond](https://www.designcouncil.org.uk/resources/the-double-diamond/).

## 7. Arquitetura da Informação: organizar para facilitar a compreensão

A Arquitetura da Informação (AI) trata da organização, estruturação e identificação dos conteúdos para facilitar sua compreensão e localização.

Ela considera a relação entre usuários, informações e contexto.

Dan Brown apresentou oito princípios para orientar esse trabalho: objetos, escolhas, revelação, exemplares, portas da frente, classificação múltipla, navegação focada e crescimento.

Entre as aplicações práticas desses princípios estão a definição de menus coerentes, agrupamento de conteúdos relacionados, apresentação progressiva de informações e planejamento de estruturas que possam crescer.

Considere um portal corporativo com diversos serviços. Se as categorias não representam a forma como os colaboradores compreendem suas necessidades, localizar uma funcionalidade pode se tornar uma tarefa complicada.

Uma boa Arquitetura da Informação ajuda a reduzir esse esforço.

Além disso, ela possui relação com a arquitetura de software, embora sejam disciplinas diferentes: enquanto a arquitetura de software organiza responsabilidades e componentes técnicos, a Arquitetura da Informação organiza conteúdos e caminhos de acesso sob a perspectiva do usuário.

**Fundamentação:** Dan Brown, [Eight Principles of Information Architecture](https://doi.org/10.1002/bult.2010.1720360609); [Information Architecture — NN/g](https://www.nngroup.com/articles/ia-study-guide/).

## 8. Prototipagem e heurísticas: validar antes de desenvolver

A prototipagem permite representar e experimentar soluções antes de investir no desenvolvimento completo.

Os protótipos podem apresentar diferentes níveis de fidelidade.

**Baixa fidelidade (Low-Fi):** esboços, wireframes e representações simplificadas, úteis para explorar ideias, organizar informações e revisar fluxos.

**Alta fidelidade (Hi-Fi):** representações visualmente próximas do produto final, que podem permitir a simulação de interações mais detalhadas.

O nível de fidelidade deve ser escolhido conforme o objetivo da avaliação. Um protótipo simples pode ser suficiente para identificar problemas importantes de navegação.

Outro recurso fundamental são as **10 heurísticas de usabilidade de Jakob Nielsen**, que abordam visibilidade do estado do sistema, correspondência com o mundo real, controle do usuário, consistência, prevenção de erros, reconhecimento em vez de memorização, flexibilidade, minimalismo, recuperação de erros e ajuda.

Em uma aplicação empresarial, essas heurísticas podem orientar melhorias como mensagens de erro compreensíveis, indicadores de processamento, confirmação de ações críticas e utilização de terminologias familiares ao usuário.

A prototipagem combinada com testes de usabilidade ajuda a identificar problemas antes que eles se tornem parte do produto entregue.

**Fundamentação:** [UX Prototypes: Low Fidelity vs. High Fidelity — NN/g](https://www.nngroup.com/articles/ux-prototype-hi-lo-fidelity/); [10 Usability Heuristics for User Interface Design — NN/g](https://www.nngroup.com/articles/ten-usability-heuristics/).

## 9. Design Emocional: a experiência também é construída por percepções

Donald Norman propôs três níveis de processamento relacionados ao design emocional.

**Visceral:** associado às primeiras impressões, à aparência e às reações imediatas.

**Comportamental:** relacionado à experiência durante o uso, considerando funcionalidade, facilidade e sensação de controle.

**Reflexivo:** envolve interpretações, memórias, identidade e significado atribuído à experiência.

Isso demonstra que produtos não são avaliados exclusivamente por suas funcionalidades.

Uma interface organizada pode transmitir confiança. Uma resposta rápida e clara pode proporcionar sensação de controle. Um processo confuso pode gerar insegurança, mesmo quando o resultado técnico está correto.

O design emocional também inclui elementos de surpresa e diversão, desde que sejam adequados ao contexto e não comprometam a clareza das interações.

Em sistemas corporativos, muitas vezes uma experiência emocional positiva não depende de animações ou elementos visuais sofisticados, mas da sensação de segurança, previsibilidade e eficiência.

**Fundamentação:** Donald Norman, [Emotional Design: People and Things](https://jnd.org/emotional-design-people-and-things/).

## 10. UX e Engenharia de Software: uma responsabilidade compartilhada

Ao conectar os conceitos estudados com a Engenharia de Software, fica evidente que UX não deve ser considerada uma atividade restrita à criação de interfaces.

Ela influencia decisões durante todo o ciclo de desenvolvimento.

Na análise de requisitos, ajuda a compreender os problemas reais. Na definição da solução, contribui para a organização dos fluxos. No desenvolvimento, orienta interações e feedbacks. Nos testes, permite avaliar se o usuário consegue atingir seus objetivos.

Esse entendimento também pode ser incorporado a práticas ágeis, critérios de aceite e processos de melhoria contínua.

Uma funcionalidade não deveria ser considerada bem-sucedida apenas porque passou nos testes técnicos. Também precisamos compreender se ela entrega valor de maneira acessível, compreensível e eficiente.

**Minha principal reflexão é que qualidade de software não está apenas naquilo que construímos internamente, mas também na experiência que proporcionamos externamente.**

Como profissionais de tecnologia, precisamos equilibrar as necessidades dos usuários, os objetivos de negócio e as restrições técnicas.

Esse equilíbrio é fundamental para transformar implementações tecnicamente corretas em soluções verdadeiramente úteis.

## Conclusão

Estudar User Experience amplia nossa percepção sobre o que significa construir bons sistemas.

Os conceitos apresentados demonstram que uma experiência de qualidade envolve pesquisa, estratégia, organização da informação, prototipagem, usabilidade, acessibilidade e aspectos emocionais.

Mais do que desenvolver funcionalidades, precisamos compreender como a tecnologia participa da rotina das pessoas e quais problemas ela efetivamente resolve.

Na minha jornada pelo MBA em Engenharia de Software, esse é um dos aprendizados que considero importantes: **a Engenharia de Software precisa considerar tanto a qualidade técnica da solução quanto a experiência de quem vai utilizá-la.**

Afinal, software não existe apenas para executar processos. Ele existe para ajudar pessoas a alcançar objetivos.

---

### Referência acadêmica

FURTADO, Daniel. *User Experience (UX).* Material didático apresentado na disciplina de User Experience, MBA em Engenharia de Software, USP/Esalq, 12 nov. 2026.

As referências complementares estão vinculadas às respectivas seções do artigo.
