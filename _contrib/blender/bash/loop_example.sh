#!/bin/bash

set -e

# for scripts that require to be called by an external script, this is that external script
# you'll need to update:
# - the directory that is looped over
# - the extension of the files
# - the name of the script that is called
# the above three can be found at the bottom of this file
# depending on the machine you run this on, you may need to update the number of jobs run at same time (variable N)

# most of this file is taken from https://unix.stackexchange.com/questions/103920/parallelize-a-bash-for-loop

# initialize a semaphore with a given number of tokens
open_sem(){
    mkfifo pipe-$$
    exec 3<>pipe-$$
    rm pipe-$$
    local i=$1
    for((;i>0;i--)); do
        printf %s 000 >&3
    done
}

# run the given command asynchronously and pop/push tokens
run_with_lock(){
    local x
    # this read waits until there is something to read
    read -u 3 -n 3 x && ((0==x)) || exit $x
    (
     ( "$@"; )
    # push the return code of the command to the semaphore
    printf '%.3d' $? >&3
    )&
}

N=12 # set close to max number of cores on your machine
open_sem $N

find /data/example_dir -name '*.ext' | while read i; do
    run_with_lock bash /data/scripts/SCRIPT.sh $(basename $i)
done
