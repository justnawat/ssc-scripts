# Python Scripts for Filling SA Documents

These scripts are used to help the secretaries(?) of Science Society Club (and possibly of other clubs as well) to fill out the documents for SA.

## Dependencies

* Python 3 (tested with Python 3.9.7 on Windows 10)
  * Windows: [Python's website](https://www.python.org/downloads/)
  * MacOS: installation through Homebrew is recommended
* PyAutoGUI
  * `pip install pyautogui`
* Pandas
  * `pip install pandas`

## Usage

* `activity_members.py` is used to copy the responses from the spreadsheet into SA05
* `combine_members.py` parses every activity response file and combine them into one single csv file that is the list of club members (default name is `out.csv`)
* `trimrep_members.py` is used to add the club members from a csv file to SA05