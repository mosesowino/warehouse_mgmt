import frappe
from frappe.model.document import Document

class StockEntryItem(Document):
    def validate(self):
        # Fetch parent type to determine logic
        entry_type = self.get_parent_doc().stock_entry_type if self.get_parent_doc() else None

        if entry_type == "Receipt":
            if not self.target_warehouse:
                frappe.throw("Target Warehouse is required for Receipt type entries.")
        elif entry_type == "Consume":
            if not self.source_warehouse:
                frappe.throw("Source Warehouse is required for Consume type entries.")
        elif entry_type == "Transfer":
            if not self.source_warehouse or not self.target_warehouse:
                frappe.throw("Both Source and Target Warehouses are required for Transfer type entries.")

    def get_parent_doc(self):
        # Use cached _parent or fetch fresh if necessary
        if hasattr(self, "_parent") and self._parent:
            return self._parent
        return self.get_parent_doc_from_db()

    def get_parent_doc_from_db(self):
        if self.parenttype and self.parent:
            return frappe.get_doc(self.parenttype, self.parent)
        return None
