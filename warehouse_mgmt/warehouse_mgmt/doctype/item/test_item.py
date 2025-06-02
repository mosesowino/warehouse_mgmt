# Copyright (c) 2025, Warehouse Mgmt and contributors
# License: MIT. See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase
from frappe import _

class TestItem(FrappeTestCase):

    def setUp(self):
        if not frappe.db.exists("Warehouse", "Test Warehouse"):
            frappe.get_doc({
                "doctype": "Warehouse",
                "warehouse_name": "Test Warehouse",
                "is_group": 0
            }).insert()

    def test_create_item(self):
        item = frappe.get_doc({
            "doctype": "Item",
            "item_code": "ITEM-001",
            "item_name": "Test Item",
            "description": "A test item",
            "default_warehouse": "Test Warehouse",
            "current_quantity": 10,
            "minimum_stock_level": 2,
            "uom": "Nos"
        })
        item.insert()

        self.assertEqual(item.item_code, "ITEM-001")
        self.assertEqual(item.default_warehouse, "Test Warehouse")
        self.assertEqual(item.current_quantity, 10)

    def test_required_fields(self):
        item = frappe.get_doc({
            "doctype": "Item",
            "item_code": "ITEM-REQ-TEST",
            "item_name": "",
            "uom": ""
        })
        with self.assertRaises(frappe.exceptions.MandatoryError):
            item.insert()


    def test_unique_item_code(self):
        frappe.get_doc({
            "doctype": "Item",
            "item_code": "ITEM-UNIQUE",
            "item_name": "First Item",
            "uom": "Nos",
            "current_quantity": 5
        }).insert()

        item = frappe.get_doc({
            "doctype": "Item",
            "item_code": "ITEM-UNIQUE",
            "item_name": "Duplicate Item",
            "uom": "Nos",
            "current_quantity": 3
        })

        with self.assertRaises(frappe.DuplicateEntryError):
            item.insert()

    def tearDown(self):
        for name in ["ITEM-001", "ITEM-UNIQUE"]:
            if frappe.db.exists("Item", name):
                frappe.delete_doc("Item", name, force=1)
        if frappe.db.exists("Warehouse", "Test Warehouse"):
            frappe.delete_doc("Warehouse", "Test Warehouse", force=1)
