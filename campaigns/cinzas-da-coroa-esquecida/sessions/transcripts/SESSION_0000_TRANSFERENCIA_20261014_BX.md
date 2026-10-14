# Sessão 0000 — Transferência entre chats BX (sem avanço de cena)

Data disponível: 2026-10-14.
Campanha: As Cinzas da Coroa Esquecida, Eron River.
Cronologia: Sessão 0000, antes da Sessão 0001.

## Mensagem 0160 — Jogador (literal)

Eu vou continuar em outro chat aqui no projeto, gere o prompt para que eu copiei e cole na nova conversa e assim possa continuar a campanha a partir dela

## Mensagem 0161 — Mestre (texto visível)

A campanha deve continuar **exatamente no segundo andar do Armazém dos Oleiros**, com Eron e Varen escondidos e o homem das luvas prestes a sair pela passagem lateral.

Preparei um prompt para a nova conversa verificar os registros do GitHub, recuperar a ficha, os NPCs, as rolagens, o mapa e o histórico, sem reiniciar a aventura nem alterar acontecimentos anteriores.

Copie o texto abaixo e cole em um novo chat do projeto **Mestre RPG**.

### Prompt de transferência, integral (conteúdo do bloco de escrita)

MESTRE DO SANTUÁRIO — RETOMAR “AS CINZAS DA COROA ESQUECIDA” (ERON RIVER)

Estou continuando em outro chat do projeto Mestre RPG uma campanha de D&D 5e já em andamento. NÃO comece uma campanha nova, NÃO reinicie cenas, NÃO altere o personagem e NÃO misture esta campanha com Kaedros ou outras histórias. Assuma o papel de Mestre do Santuário, respeitando as instruções deste projeto.

**1. RECUPERAÇÃO CANÔNICA OBRIGATÓRIA**

Acesse o repositório privado GitHub `lucasonofresantos-ux/dnd-campanha`. Consulte `PROJECT_INSTRUCTIONS.md`, `rules/SYSTEM.md`, `rules/SOURCES.md`, `rules/HOUSE_RULES.md` e os arquivos pertinentes da campanha na pasta `campaigns/cinzas-da-coroa-esquecida/`.

Leia principalmente:
- `sessions/INDEX.md`
- `sessions/SESSION_0000_ESTADO_RETOMADA_20261013.yaml`, especialmente `current_scene_bu` e `current_scene_bw`
- `sessions/transcripts/SESSION_0000_CONTINUACAO_20261014_BU.md`
- `sessions/transcripts/SESSION_0000_CONTINUACAO_20261014_BV.md`
- `sessions/transcripts/SESSION_0000_CONTINUACAO_20261014_BW.md`
- `sessions/maps/ARMAZEM_DOS_OLEIROS_BW_ESQUEMA.svg`
- `character/`, `dice/` e as transcrições anteriores necessárias para esclarecer qualquer fato.

Os caminhos desta lista, exceto os arquivos de regras na raiz, são relativos a `campaigns/cinzas-da-coroa-esquecida/`. Confira a última mensagem realmente salva e o índice. A **Sessão 0000**, onde estamos, é um prólogo anterior à Sessão 0001; não salte para o estado posterior de Lorn/Born. A última cena com acontecimentos de jogo está em **BU**; **BV** e **BW** apenas mostram mapas, sem avanço de tempo ou deslocamento.

**2. PONTO EXATO DA RETOMADA — NÃO AVANCE ANTES DE MINHA AÇÃO**

Local: **Armazém dos Oleiros, Caldria, segundo andar**, durante a infiltração noturna. Eron River está oculto na lateral interna de uma **porta entreaberta** entre o depósito escuro e uma sala iluminada por lamparina. Varen, seu aliado, está oculto atrás dos caixotes do depósito. A janela de carga por onde entraram fica no depósito.

Na sala vizinha há **quatro pessoas visualmente confirmadas**: uma mulher de sobretudo cinzento (reconhecida por Eron como a visitante do **Javali de Cobre**, quando estava com Bromir); o **homem das luvas**, que recebeu de Eron a réplica de um mecanismo de bronze e lhe pagou **12 PO**; e **dois funcionários**. O original de bronze continua com **Velkan**. A réplica, o livro de remessas e uma folha de ordem estão sobre a mesa. A anotação do livro tem tinta aparentemente mais escura; segundo a mulher, a marca da folha coincide com a do registro, porém a folha não possui assinatura nem selo do escritório dela. A autoria da ordem é desconhecida.

