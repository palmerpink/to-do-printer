@echo off
REM Change directory to your project root if necessary
cd C:\Users\cmacm\OneDrive\Documents\Git Projects\to-do

REM Run your Python script using the venv's Python interpreter
REM Replace 'venv' with the name of your virtual environment folder
.venv\Scripts\python.exe quote.py

REM The script automatically exits the venv context when finished
Pause