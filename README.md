# 🛒 SwagLabs Test Automation Framework

This project is a robust, scalable Selenium-based test automation framework for the [SwagLabs demo website](https://www.saucedemo.com). 
It uses Python, Pytest, and Page Object Model (POM) design pattern.

---

## 🚀 Tech Stack

- **Language**: Python 3.x
- **Automation Tool**: Selenium WebDriver
- **Test Runner**: Pytest
- **Design Pattern**: Page Object Model (POM)
- **Test Data Format**: JSON
- **Reports**: pytest-html
- **Logging**: Python built-in logging module

---

## 📁 Project Structure

E-commerceDemotest/
│
├── pageObjects/ # All page object files
│ ├── Login_Page.py
│ └── Products_Page.py
│ └── checkout_page.py
├── test_Data/
│ └── test_swaglabs.json # JSON test data for parameterized testing
│
├── tests/
│ └── test_login.py # Main test file with login & checkout flow
│
├── utilsfile/
│ ├── browser_utils.py
│ └── logger.py # Custom logger for logging to file
│
├── screenshots/ # Stores screenshots on failure
├── Logs/ # Contains log files
├── Reports/ # HTML test reports
│
├── conftest.py # Fixtures for browser and setup
├── requirements.txt # Python dependencies
└── README.md # You're here!

yaml
Copy
Edit

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/<your-username>/SwagLabs-TestAutomation.git
cd SwagLabs-TestAutomation
Create and activate a virtual environment

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # For Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
🧪 How to Run Tests
Run all tests
bash
Copy
Edit
pytest tests/
Run with HTML report
bash
Copy
Edit
pytest tests/ --html=Reports/report.html --self-contained-html
🖼️ Screenshots
Screenshots are saved in /screenshots/ folder if login or checkout fails.

📊 Logging
All test actions and results are logged in Logs/test_log.log using a custom Python logger.

✅ Features
 JSON-based test data

 Parametrized tests using pytest.mark.parametrize

 Dynamic screenshot capture on failure

 Reusable browser utilities

 POM-based structure for maintainability

 HTML test report generation

 Logging integration

🧹 To Do
 Add CI/CD integration (GitHub Actions or Jenkins)

 Integrate headless browser mode

 Dockerize the project (optional)

👨‍💻 Author
Your Name
Your GitHub Profile

📝 License
This project is for demo and educational purposes. Use it to learn and improve automation skills!

yaml
Copy
Edit

---

## ✅ Next Steps

- Paste this `README.md` into your project folder.
- Replace `Your Name` and GitHub links with yours.
- Commit and push again:

```bash
git add README.md
git commit -m "Add project README"
git push
