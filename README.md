1. Clone the repository
2. Create virtual environment
   ```bash
   python3 -m venv venv
   ```
3. Activate virtual environment
   ```bash
   source venv/bin/activate  
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run tests by running bash script:
   ```bash
      ./run_tests.sh  
   ```
6. Generate report:
   ```bash
   allure serve allure-results
   ```
## 🐳 Docker
```bash
docker-compose up --build
```