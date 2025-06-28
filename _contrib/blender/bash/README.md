# bash-migration-tools

To be used in combination with [python-migration-tool](https://future.projects.blender.org/blender-migration/python-migration-tool).

## Directories:

The list of directories, and what they contain. At least, what the shell scripts assume they contain.

```text
/data/blender     - a git clone of https://git.blender.org/blender.git
/tmp/blender_XYZ  - a temporary clone of /data/blender, where XYZ is the
					unique identifier to be used during git apply/am testing
/data/scripts     - all of the below shell scripts
/data/phid_user   - storing all PHID-USERs
/data/phid_cmit   - storing all PHID-CMITs
/data/phid_diff   - storing all PHID-DIFFs
/data/phid_drev   - storing all PHID-DREVs
/data/drev_transactions/NN/NNN.json - storing all transactions for a DREV (where N is an int ID of drev/txn)

/data/diffs       - storing all extracted diffs (using DIFF numerical ID)
/data/base        - storing all generated base commit sha1s (using DIFF numerical ID)
/data/patches     - storing all extracted patches from git (using PHID-DIFF)
/data/gen_patches - storing all extracted patches from git (using PHID-DIFF)
/data/combine_patches - a combination of patches & gen_patches folder (created using cp and making sure that
                        there is a conflict then the real patches from /data/patches are used)

/data/convert     - patch files, that are named as the PR number they match
                    this will be copied to the import directory of that Gitea
                    will use in combination with the yaml from python-migration-tool
```

Note: the phid_*, drev_transactions, and diffs directories assumed to be populated from export from Phabricator

## shell scripts:

* dump_users.sh
  * outputs all users from Phabricator into /data/phid_user
* dump_drev.sh
  * outputs all drevs from Phabricator into /data/phid_drev
* loop_example.sh
  * an example of a script that could be used to loop over files to be the external script to call both generate_base_commit.sh and generate_patch_stats.sh
* copy_known_base_ref.sh
  * loops over all Phid_diffs, and copies the base ref from the diff to the base directory
* generate_base_commit.sh
  * create synthetic base commit for all remaining diffs
  * to be run after copy_known_base_ref.sh
  * to be called from from an external script as "bash generate_base_commit_ref.sh PHID-DIFF-xyz.json" due to concurrency requirements
* export_real_patch_from_git.sh
  * export real patch from git, for all diffs
* generate_patch_stats.sh
  * creates a git patch file from diff, and generates stats using bases, and generates header from phab json
  * to be called from from an external script as "bash generate_patch_stats.sh 123.diff" due to concurrency requirements
  * to be run after generate_base_commit.sh
* copy_patch_to_pr_dir.sh
  * this is for getting the patch for a PR and copying it into the import directory for gitea named as the drev ID aka the PR ID
  * to be run last