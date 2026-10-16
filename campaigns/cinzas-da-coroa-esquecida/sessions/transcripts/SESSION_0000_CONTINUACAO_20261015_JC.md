# Sessão 0000 — Continuação JC (solicitação de rolador interativo)
Campanha: As Cinzas da Coroa Esquecida
Data do registro: 2026-10-15
Nota: a imagem anexada pelo jogador mostra um rolador de d20 e um exemplo 1d20+5, dado 10, total 15; a referência à imagem não é uma transcrição do anexo.

## Mensagem 0532 — Jogador (literal, texto)

Me dá um rolador aqui, igual esse 

Anexo: imagem de referência disponibilizada nesta interação, nome verificado `1000232257.png`. Não converter imagem em texto original do jogador.

## Mensagem 0533 — Mestre (texto visível integral)

Aqui está um **rolador de d20 interativo**, parecido com o da imagem. Já deixei o modificador **+6 de Percepção de Eron**, mas você pode alterá-lo para outros testes.

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

**[LOG DE MEMÓRIA DA CAMPANHA]**

- **Localização Atual:** Estrada Caldria–Lorn, parada do comboio junto ao riacho.
- **NPCs Presentes e Relação:** Orven Rusk, contratante; Darin, guarda aliado; condutores.
- **Linha de Missão Ativa:** Escoltar as três carroças até Lorn; 8 PO pendentes.
- **Eventos Cruciais Ocorridos:** Rolador de d20 disponibilizado para Eron com modificador +6. Nenhuma rolagem foi incorporada à campanha ainda; aguarda clique em “Usar na campanha” ou execução pelo Python.
- **Condições do Jogador:** 11/11 PV, CA 13, 20 flechas; 119 PO, 9 PP e 5 PC; Inspiração Heroica e 1d8 de Vida disponíveis.
