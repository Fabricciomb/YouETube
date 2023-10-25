:: Check if Python is installed
python --version 2>NUL
if %errorlevel% neq 0 (
    echo Python is not installed. Installing Python...
    :: Download the Python installer
    curl -o python-installer.exe https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe
    :: Install Python silently
    python-installer.exe /quiet PrependPath=1 Include_test=0
    echo Python installed successfully.
    del python-installer.exe
)

:: Update pip
python -m pip install --upgrade pip

:: Install dependencies from requirements.txt
python -m pip install -r requirements.txt

:: Run main.py
python main.py

:: Pause for result visualization
pause
