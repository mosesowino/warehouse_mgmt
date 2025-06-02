from .stock_entry_controller import StockEntry

import frappe
from frappe.model.document import Document

class StockEntry(Document):
    def on_submit(self):
        for item in self.items:
            self.create_ledger_entry(
                item=item.item,
                warehouse=item.target_warehouse or item.source_warehouse,
                posting_date=self.posting_date,
                qty=item.qty,
                valuation_rate=item.valuation_rate
            )

    def create_ledger_entry(self, item, warehouse, posting_date, qty, valuation_rate):
        frappe.get_doc({
            "doctype": "Stock Ledger Entry",
            "item": item,
            "warehouse": warehouse,
            "posting_date": posting_date,
            "qty_change": qty,
            "valuation_rate": valuation_rate,
            "stock_value_change": qty * valuation_rate,
            "parent": self.name,
            "parenttype": "Stock Entry",
            "parentfield": "auto_created"  # Arbitrary name since it's not a declared child table
        }).insert(ignore_permissions=True)
