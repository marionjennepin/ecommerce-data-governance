# E-commerce Data Governance Framework
## Contexte:

Ce projet illustre la mise en place d’un framework de gouvernance des données appliqué à un cas e-commerce.

L’objectif est de simuler un environnement réel avec :
- des données de mauvaise qualité
- des incohérences métier
- des enjeux de conformité (RGPD)

---

## Objectifs:

- Améliorer la qualité des données
- Structurer la gouvernance des données
- Identifier et protéger les données sensibles (PII)
- Mettre en place des indicateurs de pilotage

---

## Périmètre:

Trois domaines métiers :

- Clients
- Produits
- Commandes

---

## Data Quality:

Mise en place de règles de contrôle :

- unicité des identifiants
- complétude des données
- validation des formats (email)
- règles métier (prix > 0, stock ≥ 0)
- intégrité référentielle

---

## Pipeline de transformation:

- suppression des doublons
- gestion des valeurs nulles
- filtrage des anomalies
- enrichissement des données

---

## Gouvernance des données:

- data dictionary
- définition des rôles (data owner)
- formalisation des règles de gouvernance
- suivi via KPI

---

## RGPD :
 
- identification des données sensibles
- hachage des emails
- anonymisation des utilisateurs
- simulation du droit à l’effacement

---

## KPI de gouvernance:

- taux de conformité des règles
- nombre d’anomalies détectées
- volumétrie des données traitées
- suivi des données sensibles

## Comment exécuter le projet: 

1) installer les dépendances : 
pip install -r requirements.txt

2) Générer les données :
python scripts/generate_data.py

3) Lancer les contrôles de qualité : 
python scripts/data_quality_checks.py

4) Transformer et nettoyer les données : 
python scripts/transform_data.py

5) Calculer les KPI de gouvernance : 
python scripts/governance_kpis.py

6) Lancer le dashboard : 
python -m streamlit run dashboard/app.py

## Résultats

Le projet permet de :

- détecter automatiquement les anomalies de qualité des données
- corriger les incohérences dans une couche "curated"
- suivre des indicateurs de gouvernance (qualité, volumétrie, conformité)
- visualiser les résultats via un dashboard interactif


## Structure du projet : 
```
ecommerce-data-governance/
│
├── data/
│ ├── raw/ # Raw input datasets with quality issues
│ └── curated/ # Cleaned and enriched datasets
│
├── scripts/ # Core data processing logic
│ ├── generate_data.py
│ ├── data_quality_checks.py
│ ├── transform_data.py
│ ├── rgpd_actions.py
│ └── governance_kpis.py
│
├── docs/ # Governance documentation
│ ├── data_dictionary.md
│ ├── governance_rules.md
│ ├── rgpd_policy.md
│ └── architecture.md
│
├── reports/ # Outputs and monitoring
│ ├── data_quality_report.csv
│ ├── governance_kpis.csv
│ └── screenshots/
│
├── dashboard/ # Streamlit app
│ └── app.py
│
├── requirements.txt
└── README.md
```


