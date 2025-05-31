#!/bin/bash

# name: generate_base_commit_ref.sh
# this is called from from an external script as "bash generate_base_commit_ref.sh PHID-DIFF-xyz"

# loop over json array jq
# PHID-DIFF-* from phab
jq -c '.[]' /data/phid_diff/$1 | while read i; do
	# get created time of diff
    UT=$(echo $i | jq -r '.fields.dateCreated')
    
	# convert to git readable date
	DT=$(date -d @$UT +"%F %T")
    LOOP_ID=$(echo $i | jq -r '.id')
    if [ -f /data/base/$LOOP_ID.base ];
    then
        echo "$LOOP_ID base exists"
        continue
    fi
    REFS_LEN=$(echo $i | jq '.fields.refs | length')
    if [ $REFS_LEN -ne "0" ];
    then
        echo "$LOOP_ID has refs"
        # If there is a base ref here, then use that and skip below
        # This now exists as "copy_known_base_ref.sh"
        continue
    fi

	# temporary git repo to operate on (as we assume we are running this script concurrently)
    git clone /tmp/blender /tmp/blender_$LOOP_ID
    cd /tmp/blender_$LOOP_ID
	# get sha of commit that was made directly prior to datetime
    HASH=$(git log --before="$DT" --pretty=format:"%H" -1)

	# checkout that commit
    git checkout $HASH
	# attempt to apply diff from phabricator
    git apply --check /data/diffs/$LOOP_ID.diff
    EX=$(echo $?)
    if [ $EX -eq "0" ];
    then
        echo "$LOOP_ID is good"
        echo "$HASH" > /data/base/$LOOP_ID.base
    else    
        echo "$LOOP_ID is bad"
    fi
    rm -rf /tmp/blender_$LOOP_ID
done