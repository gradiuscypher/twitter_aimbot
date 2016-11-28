#!/bin/bash

IFS='/' read -a SPLIT <<< $2
FULLPATH=`realpath $2`
ACTION=$1

if [ "$1" == "enable" ]
then
    ln -s $FULLPATH tactical_visors_active/${SPLIT[-1]}
fi

if [ "$1" == "disable" ]
then
    rm $2
fi
