# Auditoria de continuidade — Sessão 0 — 2026-10-13

Campanha: `cinzas-da-coroa-esquecida`. Auditoria feita mediante leitura direta dos arquivos do GitHub e consulta a contexto recuperável da conversa anterior. Não é uma reconstrução literal de mensagens que não estejam acessíveis.

## Continuidade selecionada pelo jogador
Em 2026-10-12, o jogador esclareceu que a Sessão 0 com Bromir e Velkan é a continuidade a seguir, com possível ligação futura a Lorn. Não deseja recuperar lacunas da criação da ficha. A abertura alternativa da Sessão 0001 em Lorn continua preservada como outro ramo; não é um evento vivido desta Sessão 0.

## Ordem dos arquivos históricos relevantes
1. `SESSION_0000_EXECUCAO_FULL.md` — estrada, Bromir e chegada ao Javali de Cobre, termina em pedido de Percepção.
2. `SESSION_0000_PENDENCIAS_20261012.md` — continuação da estalagem até a oficina e o confronto no depósito; há trechos recuperados e possíveis descontinuidades de ordem.
3. `SESSION_0000_RECUPERACAO_20261012.md` — complemento de mensagens acessíveis do ataque e início do beco; sobrepõe parcialmente outras fontes, não duplicar na cronologia.
4. `SESSION_0000_CONTINUACAO_20261012_B.md` — combate do beco, prisioneiros e interrogatório.
5. `SESSION_0000_CONTINUACAO_20261012_C.md` — continuidade dos interrogatórios e da convivência com Bromir.
6. `SESSION_0000_CONTINUACAO_20261012_D.md` — chegada de Haldren, acordo com a patrulha, reconhecimento do armazém, encontro com Varen, confronto no curtume e retorno à oficina de Velkan; é o registro mais avançado encontrado.

## Última interação efetivamente preservada
**Jogador (literal, no final do arquivo D):**
> A forma que ele se porta e fala, as vestes também, é bem treinado, tem várias cicatrizes sobre os dedos, aquilo é de treinamento, e já vi agentes reais ou de nobres ele me lembra eles

**Mestre:** a resposta completa está nas últimas linhas do arquivo D. Haldren reconhece os indícios de treinamento mas não confirma vínculos de Varen, e pergunta a Eron: **“onde você teve contato com agentes da Coroa e de casas nobres?”** Ao fim dessa fala, Haldren aguarda a resposta, com pão, carne fria e queijo sobre a mesa. Nenhuma resposta subsequente de Eron foi localizada nos arquivos inspecionados.

## Lacunas comprovadas e limites da literalidade
- No começo de `SESSION_0000_CONTINUACAO_20261012_D.md`, após a fala do jogador **“Conversamos um pouco, crie um diálogo como se eu pergunta se a Bromir que ele está muito a vontade com a situação Até Velkan chegar com Haldren”**, a resposta do Mestre está substituída pela frase **“Transcrição literal da resposta pendente de sincronização. NÃO é transcrição completa; consultar a conversa original para recuperar o texto integral.”** O diálogo original não foi recuperado integralmente nesta conferência; não substituí-lo por texto inventado.
- `SESSION_0000_FULL.md`, relativo à preparação e criação de ficha, possui várias respostas antigas do Mestre marcadas como pendentes. O jogador dispensou recuperar a criação do personagem, mas esses registros continuam historicamente incompletos.
- O arquivo `SESSION_0000_PENDENCIAS_20261012.md` foi assim nomeado precisamente por não demonstrar transcrição original contínua e íntegra; algumas lacunas na sequência anterior requerem exportação da conversa para verificação definitiva.
- Interfaces visuais e controles interativos dos dados foram por vezes **descritos**, sem registro integral de sua representação; não equivalem a transcrições literais da interface.
- Há rolagens visíveis no arquivo D ausentes de `dice/ROLL_LOG.csv`. Um suplemento separado guarda os valores concretos identificados; resultados históricos atribuídos a Python são registros de afirmação anterior e não nova execução/verificação de sorteio.

**Conclusão:** é possível identificar o ponto jogável mais recente e preservar a continuidade, mas NÃO está comprovado que a transcrição integral de toda a conversa “01.02 As Cinzas da Coroa Esquecida” esteja completa. Não atribuir literalidade às lacunas.

## Ramo narrativo e proteção de estado
O `CAMPAIGN_STATE.yaml` principal da pasta da campanha aponta para a execução alternativa da Sessão 0001 em Lorn, sem as ações de Bromir. **Não utilizá-lo para resumir a Sessão 0**, nem apagá-lo retroativamente. Estado operacional específico desta Sessão 0 em `sessions/SESSION_0000_ESTADO_RETOMADA_20261013.yaml`; rolagens suplementares em `dice/ROLL_LOG_SESSAO_0000_SUPLEMENTO_20261013.csv`. Nenhuma informação dos arquivos `dm/` é incluída nesta auditoria.
