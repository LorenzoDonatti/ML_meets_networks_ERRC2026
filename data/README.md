# Dados preparados para o minicurso

Os CSVs são recortes didáticos, não novos datasets independentes. Preservam-se as atribuições
e licenças indicadas abaixo. Os originais completos não estão neste repositório.

## Localização — Antwerp

Autores: Michiel Aernouts, Rafael Berkvens, Koen Van Vlaenderen e Maarten Weyn.
*Sigfox and LoRaWAN Datasets for Fingerprint Localization in Large Urban and Rural Areas*, v1.3.
[Fonte oficial](https://doi.org/10.5281/zenodo.3904158).
Licença dos originais e derivados: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

- `antwerp_localization.csv`: 12.000 pacotes; entradas RSSI e metadados.
- `antwerp_gateways.csv`: coordenadas de 39 gateways, vinculadas às colunas pelo ID.
- `antwerp_manifest.json`: hashes SHA-256, exclusões e protocolo de preparação.

Modificações pelos tutores: JSON original convertido em tabela; ausência de recepção vira NaN;
timestamp corresponde à primeira recepção do pacote em UTC; GPS permanece como rótulo.
Dos 44 IDs observados no JSON, cinco não têm coordenadas no arquivo oficial e ficam fora das
entradas de todos os métodos. Foram excluídos 163 pacotes sem recepção nos 39 gateways conhecidos.
Nenhum filtro dependeu do resultado dos modelos.

Dias UTC inteiros foram separados em ordem temporal: treino até 24/01/2019, validação de
25/01 a 01/02/2019 e teste posterior. Em cada parte, amostragem uniforme sem reposição,
semente 42: 8.000 / 2.000 / 2.000 pacotes. A distribuição espacial não foi balanceada.
O manifesto também identifica arquivos originais que permanecem no Zenodo, fora deste repositório.
Não se reproduzem aqui as divisões de benchmark dos artigos.

## Forecasting — RSSI de um enlace LoRaWAN

Autores: Emanuele Goldoni, Pietro Savazzi, Luigi Favalli e Anna Vizziello.
*Correlation between weather and signal strength in LoRaWAN networks: An extensive dataset* (2022).
[Artigo](https://doi.org/10.1016/j.comnet.2021.108627) e
[repositório original](https://github.com/emanueleg/lora-rssi/tree/master/vineyard-2021_data).
Licença original e do derivado: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
Texto disponibilizado pelos autores preservado em `LICENSE_vineyard.md`.

`rssi_hourly.csv`: nó RSSI_01, maior trecho horário contínuo sem lacunas, escolhido por
disponibilidade e não por desempenho. São 1.059 horas, de 30/11/2020 10:00 UTC a
13/01/2021 12:00 UTC. Modificações pelos tutores: seleção do nó/trecho, conversão do timestamp
e renomeação das colunas. Sem interpolação ou suavização adicional.
O agregado só é considerado disponível após fechar sua hora; não se comprova latência operacional.

## Caso complementar — Sálvora

O primeiro notebook inclui três figuras de um experimento anterior, sem treinamento extra em aula.
`salvora_diagnostico.csv` contém 1.210 posições (984 treino / 226 teste), medições RSSI/SNR,
identificação dos blocos e previsões dos quatro métodos nas linhas de teste. Ausências originais
RSSI=0 foram interpretadas como falta de recepção, hipótese de curadoria; SNR correspondente
também ficou ausente. SNR=0 com RSSI válido foi mantido. Blocos: 30 minutos por dispositivo.
`salvora_manifest.json` registra parâmetros, gateways, split e hashes. Gráficos e métricas são
recalculados ao executar o notebook; não entram como atributos de treinamento.
O CSV é baixado do commit `57717d4745a1745b8484b035c5bb5a787b98d829`.
Para reproduzir as previsões: `python scripts/prepare_salvora_case.py`, a partir da raiz;
o script descarta as previsões armazenadas e usa somente as features e os rótulos originais.
Fonte: López Escobar, Fondo-Ferreiro, González-Castaño e Gil-Castiñeira,
[LoRa signal quality and GPS positioning time series dataset](https://doi.org/10.5281/zenodo.13835721),
CC BY 4.0. Não comparar seus erros com Antwerp como ranking: cenários e protocolos são distintos.

As licenças dos dados não constituem uma licença global para o código, slides ou textos do curso.
