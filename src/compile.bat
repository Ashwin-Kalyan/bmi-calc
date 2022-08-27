cd "C:\Users\Ashwin\Desktop\Programming Portfolio\Finished Projects\bmi-calc\src"
python.exe -m pip install --upgrade pip
pip install pyinstaller
pyinstaller --onefile --noconsole --icon="C:\\Users\\Ashwin\\Desktop\\Programming Portfolio\\Finished Projects\\bmi-calc\\icon\\favicon.ico" -w "main.py"