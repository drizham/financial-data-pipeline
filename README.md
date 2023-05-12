The beginnings of an extensible data pipeline in python

### Built With

- [[yfinance][https://pypi.org/project/yfinance/]

### Prerequisites

This project runs on python3 & (To be confirmed)

## Getting started

Download this repository
Create a virtual environment with virtualenv

- Download virtualenv with pip or pip3:
  ```sh
  pip3 install virtualenv
  ```

From folder root, create virtual environment with:

```sh
virtualenv venv
```

Activate the virtual environment:

```sh
source venv/bin/activate
```

Install dependencies:

```sh
pip3 install yfinance
pip3 install python-dotenv (to load environment variables)
pip3 install kensu
pip3 install pyspark==3.3.0 (for custom lineage and data transfer)
pip3 install jupyter (optional)
pip3 install GitPython
pip3 install pandas==1.3.5
```

### Installation notes

- Pandas will be installed by yfinance
  Please replace it with pandas 1.3.5 for Kensu compatibility
  Please install it independently!

### Setting environment variables

If using a .env file to store environment variables such as

- kensu_ingestion_url
- kensu_ingestion_token

Load them in the current shell / terminal with:

```sh
export $(xargs < .env)
```

Within python use this to access the environment variables:

```sh
import os
print(os.environ['kensu_ingestion_url'])
```

## Usage

The entry file point is pipeline4.py
This file (includes Kensu observability)

1. Deletes previously downloaded and processed data files in the 'data lake'
2. Downloads and saves a single financial data instrument from yahoo finance with a wrapped yfinance call.
3. Calls interim application that sends the basic observability / statistics of the downloaded files in step one and saves it to another folder (interim0).
4. Appends data to a 'bronze' table (if there is no table it builds it)

pipeline4.py is where more processing steps should be added to.

TODO: BROKEN - Need to rebuild a pipeline that uses the direction suggester!!
pipeline3.py is the entry point for an emulator that emulates an bot that suggests trade directions based on a weeks worth of data.
It also includes a very basic data quality check before suggesting the trade direction

```sh
python3 pipeline4.py 'ES=F' 'lake1/' 'start_end_dates.csv'
```

When done running pipelines deactivate the virtual environment with:

```sh
deactivate
```

## Roadmap

- [] Downstream data processors
- [] Prediction with machine learning

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Contact

contact: contact@kensu.io
This project is supported by: https://www.kensu.io/
Try out the kensu community edition: https://www.kensu.io/community-edition-form
