#!/bin/bash

# Remove known top-level files.
rm -f \
  convert/import-all.sh \
  convert/tasks-to-org-repos.yml

# Erase everything except the Blender git directory, it's too cumbersome to keep cloning it.
for org_path in convert/*; do
  if [ "$org_path" = "convert/*" ]; then
    echo "Convert dir is already empty"
    break
  fi

  if [ -f $org_path ]; then
    # This is just a file, and since it wasn't erased at the top of this script,
    # it's either unknown or something that should be kept around (like convert/user-ids.json).
    echo "Not deleting file $org_path"
    continue
  fi

  echo $org_path
  for repo_path in $org_path/*; do
    if [ "$repo_path" = "$org_path/*" ]; then
      echo "    Organisation is already empty"
      break
    fi
    echo "    $repo_path"
    rm  -f $repo_path/*.yml
    rm -rf $repo_path/comments
    case $repo_path in
      convert/blender/blender)
        echo "      - not removing Blender git"
        ;;
      convert/blender/blender-translations)
        echo "      - not removing Blender Translations git"
        ;;
      *)
        rm -rf $repo_path/git
        ;;
    esac
    rmdir --ignore-fail-on-non-empty $repo_path
  done
  rmdir --ignore-fail-on-non-empty $org_path
done
