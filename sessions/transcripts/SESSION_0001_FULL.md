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

## [011] JOGADOR — 2026-11-23

gostei da distribuição do ladino, vou ficar com ela, e o idioma seria comum, goblin, anão, elfico, e giria de ladrão claro. vou com os dois antecendentes, guarda e artesão, quero a campanha para a questão dos pais dele, e o salão dos 6 sem ligação com esse acontecimento mas como duas campanhas principais na mesma campanha, para desenvolver o personagem eron river, o salão esta esquecido a milenios e ninguem mais lembra por isso é algo isolado do acontecimento dos pais dele, coloque como ele achou isso numa caçada a um lobo no monte veyra, ou de alguma forma conecte tudo... mas no começo que ninguem saiba ou se lembre do salão dos 6 e seus caminhos, e ja vamos terminar o personagem

**Anexos fornecidos junto à mensagem:** `Eron_River_Historia_Revisada.pdf`; `Thun-Khazad_Cronicas_do_Imperio_Esquecido.pdf`. PDFs referenciados, não copiados neste arquivo de transcrição. O conteúdo dos anexos não é fala literal do usuário.

## [012] MESTRE — 2026-11-23 (mensagem parcial visível, interrompida antes da resposta final)

# Eron River — Preparação da campanha e ficha

Li os dois documentos que você enviou: *Eron River — A Marca da Bigorna Velada* e *Thûn-Khazad — Crônicas do Império Esquecido*.

Vamos preservar a história revisada de Eron, seus 25 anos, a família que o criou, sua formação na forja, o serviço na Guarda Real e os acontecimentos que o levaram ao exílio.

Também fica estabelecido que teremos **uma campanha longa com duas tramas principais independentes**:

1. **A verdade sobre Aldren e Mirella River:** investigar os acontecimentos que destruíram a família de Eron e suas consequências.
2. **O Salão dos Seis Caminhos:** um mistério de exploração, engenharia e história antiga ligado ao Monte Veyra, mas não à conspiração envolvendo seus pais.

O Salão está esquecido há milênios. No começo da aventura, ninguém conhece sua localização, seus Caminhos ou sua verdadeira história. A possibilidade de descoberta surgirá naturalmente durante os acontecimentos, sem obrigar Eron a seguir esse caminho.

## Ficha de Eron River

