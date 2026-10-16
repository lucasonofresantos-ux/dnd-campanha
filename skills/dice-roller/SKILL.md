# Dice Roller — Mestre RPG

## Objetivo
Rolagens auditáveis de dados para D&D 5e, sem inventar resultados.

## Requisitos
Python 3.9+; somente biblioteca padrão. O ChatGPT não executa arquivos do GitHub automaticamente. Usar apenas quando houver um executor Python habilitado e acessível na sessão, ou executar externamente e informar o resultado ao Mestre.

## Comandos
`python skills/dice-roller/dice_roller.py 1d20+5`
`python skills/dice-roller/dice_roller.py 2d20kh1` — vantagem
`python skills/dice-roller/dice_roller.py 2d20kl1` — desvantagem
`python skills/dice-roller/dice_roller.py 4d6dl1` — descarta o menor
`python skills/dice-roller/dice_roller.py 8d6` — dano

Suporta d4, d6, d8, d10, d12, d20, d100, de 1 a 100 dados, modificador inteiro. `kh1` mantém maior; `kl1` mantém menor; `dl1` descarta um menor. Resultados são pseudoaleatórios criptograficamente seguros via `secrets.randbelow`.

## Regras de uso
1. Execute o script de fato; nunca apresente números como sorteados se a execução não ocorreu.
2. Mostre os resultados individuais, índices mantidos, modificador e total.
3. Para vantagem/desvantagem, use 2d20kh1 / 2d20kl1. Um 20 natural é determinado pelo d20 efetivamente mantido, não pelo total.
4. Registre rolagens relevantes em `dice/ROLL_LOG.csv` segundo o formato já existente no projeto; não reescreva registros antigos.
5. Caso o executor não esteja disponível, informe a limitação e peça uma rolagem externa; não simule.
6. Não altere resultados para proteger personagens ou forçar a narrativa.

## Rolador visual reutilizável no ChatGPT

Quando o jogador pedir para **mostrar/abrir um rolador de dados na conversa**, consultar `skills/dice-roller/ROLADOR_VISUAL_D20.md` e recriar a interface visual lá documentada, com dado d20 azul, modificador ajustável (Percepção de Eron +6 por padrão), resultado e opção de enviar à campanha. O modelo distingue sorteio local via `Math.random()` de execução Python auditável via `secrets.randbelow`; nunca afirmar equivalência nem inventar resultados. Aceitar a face natural do dado físico/Roll20 do jogador sem rerrolar e aplicar o bônus da ficha. Atualizar a transcrição literal, ficha/estado e o log da campanha ao receber o resultado.
