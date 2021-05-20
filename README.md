# inconsistencies-bash
Simple Python based script to remedy inconsistent transactions. 

## Running Instructions

1. Clone repository

```
git clone
```

2. Paste dup-tool CSV output into file named execute.csv (including column names)

- *Get inconsistent transactions*
```
duptool get --date-from 2021-05-13T11:00:00Z --date-to 2021-05-19T13:00:00Z -t 'token-value'
```

- *Analyze cases*
```
duptool analyze -t=token-value
```

3. Run script

```
python3 main.py
```

## Execution

The script will execute the following steps in sequence:

- Read each line from the execution.csv file.
- Obtain transaction id and remedy curl from current csv row.
- Execute curl and obtain http status code, returning boolean value indicating if it was successful (Http status code in the 2xx range).
- Execution returns raw response if the status was not considered ok.
- Results are then written to output file containing transaction id, response status, ok value, and raw message.

## Input file structure

execute.csv file should follow the given structure of the dup-tool output:

* transaction id
* operation
* description
* result
* remedy
