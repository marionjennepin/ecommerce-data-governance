# Data Dictionary

## customers
| field | description | sensitive | owner |
|---|---|---|---|
| customer_id | unique customer identifier | yes | CRM Owner |
| first_name | customer first name | yes | CRM Owner |
| last_name | customer last name | yes | CRM Owner |
| email | customer email | yes | CRM Owner |
| city | customer city | no | Marketing |
| country | customer country | no | Marketing |
| signup_date | registration date | no | CRM Owner |
| birth_date | date of birth | yes | CRM Owner |
| phone | customer phone number | yes | CRM Owner |

## products
| field | description | sensitive | owner |
|---|---|---|---|
| product_id | unique product identifier | no | Merchandising |
| product_name | product label | no | Merchandising |
| category | product category | no | Merchandising |
| price | selling price | no | Merchandising |
| stock | available stock | no | Supply Chain |

## orders
| field | description | sensitive | owner |
|---|---|---|---|
| order_id | unique order identifier | no | Sales Ops |
| customer_id | customer reference | yes | Sales Ops |
| product_id | product reference | no | Sales Ops |
| quantity | quantity ordered | no | Sales Ops |
| order_date | order date | no | Sales Ops |
| payment_method | payment method | potentially sensitive | Finance |
| status | order status | no | Sales Ops |
| total_amount | order total amount | no | Finance |