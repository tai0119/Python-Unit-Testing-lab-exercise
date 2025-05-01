git remote -v
git remote set-url origin 

git push origin main --force


# 3. coverage report
View the Coverage Report

To see a simple report in your terminal:
coverage report

To generate a detailed HTML report:
coverage html

Then open the report:
start htmlcov/index.html   # On Windows