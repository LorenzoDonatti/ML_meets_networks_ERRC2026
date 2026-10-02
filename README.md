# Machine Learning Meets Networks

Um guia prático para aplicações de aprendizado de máquina em redes sem fio e IoT.

**ERRC 2026 · 150 minutos · nível intermediário**

Lorenzo Moreira Donatti e Deivis Felipe Guerreiro Fagundes.

Do problema de rede aos dados, ao modelo e à interpretação: duas aulas guiadas com
Python, pandas, NumPy, matplotlib e scikit-learn. Sem GPU, instalação de gateways ou coleta em aula.
Conhecimentos recomendados: Python básico e conceitos básicos de redes.

## Abrir as aulas no Google Colab

| Aula | Abrir |
|---|---|
| 01 — Localização por fingerprints LoRaWAN, Antwerp | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LorenzoDonatti/ML_meets_networks_ERRC2026/blob/errc2026-v1.1/notebooks/01_localizacao.ipynb) |
| 02 — Previsão de RSSI uma hora à frente | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LorenzoDonatti/ML_meets_networks_ERRC2026/blob/errc2026-v1.1/notebooks/02_forecasting.ipynb) |

1. Abra o notebook pelo botão e conecte um ambiente CPU padrão.
2. Salve uma cópia no seu Google Drive se quiser guardar alterações.
3. Execute as células do início ao fim com **Shift + Enter**. O código já está pronto.
4. Os CSVs são baixados automaticamente pelo GitHub Raw. Não é necessário clonar o repositório,
   montar o Drive ou enviar arquivos. É necessário acesso à Internet.

Os botões apontam para a versão `errc2026-v1.1`. Os dados usados pelos notebooks estão fixados
no commit `e7b18b4133d3544ad4d6ed15e3599167031c54f7`, com verificação SHA-256 na leitura.
Assim, uma mudança posterior na branch principal não muda os dados dessa edição da aula.
O download ocorre na célula inicial; os gráficos seguintes usam os dados em memória.

Os dois notebooks já contêm gráficos, tabelas e resultados salvos: você pode ler a análise antes
mesmo de executar. Ao rodar novamente, as saídas são atualizadas a partir dos dados versionados.
Se o download falhar, confira a conexão e tente novamente; as saídas salvas continuam disponíveis.
Não distribuímos HTML. Para consulta local, use os notebooks em Jupyter.

## O que será feito

**Localização — 40 minutos:** explorar presença dos gateways, distribuição espacial e sinais;
separar dias de treino/validação/teste; comparar centroide ponderado, k-NN e Random Forest;
interpretar mediana, P90 e recortes de avaliação. Sálvora aparece como contraponto curto:
ML não é bala de prata e concentração espacial pode favorecer estimativas quase constantes.

**Forecasting — 40 minutos:** explorar o histórico de um enlace, construir lags, respeitar
a ordem temporal e comparar persistência com Ridge. A previsão é de uma hora à frente.

O tempo total inclui 15 min de motivação, 15 min de formulação, as duas práticas de 40 min,
5 min de pausa, 20 min de armadilhas metodológicas e 15 min de síntese e perguntas.

## Materiais

- [Notebook 01](notebooks/01_localizacao.ipynb) e [notebook 02](notebooks/02_forecasting.ipynb).
- [Slides acadêmicos em PDF](slides/minicurso.pdf), produzidos em LaTeX/Beamer.
- [Fonte LaTeX](slides/minicurso.tex), [template](slides/template.tex) e [instruções de compilação](slides/README.md).
- [Dados, fontes, licenças e transformações](data/README.md).
- [Dependências para execução local opcional](requirements.txt).

Os CSVs preparados têm aproximadamente 1,9 MB (Antwerp), 1,7 KB (gateways) e 42 KB (forecasting).
Os grandes arquivos originais permanecem nos repositórios dos autores. Esta publicação não inclui
PDFs de submissão, currículos, arquivos privados, ambientes virtuais ou o histórico de desenvolvimento.

## Cuidados com a interpretação

O teste de Antwerp é temporal na mesma rede, não geograficamente independente. Regiões e
dispositivos podem reaparecer. A aula mostra concentração espacial e erros extremos para não
confundir mediana baixa com precisão universal. O recorte não reproduz splits dos artigos;
seus números não devem ser comparados diretamente aos benchmarks publicados.

As duas aulas foram executadas e verificadas localmente lendo dados do GitHub Raw. Isso não
substitui ensaio cronometrado nem teste na rede e no runtime Colab usados no evento.

## Licenças e atribuição

Antwerp: **CC BY 4.0**. Série temporal Goldoni et al.: **CC BY-SA 4.0**.
Autores, fontes e modificações estão documentados em [data/README.md](data/README.md).
As licenças dos dados não constituem licença global do código, textos ou slides deste repositório.
