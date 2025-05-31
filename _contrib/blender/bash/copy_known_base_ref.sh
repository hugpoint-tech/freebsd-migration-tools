#!/bin/bash

# name: copy_known_base_ref.sh
# this file is called directly, as it doesn't need to be run concurrently

find /data/phid_diff -name '*.json' | while read i; do
    jq -c '.[]' $i | while read j; do
        LOOP_ID=$(echo $j | jq -r '.id')
        if [ -f /data/base/$LOOP_ID.base ];
        then
            echo "$LOOP_ID base exists"
            continue
        fi

        REFS_LEN=$(echo $j | jq '.fields.refs | length')
        if [ $REFS_LEN -eq "0" ];
        then
            echo "$LOOP_ID has no refs"
            continue
        fi
        BASE=$(echo $j | jq -r '.fields.refs[] | select(.type = "base") | .identifier')
        echo $BASE > /data/base/$LOOP_ID.base
    done
done