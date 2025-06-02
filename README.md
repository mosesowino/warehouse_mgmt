### Warehouse Mgmt

for electronics x

---

## Installation

Follow these steps to install the **Warehouse Mgmt** application in your local Frappe bench environment.

### 1. Prerequisites

- You must have [Frappe Bench](https://frappeframework.com/docs/v14/user/en/bench) installed on your local machine.
- You should have at least one Frappe site already created in your bench instance.
- Ensure you have Git installed.

### 2. Navigate to Your Frappe Bench Directory

Open your terminal and change directory to your Frappe bench instance. For example:

```bash
cd /path/to/your/frappe-bench
```

### 3. Get the Warehouse Mgmt App from GitHub

Use the `bench get-app` command to download the app directly from this GitHub repository:

```bash
bench get-app https://github.com/mosesowino/warehouse_mgmt.git --branch main
```
This command will clone the app into your `apps` directory.

### 4. Install the App on Your Site

Now, install the app to a specific site in your bench. Replace `your-site-name` with the actual name of your site:

```bash
bench --site your-site-name install-app warehouse_mgmt
```
- If you are unsure about your site names, you can list them using:
  ```bash
  bench list-sites
  ```

**Note:** If your bench is running, you may need to restart it after installing the app.

### 5. Verify Installation

Login to your Frappe site via browser and check if "Warehouse Mgmt" appears in your modules.

---

## Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/warehouse_mgmt
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

---

## License

MIT
