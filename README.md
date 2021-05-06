# gspread (Google Spreadsheets Python API) Demo

## Description
Demo of basic functions of using `gspread` to read contents of a GoogleSheet.

## Prerequisites
- Python 3
- gpread
- Google Cloud Project with "Google Drive API" and "Google Sheets API" enabled
- Google Cloud Project Authentication Credentials

## Project Set-up
- Create a Google Cloud Project
  - Go to the Google Cloud Console[1] and create a new project (or select an existing project).
  - Enable the "Google Drive API" for the project
  - Enable the "Google Sheets API" for the project

[1] https://console.cloud.google.com/

- Create credentials for the project (this project uses a Service Account)[2]
  - Go to “APIs & Services > Credentials” and choose “Create credentials > Service account key”
  - Click on "Manage service accounts" and click on project in the "Email" column
  - Click on "KEYS" and add a new JSON type key. This will automatically download the credentials file.
  - Go to your spreadsheet and share it with the _client_email_ in the credentials file.
  - Move the downloaded file to ~/.config/gspread/service_account.json. Windows users should put this file to %APPDATA%\gspread\service_account.json.
  - The set-up is now ready to run your Python script to access the gSheet data!
See the gspread docs [2] for more details.

[2] https://gspread.readthedocs.io/en/latest/oauth2.html


## Usage
- Create a virtual environment:\
  `python3 -m venv env`

- Activate the virtual environment:\
  `source env/bin/activate`
  (Note: to deactivate the virtual environment type `deactivate`)

- Install the requirements
  `pip install -r requirements.txt`

- Run the script
`python main.py`

