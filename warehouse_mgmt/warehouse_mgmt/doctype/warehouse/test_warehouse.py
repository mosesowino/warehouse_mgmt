import frappe
from frappe.tests.utils import FrappeTestCase

class TestWarehouse(FrappeTestCase):
    def test_create_warehouse(self):
        parent_warehouse = frappe.get_doc({
            "doctype": "Warehouse",
            "warehouse_name": "Parent Warehouse",
            "is_group": 1,
            "warehouse_type": "Storage"
        }).insert()

        self.assertEqual(parent_warehouse.warehouse_name, "Parent Warehouse")
        self.assertTrue(parent_warehouse.is_group)
        self.assertEqual(parent_warehouse.warehouse_type, "Storage")

        child_warehouse = frappe.get_doc({
            "doctype": "Warehouse",
            "warehouse_name": "Test Warehouse",
            "parent_warehouse": parent_warehouse.name,
            "is_group": 0,
            "warehouse_type": "Dispatch"
        }).insert()

        self.assertEqual(child_warehouse.parent_warehouse, parent_warehouse.name)
        self.assertFalse(child_warehouse.is_group)
        self.assertEqual(child_warehouse.warehouse_type, "Dispatch")

        self.assertEqual(child_warehouse.parent_warehouse, parent_warehouse.name)
