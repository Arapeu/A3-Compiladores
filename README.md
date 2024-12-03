# A3-Compiladores

# Compilador Latinus

## 1. Autores do Projeto
- **Elias Neves Conceição** – 12722127604  
- **Felipe Checcucci Ribeiro Rangel** – 12722211197  
- **Pedro Henrique de Araújo Ribeiro** – 1272122069  
- **Petson Brenner Santos Alves** – 12722130640  
- **João Victor Moura Brandão** – 1272123051  

---

## 2. Introdução
O desafio proposto foi desenvolver um compilador que atendesse aos requisitos léxicos e sintáticos de uma linguagem fictícia, capaz de converter código para outra linguagem preexistente.  
A linguagem escolhida como alvo foi o **Python**, devido à familiaridade da maioria dos integrantes do grupo com essa linguagem.  

A linguagem fictícia criada, denominada **Latinus**, tem como conceito central o uso de palavras reservadas, comandos e tipos de dados traduzidos para o latim. O latim, apesar de ser uma língua morta, é amplamente documentado e reconhecido como a “língua mãe” de muitos idiomas modernos, como português, espanhol, italiano, francês e romeno.

---

## 3. Estrutura da Linguagem Latinus
Os tokens da linguagem e suas equivalências em Python são apresentados a seguir:

| **Latinus**  | **Python**  | **Descrição**       |
|--------------|-------------|---------------------|
| `TOTUM`      | `int`       | Tipo inteiro        |
| `DECIMALE`   | `float`     | Tipo float          |
| `VERBUM`     | `str`       | Tipo string         |
| `LEGERE()`   | `print()`   | Função `print`      |
| `SCRIBE()`   | `input()`   | Função `input`      |
| `TRACTUS`    | `range()`   | Função `range`      |
| `IN`         | `in`        | Operador `in`       |
| `CASUS`      | `if`        | Estrutura `if`      |
| `ALITER`     | `else`      | Estrutura `else`    |
| `DUM`        | `while`     | Estrutura `while`   |
| `TO`         | `for`       | Estrutura `for`     |

---

## 4. Bibliotecas Utilizadas
Para a implementação do compilador, foram empregadas as seguintes bibliotecas:
- **PLY (Python Lex-Yacc)**: Utilizada para facilitar a criação do analisador léxico e sintático. Permitiu uma abordagem robusta e eficiente para a análise do código fonte.
- **Tkinter**: Usada para desenvolver a interface do terminal do compilador. Foi escolhida por suas ferramentas versáteis e facilidade de integração com projetos em Python.

---

## 5. Ambiente de Desenvolvimento
O projeto foi desenvolvido na **IDE Visual Studio Code**, escolhida pela sua popularidade e pelas funcionalidades que tornam o ambiente de trabalho eficiente e intuitivo.

---

## 6. Dificuldades Encontradas Durante o Processo
Ao longo do desenvolvimento do compilador, enfrentamos os seguintes desafios:

1. **Estabelecimento da Tabela de Precedência**  
   - Erros na definição inicial causaram problemas, que foram corrigidos após diversas revisões e pesquisas.

2. **Redundância no Parser**  
   - Funções duplicadas geraram ambiguidades, resultando em **warnings de shift/reduce**. Após reescrever funções e ajustar a tabela de precedência, conseguimos reduzir de 120 para 0 warnings.

3. **Problemas de Colaboração Simultânea**  
   - Alterações simultâneas ocasionaram exclusão acidental de linhas e duplicidade de funções. A boa comunicação entre os integrantes ajudou a solucionar essas questões.

---

## 7. Conclusões Finais
O desenvolvimento do **Compilador Latinus** foi uma experiência enriquecedora, unindo criatividade e aprendizado técnico. Apesar dos desafios, como a correção da tabela de precedência e a resolução de ambiguidades no parser, o projeto destacou:
- A importância do trabalho em equipe;
- A dedicação contínua à resolução de problemas;
- A escolha única do latim como base para a linguagem fictícia, agregando valor cultural.

O projeto não apenas cumpriu os requisitos propostos, mas também expandiu as habilidades dos integrantes, deixando uma base sólida para futuras iniciativas.

---


### 🛠 **Como Executar**
1. Certifique-se de ter o Python instalado.
2. Clone o repositório:  
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
