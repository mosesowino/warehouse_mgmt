from frappe import _

def get_data():
    return [
        {
            "module_name": "Warehouse Mgmt",
            "color": "blue",
            "icon": "octicon octicon-file-directory",
            "type": "module",
            "label": _("Warehouse Mgmt"),
            "description": _("Warehouse Management Module"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Warehouse",
                    "label": _("Warehouse"),
                    "description": _("Manage warehouses and their hierarchy."),
                    "onboard": 1
                },
                {
                    "type": "doctype",
                    "name": "Stock Entry",
                    "label": _("Stock Entry"),
                    "description": _("Record stock receipts, consumption, and transfers."),
                    "onboard": 1
                },
                {
                    "type": "doctype",
                    "name": "Stock Entry Item",
                    "label": _("Stock Entry Item"),
                    "description": _("Items included in a stock entry."),
                },
                {
                    "type": "doctype",
                    "name": "Stock Ledger Entry",
                    "label": _("Stock Ledger Entry"),
                    "description": _("Ledger entries for stock movements."),
                },
                {
                    "type": "doctype",
                    "name": "Item",
                    "label": _("Item"),
                    "description": _("Items managed in the warehouse."),
                },
                {
                    "type": "report",
                    "name": "Stock Ledger",
                    "doctype": "Stock Ledger Entry",
                    "is_query_report": True,
                    "label": _("Stock Ledger"),
                    "description": _("Report showing stock ledger entries."),
                },
                {
                    "type": "report",
                    "name": "Stock Balance",
                    "doctype": "Stock Ledger Entry",
                    "is_query_report": True,
                    "label": _("Stock Balance"),
                    "description": _("Report showing stock balances."),
                }
            ]
        }
    ]
