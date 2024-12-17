# Expense Management API

## Setup Instructions
1. Clone the repository.
2. Install dependencies: `pip install django djangorestframework`
3. Apply migrations: `python manage.py makemigrations && python manage.py migrate`
4. Run the server: `python manage.py runserver`

## Available Endpoints
- `POST /api/expenses/` : Create an expense
- `GET /api/expenses/` : List all expenses
- `GET /api/expenses/{id}/` : Retrieve an expense
- `PUT /api/expenses/{id}/` : Update an expense
- `DELETE /api/expenses/{id}/` : Delete an expense
- `GET /api/expenses/list_by_date/?user_id=&start_date=&end_date=` : List expenses by date range
- `GET /api/expenses/category_summary/?user_id=&month=&year=` : Get total expenses per category
