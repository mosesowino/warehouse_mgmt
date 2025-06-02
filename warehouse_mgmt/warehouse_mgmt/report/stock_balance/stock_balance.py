import frappe
from frappe.utils import flt

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {"label": "Item", "fieldname": "item", "fieldtype": "Link", "options": "Item", "width": 150},
        {"label": "Warehouse", "fieldname": "warehouse", "fieldtype": "Link", "options": "Warehouse", "width": 150},
        {"label": "Quantity", "fieldname": "qty", "fieldtype": "Float", "width": 100},
        {"label": "Stock Value", "fieldname": "stock_value", "fieldtype": "Currency", "width": 120},
    ]

def get_data(filters):
    conditions = ""
    if filters.get("as_on_date"):
        conditions += f" AND posting_date <= '{filters['as_on_date']}'"

    return frappe.db.sql("""
        SELECT
            item,
            warehouse,
            SUM(qty_change) AS qty,
            SUM(stock_value_change) AS stock_value
        FROM `tabStock Ledger Entry`
        WHERE 1=1 {conditions}
        GROUP BY item, warehouse
        HAVING qty != 0
        ORDER BY item, warehouse
    """.format(conditions=conditions), as_dict=True)
