#!/bin/bash
#A simple time tracker
#...............................................................................
flag=0 #Tracks if the task is running
start_time=$(date)
LOGFILE=~/.local/share/timer_logfile.txt
ELAPSED=~/.local/share/elapsed_logfile.txt
function track {
  if ! [ -f "$LOGFILE" ]; then
        touch $LOGFILE #Create a timer_logfile.txt if it is not existing already
  fi
  if ! [ -f "$ELAPSED" ]; then
        touch $ELAPSED #Create a elapsed_logfile.txt if it is not existing already
  fi
  function start {
    if [ "$flag" -eq 1 ]; then
      echo "Another task is already running. Use stop to stop the task" #Print an error message if the task is already running
    else
      if [ "$#" -eq 1 ]; then
        label=$1
        start_time=$(date)
        elapsed_start=$(date +%s) #converting the date to int
        flag=1
        echo "START $start_time" >> $LOGFILE #Add START line to the logfile
        echo "LABEL $label" >> $LOGFILE #Add LABEL line to the logfile
      else
        echo "This shell script needs one commandline argument [label]. Use start [label] to start a new task with a label" #Print an error message if the argument is missing
      fi
    fi
  }
  function stop {
    if [ "$flag" -eq 0 ]; then
      echo "No task is running. Use start [label] to start a new task with a label" #Print an error message if no task is running
    else
      stop_time=$(date)
      flag=0
      echo "END $stop_time" >> $LOGFILE #Add END line to the logfile
      echo " " >> $LOGFILE
      elapsed_stop=$(date +%s) #converting the date to int
      secounds=$(( (elapsed_stop-elapsed_start) )) #end time - start time
      echo "$label: $((secounds/3600)):$((secounds%3600/60)):$((secounds%60))" >> $ELAPSED
    fi
  }
  function status {
    if [ "$flag" -eq 0 ]; then
      echo "No task is currently running." #Tell if no task is currently running
    else
      echo "$label is currently running" #Tell which task is currently running
    fi
  }
  function log {
    cat $ELAPSED #Read the file
  }
  $1 $2
}
