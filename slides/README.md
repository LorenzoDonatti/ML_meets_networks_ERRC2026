# Slides acadêmicos — LaTeX / Beamer

`minicurso.pdf` é a apresentação pronta, em 16:9. `minicurso.tex` é a fonte completa.
`template.tex` usa o tema **Dresden** e a paleta **LSC** fornecida pelo proponente:
verde RGB (0,130,137), títulos em faixa colorida e navegação superior por seções.
Sem logotipos. São 38 slides que contextualizam localização e forecasting, situam brevemente
os tipos de aprendizado e alternam diagramas vetoriais TikZ com gráficos reais das aulas.
A abertura apresenta as duas frentes; não há repetição de roteiro a cada seção.
O slide 3 alinha a proposta e os resultados de aprendizagem em cerca de um minuto,
dentro dos 15 minutos de abertura.
Antes da formulação, três slides apresentam LoRa/LoRaWAN, nó, gateway e uplink,
a escala do RSSI em dBm e a diferença para SNR em dB (6 minutos no bloco de formulação).
Os métodos têm uma base matemática curta, alinhada aos notebooks: centroide por potência
relativa, k-NN ponderado pela distância, médias da Random Forest, persistência e objetivo
regularizado da Ridge com lags padronizados. Exemplos numéricos são fictícios e identificados.
O guia reserva 7 minutos para métodos/execução na localização e 4 no forecasting, dentro das práticas.
Os temas externos Lsc/rounded do exemplo não são necessários: o exemplo principal usa Dresden.
O cabeçalho de autoria/licença do arquivo de cores foi preservado em `beamercolorthemelsc.sty`.

Para compilar a fonte completa nesta pasta:

```bash
pdflatex -interaction=nonstopmode -halt-on-error minicurso.tex
pdflatex -interaction=nonstopmode -halt-on-error minicurso.tex
```

Dependências TeX Live: latex-base, latex-recommended (Beamer), pictures (PGF), lang-portuguese
e fontes Latin Modern. Para o Overleaf, envie `minicurso.tex`, `beamercolorthemelsc.sty` e `figures/`.
O template usa fontes padrão e não depende de estilos externos baixados em tempo de compilação.

`conteudo.tex` contém o roteiro editável e os diagramas. `template.tex` define o estilo.
No workspace de desenvolvimento, `scripts/build_slides.py` combina os dois, copia os gráficos
das execuções dos notebooks, compila duas vezes e verifica overflow e caracteres ausentes.
Na publicação GitHub basta editar/compilar `minicurso.tex`; scripts internos não são necessários.

Os slides das práticas substituem explicações dos notebooks: não aumentam os 150 minutos.
Exemplos fictícios, esquemas qualitativos e gráficos dos datasets são identificados separadamente.
