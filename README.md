# WeatherAPI

The application sends an API request to the weather site, 
then writes this data to the DB,
and these actions are repeated every hour (since the data on the site itself is updated hourly). 
In parallel with this, when launched, the data is exported from the database to an .xlsx file.

## Setup

1. clone repository
    ```bash
    git clone https://github.com/Trydimas/WeatherAPI
    cd WeatherAPI
    ```
2. setup requirements
    ```bash
    pip install -r requirements.txt
    ```

## Use

```bash
    cd src
    py main.py weather.xlsx
```


