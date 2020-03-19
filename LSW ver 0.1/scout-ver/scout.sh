#!/bin/bash

#Especialidades
function esp() {
    espec=$1
    export espec
    python3 especialidad_auto.py
}

function show-e () {
    for subject in `ls Especialidades`
    do
        echo $subject
    done
}

function new-e() {
    esp_name=$1
    export esp_name
    python3 especialidad_create.py
}


#Primera Clase
function 1era () {
    tarea=$1
    export tarea
    python3 firstclass_auto.py
}

function new-1() {
    tarea=$1
    export tarea
    python3 firstclass_create.py
}

function show-1 (){
    for tarea in `ls 1era\ Clase`
    do
        echo $tarea
    done
}

