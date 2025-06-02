from frappe import _

def get_data():
    return {
        "module_name": "Warehouse Mgmt",
        "color": "blue",
        "icon": "octicon octicon-file-directory",
        "type": "module",
        "label": _("warehouse management"),
        "items": [
            {
                "type": "doctype",
                "name": "Item",
                "label": _("Item"),
            },
            {
                "type": "doctype",
                "name": "Warehouse",
                "label": _("Warehouse"),
            },
            {
                "type": "doctype",
                "name": "Stock Ledger Entry",
                "label": _("Stock Ledger Entry"),
            },
            {
                "type": "doctype",
                "name": "Stock Entry Item",
                "label": _("Stock Entry Item"),
            },
            {
                "type": "doctype",
                "name": "Stock Entry",
                "label": _("Stock Entry"),
            },
        ]
    }