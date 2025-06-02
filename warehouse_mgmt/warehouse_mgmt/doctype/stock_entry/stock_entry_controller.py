import frappe
from frappe.model.document import Document

class StockEntry(Document):
    def on_submit(self):
        for item in self.items:
            qty = item.qty
            valuation_rate = item.valuation_rate or 0.0

            if self.stock_entry_type == "Receipt":
                self.create_ledger_entry(
                    item.item,
                    item.target_warehouse,
                    self.posting_date,
                    qty,
                    valuation_rate
                )

            elif self.stock_entry_type == "Consume":
                self.create_ledger_entry(
                    item.item,
                    item.source_warehouse,
                    self.posting_date,
                    -qty,
                    valuation_rate
                )

            elif self.stock_entry_type == "Transfer":
                # Out from source
                self.create_ledger_entry(
                    item.item,
                    item.source_warehouse,
                    self.posting_date,
                    -qty,
                    valuation_rate
                )
                # Into target
                self.create_ledger_entry(
                    item.item,
                    item.target_warehouse,
                    self.posting_date,
                    qty,
                    valuation_rate
                )

    def create_ledger_entry(self, item, warehouse, posting_date, qty_change, valuation_rate):
        if not warehouse:
            frappe.throw("Warehouse must be specified for ledger entry.")

        stock_value_change = qty_change * valuation_rate

        frappe.get_doc({
            "doctype": "Stock Ledger Entry",
            "item": item,
            "warehouse": warehouse,
            "posting_date": posting_date,
            "qty_change": qty_change,
            "valuation_rate": valuation_rate,
            "stock_value_change": stock_value_change
        }).insert(ignore_permissions=True)
