import frappe
from frappe import _


@frappe.whitelist(allow_guest=True)
def get_available_items():
    return frappe.get_all("Item", filters={"current_quantity": [">", 0]}, fields=["item_code", "item_name", "current_quantity"])