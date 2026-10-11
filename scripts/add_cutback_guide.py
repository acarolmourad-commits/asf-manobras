# One-shot (10/10/2026): insere o Guia Completo do Cutback no ASF Manobras (unificacao do conteudo que estava inline na home do asf-app)
import pathlib

p = pathlib.Path('index.html')
html = p.read_text(encoding='utf-8')

if 'guia-cutback-completo' in html:
    print('Guia ja presente. Nada a fazer.')
    raise SystemExit(0)

CARD = """
<div class="card" id="guia-cutback-completo">
<h2>\u2197\ufe0f Guia Completo: Como Fazer o Cutback Perfeito</h2>
<p style="font-size:.8rem;color:#777">Tecnica avancada \u2022 ~15 min de leitura \u2022 conteudo oficial ASF (unificado da home do asf-app)</p>
<p><b>Passo 1: Velocidade e tudo.</b> Antes de tentar o cutback, voce precisa de velocidade. Faca 2-3 bottom turns fortes para gerar speed. Sem velocidade, o cutback vira um floater sem graca.</p>
<p><b>Passo 2: Olhe para onde quer ir.</b> Seus olhos guiam seu corpo. Olhe de volta para a parte alta da onda ANTES de iniciar a manobra. Seu corpo vai seguir naturalmente.</p>
<p><b>Passo 3: Peso na traseira.</b> Transfira peso para a perna traseira enquanto gira os ombros. O tail da prancha vai deslizar. Use seus bracos como contrapeso \u2014 estenda o braco de fora.</p>
<p><b>Passo 4: O retorno.</b> A parte mais dificil: voltar para a base da onda. Pressione o rail de volta, transfira peso para frente e acelere. Isso e o que separa um cutback bom de um excelente.</p>
<p><b>Erros comuns:</b><br>
\u274c Nao olhar para tras antes de girar<br>
\u274c Girar so com os pes (use o corpo inteiro!)<br>
\u274c Fazer na parte errada da onda (muito baixo)<br>
\u274c Desistir no meio da manobra</p>
<p><b>\ud83c\udfaf Exercicio no seco:</b> pratique a rotacao de ombros em casa. Deixe o skate te ajudar \u2014 faca carvebacks no skate para treinar o movimento!</p>
<p style="font-size:.85rem;color:#777">Complete o checklist da trilha abaixo para ganhar XP quando dominar o cutback! \ud83d\udcaa</p>
</div>
"""

ANCHOR = 'Todo cutback, off the lip e floater nasce de um bottom turn s\u00f3lido. Se algo n\u00e3o sai, volte aqui.</p></div>'
assert ANCHOR in html, 'ancora nao encontrada'
html = html.replace(ANCHOR, ANCHOR + CARD, 1)
p.write_text(html, encoding='utf-8')
print('Guia do cutback inserido no ASF Manobras')
