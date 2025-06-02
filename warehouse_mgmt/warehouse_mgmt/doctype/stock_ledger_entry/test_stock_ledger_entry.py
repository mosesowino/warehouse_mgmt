import frappe
from frappe.tests.utils import FrappeTestCase, patch
from datetime import date

class TestStockLedgerEntry(FrappeTestCase):

    def setUp(self):
        self.test_item = frappe.db.get_value("Item", {}, "name")
        self.test_warehouse = frappe.db.get_value("Warehouse", {}, "name")

        if not self.test_item or not self.test_warehouse:
            self.skipTest("No Item or Warehouse found in DB, skipping Stock Ledger Entry tests.")

    def test_stock_ledger_entry_created_via_stock_entry(self):
        stock_entry = frappe.get_doc({
            "doctype": "Stock Entry",
            "posting_date": date.today(),
            "items": [
                {
                    "doctype": "Stock Entry Item",
                    "item": frappe.db.get_value("Item", {}, "name"),
                    "qty": 5,
                    "source_warehouse": frappe.db.get_value("Warehouse", {}, "name"),
                    "target_warehouse": frappe.db.get_value("Warehouse", {}, "name"),
                    "valuation_rate": 100.0
                }
            ]
        })
        stock_entry.insert()
        stock_entry.submit() 

        sle = frappe.get_all("Stock Ledger Entry",
                             filters={"item": stock_entry.items[0].item},
                             limit=1,
                             order_by="posting_date desc")

        self.assertTrue(len(sle) > 0, "Stock Ledger Entry should be created automatically")

        sle_doc = frappe.get_doc("Stock Ledger Entry", sle[0].name)
        self.assertEqual(sle_doc.qty_change, 5)
        self.assertEqual(sle_doc.valuation_rate, 100.0)

