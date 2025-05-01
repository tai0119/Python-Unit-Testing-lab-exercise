git init

git add .

git commit -m "change"

git branch -M main

git push -u origin main


git remote -v

git remote set-url origin

git push origin main --force

# 2. Test Automation with GitHub Actions
python -m unittest discover -s . -p "*_test.py"
# 3. coverage report
View the Coverage Report

To see a simple report in your terminal:
coverage report

To generate a detailed HTML report:
coverage html

Then open the report:
start htmlcov/index.html   # On Windows