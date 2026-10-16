# Modelo reutilizável — rolador visual d20 para D&D 5E

**Objetivo:** quando o jogador pedir "o rolador", "rolador igual ao da imagem" ou "mostrar o d20", recriar no ChatGPT o controle visual abaixo, com dado azul, face, modificador, total, histórico e opção de enviar resultado à campanha.

**Padrão de Eron River (2024):** Sabedoria (Percepção) = `1d20+6`; permitir modificar o bônus para outros testes. Aplicar modificador e resultado de forma separada, sem inventar sorteios. Este arquivo é um **modelo de interface**, não um executor automático do Python nem um histórico de resultados.

**Segurança e procedência das rolagens:**
- O botão "Rolar d20" da interface usa `Math.random()` no cliente, que **não é verificavelmente igual** ao método criptográfico `secrets.randbelow()`. Não anunciar essa opção como sorteio pelo Python.
- O botão "Rolar com Python" envia um pedido explícito de rolagem ao Mestre, que deverá **executar de fato** `skills/dice-roller/dice_roller.py` em um ambiente Python e apresentar dados individuais e total.
- Se o jogador rolar no Roll20 ou em dados físicos, aceitar **o valor natural informado pelo jogador**, somar o bônus da ficha, identificar a origem como `jogador_roll20` ou `jogador_dados_fisicos` e registrar no log — sem rerrolar por conta própria.
- O botão "Usar na campanha" envia o valor para uma nova mensagem e **só então** o Mestre deve aplicar o teste ao estado do jogo. O resultado local que não foi enviado não é canônico.
- Nunca alterar históricos ou reexecutar dados sem autorização expressa. Usar `dice/ROLL_LOG.csv` do diretório de cada campanha.
- Trata-se de modelo para gerar interface de ChatGPT, **não** de arquivo Python/HTML pronto para instalação.

## Bloco de interface para reutilização

Ao exibir o rolador, adaptar os rótulos ao personagem/perícia, manter os controles ativos e emitir o código de interface abaixo **sem** cercá-lo com bloco Markdown.

```jsx
{@body const [bonusText,setBonusText] = DIL.useState("6"); const [result,setResult] = DIL.useState(null); const [history,setHistory] = DIL.useState([]); const bonus = Math.max(-30,Math.min(30,Math.trunc(Number(bonusText)||0))); const rollDice = () => { const face = Math.floor(Math.random()*20)+1; const next = {face,bonus,total:face+bonus}; setResult(next); setHistory(old=>[next,...old].slice(0,6)); }; }
<box maxWidth="440px">
  <card gap={3}>
    <col align="center" gap={1}>
      <title size="lg">Rolador de D&D — d20</title>
      <text color="secondary" size="xs">Eron River · Sabedoria (Percepção)</text>
      <svg viewBox="0 0 220 215" width="210px" height="206px" xmlns="http://www.w3.org/2000/svg">
        <polygon points="110,10 195,67 175,163 110,205 45,163 25,67" fill="#205A82" stroke="#97D9FF" strokeWidth="3"/>
        <polygon points="110,10 195,67 110,59 25,67" fill="#367CA7" stroke="#97D9FF" strokeWidth="2"/>
        <polygon points="110,59 195,67 175,163 45,163 25,67" fill="#245F8C" stroke="#97D9FF" strokeWidth="2"/>
        <path d="M110 59 L45 163 M110 59 L175 163 M45 163 L110 205 L175 163" fill="none" stroke="#97D9FF" strokeWidth="2"/>
        <text x="110" y="131" fill="#FFFFFF" fontSize="64" fontWeight="700" textAnchor="middle">{result===null?"?":result.face}</text>
      </svg>
      <text color="secondary" size="sm">1d20 {bonus>=0?"+":"−"} {Math.abs(bonus)}</text>
      {#if result!==null}
        <title size="2xl" tabularNums color="success">{result.total}</title>
        **Resultado total**
        <text color="secondary" tabularNums>{result.face} {result.bonus>=0?"+":"−"} {Math.abs(result.bonus)} = {result.total}</text>
        {#if result.face===20}
          <badge color="success">20 natural!</badge>
        {:else if result.face===1}
          <badge color="warning">1 natural</badge>
        {/if}
      {:else}
        <title size="lg" color="tertiary">Aguardando rolagem</title>
      {/if}
    </col>
    <row align="end" gap={3}>
      <box flex={1} gap={1}>
        <label>Modificador</label>
        <input inputType="number" value={bonusText} onChange={setBonusText} placeholder="6"/>
      </box>
      <box flex={2}>
        <button block onClick={rollDice}><icon name="dices" inline/> Rolar d20</button>
      </box>
    </row>
    {#if result!==null}
      <row gap={2}>
        <box flex={2}>
          <button block color="primary" variant="outline" onClick={()=>GenUI.issueNewTurn(`Na parada do comboio junto ao riacho, use esta minha rolagem: 1d20 [${result.face}] ${result.bonus>=0?"+":""}${result.bonus} = ${result.total}. Aplique ao teste de Percepção de Eron e continue a cena.`)}>Usar na campanha</button>
        </box>
        <button color="secondary" variant="outline" onClick={()=>GenUI.copy(`1d20 [${result.face}] ${result.bonus>=0?"+":""}${result.bonus} = ${result.total}`)}><icon name="copy" inline/> Copiar</button>
      </row>
      <divider color="subtle"/>
      <text weight="medium" size="sm">Últimas rolagens</text>
      <text size="xs" color="secondary" tabularNums>{history.map(h=>`[${h.face}] ${h.bonus>=0?"+":""}${h.bonus} = ${h.total}`).join("  ·  ")}</text>
    {/if}
  </card>
</box>

**Importante:** o botão **Rolar d20** usa sorteio local no aplicativo, não executa Python. Para usar especificamente o método `secrets.randbelow()` da campanha, utilize este outro botão, que solicita a execução no chat:

<button variant="outline" block={false} onClick={()=>GenUI.issueNewTurn(`Execute agora uma rolagem real de 1d20${bonus>=0?"+":""}${bonus} usando Python e secrets.randbelow. Mostre o dado individual e o total e aplique ao teste de Percepção de Eron na parada junto ao riacho. Não invente resultados.`)}><icon name="shield-check" inline/> Rolar com Python</button>
```

## Referências na campanha

- Exemplo original: `campaigns/cinzas-da-coroa-esquecida/sessions/transcripts/SESSION_0000_CONTINUACAO_20261015_JC.md`.
- Acompanhamento da rolagem do jogador no Roll20: anotar somente a face real informada e o modificador real, nunca o total +5 do exemplo de imagem, pois a Percepção de Eron tem bônus +6.
- A interface pode precisar de ajustes se os controles do aplicativo ChatGPT mudarem; não alegar que o modelo foi executado só porque o arquivo foi consultado.
