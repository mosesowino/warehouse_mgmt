import frappe
from frappe.tests.utils import FrappeTestCase
from datetime import date

class TestStockEntryItem(FrappeTestCase):

    def setUp(self):
        # Grab some existing item and warehouse for linking
        self.test_item = frappe.db.get_value("Item", {}, "name")
        self.test_warehouse = frappe.db.get_value("Warehouse", {}, "name")

        if not self.test_item or not self.test_warehouse:
            self.skipTest("No Item or Warehouse found in DB, skipping Stock Entry Item tests.")

    def test_create_stock_entry_item(self):
        # Create a Stock Entry with one Stock Entry Item child
        stock_entry = frappe.get_doc({
            "doctype": "Stock Entry",
            "stock_entry_type": "Receipt",
            "posting_date": date.today(),
            "items": [
                {
                    "doctype": "Stock Entry Item",
                    "item": self.test_item,
                    "qty": 5.0,
                    "source_warehouse": self.test_warehouse,
                    "target_warehouse": self.test_warehouse,
                    "valuation_rate": 100.0
                }
            ]
        })

        stock_entry.insert()
        self.assertTrue(stock_entry.name.startswith("STE-"))
        self.assertEqual(len(stock_entry.items), 1)

        item = stock_entry.items[0]
        self.assertEqual(item.item, self.test_item)
        self.assertEqual(item.qty, 5.0)
        self.assertEqual(item.source_warehouse, self.test_warehouse)
        self.assertEqual(item.target_warehouse, self.test_warehouse)
        self.assertEqual(item.valuation_rate, 100.0)

    def test_required_fields_on_stock_entry_item(self):
        # Test missing required fields in Stock Entry Item

        # Missing 'item' field
        stock_entry = frappe.get_doc({
            "doctype": "Stock Entry",
            "stock_entry_type": "Receipt",
            "posting_date": date.today(),
            "items": [
                {
                    "doctype": "Stock Entry Item",
                    "qty": 5.0,
                    "source_warehouse": self.test_warehouse,
                    "target_warehouse": self.test_warehouse,
                    "valuation_rate": 100.0
                }
            ]
        })

        with self.assertRaises(frappe.exceptions.MandatoryError):
            stock_entry.insert()

        # Missing 'qty' field
        stock_entry = frappe.get_doc({
            "doctype": "Stock Entry",
            "stock_entry_type": "Receipt",
            "posting_date": date.today(),
            "items": [
                {
                    "doctype": "Stock Entry Item",
                    "item": self.test_item,
                    "source_warehouse": self.test_warehouse,
                    "target_warehouse": self.test_warehouse,
                    "valuation_rate": 100.0
                }
            ]
        })

        with self.assertRaises(frappe.exceptions.MandatoryError):
            stock_entry.insert()
