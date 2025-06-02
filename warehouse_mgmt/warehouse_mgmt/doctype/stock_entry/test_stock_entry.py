import frappe
from frappe.tests.utils import FrappeTestCase
from datetime import date

class TestStockEntry(FrappeTestCase):

    def setUp(self):
        # Fetch existing Item and Warehouse names
        self.test_item = frappe.db.get_value("Item", {}, "name")
        self.test_warehouse = frappe.db.get_value("Warehouse", {}, "name")

        if not self.test_item or not self.test_warehouse:
            self.skipTest("No Item or Warehouse found in DB, skipping Stock Entry tests.")

    def test_create_stock_entry(self):
        doc = frappe.get_doc({
            "doctype": "Stock Entry",
            "stock_entry_type": "Receipt",
            "posting_date": date.today(),
            "items": [
                {
                    "doctype": "Stock Entry Item",
                    "item": self.test_item,
                    "qty": 10,
                    "target_warehouse": self.test_warehouse
                }
            ]
        })
        doc.insert()
        self.assertTrue(doc.name.startswith("STE-"))
        self.assertEqual(doc.stock_entry_type, "Receipt")
        self.assertEqual(len(doc.items), 1)

    def test_required_fields(self):
        doc = frappe.get_doc({
            "doctype": "Stock Entry"
        })
        with self.assertRaises(frappe.exceptions.MandatoryError):
            doc.insert()
