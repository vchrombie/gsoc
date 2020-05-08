> This directory consists the scripts that I used for my work during the GSoC period.

### irc-chat-log-cleaner

A script for cleaning and storing the irc chat log `dump.txt` in a target file.

The script can be run via the command line:

```
$ python3 irc-chat-log-cleaner.py -t 07-05-2020-community-bonding-1.txt
```

Examples:

* Create a file `meeting.txt` from the chat log file, `meeting-dump.txt`:

```
$ python3 irc-chat-log-cleaner.py --source meeting-dump.txt --target meeting.txt
```

This work was initially made by Polaris000, [LogCleaner.py](https://github.com/Polaris000/GSoC_19_Perceval_Implementations/blob/master/IRC_chats/LogCleaner.py).
