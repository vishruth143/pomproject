python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
py.test -s -v --html=reports/report.html --capture=tee-sys --junitxml="reports/result.xml"