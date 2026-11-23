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
