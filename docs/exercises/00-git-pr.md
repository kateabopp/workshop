## Create a new feature branch from the command line

```shell
# The '-b' argument tells git to create a new branch named 
# "add-divide-func-to-math" and change to that branch
git checkout -b add-divide-func-to-math
```

## Open 01-math.py, add a divide function and a call to test it

## Commit the change

```shell
# The "-m" argument tells git to set the specific message on the commit object
# The "." argument (not generally recommended) tells git to commit all changed files
git commit -m "Adding divide function to math" .

# The right way to target only the changed files is to list them one at a time
git commit -m "Adding divide function to math" practice/01-math.py docs/notes.txt
```

## Push the change

```shell
git push --set-upstream origin add-divide-func-to-math
```

## Check that the branch appeared on GitHub

## Create a Pull Request from GitHub

- Use the "add-divide-func-to-math" branch as the source branch
- Use the "main" branch as the target branch
- Review the changes for correctness
- If correct, merge the PR and delete the branch

## Check that the main branch has the changes you made

## Delete the feature branch from your laptop

```shell
# First change to the main branch
git checkout main

# Then delete the feature branch
git branch -D add-divide-func-to-math

# Refresh your local main
git pull
```
