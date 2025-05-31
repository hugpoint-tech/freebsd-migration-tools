#!/bin/bash

# name: generate_patch_stats.sh
# called from an external script as "bash generate_patch_stats.sh 123.diff"

# trim .diff from filename
d_id=$(echo $1 | rev | cut -c 6- | rev)

# skip if base doen't exist for $d_id
if [ ! -f /data/base/$d_id.base ]; then
    echo "skip de $d_id"
    exit 0
fi

# skip if patch file already exists
if [ -f /data/gen_patches/$d_id.patch ]; then
    echo "skip pe $d_id"
    exit 0
fi

## step 1
## generate header for patch file
##

# find id in DIFFs via regex :(
diff_phid=$(grep -ir "id\":$d_id," /data/phid_diff | awk -F':' '{print $1}')
drev_id=$(cat $diff_phid | jq -r '.fields.revisionPHID')

drev_title=$(cat /data/phid_drev/$drev_id.json | jq -r '.fields.title')
drev_summary=$(cat /data/phid_drev/$drev_id.json | jq -r '.fields.summary')
author_id=$(cat /data/phid_drev/$drev_id.json | jq -r '.fields.authorPHID')
#/data/user is PHID-USER-*
author_real=$(cat /data/phid_user/$author_id.json | jq -r '.fields.realName')
author_usern=$(cat /data/phid_user/$author_id.json | jq -r '.fields.username')
date_created=$(cat $diff_phid | jq -r '.fields.dateCreated' | awk '{print strftime("%c", $0)}')
bbase=$(cat /data/base/$d_id.base | sed 's/ *$//g')

touch /data/gen_patches/$d_id.patch

tee -a /data/gen_patches/$d_id.patch <<EOF
From $bbase Mon Sep 17 00:00:00 2001
From: $author_real <$author_usern@noreply.gitea.example>
Date: $date_created
Subject: [PATCH] $drev_title

$drev_summary
---
EOF

## step 2:
## generate diff stats
##

# copy clean repo
git clone /tmp/blender /tmp/blender_$d_id >/dev/null 2>&1
cd /tmp/blender_$d_id
base=$(cat /data/base/$d_id.base)

echo "base: $base"
git checkout $base
# diff cache is literal diff file exported from phabricator
# so this will generate the diff stats
git apply --stat /data/diffs/$1 > /data/gen_patches/$d_id.patch

## step 3:
## copy actual diff into patch file
echo "" >> /data/gen_patches/$d_id.patch
cat /data/diffs/$1 >> /data/gen_patches/$d_id.patch

# exit git repo before rm
cd /data
rm -rf /tmp/blender_$d_id