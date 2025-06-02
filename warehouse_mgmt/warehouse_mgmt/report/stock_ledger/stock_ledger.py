import frappe
from frappe.utils import flt

def execute(filters=None):
    columns = [
        {"label": "Posting Date", "fieldname": "posting_date", "fieldtype": "Date", "width": 100},
        {"label": "Item", "fieldname": "item", "fieldtype": "Link", "options": "Item", "width": 150},
        {"label": "Warehouse", "fieldname": "warehouse", "fieldtype": "Link", "options": "Warehouse", "width": 150},
        {"label": "Qty In", "fieldname": "qty_in", "fieldtype": "Float", "width": 100},
        {"label": "Qty Out", "fieldname": "qty_out", "fieldtype": "Float", "width": 100},
        {"label": "Valuation Rate", "fieldname": "valuation_rate", "fieldtype": "Currency", "width": 120},
        {"label": "Stock Value Change", "fieldname": "stock_value_change", "fieldtype": "Currency", "width": 150},
    ]

    conditions = []
    if filters.get("item"):
        conditions.append(f"item = '{filters.item}'")
    if filters.get("warehouse"):
        conditions.append(f"warehouse = '{filters.warehouse}'")
    if filters.get("from_date"):
        conditions.append(f"posting_date >= '{filters.from_date}'")
    if filters.get("to_date"):
        conditions.append(f"posting_date <= '{filters.to_date}'")

    where_clause = f"WHERE {' AND '.join(conditions)}" if conditions else ""

    data = frappe.db.sql(f"""
        SELECT
            posting_date,
            item,
            warehouse,
            CASE WHEN qty_change > 0 THEN qty_change ELSE 0 END AS qty_in,
            CASE WHEN qty_change < 0 THEN ABS(qty_change) ELSE 0 END AS qty_out,
            valuation_rate,
            stock_value_change
        FROM `tabStock Ledger Entry`
        {where_clause}
        ORDER BY posting_date ASC
    """, as_dict=True)

    return columns, data
