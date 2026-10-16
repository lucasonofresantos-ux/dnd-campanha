# Sessão 0000 — Continuação JG
Campanha: As Cinzas da Coroa Esquecida
Data de registro: 2026-10-15

## Mensagem 0540 — Jogador (literal)

Bem agora é esperar ele passar pela fiscalização, e entregar a mercadoria, enquanto isso me dê o rolador de dados para rolar percepção, quero ver se alguém me segue enquanto isso

## Mensagem 0541 — Mestre (texto visível integral)

Orven entrega os documentos ao guarda, que os passa ao escrivão. Enquanto um deles verifica os lacres das carroças, a fila avança lentamente sob a luz do fim da tarde. Eron permanece junto ao comboio, observando também quem entra e sai da fila, os transeuntes e os rostos que eventualmente se voltam em sua direção. **A fiscalização está em andamento; a entrega e o pagamento ainda não aconteceram.**

Para verificar se alguém está seguindo Eron, faça um **novo teste de Sabedoria (Percepção): 1d20 + 6**. Este é um objetivo de observação diferente da vigilância da estrada. A cena aguardará o resultado antes de revelar o que Eron percebe.

{@body const [bonusText,setBonusText] = DIL.useState("6"); const [result,setResult] = DIL.useState(null); const [history,setHistory] = DIL.useState([]); const bonus = Math.max(-30,Math.min(30,Math.trunc(Number(bonusText)||0))); const rollDice = () => { const face = Math.floor(Math.random()*20)+1; const next = {face,bonus,total:face+bonus}; setResult(next); setHistory(old=>[next,...old].slice(0,6)); }; }
<box maxWidth="440px">
  <card gap={3}>
    <col align="center" gap={1}>
      <title size="lg">Rolador de D&D — d20</title>
      <text color="secondary" size="xs">Eron River · Percepção de possíveis perseguidores</text>
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
          <text color="success" weight="medium">20 natural</text>
        {:else if result.face===1}
          <text color="secondary" weight="medium">1 natural</text>
        {/if}
      {:else}
        <title size="md" color="secondary">Aguardando rolagem</title>
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
          <button block variant="outline" color="primary" onClick={()=>GenUI.issueNewTurn(`Na fiscalização de entrada em Lorn, Eron observa se alguém o segue. Use o resultado do meu rolador visual local: 1d20 [${result.face}] ${result.bonus>=0?"+":""}${result.bonus} = ${result.total}. Registre esta rolagem como local, resolva a Percepção e continue a inspeção e a entrega da carga sem decidir ações por Eron.`)}>Usar na campanha</button>
        </box>
        <button variant="outline" color="secondary" onClick={()=>GenUI.copy(`1d20 [${result.face}] ${result.bonus>=0?"+":""}${result.bonus} = ${result.total}`)}><icon name="copy" inline/> Copiar</button>
      </row>
      <divider color="subtle"/>
      <text size="sm" weight="medium">Últimas rolagens</text>
      <text size="xs" color="secondary" tabularNums>{history.map(h=>`[${h.face}] ${h.bonus>=0?"+":""}${h.bonus} = ${h.total}`).join("  ·  ")}</text>
    {/if}
  </card>
</box>

<text color="secondary" size="xs">O botão visual usa sorteio local (`Math.random`), **não** o script Python. Se preferir um resultado conferível no Roll20, informe a face que saiu no d20. O resultado só será aplicado à campanha quando você usar “Usar na campanha” ou enviá-lo na conversa.</text>

<button variant="outline" onClick={()=>GenUI.issueNewTurn(`Execute com Python e secrets.randbelow uma rolagem real de 1d20${bonus>=0?"+":""}${bonus} para Percepção de Eron enquanto observa se alguém o segue no posto de entrada de Lorn. Apresente dado e total, registre a rolagem e continue a fiscalização.`)}><icon name="shield-check" inline/> Rolar com Python</button>

**[LOG DE MEMÓRIA DA CAMPANHA]**

- **Localização Atual:** Fiscalização de entrada de Lorn, fim da tarde; três carroças na fila.
- **NPCs Presentes e Relação:** Orven Rusk, contratante; Darin, aliado; condutores, guardas e escrivão.
- **Linha de Missão Ativa:** Entregar carga das três carroças em Lorn; 8 PO ainda devidos.
- **Eventos Cruciais Ocorridos:** Orven apresentou a documentação e a inspeção começou. Eron aguarda, atento a possíveis perseguidores. **Percepção 1d20+6 solicitada; resultado pendente.**
- **Condições do Jogador:** 11/11 PV, CA 13, 20 flechas; 119 PO, 9 PP, 5 PC; Inspiração Heroica e 1d8 disponíveis.
