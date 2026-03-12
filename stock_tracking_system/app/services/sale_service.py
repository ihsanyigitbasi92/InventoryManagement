
"""
Service layer for sale operations.
"""

def calculate_total_sales(sales):
    return sum(sale.total_price for sale in sales)
