 🛒 SwagLabs Test Automation Framework

This project is a robust, scalable Selenium-based test automation framework for the [SwagLabs demo website](https://www.saucedemo.com). 
It uses Python, Pytest, and Page Object Model (POM) design pattern.

🚀 Tech Stack

- **Language**: Python 3.x
- **Automation Tool**: Selenium WebDriver
- **Test Runner**: Pytest
- **Design Pattern**: Page Object Model (POM)
- **Test Data Format**: JSON
- **Reports**: pytest-html
- **Logging**: Python built-in logging module

 📁 Project Structure

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

📦 Installation

1. Clone the repository

git clone https://github.com/sangeetha-sivarajan/SwagLabs-Software_Testing.git
cd SwagLabs-TestAutomation
2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate  # For Windows
3. Install dependencies
pip install -r requirements.txt
🧪 How to Run Tests
1. Run all tests

pytest tests/
2. Run with HTML report

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


👨‍💻 Author

Sangeetha R
Github profile  : sangeetha-sivarajan

📝 License
This project is for demo and educational purposes. Use it to learn and improve automation skills!



 
