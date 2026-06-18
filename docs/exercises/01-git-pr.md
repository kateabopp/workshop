## Before starting on a new feature or bug fix, *always* make sure your local main branch is current with origin (GitHub in your case)

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
- Add a call to divide with y = 0 to test it

## Commit the change

```shell
# The "-m" argument tells git to set the specific message on the commit object
git commit -m "Adding error handling to divide function in math" practice/01-math.py
```

## Push the branch to origin, i.e. GitHub

```shell
git push --set-upstream origin add-error-handling-to-divide
```

## Check that the branch appeared on the GitHub UI

## Create a Pull Request from GitHub

- Use the "add-error-handling-to-divide" branch as the source branch
- Use the "main" branch as the target branch
- Review the changes for correctness
- If correct, merge the PR and delete the branch in the GitHub UI

## Check that the main branch has the changes you made from the GitHub UI

## Check that the main branch on your laptop does NOT have the changes yet after changing to it

```shell
git checkout main
```

## Refresh the main branch on your laptop and verify you got the changes 

```shell
git pull
```

## Delete the feature branch from your laptop

```shell
git branch -D add-error-handling-to-divide
```
