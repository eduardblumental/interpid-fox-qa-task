## **Interpid Fox QA Task**

### **Test Description**
This test suite automates the process of **requesting a demo** on the [Intrepid Fox](https://www.intrepidfox.tech) website using **Playwright**. It performs the following steps:

1. Opens the homepage and clicks the "Get a Demo" button.
2. Navigates to the Request Demo page and verifies the URL.
3. Fills in the demo request form with test data.
4. Checks the required checkbox for terms confirmation.
5. Submits the form and verifies that the CAPTCHA dialog appears.

---

### **Running the test**
1. Ensure you have **Python 3.9+** installed. 
2. Clone the repo and install the required dependencies.
```bash
pip install -r requirements.txt
playwright install
```
3. Run the test.
```bash
python -m pytest [-vs] [--headed] [file_or_dir]
```
