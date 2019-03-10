#  TrampoÁgil
### Conectando recrutadores e candidatos de forma ágil

Nossa proposta é viabilizar candidaturas às vagas de maneira ágil, quebrando o silêncio e a espera por retornos e/ou feedbacks.

## A Metodolodia Ágil

Uma das grandes características da gestão de projetos baseados em metodologia ágil é a capacidade de controlar as etapas de projeto (sprints) de maneira clara, simples e bem definida.

Em nosso mundo do TrampoÁgil, cada candidatura segue um fluxo pré-definido por nossa plataforma, porém, com a flexibilidade de cada empresa/recrutador definir qual prazo cada sprint deverá ter.

Empresas podem customizar o seu fluxo de processo seletivo. Candidatos podem se candidatar às vagas nas empresas que possuam os fluxos mais condizentes ao seu atual momento.

## Como Funciona o Fluxo de Processo Seletivo

Um fluxo básico sugerido seria semelhante ao abaixo:

```
Status 1: Candidatura
- Etapa inicial do workflow de processo seletivo
- A empresa: disponibiliza a vaga com um prazo pré-definido de expiração (sugestão - 30 a 60 dias)
- O candidato: se candidata à vaga a qualquer momento dentro da janela de candidatura
- Ao fim do prazo, a empresa deve informar se o candidato será entrevistado ou não
```

```
Status 2: Entrevista
- Segunda etapa, caso o candidato passe pela etapa inicial
- A empresa: agenda data, horário e local de entrevista (sugestão: até 2 semanas após aceite da candidatura)
- O candidato: comparece à entrevista (ou entrevistas)
- Ao fim do prazo, o workflow segue automaticamente para Análise
```

```
Status 3: Análise
- Terceira etapa, após entrevistas
- A empresa: analisa a candidatura e define quem será contratado (sugestão: entre 1 e 2 semanas após entrevistas)
- O candidato: aguarda a análise, sabendo que a empresa entrará em contato até determinado dia
- Ao fim do prazo, a empresa deve seguir para o status de feedback
```

```
Status 4: Feedback
- Última etapa, finalizando o fluxo de processo seletivo
- A empresa: expõe o feedback ao candidato, contratando-o ou não
- O candidato: aceita a contratação ou se candidata à outras vagas
```

## Detalhes da Aplicação

### Minimum Viable Product (Produto Mínimo Viável)

Ainda em nível de desenvolvimento, nosso MVP contempla os fluxos de cadastro de empresas e candidatos, além da captação de candidatos, com um painel de vagas para todos os interessados popularem a plataforma.

Existe a "dor" de um candidato receber contatos das empresas, inclusive participar de processos seletivos e entrevistas, mas sem receber retornos ou feedbacks.

Acreditamos que um prazo e um fluxo bem definidos promove um maior bem estar ao candidato, e um feedback bem estruturado garante um crescimento exponencial.

No próximo Release, as empresas poderão cadastrar suas respectivas vagas.

### App Revenue Model $$

Nossa plataforma segue o modelo de Subscription, onde cada empresa e candidato pode aderir à plataforma pagando uma subscription mensal. A implantação deverá ocorrer com PayPal nos primeiros meses de beta.

A gratuidade ocorre quando:

* Um usuário não logado desejar conferir as vagas ofertadas, mas sem direito à candidatura
* Uma empresa ou um candidato que deseja testar a plataforma por 30 dias, sem custos adicionais

## Tecnologias da Aplicação

* [Django](https://www.djangoproject.com/) - O framework web utilizado
* [Heroku](https://www.heroku.com/) - Plataforma de hospedagem da aplicação

## Autores

* **Daniel Ogata** - [dankogata](https://github.com/dankogata)
* **Gabriel Nascimento** - [gabrielfallcon](https://github.com/gabrielfallcon)
* **Leandro Vieira** - [leandrovi](https://github.com/leandrovi)
* **Natália Sakamoto** - [nataliareikos](https://github.com/nataliareikos)
* **Vanessa Martins** - [Neeehmartins](https://github.com/Neeehmartins)
