## Before starting on a new feature or bug fix, *always* make sure your local main branch is current with origin (GitHub in your case)

```shell
# The "checkout" command without any arguments tells git to change to that branch
git checkout main
git pull
```

## Create a new feature branch from the tip of the main branch

```shell
# The "checkout" command with the '-b' argument tells git to create a new 
# branch named "test-error-handling" and change to that branch
git checkout -b test-error-handling
```

## Make a few updates to files

- Update the message to "Hello world! Git rules!" in 00-hello.py
- Uncomment the "Test error case" lines in both 02-factorial.py and 03-fibonacci.py
- Run both and verify expected behavior

## Commit the changes

```shell
# The "-m" argument tells git to set the specific message on the commit objects
git commit -m "Changing the hello message" practice/00-hello.py
git commit -m "Testing the error cases in fibonacci and factorial" practice/02-factorial.py practice/03-fibonacci.py
```

## Push the branch to origin, i.e. GitHub

```shell
git push --set-upstream origin test-error-handling
```

## Check that the branch appeared on the GitHub UI

## Create a Pull Request from GitHub

- Use the "test-error-handling" branch as the source branch
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
git branch -D test-error-handling
```
