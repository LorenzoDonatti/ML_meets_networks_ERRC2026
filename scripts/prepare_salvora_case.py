"""Preserva o experimento Sálvora para leitura gráfica, sem treino extra durante a aula."""
from pathlib import Path
import hashlib
import json
import numpy as np
import pandas as pd
from sklearn.model_selection import GroupShuffleSplit
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'data/localization.csv'
if not source.exists():
    source = ROOT / 'data/salvora_diagnostico.csv'
input_digest = hashlib.sha256(source.read_bytes()).hexdigest()
d = pd.read_csv(source)
# O arquivo de diagnóstico também preserva as entradas originais. Ao reproduzir,
# descartamos as saídas anteriores: elas nunca entram no treinamento.
d = d.drop(columns=['split', *[f'{name}_{coord}' for name in ('constante', 'centroide', 'knn', 'rf')
                              for coord in ('lat', 'lon')]], errors='ignore')
features = [f'{m}_{g}' for g in (1, 2, 3) for m in ('rssi', 'snr')] + ['spreading_factor']
tr, te = next(GroupShuffleSplit(n_splits=1, test_size=.2, random_state=42).split(d, groups=d.block_id))
X, y = d[features], d[['lat', 'lon']]
rf = make_pipeline(SimpleImputer(strategy='median', add_indicator=True),
                   RandomForestRegressor(n_estimators=100, max_depth=10, min_samples_leaf=3,
                                         random_state=42, n_jobs=1))
knn = make_pipeline(SimpleImputer(strategy='median', add_indicator=True), StandardScaler(),
                    KNeighborsRegressor(n_neighbors=5, weights='distance'))
g = np.array([[42.46972, -9.01345], [42.49955, -9.00654], [42.50893, -9.04902]])
r = X.iloc[te][['rssi_1', 'rssi_2', 'rssi_3']].to_numpy()
w = np.nan_to_num(10 ** ((r - np.nanmax(r, axis=1, keepdims=True))/10))
w /= w.sum(axis=1, keepdims=True)
predictions = {'constante': np.tile(y.iloc[tr].median().to_numpy(), (len(te), 1)),
               'centroide': w @ g,
               'knn': knn.fit(X.iloc[tr], y.iloc[tr]).predict(X.iloc[te]),
               'rf': rf.fit(X.iloc[tr], y.iloc[tr]).predict(X.iloc[te])}
d['split'] = 'treino'
d.loc[te, 'split'] = 'teste'
for name, pred in predictions.items():
    d.loc[te, [f'{name}_lat', f'{name}_lon']] = pred
target = ROOT / 'data/salvora_diagnostico.csv'
d.to_csv(target, index=False)
manifest = {'source': 'https://doi.org/10.5281/zenodo.13835721', 'license': 'CC-BY-4.0',
            'rows': len(d), 'train': len(tr), 'test': len(te), 'features': features,
            'split': 'GroupShuffleSplit(.2, random_state=42); blocos de 30 min por dispositivo.',
            'purpose': 'Diagnóstico retrospectivo; previsões pré-calculadas, treino sem previsões.',
            'gateway_coordinates_lat_lon': g.tolist(),
            'models': {'rf': '100 árvores, max_depth=10, min_samples_leaf=3, seed=42; imputação mediana + indicadores.',
                       'knn': 'k=5, weights=distance; imputação mediana + indicadores; StandardScaler no treino.',
                       'centroide': 'Pesos proporcionais a 10**(RSSI/10), normalizados nas recepções presentes.',
                       'constante': 'Mediana de cada coordenada do treino.'},
            'sha256': hashlib.sha256(target.read_bytes()).hexdigest(),
            'input_sha256': input_digest}
(ROOT / 'data/salvora_manifest.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False)+'\n')
print(f'{len(d)} posições preservadas; previsões para {len(te)} pacotes de teste.')
