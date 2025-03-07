1. Clone the repository
2. Activate virtual environment
   ```bash
   source venv/bin/activate  
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run tests:
   ```bash
   pytest --alluredir=allure-results
   ```
5. Generate report:
   ```bash
   allure serve allure-results
   ```
## 🐳 Docker
```bash
docker-compose build
docker-compose up
```