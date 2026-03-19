# Governance Rules

## Data Quality Controls
- customer_id must be unique and not null
- email must follow a valid format
- product price must be > 0
- stock cannot be negative
- order_id must be unique
- quantity must be > 0
- total_amount cannot be negative
- payment_method must not be null
- customer_id in orders must exist in customers
- product_id in orders must exist in products

## Governance Roles
- CRM Owner: accountable for customer master data
- Merchandising: accountable for product attributes
- Sales Ops: accountable for order integrity
- Finance: accountable for payment and revenue metrics