# README.md Assignment2 

## Task 2.1

### Prerequisites

- You need bash to run this shell script.

### Functionality

- Checks that the first directory exists and returns an error message to the user if it is not.
- Checks that the second directory (destination directory) exists and returns an error message to the user if it is not.
- Checks that there are at two commandline arguments passed and returns an error message to the user if the number of commandline arguments was wrong (not equal to two).
- The user can enter both the relative path and the full path as the arguments.
- The user can choose to move all the files or just spesific type of files.
- If the secound directory does not exist already, the directory gets created automatically (using the name passed as commandline argument by the user) if the user want.
- The user can choose to have the current date and time in the format YYYY-MM-DD-hh-mm added to the file name.

### Missing Functionality

- No "nice" options to stop the code when its running.

### Usage

- This shell script needs two argument provided by the user. The first argument should be the directory name (or the path) that the user want to move the files from and the secoud argument should be the directory that the user want to move the files to. 
- If the second directory does not exist, the user should answer y (for yes) or n (for no) when asked in order to create a new directory with the name passed as the second commandline argument by the user.
- The user should answer if the user wants to add the current time to the directory name when asked, y (for yes) or n (for no).
- If the user want to specify the type of files to be moved, the user can type ".datatype" (e.g. ".txt") when asked or hit enter to move all the files. The user should not enter quotes in the answer. 

## Task 2.2

### Prerequisites

- You need bash to run this shell script.

### Functionality

- Starts a new task with a label. (function start)
- Print an error message if a task is already running.
- Stops the current task, if there is one running. (function stop)
- Tells us what task we are currently tracking, or if we don’t have an active task (function status).
- If none arguments are given an error message is displayed in the terminal.
- If another task is running already an error message is displayed in the terminal.
- If no task is running but the user is trying to stop tracking an error message is displayed in the terminal.
- Data is stored in the timer_logfile.txt file
- The timer_logfile.txt is created by the script and located in ∼/.local/share/

### Usage

- Use source track.sh to use the function in the command line 
- **track start [label]**: Starts a new task with a label.
- **track stop**: Stops the current task if there is one running.
- **track status**: Tells us what task we are currently tracking, or if we don’t have an active task.
- Data is stored in the timer_logfile.txt file

## Task 2.3

### Prerequisites

- You need bash to run this shell script.

### Functionality

- Data is stored in the elapsed_logfile.txt file
- The elapsed_logfile.txt is created by the script and located in ∼/.local/share/
- Displays the time spent on each task

### Usage

- Use source track.sh to use the function in the command line 
- **track log**: Displays the time spent on each task
