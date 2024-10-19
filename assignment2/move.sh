#!/bin/bash
#A simple shell script which moves all of the files in a directory to another directory
#-------------------------------------------------------------------------------
function move {
  #We take two commandline arguments and assign them to the variables
  src=$1 #1. argument is where the files you want to move are located
  dst=$2 #2. argument is where the files should be moved to
  #We check if we have two commandline arguments
  if [ "$#" -eq 3 ]; then
    echo "This shell script needs two commandline arguents." #Prints a error message
    exit
  #We check if a source directory does exists
  elif [ ! -d "$src" ]; then
    echo "Directory $src DOES NOT exists." #Prints a error message
    exit
  #We check if a destination directory does exists
  elif [ ! -d "$dst" ]; then
    echo "Directory $dst DOES NOT exists." #Prints a error message
    #And if wanted creating a one
    read -p "Do you want to create $dst (y/n)?" choice
    if [ "$choice" = y ]; then
      #Now we check if the user wants to add the current time to the directory name
      read -p "Do you want to add current time to the directory name (y/n)?" choice2
      if [ "$choice2" = n ]; then
        mkdir ${dst} #Makes a directory with a name provided by the user
      else
        dst="$dst-$(date +%Y-%m-%d-%H-%M)" #Adds a current time to the directory name
        mkdir "$dst"
      fi
    else
      exit
    fi
  fi
  #We check if the user want to move all the files or just a spesific type og files
  echo "Specify type of files to be moved (.datatype) or hit enter to move all"
  read
  mv ${src}/*$REPLY ${dst} #We now move the files
  exit
}
move $* #Run/call the function
