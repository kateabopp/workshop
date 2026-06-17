## Make sure your local main branch is current with origin (GitHub in your case)

```shell
# The "checkout" command without any arguments tells git to change to that branch
git checkout main
git pull
```

## Create a new feature branch from the tip of the main branch

```shell
# The "checkout" command with the '-b' argument tells git to create a new 
# branch named "add-error-handling-to-divide" and change to that branch
git checkout -b add-error-handling-to-divide
```

## Open 01-math.py, update the divide function as follows

- If y is 0, then print an error saying so
- Otherwise, return the quotient (i.e. current behavior)

## Commit the change

```shell
# The "-m" argument tells git to set the specific message on the commit object
git commit -m "Adding error handling to divide function in math" practice/01-math.py
```

## Push the change to origin, i.e. GitHub

```shell
git push --set-upstream origin add-error-handling-to-divide
```

## Check that the branch appeared on GitHub

## Create a Pull Request from GitHub

- Use the "add-error-handling-to-divide" branch as the source branch
- Use the "main" branch as the target branch
- Review the changes for correctness
- If correct, merge the PR and delete the branch in the GitHub UI

## Check that the main branch has the changes you made on GitHub

## Delete the feature branch from your laptop

```shell
# First change to the main branch
git checkout main

# Then delete the feature branch
git branch -D add-error-handling-to-divide

# Refresh your local main and make sure that you have the updated divide function locally
git pull
```
