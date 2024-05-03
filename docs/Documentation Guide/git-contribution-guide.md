# Using GitHub to Contribute

## Introduction

Before getting started, make sure to reach out to Jonathan Briganti ([jonbrig@vt.edu](mailto:jonbrig@vt.edu)) to be added as a contributor to our GitHub repository.

You will need:

* A [GitHub](https://github.com/) account
* A terminal with Bash/Git Bash installed
* A code editor, such as Visual Studio Code

Some code editors have GitHub integration that allow you to do a majority of the workflow through their user interface. Since this may differ between programs, this guide only walks through the command line workflow. For a webpage-based workflow, see the [general GitHub guide](../Lab%20Protocols/github-guide.md).

## Getting Started

### Cloning the repository

You will need to clone the lab's [GitHub repository](https://github.com/Brown-and-Briganti/bel-docs) before you can begin. Having a copy of the repository on your computer will make it easier to make and merge changes.

GitHub provides a guide on how to clone a repository in [their documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository).

---

Note that *remote* and *local* repositories are different:

* The [lab repository](https://github.com/Brown-and-Briganti/bel-docs) is the **remote** (or primary) repository whose contents are shown on these documentation webpages.
* The **local** repository is the copy of the lab's repository saved on your computer.

Changes made locally will not affect the remote repository until they are pushed and approved.

### Installing MkDocs (optional)

Installing Material for MkDocs locally is **completely optional**. However, if you plan to make multiple contributions to the documentation, a local installation is highly encouraged as it allows you to view your changes live before pushing changes to GitHub.

Material for MkDocs and all dependencies (including MkDocs) can be installed using [`pip`](https://pip.pypa.io/en/stable/installation/) in a terminal:

```
pip install mkdocs-material
```

A local installation allows us to use the `mkdocs serve` command, which opens a server to preview your changes. To preview changes, use `mkdocs serve` while in the same directory as the `mkdocs.yml` file. After the server initializes, there will be a link to the site preview in the terminal. The site will rebuild every time you save a file and can be closed using `Ctrl/Cmd+C` in the terminal.

## General GitHub workflow

### Making changes to the repository

#### Creating and working on branches

We advise you work on a separate branch to avoid accidentally overwriting existing files. A branch is a snapshot of the primary repository that you can edit independently of the main code base, allowing people to work on the same repository safely.

Before creating a new branch, make sure your copy of the main branch is up to date. Updating your local copy before opening new branches will prevent merge conflicts down the line.

```bash
git switch main # switches branch to main
git pull origin main # pulls and synchronizes changes from remote repo
```

Then, create a new branch:

```bash
git switch -c <branch name> # creates new branch then switches to that branch
```

You can check which branch you are on, as well as see any other branches you may have, by entering `git branch` in your terminal. Your active branch is denoted by an `*`.

From here, you are free to make your changes!

### Staging and committing changes

As pages are finished, they need to be staged and committed before they can be merged into the primary repository.

*Staging* serves as a record of files that are ready to be committed. Files that have been staged can be easily unstaged if you need to make additional changes. A real life analogy would be placing items into an online shopping cart.

*Committing* updates the local repository with your changes. This would be similar to purchasing the items in that shopping cart.

It is ideal to bundle similar changes into smaller commits, rather than one big commit, for easier code review. In some cases, this can also make it easier to troubleshoot merge conflicts.

To view the current status of the staging area:

```bash
git status
```

This will print a summary of your current branch in the terminal, including staged, unstaged, and untracked changes. New files are considered untracked.

While not necessary, it is advised to use `git status` between steps to make sure your commands are working as intended.

You can add files to the staging area by:

```bash
git add . # adds all files in the current directory

git add <file> # add specific files only
```

Similarly, you can remove files from the staging area:

```bash
git restore --staged <file>
```

Once you are satisfied with your staged files, you can commit them:

```bash
git commit -m "commit message"
```

The commit message should briefly describe the contents of the commit. It should be easy for someone to figure out what changes you made or added.

#### Temporarily stashing changes

Alternatively, you may find that you need to switch branches for some reason, but your current branch is not ready to be committed. Attempting to switch branches with uncommitted changes will warn you to commit or stash them first.

*Stashing* will temporarily save your changes locally and reverts the working directory to a clean state.

```bash
git stash # temporarily save tracked changes, cleans working directory

git stash push -m "description of stash" # expanded command + optional message
```

When you are ready to commit your changes, you can reinstate them:

```bash
git stash pop # restores latest stash and removes it from memory
```

This will bring the branch back into the pre-stashed state, or allows you to transfer changes to a different branch. You can confirm both of these commands work by using `git status`.

### Pushing changes

Commits do not automatically update the remote repository. They need to be pushed, reviewed, then merged before any changes appear on the website.

To push your changes:

```bash
git push origin <current branch>
```

If you forget the name of your current branch, it is printed in the first line of the `git status` command.

#### Creating a pull request (PR)

Once you push your commit, you will need to create a pull request on GitHub. Navigate to the lab repository page and click **Compare & pull request** in the header to open a pull request.

Alternatively, navigate to **Pull requests**, then click **New pull request**. Click the drop-down box that says `compare: main`, then select your branch.

<figure markdown="span">
  ![Drop-down box after clicking on "compare: main"](../assets/user%20guide/github-contribute/github_flow_01.png)
</figure>

On the next page, add a descriptive title and a bulleted description of changes you have made. You can view previous (closed) PRs for examples. Remember to assign Jon as a reviewer in the right-hand menu.

After that, click **Create pull request**. You are done!

## Summary of workflow

<figure markdown="span">
  ![Flowchart of the GitHub workflow described above.](../assets/user%20guide/github-contribute/github_flow_02.svg){ width="375" }
</figure>

## Additional Resources

* [GitHub documentation](https://docs.github.com/en/repositories/)
* [Git documentation](https://git-scm.com/docs)