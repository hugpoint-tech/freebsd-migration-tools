#!/bin/bash


## name: copy_patch_to_pr_dir.sh
## this is for getting the patch for a PR and copying it into
## the import directory for gitea named as the drev ID aka the PR ID

# make temp file so you can store variables without worrying about scope
tmpfile=$(mktemp /tmp/abc-script.XXXXXX)

# loop through all `PHID-DREV-*`
find /data/phid_drev -name "*.json" | while read line
do
	# get numerical ID so we can translate drev into PR
	drev_id=$(cat $line | jq -r '.id')
	echo "" > $tmpfile # set to blank
	# if patch file already exists then skip
	if [ -f "/data/convert/patches/$drev_id.patch" ]; then
		echo "skipping $drev_id"
		continue
	fi
	# loop through all transactions for drev (reference via numeric ID of drev)
	find /data/drev_transaction/$drev_id -name "*.json" | while read line2
	do
		# get commit phid from transaction so you can find newest
		# commit referenced in drev
		blaaah=$(cat $line2 | jq -r '.fields| .commitPHIDs? | .[]' 2> /dev/null)
		if [ "$blaaah" == "" ]; then
			continue
		fi
		if [[ $(echo $blaaah | grep '^PHID-CMIT.*') ]]; then
			echo $blaaah > $tmpfile
		fi
	done
	commit_id=$(cat $tmpfile)
	if [ "$commit_id" == "" ]; then
		continue
	fi
	echo $commit_id
    # note, this assumes that patches and gen_patches have been combined into same folder
	cp /data/combine_patches/$commit_id.patch /data/convert/patches/$drev_id.patch
done
rm "$tmpfile"