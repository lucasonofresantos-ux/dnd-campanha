# Sessão 0000 — Continuação MR — Marco de pedra e flechas

Campanha: As Cinzas da Coroa Esquecida
Registro: 2026-10-17

## Mensagem 0720 — Jogador (literal)

Bem, eu vou pegar minhas duas flechas e vamos examinar este marco.
Role percepção e investigação para o marco

## Mensagem de andamento visível do Mestre (literal)

Vou conferir a posição das duas flechas e o último estado da campanha antes de resolver a ação. Depois executo Percepção e Investigação com o rolador Python, examino o marco conforme os resultados e tento sincronizar tudo no GitHub.

## Mensagem 0721 — Mestre (resposta visível integral, DIL preservado)

## As Cinzas da Coroa Esquecida — O marco de pedra

<box border radius="lg" padding={3} gap={3}>
  <grid columns={2} gap={3}>
    <grid-item>
      <text color="secondary" weight="medium" size="xs">Sabedoria (Percepção)</text>
      <title size="2xl" tabularNums>18</title>
      <text color="secondary" size="xs">1d20 [12] +6</text>
    </grid-item>
    <grid-item>
      <text color="secondary" weight="medium" size="xs">Inteligência (Investigação)</text>
      <title size="2xl" tabularNums>7</title>
      <text color="secondary" size="xs">1d20 [3] +4</text>
    </grid-item>
  </grid>
  <caption>Duas rolagens reais, executadas com o script Python da campanha e `secrets.randbelow()`.</caption>
</box>

Eron retorna à entrada da guarita e recupera a primeira flecha, que havia disparado contra o chão. A haste e a ponta permanecem íntegras, embora as penas estejam molhadas. **Uma flecha utilizável é recuperada: 18 → 19 flechas.**

Em seguida, cruza a estrada na direção do marco de pedra, com Neris acompanhando alguns passos atrás. Sob os salgueiros, ele encontra a segunda flecha, mas a haste está partida em dois pedaços e a ponta deformada pelo impacto. Pode recolher seus restos, mas **essa flecha não está em condições de disparo**.

### Exame do marco

A pedra é um bloco antigo de granito acinzentado, pouco mais alto que a cintura de Eron. Sua superfície está coberta por líquens amarelados e musgo escuro. O disparo deixou uma lasca recente na borda superior, claramente diferente das rachaduras antigas.

Com **Percepção 18**, Eron percebe, na face voltada para a estrada, vestígios de uma gravação muito desgastada. Sob o musgo, há dois sulcos retos que parecem deliberados, e uma marca curva quase apagada. Também encontra a vegetação amassada atrás da pedra, no ponto onde Neris estava agachada.

Entretanto, **Investigação 7** não permite estabelecer o significado da gravação. A erosão e o musgo dificultam distinguir símbolos de danos naturais. Tampouco há marcas claras que indiquem um compartimento oculto ou que relacionem a pedra ao desaparecimento de Tomas.

Neris inclina a cabeça, observando a superfície.

— É mais antiga do que imaginei. Talvez fosse um marco de distância ou de divisão de terras, antes de construírem esta guarita.

Ela passa os olhos pela gravação, sem tocá-la.

— Mas não reconheço esses sinais.

O vento move os galhos acima dos dois. Da estrada chega o ranger distante de uma carroça, e o rio continua correndo além das árvores.

## Proveniência das rolagens
Executado em 2026-10-17 no container: `python /mnt/data/rpg_work/dice_roller.py '1d20+6'` → `{"expression": "1d20+6", "rolls": [12], "kept_indices": [0], "modifier": 6, "total": 18}`; depois `python /mnt/data/rpg_work/dice_roller.py '1d20+4'` → `{"expression": "1d20+4", "rolls": [3], "kept_indices": [0], "modifier": 4, "total": 7}`. Script local cotejado com o conteúdo do repo `skills/dice-roller/dice_roller.py`.
