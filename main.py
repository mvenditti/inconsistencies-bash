import csv
import subprocess
from datetime import datetime
import re

file = "execute.csv"
results = "result.csv"


# Reads csv file and iterates over each row to execute bash command.
def read_file(file_name):
    results_file = "results-{}".format(datetime.now())
    init_result_file(results_file)
    lines = get_lines(file_name)
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            transaction = row[0]
            curl = row[4]
            if line_count != 0:
                print("----- STARTED PROCESS {} of {}".format(line_count, lines))
                print("----- START COMMAND EXECUTION ON TRANSACTION {} –––––".format(transaction))
                status, ok, raw = execute_command(curl)
                write_result(results_file, transaction, status, ok, raw)
                print("----- END COMMAND EXECUTION ON TRANSACTION {} –––––".format(transaction))
            line_count += 1


# Executes bash command as a system call.
def execute_command(curl):
    command = curl[:5] + ' -i ' + curl[5:]
    process = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    raw = str(process.stdout)
    output = raw.split(" ")
    status = output[1]
    ok = re.match("2\d\d", status) is not None
    print("----- STATUS OBTAINED: {} -----".format(status))
    if ok:
        raw = "Success"
    return status, ok, raw


def write_result(file_name, transaction, status, ok, raw):
    with open(file_name, 'a') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerow([transaction, status, ok, raw])


def init_result_file(file_name):
    with open(file_name, 'a') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerow(["Transaction ID", "Status", "Ok", "Raw"])


def get_lines(file_name):
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line_count += 1
        return line_count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_file(file)
