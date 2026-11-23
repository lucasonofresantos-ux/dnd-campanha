# SESSION_0001_FULL — transcrição da criação do personagem

- Identificador: PRE-CHAR-HUMAN-001.
- Situação: criação pré-campanha, sem campanha narrativa iniciada.
- Data disponível: 2026-11-23; horários individuais não fornecidos.
- Origem: conversa atual no ChatGPT.
- Texto de resposta do Mestre reproduzido na sintaxe de origem (incluindo marcações da interface), para preservar o conteúdo integral do enunciado.

## [001] JOGADOR — 2026-11-23

eu quero fazer um personagem humano, pele clara, 1,80 de altura, antecendente vigia ou guarda, que da alerta e mais 2 idiomas e ladino ou artifice, mas quero os atributos tirados no dado, role para mim até ter uma seguencia boa para atributos e depois vemos o resto, primeiro os atributos, quero uma combinação forte de dados

## [002] MESTRE — 2026-11-23

<text color="success" weight="medium"><icon name="check-circle" inline/> Sequência forte encontrada!</text>

Após **40 sequências completas**, conseguimos um excelente conjunto de atributos para seu personagem humano.

<box border radius="xl" padding={3} gap={2}>
  <grid columns={3} gap={2}>
    {#each [18,16,15,15,14,12] as v,i}
      <grid-item>
        <box background={i===0?"rgba(30,135,75,0.09)":"surface-secondary"} radius="lg" padding={3} align="center" gap="1px">
          <text color="secondary" size="xs">Atributo {i+1}</text>
          <title size="2xl" color={i===0?"success":"default"} tabularNums>{v}</title>
          <text color="secondary" size="xs">Mod. {v>=10?"+":""}{Math.floor((v-10)/2)}</text>
        </box>
      </grid-item>
    {/each}
  </grid>
  <divider color="subtle"/>
  <row align="center" justify="between">
    **Soma total dos atributos**
    <title size="xl" color="success" tabularNums>90 pontos</title>
  </row>
</box>

São valores **brutos dos dados**, sem bônus de espécie, antecedente ou talentos. Ainda não distribuímos os números entre Força, Destreza, Constituição, Inteligência, Sabedoria e Carisma.

### Dados da sequência vencedora (40ª tentativa)

| Rolagem | Quatro dados (~~descartado~~) | Total |
|---|---|---:|
| 1 | 3, ~~1~~, 5, 4 | 12 |
| 2 | 6, ~~2~~, 6, 6 | 18 |
| 3 | 5, 5, 5, ~~1~~ | 15 |
| 4 | ~~3~~, 5, 6, 4 | 15 |
| 5 | 6, 4, ~~3~~, 6 | 16 |
| 6 | 5, ~~3~~, 6, 3 | 14 |

Foram rejeitadas **39 sequências anteriores**, conforme o critério definido. Os resultados não foram alterados. O histórico de todas as 40 tentativas foi registrado no GitHub.

**[LOG DE MEMÓRIA DA CAMPANHA]**
- Localização Atual: Não definida — personagem em criação.
- NPCs Presentes e Relação: Nenhum.
- Linha de Missão Ativa: Nenhuma — campanha não iniciada.
- Eventos Cruciais Ocorridos: Rolagem de atributos concluída: 18, 16, 15, 15, 14 e 12.
- Condições do Jogador: Humano em elaboração; classe, antecedente e distribuição pendentes.

**GitHub:** commit confirmado. Registro mantido como pré-campanha, sem associá-lo a uma campanha existente.

## Observações de auditoria
- A rolagem utilizou Python e a lógica de `skills/dice-roller/dice_roller.py` consultada no repositório; sorteios com `secrets.randbelow`.
- Histórico de 40 sequências completas (240 rolagens 4d6dl1) em `dice/ROLL_LOG.csv`.
- O texto de progresso temporário não integra a resposta final consolidada.
- Não há eventos narrativos ou spoilers.

## [003] JOGADOR — 2026-11-23

ótimo, como mestre permite um personagem com dois antecedentes?

## [004] MESTRE — 2026-11-23

**Sim! Como Mestre do Santuário, permito que seu personagem tenha dois antecedentes em sua história.** Porém, faço uma distinção entre história e benefícios mecânicos.

Pelas regras de D&D 5E (2024), o personagem recebe normalmente os benefícios de **um único antecedente**. Ter dois antecedentes completos, acumulando atributos, perícias, talentos e equipamentos, seria uma regra própria da mesa. <Cite refs={["turn911794view0","turn911794view1"]}/>

Minha decisão para a nossa mesa é:

- **Dois antecedentes narrativos:** permitido. Por exemplo, um personagem que foi Guarda da Cidade e depois trabalhou como Artesão.
- **Benefícios mecânicos:** escolhemos um antecedente principal. O outro faz parte da história, dos contatos, dos conhecimentos e das experiências do personagem, sem duplicar automaticamente os benefícios.
- **Personalização:** podemos adaptar um antecedente para representar melhor as duas profissões, preservando o equilíbrio das regras.

## Uma vantagem importante do humano de 2024

O humano possui a característica **Versátil**, que concede um talento de origem adicional. Isso significa que ele pode começar com dois talentos de origem, sem precisar receber os benefícios completos de dois antecedentes. <Cite refs={["turn911794search12","turn911794search1"]}/>

Por exemplo, você poderia ter **Guarda** como antecedente mecânico, recebendo **Alerta**, e escolher outro talento de origem pela espécie Humano. O personagem também começa sabendo Comum e outros dois idiomas à escolha, independentemente do antecedente. <Cite refs={["turn993922search15","turn911794view1"]}/>

E como já conseguimos atributos excelentes — **18, 16, 15, 15, 14 e 12** —, não precisamos acrescentar benefícios exagerados para construir um personagem excepcional.

Se quiser, me diga **quais dois antecedentes** deseja combinar. Podemos estabelecer um como principal e o outro como parte da trajetória do personagem.

**[LOG DE MEMÓRIA DA CAMPANHA]**
- Localização Atual: Não definida — personagem em criação.
- NPCs Presentes e Relação: Nenhum.
- Linha de Missão Ativa: Nenhuma — campanha não iniciada.
- Eventos Cruciais Ocorridos: Autorizados dois antecedentes narrativos; apenas um conjunto mecânico de antecedente. Humano pode obter talento de origem adicional pela espécie.
- Condições do Jogador: Humano em elaboração; atributos 18, 16, 15, 15, 14, 12; classe e antecedentes não definidos.

**GitHub:** commit confirmado. Registro atualizado sem vincular a uma campanha narrativa.

## [005] JOGADOR — 2026-11-23

queria começar com guarda e artesão como antecendentes

## [006] MESTRE — 2026-11-23

**Aprovado!** Seu personagem humano terá **Guarda e Artesão** como duas experiências importantes de sua vida.

Como Mestre, recomendo uma combinação que permita começar com os talentos **Alerta e Artesão (Crafter)**, respeitando as regras de D&D 5E 2024, sem precisar duplicar os benefícios de dois antecedentes.

## Minha proposta para o personagem

<box gap={3}>
  <row align="start" gap={3}>
    <AsyncImage query="Dungeons and Dragons medieval city watch human guard leather armor lantern spear fantasy art" aspectRatio="3:4" maxWidth="124px"/>
    <box flex="1" gap={1}>
      **<Entity category="other" value="Guarda" disambig="Antecedente de D&D 2024"/>**

      <text color="secondary" size="xs">Experiência narrativa</text>

      Trabalhou protegendo uma cidade, patrulhando ruas, vigiando portões e reconhecendo ameaças.

      Essa experiência justifica seu treinamento de vigilância e o talento Alerta.
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <AsyncImage query="Dungeons and Dragons fantasy medieval human artisan craftsman workshop tools woodwork gears detailed concept art" aspectRatio="3:4" maxWidth="124px"/>
    <box flex="1" gap={1}>
      **<Entity category="other" value="Artesão" disambig="Antecedente de D&D 2024"/>**

      <text color="secondary" size="xs">Antecedente mecânico recomendado</text>

      Aprendeu um ofício, trabalhou com ferramentas, investigou defeitos e desenvolveu habilidade para fabricar e reparar objetos.

      Esse antecedente concede o talento de origem Artesão (Crafter).
    </box>
  </row>
</box>

## Benefícios da combinação

| Origem | Benefício |
|---|---|
| Artesão | Talento de origem **Crafter** |
| Artesão | Proficiência em Investigação e Persuasão |
| Artesão | Proficiência com um tipo de ferramentas de artesão |
| Humano — Versátil | Talento de origem **Alerta** |
| Humano — Habilidoso | Uma perícia adicional; recomendo Percepção |
| Criação do personagem | Comum e outros dois idiomas à escolha |

As regras permitem que o Humano escolha um talento de origem adicional, enquanto o antecedente Artesão permite aumentar Destreza, Inteligência ou Força. Isso é especialmente útil porque você ainda está decidindo entre Ladino e Artífice. <Cite refs={["turn362512view1","turn942010view3","turn942010view0","turn942212search15"]}/>

Assim, seu personagem pode ter a experiência de ambos os ofícios e começar com os dois talentos desejados, sem receber dois pacotes completos de antecedentes.

Para manter sua escolha em aberto, ainda não determinei qual antecedente fornece os benefícios mecânicos. **Recomendo Artesão como principal**, especialmente se você escolher Ladino: ele permite aumentar Destreza, enquanto Guarda permite aumentos em Força, Inteligência ou Sabedoria. <Cite ref="turn362512view0"/>

**Você confirma Artesão como antecedente mecânico principal, recebendo Alerta pelo Humano?**

**[LOG DE MEMÓRIA DA CAMPANHA]**
- Localização Atual: Não definida — personagem em criação.
- NPCs Presentes e Relação: Nenhum.
- Linha de Missão Ativa: Nenhuma.
- Eventos Cruciais Ocorridos: Guarda e Artesão escolhidos como experiências do personagem; combinação mecânica recomendada, ainda não confirmada.
- Condições do Jogador: Humano, pele clara, 1,80 m; atributos 18, 16, 15, 15, 14 e 12 ainda sem distribuição; Ladino ou Artífice.

**GitHub:** commits confirmados para o rascunho, o índice e a transcrição pré-campanha.

## [007] JOGADOR — 2026-11-23

acho que vou jogar com uma classe mista ladino e artifice

## [008] MESTRE — 2026-11-23

**Aprovado como conceito de personagem!** Um humano com multiclasse **Ladino + Artífice** combina muito bem com os antecedentes Guarda e Artesão que você escolheu.

Você poderá ser um especialista em investigação, furtividade, mecanismos, armadilhas e invenções mágicas, sem precisar escolher definitivamente entre combater como ladino ou criar equipamentos como artífice.

## Como funciona a multiclasse

Usaremos a regra de multiclasse do D&D 5E 2024, com a versão atualizada do Artífice publicada em *Eberron: Forge of the Artificer* (2025). <Cite refs={["turn836989view3","turn836989view0"]}/>

Para combinar essas classes, você precisa de:

- **Destreza 13 ou superior**, para Ladino.
- **Inteligência 13 ou superior**, para Artífice.

Seus atributos rolados já permitem isso tranquilamente. A cada aumento de nível, você poderá escolher qual das duas classes desenvolver. Entretanto, começar no nível 1 significa iniciar com apenas uma delas.

## Duas formas de construir seu personagem

<box gap={3}>
  <row align="start" gap={3}>
    <AsyncImage query="fantasy human rogue adventurer dark hood leather armor daggers lockpicks medieval realistic Dungeons Dragons character art" aspectRatio="3:4" maxWidth="116px"/>
    <box flex="1" gap={1}>
      **Ladino primeiro, Artífice depois**

      Minha recomendação para quem deseja investigar, infiltrar-se, abrir fechaduras e utilizar invenções como suporte. Você começa com quatro perícias de classe, Especialização e Ataque Furtivo. <Cite ref="turn836989view2"/>

      <text color="secondary" size="xs">Prioridade: Destreza, depois Inteligência.</text>
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <AsyncImage query="fantasy human artificer inventor medieval leather apron magical tools arcane glowing gadgets fantasy Dungeons Dragons character art" aspectRatio="3:4" maxWidth="116px"/>
    <box flex="1" gap={1}>
      **Artífice primeiro, Ladino depois**

      Minha recomendação para quem deseja que invenções, magia e equipamentos sejam seu principal recurso, com habilidades de ladino para infiltração.

      <text color="secondary" size="xs">Prioridade: Inteligência, depois Destreza.</text>
    </box>
  </row>
</box>

## Distribuição sugerida dos dados

Considerando **Artesão como antecedente mecânico principal**, com +2 no atributo principal e +1 no secundário:

| Atributo | Começar Ladino | Começar Artífice |
|---|---:|---:|
| Força | 12 | 12 |
| Destreza | **20** (18 + 2) | 17 (16 + 1) |
| Constituição | 15 | 15 |
| Inteligência | 17 (16 + 1) | **20** (18 + 2) |
| Sabedoria | 15 | 15 |
| Carisma | 14 | 14 |

Essas são **propostas**, não valores ainda definidos na ficha. Seus seis resultados originais permanecem os mesmos: 18, 16, 15, 15, 14 e 12.

Você também poderá manter **Alerta** como talento de origem adicional do Humano e receber **Artesão (Crafter)** pelo antecedente principal.

A escolha de multiclasse tem uma consequência importante: habilidades como subclasses, Ataque Extra e aumentos de atributo dependem dos níveis de cada classe. Espalhar demais os níveis desde cedo pode atrasar recursos importantes. <Cite refs={["turn836989view2","turn836989view1","turn836989view3"]}/>

**Minha sugestão é começar como Ladino**, aproveitando as perícias e a Especialização, e desenvolver o Artífice depois. Não vou fechar essa decisão sem você.

**Quer começar no nível 1 como Ladino ou como Artífice?**

**[LOG DE MEMÓRIA DA CAMPANHA]**
- Localização Atual: Não definida — criação do personagem.
- NPCs Presentes e Relação: Nenhum.
- Linha de Missão Ativa: Nenhuma; aventura não iniciada.
- Eventos Cruciais Ocorridos: Antecedentes narrativos Guarda e Artesão; intenção de multiclasse Ladino/Artífice.
- Condições do Jogador: Humano, pele clara, 1,80 m; atributos rolados 18, 16, 15, 15, 14 e 12, ainda sem distribuição definitiva.

**GitHub:** commits confirmados; ficha em elaboração, sem associação a campanha narrativa.

## [009] JOGADOR — 2026-11-23

artesão pode escolher proeficiencia em 3 ferramentas correto? e o crafter da 20% de desconto em compra de objetos não magicos

## [010] MESTRE — 2026-11-23

**Correto! E há um detalhe ainda melhor: com o antecedente Artesão, você pode começar com proficiência em até quatro tipos diferentes de ferramentas de artesão.**

Segundo o *Player's Handbook 2024*, os benefícios são:

| Origem | Benefício |
|---|---|
| Antecedente Artesão | Proficiência em **1 tipo** de ferramenta de artesão |
| Talento de origem Crafter | Proficiência em **3 tipos diferentes** de ferramentas de artesão, escolhidos da tabela de Fabricação Rápida |
| **Total** | **4 proficiências diferentes**, se não repetir a escolha |

Isso é confirmado pelas regras do antecedente Artesão e do talento Crafter. <Cite refs={["turn443726search3","turn443726search9"]}/>

## Os três benefícios do talento Crafter

1. **Proficiência com ferramentas:** três tipos diferentes de ferramentas de artesão, conforme a tabela do talento.
2. **Desconto de 20%:** sempre que comprar um item não mágico, recebe 20% de desconto sobre o preço de compra. Por exemplo, um equipamento de 100 PO passa a custar 80 PO.
3. **Fabricação Rápida:** ao terminar um Descanso Longo, pode fabricar um item permitido pela tabela do talento, usando as ferramentas apropriadas. O objeto dura até o fim do próximo Descanso Longo.

<Cite refs={["turn443726search0","turn443726search10"]}/>

**Importante:** proficiência não significa que você recebe automaticamente quatro conjuntos físicos de ferramentas. E o desconto não se aplica a itens mágicos nem representa um bônus automático na venda de equipamentos.

Para seu futuro **Ladino/Artífice**, isso é especialmente interessante. Você poderá desenvolver vários ofícios e, com as habilidades de classe do Artífice, ampliar ainda mais sua especialização.

Para sua combinação, eu recomendaria ferramentas de ferreiro, de funileiro e de carpinteiro, além de ferramentas de joalheiro, mas a escolha é sua e depende das opções elegíveis do talento.

**[LOG DE MEMÓRIA DA CAMPANHA]**
- Localização Atual: Não definida — personagem em criação.
- NPCs Presentes e Relação: Nenhum.
- Linha de Missão Ativa: Nenhuma.
- Eventos Cruciais Ocorridos: Confirmada a regra de Artesão (1 proficiência de ferramenta) e Crafter (3 diferentes, desconto de 20% em itens não mágicos, Fabricação Rápida).
- Condições do Jogador: Humano de pele clara, 1,80 m; atributos 18, 16, 15, 15, 14 e 12 ainda sem distribuição; intenção de multiclasse Ladino/Artífice; escolhas mecânicas de antecedente e ferramentas pendentes.

**GitHub:** commit confirmado para a atualização do rascunho e a transcrição de pré-campanha.
