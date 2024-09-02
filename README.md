# 🚀 Automation Script Commits

Welcome to the **Automation Script Commits** repository! This project is designed to automate daily commits to a GitHub repository using a Python script. The script is configured to make multiple commits daily, which can be useful for testing or other purposes.

## 📁 Table of Contents

- [📜 Overview](#-overview)
- [⚙️ Setup](#-setup)
- [🔧 Configuration](#-configuration)
- [📅 Scheduling](#-scheduling)
- [📜 Usage](#-usage)
- [🛠️ Troubleshooting](#-troubleshooting)
- [📄 License](#-license)

## 📜 Overview

This project uses a Python script to create multiple commits in a GitHub repository daily. It leverages GitHub Actions to automate the running of this script at a specified time each day.

## ⚙️ Setup

### 🖥️ Prerequisites

- Python 3.9+
- Git
- GitHub account

### 🛠️ Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/CodeWithMayank-Py/automation-script-commits-new.git
    cd automation-script-commits-new
    ```

2. **Set up a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Configure GitHub Actions:**

   Ensure the `.github/workflows/daily-commits.yml` file is set up with the correct schedule and environment as described in the [Scheduling](#-scheduling) section.

## 🔧 Configuration

### 🌟 Customizing the Script

Edit `main.py` to customize the commit messages or the number of commits:

- **Modify commit messages:** Change the `commit_message` variable.
- **Adjust the number of commits:** Update the `for i in range(40)` loop in `main.py`.

### 📅 GitHub Actions

Ensure that the GitHub Actions YAML file in `.github/workflows/daily-commits.yml` is properly configured. It should look like:

```yaml
name: Daily Commits

on:
  schedule:
    - cron: '30 12 * * *'  # Runs at 12:30 PM UTC (05:30 PM IST)
  workflow_dispatch:  # Allows manual trigger if needed

jobs:
  daily-commits:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.9

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run script
        run: python main.py

      - name: Commit changes
        run: git status

```
## 📅 Scheduling

The script is scheduled to run daily at **05:30 PM IST** (12:30 PM UTC) using GitHub Actions. To confirm or adjust the schedule, edit the `cron` expression in the `.github/workflows/daily-commits.yml` file.

### Cron Expression

- **Cron Syntax:** `30 12 * * *`
  - `30` - Minute (30th minute)
  - `12` - Hour (12 PM UTC)
  - `*` - Day of the month (Every day)
  - `*` - Month (Every month)
  - `*` - Day of the week (Every day of the week)

## 📜 Usage

1. **Run Locally:** Test the script locally before deploying to ensure it behaves as expected. Run the following command:

    ```sh
    python main.py
    ```

2. **Deploy:** Once you have confirmed that everything works correctly, push your changes to the GitHub repository. The GitHub Actions workflow will handle the rest.

3. **Monitor Actions:** Check the "Actions" tab on GitHub to ensure the workflow is running as expected. This tab will provide information about each run and any potential errors.

## 🛠️ Troubleshooting

- **Workflow Not Triggering:** If the workflow is not running as expected:
  - Ensure that the `cron` schedule is correctly set in the `.github/workflows/daily-commits.yml` file.
  - Verify that the workflow file is properly committed to the repository.
  - Check the "Actions" tab for any error messages or failed runs.

- **Script Errors:** If the script fails to execute:
  - Review the logs provided in GitHub Actions for specific error messages.
  - Check the script’s dependencies and ensure all required modules are installed.

- **Authentication Issues:** If you encounter authentication errors:
  - Ensure that the `GITHUB_TOKEN` has the necessary permissions.
  - Verify that any secrets or environment variables required for authentication are correctly set up in the GitHub repository settings.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

Happy coding! 🚀 If you have any questions or run into issues, feel free to [open an issue](https://github.com/CodeWithMayank-Py/automation-script-commits-new/issues).