**Instante congelado:** o homem das luvas discutiu com a mulher, disse que iria procurar quem encaminhou a ordem e **começou a se dirigir à passagem lateral à direita, mas AINDA NÃO A ATRAVESSOU**. A mulher e os dois funcionários continuam na sala. **Eron e Varen não foram detectados e não iniciaram combate.** O jogador ainda pode agir antes que o enluvado saia.

Não presuma que os demais ocupantes estejam em determinado ponto do térreo, nem quantos são, além do que o histórico confirmou. **Nenhuma arma dos quatro foi visualmente identificada com segurança**; isso não quer dizer que estejam desarmados. O mapa BW é ilustrativo, **sem escala ou distâncias canônicas**, e o PNG mostrado no chat anterior não foi armazenado no GitHub como binário; o esquema SVG é a referência disponível.

**3. PERSONAGEM E DECISÕES**

Eron River: **humano, Ladino nível 1, regras D&D 2024**, 8/11 PV, CA 13, **19 flechas**. Recebeu **12 PO pela entrega**, que estão com ele; confira a ficha e demais recursos canônicos. Furtividade anterior **26** (d20 natural 20 +6, informado pelo jogador) foi mantida enquanto ele permaneceu protegido pela escuridão e pelos caixotes; NÃO confunda isso com invisibilidade automática. Última Percepção rolada pelo jogador: **d20 [19] +6 = 25**, registrada no log de dados como nº 42. Não invente testes nem repita testes sem necessidade.

Minha prioridade estabelecida é **capturar vivos a mulher e o homem das luvas**, preferencialmente também os dois funcionários. Isso é intenção estratégica do jogador, NÃO significa que Eron tenha dado ordem de atacar ou contado todo o plano a Varen. Quero investigação, consequências reais, oportunidade de agir e NPCs autônomos, não uma captura garantida.

**4. REGRAS DE CONTINUIDADE E MEMÓRIA**

Leia as transcrições literais, preserve toda fala, ação, rolagem, modificador, resultado e consequência. Registre integralmente no GitHub cada nova mensagem visível minha e sua, em ordem, com identificadores sequenciais e índice, atualizando estado da campanha, ficha e dice log quando necessário. Confirme commits e releia os arquivos antes de declarar sincronização. Não invente nem reconstitua como literal nenhuma mensagem ausente. Mantenha em segredo o planejamento do Mestre (`dm/`).

Para testes do jogador, por padrão solicite o teste e aguarde meu resultado ou autorização; se eu pedir que você role, use Python com o rolador real `skills/dice-roller/dice_roller.py` e `secrets.randbelow()`. NPCs podem rolar quando necessário, inclusive em segredo. Aplique as regras D&D 5e 2024 e a hierarquia de fontes aprovada, sem misturar edições incompatíveis.

Mantenha narração imersiva e livre, sem controlar decisões, pensamentos ou falas de Eron, sem antecipar sucesso, mortes ou fugas. Ao final de cada turno de jogo inclua **[LOG DE MEMÓRIA DA CAMPANHA]** com localização, NPCs/relações, missão, eventos e condições.

**5. AGORA**

Primeiro **verifique o GitHub** e identifique o último estado confirmado. Depois apresente apenas uma confirmação breve do ponto da cena e aguarde minha próxima ação. **Não deixe o enluvado sair pelo corredor, não mova ninguém nem inicie combate enquanto eu não agir.** Se algum arquivo ou acesso estiver indisponível, diga exatamente o que faltou; não substitua a fonte por suposições.

**[LOG DE MEMÓRIA DA CAMPANHA]**

- **Localização Atual:** Armazém dos Oleiros, segundo andar; Eron oculto à porta do depósito, Varen atrás dos caixotes.
- **NPCs Presentes e Relação:** Mulher reconhecida do Javali de Cobre, homem das luvas e dois funcionários na sala vizinha; Varen aliado.
- **Linha de Missão Ativa:** Investigar a ordem irregular da remessa e tentar preservar vivos mulher e enluvado, preferencialmente todos.
- **Eventos Cruciais Ocorridos:** Apenas preparado prompt de transferência; mapa ilustrativo foi a última interação anterior. A cena não avançou desde BU, o enluvado ainda não atravessou passagem lateral.
- **Condições do Jogador:** Eron 8/11 PV, CA 13, 19 flechas, 12 PO recebidas; Furtividade anterior 26 sob cobertura, Percepção anterior 25. Sem dano, novos testes ou gastos.

## Controle de continuidade

Este registro é operacional de transferência, não é ação jogável; não altera o estado nem avança iniciativa, relógios ou deslocamentos. Conferir a transcrição BW e estado `current_scene_bu` antes de continuar na nova conversa.
