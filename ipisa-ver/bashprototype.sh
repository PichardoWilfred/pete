#!/bin/bash

function ipisa () {
    subject=$1
    export subject
    python3 creation.py
}

function show-s () {
    for subject in `ls 6to`
    do
        echo $subject
    done
}

function hor () {
    python3 hrio.py
}

function open (){
    subject=$1
    export subject
    python3 file_opener.py
}
