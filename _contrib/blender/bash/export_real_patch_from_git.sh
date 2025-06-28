#!/bin/bash

## name: export_real_patch_from_git.sh
## loops over PHID-CMITs, and exports the real patch for the commit sha from the git repo

# Loop through all PHID-CMIT*
find /data/phid_cmit -name "*.json" | while read line
do
	# fname is the PHID-CMIT* (with .json trimmed off end)
	fname=$(echo $(basename $line) | rev | cut -c 6- | rev)
	# cm is the URI of the cmit object
	cm=$(cat $line | jq -r '.uri')
	# hashofcommit is taken from the uri field, and the first 33 chars are trimmed due to them being https://developer.blender.org/...
	# note, this assumption doesn't hold for all commits, as some may be SVN commits, or be otherwise malformed
	hashofcommit=$(echo $cm | cut -c 33-)
	git -C /data/blender format-patch -1 $hashofcommit --stdout > /data/patches/$fname.patch
done