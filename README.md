# Table of Contents

- [Table of Contents](#table-of-contents)
  - [Requirements](#requirements)
  - [Setup](#setup)
  - [Basic Usage](#basic-usage)
  - [Tests Run](#run-tests)
  - [Directory Tree](#directory-tree)

## Requirements

Python 3.8+


## Setup

**Clone the repo**
    
    git clone https://github.com/azierariel/ufind-booking

**Create & activate virtual environment**

    python -m venv ufind.env

*Activate environment on Linux or Mac*

    source ufind.env/bin/activate

*Activate environment on Windows*

    ufind.env\Scripts\activate.bat

**Install dependencies**

    pip install -r requirements.txt

## Basic Usage

To start the crawler simply navigate to `booking_root` folder (scrapy project root's folder), and start the spider.

    scrapy crawl booking-parser

The crawler will download the html files from the [input bucket](https://objectstorage.eu-frankfurt-1.oraclecloud.com/p/HKPwyExBxajwCV6gO1UrXpYaviWXWcvXHRsh6P8t0q5apdb3ze-a63S_M7PhmaqR/n/frexf2i6jjbf/b/booking/o/) and store the scraped items in `json` format, in the [output bucket](https://objectstorage.eu-frankfurt-1.oraclecloud.com/p/L1Ls5t1H4WaIzg-Yno5lQZeYPjUVHgnc-vliGuq1fifElSTpgMYu9uH3HbMuG_G8/n/frexf2i6jjbf/b/booking-items/o/).

To list, add or download files from/into the buckets, one can use the given pre-authenticated urls and follow the simple instructions [here](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm) (See the section `Working with Pre-Authenticated Requests`).

## Tests Run

Once you've followed the setup instructions above, you can run the entire test suite locally from `booking_root` folder:

    python -m unittest booking/tests/spiders/test_booking_parser.py



## Directory Tree

    .
    ├── booking_root (scrapy project root's folder)
    │   ├── booking
    │   │   ├── helpers.py
    │   │   ├── __init__.py
    │   │   ├── items.py
    │   │   ├── middlewares.py
    │   │   ├── pipelines.py
    │   │   ├── settings.py
    │   │   ├── spiders
    │   │   │   ├── booking_parser.py
    │   │   │   └── __init__.py
    │   │   ├── task_loader.py
    │   │   └── tests
    │   │       ├── helpers.py
    │   │       ├── samples
    │   │       │   ├── invalid_booking_response.html
    │   │       │   └── valid_booking_response.html
    │   │       └── spiders
    │   │           └── test_booking_parser.py
    │   └── scrapy.cfg
    └── README.md

    6 directories, 15 files