<box border radius="xl" padding={3} gap={3}>
  <row align="center" gap={3}>
    <AsyncImage query="realistic dark medieval fantasy male human rogue adventurer age 25 messy black hair gray eyes lightly tanned fair skin short beard brown worn leather armor hood short sword bow muscular athletic portrait" aspectRatio="3:4" maxWidth="128px"/>
    <box flex="1" gap={1}>
      <title size="lg">Eron River</title>
      <text color="secondary" size="xs">Humano • 25 anos • 1,80 m</text>
      **Ladino / futuro Artífice**
      <text size="sm" color="secondary">Antecedentes: Guarda e Artesão</text>
      <badge color="secondary">Criação em andamento</badge>
    </box>
  </row>
  <divider color="subtle"/>
  <text weight="medium">Atributos confirmados</text>
  <grid columns={3} gap={2}>
    {#each [{n:"FOR",v:12,m:"+1"},{n:"DES",v:20,m:"+5"},{n:"CON",v:15,m:"+2"},{n:"INT",v:17,m:"+3"},{n:"SAB",v:15,m:"+2"},{n:"CAR",v:14,m:"+2"}] as a}
      <grid-item>
        <box background="surface-secondary" radius="md" padding={2} align="center" gap="2px">
          <text size="2xs" color="secondary" weight="medium">{a.n}</text>
          <title size="xl" tabularNums>{a.v}</title>
          <text size="xs" color="secondary">{a.m}</text>
        </box>
      </grid-item>
    {/each}
  </grid>
  <caption>Valores já incluem os bônus +2 Destreza e +1 Inteligência do antecedente Artesão, conforme sua escolha.</caption>
</box>

## Idiomas confirmados

Você poderá ter exatamente os idiomas que pediu, sem precisar de uma regra especial.

| Idioma | Origem |
|---|---|
| Comum | Criação do personagem |
| Goblin | Idioma adicional de criação |
| Anão | Idioma adicional de criação |
| Élfico | Idioma adicional da classe Ladino |
| Gíria de Ladrão | Característica de Ladino |

No nível 1, o Ladino de 2024 recebe Gíria de Ladrão e também aprende outro idioma. <Cite refs={["turn659651search0","turn659651search20"]}/>

Isso é particularmente coerente com a história: Goblin pela família de Brakka, Anão pelo convívio com Gruner e Élfico pelo contato com Thaelion.

## [013] JOGADOR — 2026-11-23

ta pera ae, agora vamos terminar de criar o personagem, me de o resultado dos dados e oque tenho que escolher e como passou de 18 para 20, vasmo chegar la juntos, oque eu preciso escolher até terminar o personagem

## [014] MESTRE — 2026-11-23

Perfeito! Vamos terminar a ficha de **Eron River juntos, uma escolha de cada vez**, sem pular nenhuma etapa.

Por enquanto, deixamos a campanha e o Salão dos Seis Caminhos de lado. Primeiro vamos concluir o personagem, conferir as regras e calcular tudo corretamente.

## 1. Resultado original dos dados

Você pediu que eu rolasse os atributos até conseguir uma combinação forte. Utilizamos **4d6, descartando o menor dado**, repetindo sequências completas até atingir o critério estabelecido.

A sequência escolhida foi a 40ª.

| Rolagem | Dados obtidos | Descartado | Resultado |
|---|---|---|---|
| 1 | 3, 1, 5, 4 | 1 | **12** |
| 2 | 6, 2, 6, 6 | 2 | **18** |
| 3 | 5, 5, 5, 1 | 1 | **15** |
| 4 | 3, 5, 6, 4 | 3 | **15** |
| 5 | 6, 4, 3, 6 | 3 | **16** |
| 6 | 5, 3, 6, 3 | Um dos 3 | **14** |

<box border radius="lg" padding={3} gap={2}>
  <text weight="medium" color="secondary" size="xs">Seus seis resultados originais, em ordem decrescente</text>
  <grid columns={6} gap={1}>
    {#each [18,16,15,15,14,12] as n,i}
      <grid-item>
        <box background={i===0?"rgba(30,140,80,0.10)":"surface-secondary"} radius="md" padding={{top:3,bottom:3,x:1}} align="center">
          <title size="lg" color={i===0?"success":"default"} tabularNums>{n}</title>
        </box>
      </grid-item>
    {/each}
  </grid>
  <text textAlign="center" weight="medium">Total: 90 pontos</text>
</box>

## 2. Como a Destreza passou de 18 para 20?

Na edição 2024, os bônus de atributos vêm do **antecedente**, não da espécie Humano.

O antecedente **Artesão** permite aumentar Força, Destreza ou Inteligência, escolhendo uma das seguintes distribuições:

- +2 em um desses atributos e +1 em outro.
- +1 em cada um dos três atributos.

Na distribuição que você escolheu, colocamos **+2 em Destreza e +1 em Inteligência**.

<box border radius="lg" padding={3} gap={3}>
  <grid columns={2} gap={3}>
    <grid-item>
      <text color="secondary" weight="medium" size="xs">DESTREZA</text>
      <row align="baseline" justify="center" gap={1}>
        <title size="2xl">18</title>
        <title color="secondary" size="md">+ 2 =</title>
        <title size="2xl" color="success">20</title>
      </row>
      <caption textAlign="center">Modificador final +5</caption>
    </grid-item>
    <grid-item>
      <text color="secondary" weight="medium" size="xs">INTELIGÊNCIA</text>
      <row align="baseline" justify="center" gap={1}>
        <title size="2xl">16</title>
        <title color="secondary" size="md">+ 1 =</title>
        <title size="2xl" color="success">17</title>
      </row>
      <caption textAlign="center">Modificador final +3</caption>
    </grid-item>
  </grid>
</box>

Portanto, **não modificamos as rolagens**. Apenas aplicamos os aumentos de atributos do antecedente, como a regra permite. O limite normal é 20.

## 3. Atributos finais que você escolheu

| Atributo | Dado | Bônus | Final | Modificador |
|---|---:|---:|---:|---:|
| Força | 12 | — | 12 | +1 |
| Destreza | 18 | +2 | **20** | **+5** |
| Constituição | 15 | — | 15 | +2 |
| Inteligência | 16 | +1 | **17** | **+3** |
| Sabedoria | 15 | — | 15 | +2 |
| Carisma | 14 | — | 14 | +2 |

Essa é a distribuição confirmada. É particularmente forte para um Ladino com futura multiclasse em Artífice.

Conferi a criação de personagens de 2024: o antecedente Artesão realmente permite esses aumentos, e nenhum deles pode elevar um atributo acima de 20. <Cite refs={["turn901867search1","turn901867search9","turn901867search18"]}/>

## 4. O que ainda falta escolher

| Etapa | Situação |
|---|---|
| Nome, espécie, idade e aparência | **Definidos:** Eron River, humano, 25 anos, 1,80 m |
| Atributos | **Definidos:** 12 / 20 / 15 / 17 / 15 / 14 |
| Antecedentes | **Definidos:** Artesão mecânico e Guarda narrativo |
| Talentos de origem | **Planejados:** Crafter pelo Artesão e Alerta pelo Humano |
| Idiomas | **Escolhidos:** Comum, Goblin, Anão, Élfico e Gíria de Ladrão |
| Classe e nível iniciais | **Falta confirmar:** Ladino de nível 1 ou outra configuração |
| Perícias e Especialização | **Falta escolher:** se começar Ladino, quatro perícias da classe, uma do Humano e duas Especializações |
| Ferramentas | **Falta escolher:** um tipo pelo Artesão e três tipos diferentes pelo Crafter |
| Maestrias em armas | **Falta escolher:** duas armas, se começar Ladino |
| Equipamento inicial | **Falta escolher:** itens ou ouro inicial, respeitando a história de Eron |
| Valores derivados | Eu calculo depois: PV, CA, iniciativa, testes de resistência, ataques e outros números |

As perícias **Investigação e Persuasão** já vêm do antecedente Artesão. A classe Ladino de 2024 traz quatro escolhas de perícias, duas Especializações e duas Maestrias em Armas no nível 1. <Cite refs={["turn901867search2","turn901867search18"]}/>

**Não precisamos escolher uma subclasse agora:** para Ladino, a subclasse chega no nível 3 da própria classe. A entrada em Artífice pode acontecer em uma progressão futura, quando você decidir.

## Próxima escolha — apenas uma por vez

**Você confirma que Eron começará como Ladino de nível 1, planejando adquirir níveis de Artífice futuramente?**

**[LOG DE MEMÓRIA DA CAMPANHA]**
- Localização Atual: Não definida; criação de personagem.
- NPCs Presentes e Relação: Nenhum em cena.
- Linha de Missão Ativa: Campanha ainda não iniciada; preparação narrativa pausada para terminar a ficha.
- Eventos Cruciais Ocorridos: Atributos finais confirmados; antecedentes Guarda e Artesão; idiomas escolhidos; intenção de multiclasse.
- Condições do Jogador: Eron River, humano, 25 anos, 1,80 m; FOR 12, DES 20, CON 15, INT 17, SAB 15, CAR 14. Classe inicial ainda não confirmada.

**GitHub:** atualizações da ficha, índice e transcrição pré-campanha confirmadas por commit.

## [015] JOGADOR — 2026-11-23

ladino nivel 1, correto

## [016] MESTRE — 2026-11-23

<badge color="success"><icon name="check-circle" inline/> Confirmado</badge>

**Eron River começará como Ladino de nível 1**, seguindo as regras de D&D 5E (2024).

O Artífice ficará para uma futura evolução, quando você decidir adquirir níveis nessa classe.

Com os atributos já definidos, Eron começa com:

| Característica | Valor |
|---|---|
| Nível | 1 |
| Classe | Ladino |
| Pontos de Vida | **10 PV** |
| Bônus de Proficiência | +2 |
| Destreza | 20 (+5) |
| Inteligência | 17 (+3) |
| Testes de Resistência proficientes | Destreza e Inteligência |
| Ataque Furtivo | 1d6 |
| Talentos de origem | Artesão (Crafter) e Alerta |

Os 10 PV vêm de 8 pontos iniciais da classe Ladino + 2 do modificador de Constituição.

## Próxima escolha: 4 perícias de Ladino

O antecedente Artesão já concede **Investigação e Persuasão**, portanto não precisamos escolhê-las novamente.

Das perícias da classe Ladino, você pode escolher **quatro** entre: **Acrobacia, Atletismo, Enganação, Intuição, Intimidação, Percepção, Prestidigitação e Furtividade**. <Cite ref="turn452788search0"/>

Minha sugestão para o investigador Eron River é **Percepção, Furtividade, Intuição e Enganação**. A perícia adicional do Humano pode ser escolhida depois, assim como as duas Especializações.

**Quais quatro perícias você quer para Eron?**

**[LOG DE MEMÓRIA DA CAMPANHA]**
- Localização Atual: Não definida — ficha em criação.
- NPCs Presentes e Relação: Nenhum em cena.
- Linha de Missão Ativa: Nenhuma; campanha ainda não iniciada.
- Eventos Cruciais Ocorridos: Eron confirmado como Ladino de nível 1.
- Condições do Jogador: 10 PV máximos; FOR 12, DES 20, CON 15, INT 17, SAB 15, CAR 14; perícias e equipamentos ainda pendentes.

**GitHub:** commit confirmado para ficha, índice e transcrição pré-campanha.

## [017] JOGADOR — 2026-11-23

vamos começar com os dois antecedentes por inteiro, sem ser narrativo, artesão e guarda

## [018] MESTRE — 2026-11-23

**Aprovado, Eron River terá os dois antecedentes completos: Guarda e Artesão, com todos os benefícios mecânicos de ambos.**

Como Mestre do Santuário, autorizo essa exceção para Eron. Será uma **regra própria da nossa mesa (homebrew)**, pois o D&D 5E 2024 normalmente permite apenas um antecedente completo. <Cite ref="turn714023search13"/>

## Benefícios dos dois antecedentes

| Benefício | Artesão | Guarda |
|---|---|---|
| Aumento de atributos | +2 e +1, ou +1/+1/+1 | +2 e +1, ou +1/+1/+1 |
| Talento de origem | Crafter | Alerta |
| Perícias | Investigação e Persuasão | Atletismo e Percepção |
| Ferramentas | 1 tipo de ferramenta de artesão | 1 tipo de conjunto de jogo |
| Equipamentos iniciais | Pacote completo ou 50 PO | Pacote completo ou 50 PO |

<Cite refs={["turn956807view0","turn956807view1"]}/>

Além disso, como Humano de 2024, Eron recebe **mais um talento de origem à escolha**, pela característica Versátil, e outra proficiência em perícia, pela característica Habilidoso. <Cite ref="turn956807view3"/>

Isso significa que ele terá:

- **3 talentos de origem:** Crafter, Alerta e mais um à sua escolha.
- **4 perícias dos antecedentes:** Investigação, Persuasão, Atletismo e Percepção.
- **4 proficiências em ferramentas de artesão:** uma do antecedente e três do Crafter, desde que diferentes e elegíveis.
- **1 proficiência em conjunto de jogo**, pelo Guarda.
- **Os dois conjuntos de aumentos de atributos**, respeitando o limite de 20 por atributo.
- **Os dois pacotes de equipamento**, além do equipamento inicial da classe Ladino, escolhendo as opções correspondentes.

Essa combinação torna Eron consideravelmente mais poderoso e versátil do que um personagem de nível 1 criado pelas regras padrão. Estou permitindo isso conscientemente, sem modificar os resultados dos dados.

## Vamos distribuir os bônus do Guarda

Já aplicamos os bônus do Artesão:

| Atributo | Dado original | Artesão | Atual |
|---|---:|---:|---:|
| Força | 12 | — | 12 |
| Destreza | 18 | +2 | **20** |
| Constituição | 15 | — | 15 |
| Inteligência | 16 | +1 | **17** |
| Sabedoria | 15 | — | 15 |
| Carisma | 14 | — | 14 |

O antecedente Guarda permite aumentar **Força, Inteligência e Sabedoria**.

Você pode colocar **+2 em um desses atributos e +1 em outro**, ou distribuir **+1 em cada um dos três**.

Minha recomendação para um futuro Ladino/Artífice é **+2 em Inteligência e +1 em Sabedoria**. Com isso, Eron ficaria com:

| Atributo | Resultado após os dois antecedentes |
|---|---:|
| Força | 12 (+1) |
| Destreza | 20 (+5) |
| Constituição | 15 (+2) |
| Inteligência | **19 (+4)** |
| Sabedoria | **16 (+3)** |
| Carisma | 14 (+2) |

Outra possibilidade é **+1 em Força, +1 em Inteligência e +1 em Sabedoria**: ficaria com FOR 13, INT 18 e SAB 16. Ambas respeitam o limite de 20.

**Você prefere minha sugestão (+2 Inteligência e +1 Sabedoria) ou quer distribuir os bônus de outra forma?** Depois dessa decisão, passamos às perícias, ferramentas, talento adicional e equipamentos, uma etapa por vez.

**[LOG DE MEMÓRIA DA CAMPANHA]**
- Localização Atual: Não definida — criação de personagem.
- NPCs Presentes e Relação: Nenhum em cena.
- Linha de Missão Ativa: Nenhuma; campanha ainda não iniciada.
- Eventos Cruciais Ocorridos: Guarda e Artesão aprovados integralmente, como exceção mecânica registrada; Ladino 1 confirmado.
- Condições do Jogador: Eron River, humano, 25 anos, 1,80 m; 10 PV máximos; FOR 12, DES 20, CON 15, INT 17, SAB 15, CAR 14 antes do bônus do Guarda.

**GitHub:** commits confirmados para regra própria, pré-ficha, índice e transcrição.

## [019] JOGADOR — 2026-11-23

aceito sim

## [020] MESTRE — 2026-11-23

<badge color="success"><icon name="check-circle" inline/> Atributos confirmados</badge>

Perfeito! Eron River receberá **+2 em Inteligência e +1 em Sabedoria** pelo antecedente Guarda, além dos bônus que já recebeu de Artesão.

## Atributos definitivos de Eron River

| Atributo | Dados | Artesão | Guarda | Final | Mod. |
|---|---:|---:|---:|---:|---:|
| Força | 12 | — | — | **12** | +1 |
| Destreza | 18 | +2 | — | **20** | +5 |
| Constituição | 15 | — | — | **15** | +2 |
| Inteligência | 16 | +1 | +2 | **19** | +4 |
| Sabedoria | 15 | — | +1 | **16** | +3 |
| Carisma | 14 | — | — | **14** | +2 |

Os bônus dos dois antecedentes são uma regra especial que aprovamos para Eron. Nenhum valor ultrapassa o limite de 20.

Essa distribuição é excelente para um Ladino investigador que pretende adquirir níveis de Artífice.

## Próxima etapa — quatro perícias de Ladino

Já temos quatro perícias concedidas pelos dois antecedentes completos:

- **Artesão:** Investigação e Persuasão.
- **Guarda:** Atletismo e Percepção.

Como Ladino de nível 1, Eron deve escolher **quatro perícias adicionais** dentre estas seis ainda disponíveis:

{@body const skillOptions = ["Acrobacia","Enganação","Intuição","Intimidação","Prestidigitação","Furtividade"]}
{@body const [selectedSkills, setSelectedSkills] = DIL.useState(["Enganação","Intuição","Prestidigitação","Furtividade"])}
<box border radius="lg" padding={3} gap={3}>
  <text weight="medium">Escolha quatro perícias</text>
  <text size="xs" color="secondary">Minha sugestão inicial está marcada. Você pode alterar as escolhas.</text>
  <grid columns={2} gap={2}>
    {#each skillOptions as skill}
      <grid-item>
        <checkbox checked={selectedSkills.includes(skill)} disabled={!selectedSkills.includes(skill)&&selectedSkills.length>=4} onChange={(checked)=>setSelectedSkills(prev=>checked?[...prev,skill]:prev.filter(x=>x!==skill))} lineThrough={false}>{skill}</checkbox>
      </grid-item>
    {/each}
  </grid>
  <row align="center" justify="between">
    <text color="secondary" size="xs">{selectedSkills.length} de 4 selecionadas</text>
    <button disabled={selectedSkills.length!==4} onClick={()=>GenUI.issueNewTurn("Escolho estas quatro perícias da classe Ladino para Eron River: "+selectedSkills.join(", ")+".")}>Confirmar perícias</button>
  </row>
</box>

Depois, escolheremos separadamente a **perícia adicional do Humano**, as duas Especializações e o restante da ficha.

**[LOG DE MEMÓRIA DA CAMPANHA]**
- Localização Atual: Indefinida; ficha em criação.
- NPCs Presentes e Relação: Nenhum em cena.
- Linha de Missão Ativa: Nenhuma; campanha não iniciada.
- Eventos Cruciais Ocorridos: Aumentos dos dois antecedentes confirmados; atributos definitivos de Eron registrados.
- Condições do Jogador: Humano, Ladino 1, 10 PV máximos; FOR 12, DES 20, CON 15, INT 19, SAB 16, CAR 14.

**GitHub:** commits confirmados para atualização da ficha, índice e transcrição pré-campanha.
