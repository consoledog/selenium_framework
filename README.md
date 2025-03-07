1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run tests:
   ```bash
   pytest --alluredir=allure-results
   ```
4. Generate report:
   ```bash
   allure serve allure-results
   ```
## 🐳 Docker
```bash
docker build -t selenium-framework .
docker run --rm selenium-framework
```