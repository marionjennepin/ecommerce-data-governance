# RGPD Policy

## Sensitive Fields
- customer_id
- first_name
- last_name
- email
- birth_date
- phone

## Implemented Controls
- email hashing in curated layer
- anonymization function
- deletion function

## Principles
- raw layer = ingestion and control
- curated layer = cleaned and analytics-ready data
- sensitive data access should be restricted by role