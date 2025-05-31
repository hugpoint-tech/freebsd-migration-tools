#!/bin/bash
set -e

# check if env var BLENDER_API_TOKEN is set
if [ -z "$BLENDER_API_TOKEN" ]; then
    echo "BLENDER_API_TOKEN is not set"
    exit 1
fi

while true; do
    echo "processing records after: $i"
    tmpfile=$(mktemp /tmp/dump_differentials.$i.XXXXXX)
    curl https://developer.blender.org/api/differential.revision.search \
        --silent \
        -d api.token=$BLENDER_API_TOKEN \
        -d after=$i -o $tmpfile
    if [ $(cat $tmpfile | jq '.result | length') -eq 0 ]; then
        rm $tmpfile
        echo "done"
        break
    fi
    i=$(cat $tmpfile | jq -r '.result.cursor.after')
    cat $tmpfile | jq '.result.cursor'

    jq -c '.result.data[]' $tmpfile | while read i; do
        # loop through each drev here and save their details
        # note, this does fail for some drevs, because the json is invalid (has quotes in the middle of a string that are unescaped)
        echo $i > /data/phid_drev/$(echo $i | jq -r '.phid').json
    done
    
done
