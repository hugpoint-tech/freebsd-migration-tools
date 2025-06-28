#!/bin/bash

set -e

source .env

if [ -z "${GITEA_EMAIL}" -o -z "${GITEA_EXECUTABLE}" ]; then
   echo "Update your .env"
   exit 1
fi

${GITEA_EXECUTABLE} manager shutdown || (echo; echo "Could not bring down Gitea"; echo)

sudo -u postgres dropdb -i gitea
sudo -u postgres createdb gitea -O gitea -E UTF-8 -l en_US.UTF-8 --template template0

GITEA_ROOT=$(dirname ${GITEA_EXECUTABLE})
rm -rf ${GITEA_ROOT}/data/gitea-repositories/*
rm -rf ${GITEA_ROOT}/data/sessions/*
rm -rf ${GITEA_ROOT}/data/indexers/issues.bleve/*

${GITEA_EXECUTABLE} migrate

${GITEA_EXECUTABLE} admin user create  \
   --username ${GITEA_USERNAME} \
   --password ${GITEA_PASSWORD} \
   --email ${GITEA_EMAIL} \
   --admin \
   --must-change-password=false

${GITEA_EXECUTABLE} admin user create  \
   --username blender-bot \
   --password ${GITEA_PASSWORD} \
   --email blenderbot@example.com \
   --must-change-password=false

${GITEA_EXECUTABLE} admin auth add-oauth \
   --name blenderid \
   --provider blenderid \
   --use-custom-urls true \
   --custom-auth-url https://id.blender.org/oauth/authorize \
   --custom-token-url https://id.blender.org/oauth/token \
   --custom-profile-url https://id.blender.org/api/me \
   --key "${BLENDER_ID_OAUTH_CLIENT}" \
   --secret "${BLENDER_ID_OAUTH_SECRET}"

rm -f ./convert/user-ids.json

echo "Now restart Gitea"
