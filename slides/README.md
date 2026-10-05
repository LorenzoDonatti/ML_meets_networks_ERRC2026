# Slides acadêmicos — LaTeX / Beamer

`minicurso.pdf` é a apresentação pronta, em 16:9. `minicurso.tex` é a fonte completa.
`template.tex` usa o tema **Dresden** e a paleta **LSC** fornecida pelo proponente:
verde RGB (0,130,137), títulos em faixa colorida e navegação superior por seções.
Sem logotipos. São 17 slides, com texto reduzido e figuras das aulas.
Há um roteiro inicial; omitimos sua repetição a cada seção para manter a apresentação enxuta.
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

No workspace de desenvolvimento, `scripts/build_slides.py` gera a fonte a partir do roteiro
e deste template, compila duas vezes e verifica overflow e caracteres ausentes.
Na publicação GitHub basta editar/compilar `minicurso.tex`; scripts internos não são necessários.
