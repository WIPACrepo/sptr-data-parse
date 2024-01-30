# sptr-data-parse
Parse sptr_data email

## Setup
Typical Python environment setup. Can skip the last step if no `requirements.txt` was added.

    python3 -m venv env
    source env/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt

## Usage
Run some commands

    mkdir test-input
    mkdir test-output

Save a bunch of sptr_data email to the test-input directory

Run the process-sptr script

    ./process-sptr

Now you've got .json in the test-output directory. Summarize the time series.

    python summarize_sptr.py

Check the results in `count.csv` and `volume.csv`
