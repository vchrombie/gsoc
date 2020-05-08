import re
import logging

import argparse
from argparse import RawTextHelpFormatter

from datetime import datetime as dt

PARTICIPANTS = set()

DAY_DATE_RE = re.compile("\[[A-Za-z ]+[a-zA-Z0-9 ]+\] ")
TIME_RE = re.compile("\[[0-9: ]+ (?:PM|AM) IST\] ")
COMMAND_RE = re.compile("[a-zA-Z0-9\<\>]+|$")

FMT = '%H:%M:%S'

LOG_FORMAT = "[%(asctime)s] - %(message)s"
DEBUG_LOG_FORMAT = "[%(asctime)s - %(name)s - %(levelname)s] - %(message)s"


def configure_logging(debug):
    """
    Configure logging.
    This function sets basic attributes for logging.
    :param debug: set the debug mode
    """
    if not debug:
        logging.basicConfig(level=logging.INFO,
                            format=LOG_FORMAT)
    else:
        logging.basicConfig(level=logging.DEBUG,
                            format=DEBUG_LOG_FORMAT)


def parse_args():
    """
    Setup command line argument parsing with argparse.
    """
    parser = argparse.ArgumentParser(
        description="log cleaner script argument parser",
        formatter_class=RawTextHelpFormatter
    )

    parser.add_argument("-t", "--target",
                        required=True,
                        help="target file\n\n")

    parser.add_argument("-s", "--source",
                        default="dump.txt",
                        help="source file of the irc log\n\n")

    parser.add_argument("-d", "--debug",
                        action='store_true',
                        help="set debug mode for logging\n\n")

    return parser.parse_args()


def get_date(content):
    """
    Extract the day and date of the meeting.
    :param content: whole content of the irc chat log
    :return day_date: the date and date string
    """
    day_date = re.findall(DAY_DATE_RE, content[0])[0]
    logging.info("date extracted")
    return day_date


def get_duration(content):
    """
    Extract the duration, start time and end time of the meeting.
    :param content: whole content of the irc chat log
    :return start_time: start time of the meeting
    :return end_time: end time of the meeting
    :return duration: duration time of the meeting
    """
    start_time = re.findall(TIME_RE, content[0])[0]
    end_time = re.findall(TIME_RE, content[-1])[0]
    duration = dt.strptime(end_time[1:-9], FMT) - dt.strptime(start_time[1:-9], FMT)
    logging.info("duration extracted")
    return start_time, end_time, duration


def check_participant(components):
    """
    Add the person to the participants.
    :param components: components of each line
    """
    par = components['command'].strip("<>")
    logging.debug("partcipant added to the list: " + par)
    PARTICIPANTS.add(par)


def parsed_line(line):
    """
    Function to breakdown the line to useful components.
    :param line: one line of the irc chat log
    :return components: components of each line
    """
    line = re.sub(DAY_DATE_RE, '', line)
    time_ = re.findall(TIME_RE, line)[0]
    line = re.sub(TIME_RE, '', line)

    command = re.findall(COMMAND_RE, line)[0]
    line = re.sub(COMMAND_RE, '', line, 1)

    line = line.strip()

    components = {
        "time_": time_,
        "command": command,
        "body": line
    }
    return components


def get_clean_line(line):
    """
    Extract the required contents from the line.
    :param line: one line of the irc chat log
    :return line: one line of the irc chat log
    """
    logging.debug("cleaning line started")
    components = parsed_line(line)

    if components["command"] == "Whois":
        line = ''
    if components["command"].startswith("<"):
        check_participant(components)

    line = components["time_"] + components["command"] + "\t" + components["body"] + "\n"
    logging.debug("cleaning line completed")
    return line


def main():
    """
    A script for cleaning and storing the irc chat log in a file.

    The script can be run via the command line:
        $ python3 irc-chat-log-cleaner.py -t 07-05-2020-community-bonding-1.txt

    Examples:
    --------

    * Create a file `meeting.txt` from the chat log file, 'meeting-dump.txt':
            $ python3 irc-chat-log-cleaner.py --source meeting-dump.txt --target meeting.txt
    """

    args = parse_args()

    target_file = str(args.target)
    source_file = str(args.source) if args.source else "dump.txt"

    configure_logging(args.debug)
    logging.info("start")

    logging.info("reading the source file of the irc log: " + source_file)
    with open(source_file) as f:
        content = f.readlines()

    start_time, end_time, duration = get_duration(content)
    date = get_date(content)

    logging.info("cleaning logs started")
    new_content = list()
    for line in content:
        new_content.append(get_clean_line(line))
    logging.info("cleaning logs completed")

    logging.info("writing into the target file: " + target_file)
    with open(target_file, "w") as f:
        f.write("date: " + date[1:-2] + "\n")
        f.write("participants: " + ", ".join(list(PARTICIPANTS)) + "\n")
        f.write("start time: " + start_time[1:-2] + "\n")
        f.write("end time: " + end_time[1:-2] + "\n")
        f.write("duration: " + str(duration) + " hours\n")
        f.write("-" * 80 + "\n\n")
        for line in new_content:
            f.write("%s" % line)


if __name__ == '__main__':
    try:
        main()
        logging.info("done!")
    except KeyboardInterrupt:
        sys.stderr.write("\n\nReceived Ctrl-C or other break signal. Exiting.\n")
        sys.exit(0)
