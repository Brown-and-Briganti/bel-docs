# Managing your files with GitHub

## Introduction

*Git* is a version control software that helps us to maintain multiple versions of files and projects simultaneously. You can use Git to record changes to your project as you work on them, providing a convenient way to track your progress.

[***GitHub***](https://github.com/) is a platform built on Git that allows collaboration and sharing of your projects. While you can use Git through the command line, GitHub provides a convenient user interface, so you can maintain your projects easily through a webpage.

You will need to create an account to use GitHub, which can be done through the link above.

## Introduction to GitHub

To get started, we recommend completing this [brief introductory course](https://github.com/skills/introduction-to-github) offered by GitHub. This course will guide you through setting up your first repository and performing your first commit and merge. It should take less than one hour to complete.

The below guide walks you through some of the features briefly introduced in the introductory course.

### Creating your repository

A *repository* (or "repo") is where all of your files are stored and maintained. You can create a new repo by clicking the **+ button** at the top right of the main GitHub page, or the **New button** in the left-hand sidebar:

=== "+ button"

    <figure markdown="span">
    ![Creating a new repo from the "+" button](../assets/user%20guide/github-student/github_00.png)
    </figure>

    ---

=== "New button"
    <figure markdown="span">
    ![Creating a new repo from the "+" button](../assets/user%20guide/github-student/github_01.png)
    </figure>
 
    ---

This will redirect you to a new page to create a new repository. Choose a descriptive repository name and provide a brief description, then set the repo's privacy (public or private). If you plan to add a longer description (such as project information), make sure **Add a README file** is also selected.

<figure markdown="span">
![Configuring your new repo](../assets/user%20guide/github-student/github_createpublicrepo.png){width="75%"}
</figure>

When you are ready, click **Create repository** to generate the new repository. You should see a page similar to this:

<figure markdown="span">
![Main page of a repository](../assets/user%20guide/github-student/github_newrepo.png){width="75%"}
</figure>

Welcome to your repository! There are a number of buttons at the top of your main repository page that you can explore. The following sections review the pages you will likely become most familiar with as you work with GitHub.

### Navigating your repository

#### Adding your files

You can add files to your repository by clicking **Add file**, next to the **<> Code** button. In the drop-down, either choose **Create new file** or **Upload files**.

Selecting **Create new file** will redirect to a page where you can create a file directly in GitHub:

<figure markdown="span">
![Creating files via GitHub GUI](../assets/user%20guide/github-student/github_newfile.png){width="75%"}
</figure>

To create your file, give it a name and file extension (.py, .md, etc.), then type the contents into the text box. You can preview the page with the **Preview** tab, which is helpful if your file type can render special styling, like bold or italics.

---

You can also **Upload files**, which will allow you to select files from your computer:

<figure markdown="span">
![Adding files via GitHub GUI](../assets/user%20guide/github-student/github_upload-file.png){width="75%"}
</figure>

Uploading a file that shares a name with an existing file will override that file in the repository. You can navigate to that file and view its change history by clicking **History** at the right-hand side. Selecting a commit (see [Committing your files](#committing-your-files)) will show you any changes made to that file, providing a way to track progress as you work on your projects.

#### Committing your files

Regardless of which method you choose, both pages have a section to **Commit changes**. A *commit* allows you to save your files or changes to the repository. Commits function as a way to record changes to files, which you can reference later.

=== "Create new file"

    <figure markdown="span">
    ![Commit changes prompt when creating a new file](../assets/user%20guide/github-student/github_createfile-commit.png){width="75%"}
     </figure>

    ---

=== "Upload file"
    <figure markdown="span">
    ![Commit changes prompt when uploading a file](../assets/user%20guide/github-student/github_upload-commit.png){width="75%"}
    </figure>
 
    ---

The first text box is the commit message. When committing changes, it is important to give it a descriptive message so you can easily figure out what each commit contains. You can optionally add a longer description in the second text box to expand on your commit message, though this should also remain relatively short (~1 sentence).

Finally, you can commit directly into the `main` branch, which will save your files directly to the repository. Alternatively, you can create a new branch and generate a pull request (see [Using branches to manage your work](#using-branches-to-manage-your-work)).

#### Using branches to manage your work

If you are working on an evolving project, like a series of scripts, it is best to work on a branch. *Branches* are snapshots of your main repository that can be edited independently from the primary code base. In shared repositories, branches allow multiple people can safely work on the same repository simultaneously without overwriting others' work. For a solo repository, branches can be helpful for working on different aspects of your projects at once. By default, your default branch will be `main`.

To navigate between branches, click the drop-down menu with the branch icon (:material-source-branch:) on the main page of your repository. You can create a new branch through the text box at the top of this menu.

<figure markdown="span">
    ![Menu to switch or create branches](../assets/user%20guide/github-student/github_newbranch.png)
    </figure>

Clicking on **:material-source-branch:Branches** will take you to the branch overview. Here, you can manage (delete, rename, or view) the branches of the repository. You can also create a new branch.

<figure markdown="span">
    ![Branch overview page](../assets/user%20guide/github-student/github_branchoverview.png){width="75%"}
    </figure>

#### Creating pull requests
Pull requests (PRs) are generally used more often in collaborative repositories, and you will likely not use PRs in a solo repository. PRs allow you to have your code reviewed and receive feedback before merging changes into the primary branch. It also makes it easier to see the changes you made, all on one page.

Navigate to **Pull requests**, then click **New pull request**. Click the drop-down box that says `compare: main`, then select your branch.

<figure markdown="span">
  ![Drop-down box after clicking on "compare: main"](../assets/user%20guide/github-contribute/github_flow_01.png)
</figure>

On the next page, add a descriptive title and a bulleted description of changes you have made. Assign any reviewers, if your group has any.

After that, click **Create pull request**. You are done!