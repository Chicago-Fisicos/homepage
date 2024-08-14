#!/bin/bash

THIS_PATH="/home/wecher/01-disco/01-projects/homepage"
LOG_FILE="${THIS_PATH}/deploy.log"

IMAGE_NAME="chicago-fisicos"
#CONTAINER_NAME="chicago-fisicos"
#FULL_NAME="${IMAGE_NAME}:${CONTAINER_NAME}"


my-echo(){
    ############################################
    ############### LOG COLUMNS ################
    ####### Date,Time,Status,Description #######
    ############################################
    echo "$(date -I),$(date +"%T"),$1,$2" >> "${LOG_FILE}"
    telegram "$1: $2"
}


# Voy a la carpeta del proyecto
cd "${THIS_PATH}"

# Notificar
my-echo "OK" "Deploy start ${IMAGE_NAME}"

# Actualizar el código
git pull

# Reconstruir las imagenes que sean necesarias
docker compose up --build --detach

# Notificar
my-echo "OK" "Deploy end ${IMAGE_NAME}"


