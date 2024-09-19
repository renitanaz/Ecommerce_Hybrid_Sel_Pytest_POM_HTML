REM chrome
pytest -v -s -m "sanity" --html=Reports\report.html Testcases/  --browser chrome
REM pytest -v -s -m "sanity and regression" --html=Reports\report.html Testcases/  --browser chrome
REM pytest -v -s -m " regression" --html=Reports\report.html Testcases/  --browser chrome

REM Firefox
pytest -v -s -m "sanity" --html=Reports\report.html Testcases/  --browser firefox
REM pytest -v -s -m "sanity and regression" --html=Reports\report.html Testcases/  --browser chrome
REM pytest -v -s -m " regression" --html=Reports\report.html Testcases/  --browser chrome
