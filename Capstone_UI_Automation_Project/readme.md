# 🛒 E-Commerce UI Automation — Capstone Project

> **IIHT | WIPRO — February 2026 | Software Testing Capstone**  
> Complete end-to-end UI automation for a live e-commerce web application using two industry-standard frameworks — Robot Framework (keyword-driven) and Pytest + Selenium (Page Object Model).

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
  - [Project 1 — Robot Framework](#project-1--robot-framework)
  - [Project 2 — Pytest + Selenium](#project-2--pytest--selenium)
- [Test Scenarios](#-test-scenarios)
- [How to Run](#-how-to-run)
  - [Robot Framework](#run-robot-framework)
  - [Pytest](#run-pytest)
- [Test Reports](#-test-reports)
- [CSV Data Files](#-csv-data-files)
- [Key Design Decisions](#-key-design-decisions)
- [Challenges Faced](#-challenges-faced)
- [Team Members](#-team-members)

---

## 📖 Project Overview

This project automates **5 critical end-to-end user journeys** on the [LambdaTest E-Commerce Demo](https://ecommerce.lambdatest.com) site using two completely different automation approaches:

| | Project 1 | Project 2 |
|---|---|---|
| **Framework** | Robot Framework | Pytest + Selenium |
| **Approach** | Keyword-Driven + Data-Driven | Page Object Model + Parametrize |
| **Test Scenarios** | 5 E2E + 1 full flow suite | 6 test functions |
| **Data Execution** | DataDriver Library + CSV | `@pytest.mark.parametrize` + CSV |
| **Total Runs** | 3 rows × 5 suites | 6 functions × 6 rows = **36 executions** |
| **Reports** | `report.html` + `log.html` | Timestamped `report_HH-MM-SS.html` |
| **Screenshots** | Auto-captured on failure via Teardown | Auto-embedded in HTML via conftest hook |

Both frameworks automate the **same 5 scenarios** — demonstrating that the same test goals can be achieved with keyword-driven and code-driven approaches.

---

## 🛠 Tech Stack

### Project 1 — Robot Framework

| Tool | Version | Purpose |
|---|---|---|
| Python | 3.x | Core language |
| Robot Framework | 6.x | Test runner & keyword orchestration |
| SeleniumLibrary | 6.x | Browser automation keywords |
| DataDriver | 1.x | CSV-based data-driven execution |
| Selenium WebDriver | 4.x | Browser control engine |
| ChromeDriver | Latest | Chrome browser driver |

### Project 2 — Pytest + Selenium

| Tool | Version | Purpose |
|---|---|---|
| Python | 3.x | Core language |
| Pytest | 7.x | Test runner & parametrize |
| Selenium WebDriver | 4.x | Browser automation |
| pytest-html | 3.x | HTML report generation |
| configparser | built-in | Read config.ini settings |

---

## 📁 Project Structure

### Project 1 — Robot Framework

```
rf_ecommerce/
│
├── 📂 tests/                        # Test suites — one file per scenario
│   ├── tc01_register_login.robot    # TC01: Registration + Login
│   ├── tc02_search_product.robot    # TC02: Product Search & Details
│   ├── tc03_add_to_cart.robot       # TC03: Add Product to Cart
│   ├── tc04_cart_update_remove.robot# TC04: Update Qty + Remove from Cart
│   ├── tc05_logout.robot            # TC05: Logout & Session Validation
│   └── tc0_endtoend_flow.robot      # 🔁 Full E2E suite (TC01→TC05 combined)
│
├── 📂 keywords/                     # Reusable keyword definitions
│   ├── login_keywords.robot         # Register + Login actions
│   ├── search_keywords.robot        # Search + Product detail actions
│   ├── cart_keywords.robot          # Cart + Update + Remove actions
│   ├── logout_keywords.robot        # Logout + Session check actions
│   └── email_generator.robot        # Dynamic email generation (timestamp-based)
│
├── 📂 resources/                    # Shared resources
│   ├── common.robot                 # Browser Open/Close + Screenshot Teardown
│   └── locators.robot               # ⭐ ALL element locators centralized here (POM)
│
├── 📂 variables/                    # Global variables
│   └── testdata.robot               # BASE_URL, BROWSER, WAIT_TIME
│
├── 📂 data/                         # CSV test data files
│   ├── register_data.csv            # 3 user rows for TC01 registration
│   ├── login_data.csv               # 3 credential rows for TC05
│   └── search_data.csv              # 3 product names for TC02/TC03/TC04
│
├── 📂 reports/                      # Auto-generated after every run
│   ├── report.html                  # Summary: pass/fail counts + suite results
│   ├── log.html                     # Detailed: every keyword step + timestamps
│   ├── output.xml                   # Machine-readable results
│   └── *.png                        # Auto-captured screenshots on failure
│
└── README.md
```

---

### Project 2 — Pytest + Selenium

```
pytest_ecommerce/
│
├── 📂 pages/                        # Page Object Model classes
│   ├── base_page.py                 # BasePage: find_element, click, send_keys, is_visible
│   ├── login_page.py                # LoginPage: navigate_to_login, login, data_register
│   ├── search_page.py               # SearchPage: search_product, select_product
│   ├── product_page.py              # ProductPage: add_to_cart_with_handling
│   ├── cart_page.py                 # CartPage: navigate_to_cart, edit_quantity, remove_item
│   └── account_page.py             # AccountPage: logout, is_logged_in, is_logged_out
│
├── 📂 tests/
│   ├── conftest.py                  # ⭐ Framework brain — fixtures + hooks
│   └── test_ecommerce.py            # 6 test functions with @pytest.mark.parametrize
│
├── 📂 config/
│   └── config.ini                   # browser=chrome, base_url=..., wait=15
│
├── 📂 data/
│   └── test_data.csv                # 6 user rows: first, last, email, password, product, qty
│
├── 📂 reports/                      # Auto-created by conftest.py
│   └── report_HH-MM-SS.html        # Timestamped HTML report (new file per run)
│
├── 📂 screenshots/                  # Auto-created on test failure
│   └── test_name_HH-MM-SS.png      # Failure screenshots embedded in HTML report
│
├── pytest.ini                       # Pytest configuration
└── README.md
```

---

## ✅ Test Scenarios

Both frameworks automate the same 5 E2E scenarios:

| TC | Scenario | CSV File | Key Assertions |
|---|---|---|---|
| **TC01** | User Registration & Login | `register_data.csv` | Success message visible · My Account page loads |
| **TC02** | Product Search & Details | `search_data.csv` | Product appears in results · Detail page title matches |
| **TC03** | Add Product to Cart | `search_data.csv` | Cart count increases · Product visible in cart |
| **TC04** | Update Cart Qty & Remove | `search_data.csv` | Qty updated · Cart empty message after remove |
| **TC05** | Logout & Session Validation | `login_data.csv` | Logout page title · URL has `route=logout` |

> ⚠️ **TC04 contains one intentional failure** — demonstrates automatic screenshot capture on failure. The failure screenshot is auto-embedded in the HTML report.

---

## ▶️ How to Run

### Prerequisites

```bash
# Install Python dependencies
pip install robotframework
pip install robotframework-seleniumlibrary
pip install robotframework-datadriver
pip install selenium
pip install pytest
pip install pytest-html
```

Make sure **ChromeDriver** is installed and matches your Chrome browser version.

---

### Run Robot Framework

```bash
# Run all test suites — save reports to reports/ folder
robot -d reports tests/

# Run a single test suite
robot tests/tc01_register_login.robot

# Run the full E2E combined suite
robot tests/tc0_endtoend_flow.robot

# Run with a specific browser
robot -v BROWSER:firefox -d reports tests/

# View reports
# Open reports/report.html in browser  → summary dashboard
# Open reports/log.html in browser     → step-by-step keyword execution
```

---

### Run Pytest

```bash
# Run all tests with HTML report
pytest tests/test_ecommerce.py -v --html=reports/report.html --self-contained-html

# Run with a specific browser (overrides config.ini)
pytest tests/test_ecommerce.py -v --browser=firefox

# Run a single test function
pytest tests/test_ecommerce.py::TestEcommerce::test_01_invalid_login -v

# View report
# Open reports/report_HH-MM-SS.html in browser
```

---

## 📊 Test Reports

### Robot Framework Reports

| File | Description |
|---|---|
| `reports/report.html` | Summary dashboard — total pass/fail, suite-level results, duration |
| `reports/log.html` | Full execution log — every keyword step, timestamps, failure screenshots embedded |
| `reports/output.xml` | Machine-readable XML output for CI integration |
| `reports/*.png` | Auto-captured failure screenshots (saved by Test Teardown) |

**Screenshot capture (Robot Framework):**
```robot
*** Settings ***
Test Teardown    Run Keyword If Test Failed    Capture Page Screenshot
```

---

### Pytest Reports

| File | Description |
|---|---|
| `reports/report_HH-MM-SS.html` | Timestamped HTML report — all 36 parametrized results, pass/fail per row |
| `screenshots/*.png` | Failure screenshots — auto-captured and base64-embedded into HTML report |

**Screenshot capture (Pytest — conftest.py hook):**
```python
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot = driver.get_screenshot_as_base64()
            # Embeds directly into HTML report
            extra = getattr(rep, "extra", [])
            extra.append(pytest_html.extras.html(
                f'<img src="data:image/png;base64,{screenshot}" style="width:100%"/>'
            ))
            rep.extra = extra
```

---

## 📋 CSV Data Files

### `register_data.csv` (Project 1 — TC01)

```csv
first_name,last_name,email,password,confirm_password,telephone
John,Smith,{random},Test@1234,Test@1234,9876543210
Jane,Doe,{random},Pass@5678,Pass@5678,9123456789
Alex,Kumar,{random},Hello@999,Hello@999,9000012345
```

> `{random}` is replaced at runtime by `email_generator.robot` — generates a unique timestamp-based email every run.

---

### `search_data.csv` (Project 1 — TC02/TC03/TC04)

```csv
search_term
HP LP3065
Nikon D300
iMac
```

---

### `test_data.csv` (Project 2 — all 6 test functions)

```csv
first_name,last_name,email,password,product,quantity
John,Smith,{random},Test@1234,HP LP3065,2
Jane,Doe,{random},Pass@5678,Nikon D300,1
Alex,Kumar,{random},Hello@999,iMac,3
...
```

---

## 💡 Key Design Decisions

### 1. Centralized Locators (POM Principle)
All element locators live in one file — `locators.robot` (RF) and individual page classes (Pytest).  
**Benefit:** If a web element changes, update ONE file — all tests stay intact.

### 2. Dynamic Email Generation
Registration tests generate a unique email using a timestamp on every run.  
**Benefit:** No "email already registered" failures across multiple test runs.

### 3. Defensive Handling for Out-of-Stock Products
```robot
${status}=    Run Keyword And Return Status    Click Element    ${ADD_TO_CART_BTN}
Run Keyword If    not ${status}    Log    Product out of stock — skipping cart step
```
**Benefit:** Tests don't crash when products are unavailable — they log and continue gracefully.

### 4. Explicit Waits over Sleep
Every element interaction uses `Wait Until Element Is Visible` (RF) or `WebDriverWait` (Pytest) with a 15-second timeout.  
**Benefit:** Tests are stable without unnecessary delays.

### 5. Timestamped Reports (Pytest)
Each run creates a new `report_HH-MM-SS.html` — old reports are never overwritten.  
**Benefit:** Full history of every test run is preserved.

---

## ⚠️ Challenges Faced

| # | Challenge | Solution |
|---|---|---|
| 1 | Duplicate email errors on re-run | `email_generator.robot` — timestamp-based unique email every run |
| 2 | Out-of-stock products crashing tests | `Run Keyword And Return Status` — skip gracefully if button missing |
| 3 | Intermittent failures due to slow page load | Replaced all `Sleep` with `Wait Until Element Is Visible` (15s timeout) |
| 4 | Locator breakage when site updated | All locators centralized in `locators.robot` — fixed once, worked everywhere |
| 5 | Cart popup load delay causing StaleElementError | Added explicit `WebDriverWait` for cart container before interacting |
| 6 | Screenshot not appearing in Pytest HTML report | Used `pytest_html.extras.html()` to embed base64 image inline |
| 7 | 36 browser launches per Pytest run (too slow) | Changed driver fixture scope to `class` — one browser per test class |

---

## 👥 Team Members

| Member | Project | Module Responsibility |
|---|---|---|
| Member 1 | Robot Framework | TC01 — Registration & Login |
| Member 2 | Robot Framework | TC02 — Product Search & Details |
| Member 3 | Robot Framework | TC03/TC04/TC05 — Cart + Logout |
| Member 4 | Pytest + Selenium | test_01/test_02 — Invalid Login & Registration |
| Member 5 | Pytest + Selenium | test_03/test_04 — Logout+Login & Search |
| Member 6 | Pytest + Selenium | test_05/test_06 — Cart Management & Logout |

---

> **IIHT | WIPRO · Software Testing Capstone · February 2026**
