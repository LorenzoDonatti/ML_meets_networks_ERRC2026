# Slides acadêmicos — LaTeX / Beamer

`minicurso.pdf` é a apresentação pronta, em 16:9. `minicurso.tex` é a fonte completa.
`template.tex` define a identidade visual: tema Beamer Boadilla, fundo branco, azul-escuro,
tipografia Latin Modern e rodapé com autores, evento e numeração. As figuras vêm das aulas.

Para compilar a fonte completa nesta pasta:

```bash
pdflatex -interaction=nonstopmode -halt-on-error minicurso.tex
pdflatex -interaction=nonstopmode -halt-on-error minicurso.tex
```

Dependências TeX Live: latex-base, latex-recommended (Beamer), pictures (PGF), lang-portuguese
e fontes Latin Modern. Também é possível enviar `minicurso.tex` e `figures/` ao Overleaf.
O template usa fontes padrão e não depende de estilos externos baixados em tempo de compilação.

No workspace de desenvolvimento, `scripts/build_slides.py` gera a fonte a partir do roteiro
e deste template, compila duas vezes e verifica overflow e caracteres ausentes.
Na publicação GitHub basta editar/compilar `minicurso.tex`; scripts internos não são necessários.
