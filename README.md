# Warehouse Mgmt

## Overview
Warehouse Mgmt is a comprehensive warehouse management module designed to efficiently manage inventory, stock movements, and warehouse operations. It provides tools to record stock receipts, consumption, transfers, and maintain accurate stock ledger entries. The app supports detailed tracking of items across multiple warehouses and generates insightful reports on stock balances and ledger entries.

## Features
- **Warehouse**: Manage warehouses and their hierarchical structure.
- **Item**: Define and manage items stored in warehouses.
- **Stock Entry**: Record stock receipts, consumption, and transfers between warehouses.
- **Stock Entry Item**: Manage individual items included in stock entries.
- **Stock Ledger Entry**: Maintain ledger entries for all stock movements.
- **Reports**:
  - **Stock Balance**: View current stock quantities and values per item and warehouse.
  - **Stock Ledger**: Detailed report of stock ledger entries.

## Installation
[Install bench](https://github.com/frappe/bench) then,

Install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app https://github.com/mosesowino/warehouse_mgmt.git --branch main
bench install-app warehouse_mgmt
```

## Usage

### Stock Entry Types
- **Receipt**: Record incoming stock to a warehouse.
- **Consume**: Record stock consumption or usage from a warehouse.
- **Transfer**: Move stock from one warehouse to another.

When a stock entry is submitted, corresponding stock ledger entries are created to reflect quantity and valuation changes in the warehouses.

### Stock Ledger
The stock ledger tracks all stock movements, maintaining accurate records of quantity changes and stock valuation over time.

## Data Models

### Warehouse
- **warehouse_name** (required): Name of the warehouse.
- **parent_warehouse**: Hierarchical parent warehouse (leave blank for top-level).
- **is_group**: Indicates if this is a logical group warehouse (not a physical location).
- **warehouse_type**: Type of warehouse - Storage, Dispatch, or Receiving (default: Storage).

Warehouses are organized hierarchically to represent physical or logical groupings.

### Item
- **item_code** (required, unique): Unique code for the item.
- **item_name** (required): Name of the item.
- **description**: Description of the item.
- **default_warehouse**: Primary storage location for this item.
- **current_quantity** (required): Manually updated quantity for simple tracking.
- **minimum_stock_level**: Alert threshold when stock falls below this level.
- **uom** (required): Unit of Measure.

### Stock Entry
- **naming_series** (required): Naming series for stock entries.
- **stock_entry_type** (required): Type of stock entry - Receipt, Consume, Transfer.
- **posting_date** (required): Date of the stock entry.
- **items** (required): Table of Stock Entry Items included in this entry.

### Stock Entry Item
- **item** (required): Linked item.
- **qty** (required): Quantity of the item.
- **source_warehouse**: Warehouse from which stock is consumed or transferred.
- **target_warehouse**: Warehouse to which stock is received or transferred.
- **valuation_rate**: Valuation rate of the item.

### Stock Ledger Entry
- **item**: Linked item (read-only).
- **warehouse**: Linked warehouse (read-only).
- **posting_date**: Date of the ledger entry (read-only).
- **qty_change**: Quantity change (positive for stock in, negative for stock out).
- **valuation_rate**: Valuation rate (read-only).
- **stock_value_change**: Computed stock value change (qty_change * valuation_rate).

## Reports

### Stock Balance
A query report showing the current stock quantity and value for each item in each warehouse. It supports filtering by date to view stock balances as of a specific date.

### Stock Ledger
A detailed report showing all stock ledger entries, providing a comprehensive audit trail of stock movements.

## Example Workflows

### Receiving Stock (Receipt)
1. Create a Stock Entry with type "Receipt".
2. Add items with quantities and target warehouse.
3. Submit the Stock Entry to update stock ledger and warehouse quantities.

### Consuming Stock (Consume)
1. Create a Stock Entry with type "Consume".
2. Add items with quantities and source warehouse.
3. Submit the Stock Entry to reduce stock quantities and update ledger.

### Transferring Stock (Transfer)
1. Create a Stock Entry with type "Transfer".
2. Add items with quantities, source warehouse, and target warehouse.
3. Submit the Stock Entry to move stock between warehouses and update ledger.

## Contributing
Moses Owino

## License
MIT
