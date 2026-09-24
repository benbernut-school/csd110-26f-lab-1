# Lab 1 - Getting Started

## Overview

In this lab you will familiarize yourself with the coding environment you will be using in CSD110 and writing your first Python code. This lab is different than the remaining labs in this course in that you will spend most of your time familiarizing yourself with the coding environment rather than actually writing Python code. There is a lot of technology at work, and it's worth spending some time acquainting yourself with it! Don't worry about having a deep knowledge of any of these; the goal here is to learn just enough to be able to load the environment, do your lab work, and submit your work when complete.

> **NOTE**: It is highly recommended to take notes in a notebook or a journal file as you work! A lot of information will be thrown at you, and writing important details down can help you remember.

Here are the main components you should know about:

### Git

Git is a tool that developers use to collaborate when working on code together. It is a very flexible and powerful tool, and you will only use a subset of its capabilities in this course. Here is a basic workflow with some definitions:

1. **Clone a repository** - A Git "repository" (also referred to as a 'repo') is a collection of files related to a coding project. Git can be used to keep track of and inspect the changes in those files. When you "clone" a repository, you are making a copy of both the files **and** the history of changes made to those files. Multiple clones of the same repo may exist on various computers; Git makes it possible to coordinate changes made in all those clones, and keep them all synchronized.
2. **Make a branch** - When you make changes to code in a repository, you do so on a "branch".  There is always one "main" branch, but it is typical for programmers to work on a separate branch until they have finished a unit of work, and then request that their changes be reviewed by a colleague before merging those changes back into the main branch.
3. **Make changes** - Edit the contents of code files, add new folders/files, remove files, etc.
4. **Commit changes** - Using Git, you can mark a set of changes as a "commit". When you make a commit, Git assigns a unique identifier to the state of the code in the repository at that time. Using commits, coders may see what a repository looked like at the time of any commit, and may compare code between any two commits.
5. **Push changes** - When a repository is cloned, the original repository is the "remote" of the clone. A "push" in Git synchronizes changes from a clone back to its remote. Specifically, all commits that have been made in the clone since the most recent push (or the original clone if no push has yet occurred) will be copied to the remote.

For coding labs in this course, you will use the above process to keep track of your changes as you work.

### GitHub

GitHub is a website that hosts Git repositories online. All coding labs in this course are hosted on GitHub. For each lab, the first thing you will do is create a **copy** of a lab template repository on your own **GitHub account**. You will also **clone** your GitHub repository onto a **development machine**, either your own, a school PC, or a virtual machine. 

Yes, that means you will have two clones: your GitHub repository, and the repository on your development machine. In terms of the workflow described in the Git section above, then, once you have copied the template repository to your GitHub account, you...

1. Clone your GitHub repo onto your development machine
2. Make a branch to use for your lab work
3. Make changes to complete the lab **on that branch**
2. Commit the changes you have made (you may make multiple commits as you work, perhaps after completing each significant portion of work)
3. Push your commits to your remote (your GitHub repo)

Once your GitHub repo contains your completed work, you are ready to make a **pull request**.

#### Pull Requests

A pull request is a way to ask that the all the changes in a branch be reviewed before merging them into another branch. Many developer teams have such a review process as a quality assurance measure.

For your labs, you will make a request to merge your lab branch with the main branch in your GitHub repository. Your teacher will then use this pull request to review your work and provide feedback. In this way, your classroom environment will be very similar to the code review process in many real working environments.

### GitHub Codespaces

GitHub offers a feature called "Codespaces".  A Codespace is a virtual machine (VM) to which you can connect with a web browser. Codespaces are free to students who have signed up for the [GitHub Student Developer Pack](https://education.github.com/pack) (if you have not already signed up, do so now). 

For labs in this course you may choose to use your own computer, a school lab computer, or a Codespace (or a combination of the above).

A key point to remember is that whether you are using a Codespace, your own computer, or a lab computer, you are working in a **separate** repository than your GitHub repository, and any changes you make on the development machine must be **commited AND pushed** to the GitHub repository in order for them to be seen there. Furthermore, if you work on multiple machines (say a lab computer and a home PC) you will need to ensure that when you complete work on one machine you push it back to GitHub so that you can **pull** those changes onto your other machine.

**TIP:** If you are new to programming, it is recommended that you start with **ONE** Codespace per lab for this course. You will be able to use that Codespace from any computer that has a web browser.

### Visual Studio Code

VS Code is a program for editing, running, and inspecting code files.  It is very popular among programmers and is widely used in the industry. It is available as a desktop application, but it is also the editor used in the default user interface of GitHub Codespaces.

### Docker

Docker is a tool that allows you to create "containers" which package files and software for a specific computing environment. Containers are isolated from the rest of the system on which the container is running. 

In this class, for example, you will use a container with all the necessary software and libraries to write Python programs. Docker will run this container, and you will do your coding "inside" the container environment without having to install anything on your computer other than Docker and VS Code. (GitHub Codespace VMs and computers in E2120 and M2030 already have Docker and VS Code installed.)

Docker has become an important tool in the computing industry as it enables developers to work on multiple projects that may have conflicting system requirements. It also allows teams of developers to share a consistent working environment despite the developers having computers with different Operating Systems and configurations.

### Devcontainers

Finally, VS Code has a "devcontainer" feature that allows a Docker container to be specified using a configuration file (see **but do NOT change** the `.devcontainer/devcontainer.json` file in this lab). VS Code detects when a folder with a devcontainer configuration is opened, and gives the user the option to work inside the container.

> **NOTE**: if you choose to do lab work for this course on your own computer, you will want to have Docker Desktop installed **and running** in order to take advantage of devcontainers.  If you do not, you will need to install Python and possibly other software on your own in order to complete your work.

## Instructions

Now that you have a basic understanding of the tools and technology involved, let's start doing things!

1. Examine the overall layout of the GitHub dashboard page you currently have loaded in your web browser as you read this document.
2. Spend a minute exploring the interface. As you navigate, if you get lost you can always click on your profile picture (top right) then click "Repositories" and find your lab repository.  At minimum, locate the...
   1. Main menu button (top left, click this button and examine the options)
   2. Profile menu button (top right, click this button and examine the options there)
   3. "Code" and "Pull Requests" tabs (you will be using these for lab work; the tab with an orange bar beneath indicates the current view)
   4. File listing area (explore the files and folders in this repository by clicking them, but do NOT edit them.)

      > **IMPORTANT**: while it is possible to make changes to files from the GitHub dashboard, do NOT do this for now as doing so will complicate synchronization once you start working on a development machine.

3. Invite your instructor as a repository collaborator (so they can view your code for troubleshooting and grading)
   1. Open the "Settings" tab on your repository in GitHub
   2. Click the "Collaborators" item in the left side menu
   3. Click the "Add people" button
   4. Add your instructor's GitHub account as a collaborator (you can find their GitHub username in the 'course-config' repository in the [CSD110](https://github.com/saultcollege-csd110/course-config) GitHub org).
5. Create a branch to work on for your changes in this lab
   1. Above the file listing, locate the dropdown with the label 'main' and click it.
   2. In the "Find or create" field, enter a name for your branch. `lab-1` would be appropriate!
   3. Click on the "Create" element that appears when you enter the name.
   4. **Observe**: the page refreshes and the dropdown now has your branch name as a label instead of 'main'.  You can use the branch dropdown to switch between branches and view the state of the code in those branches. Changes you make only apply to the current branch.
6. Clone your GitHub repository into a development machine
   1. Make sure that your lab 1 branch (NOT the 'main' branch) is selected in GitHub
   2. Click the big green Code button
   3. Select the Codespaces tab
   4. **Observe**: when you hover over the + icon, a tooltip indicates that clicking it will create a Codespace on the currently selected branch.
   5. Click the + icon to create a Codespace on your lab 1 branch.

      > **IMPORTANT:** Only create ONE Codespace! If you have already created one you will see it in the Codespaces dropdown, and you can run it from there. Each Codespace is a separate virtual machine that will have a separate clone of your repository that needs to be synchronized. Working with multiple machines is much more complicated than you need for now.
   
   6. **Observe**: A new tab will open in your browser. Give this tab a few minutes to load fully. GitHub is automatically provisioning a virtual machine with the environment specified in the `.devcontainer/devcontainer.json` file, booting that machine up, cloning your GitHub repository onto it, and giving you a web-accessible VS Code interface to that machine through which you can edit the code files in your repository and run your programs, all from any web browser. If your mind is not blown, then you are not considering all the layers of technology involved here: again, you are currently using a computer that is running a web browser through which you are accessing a VS Code interface on *another* computer on which is running an automatically provisioned environment that allows you to create and run Python software based on a clone of your GitHub repository 🤯

      > **IMPORTANT**: Remember, despite both containing the GitHub name, your GitHub repository and your GitHub Codespace are two separate things.  The **repository** is just the web-accessible **view of the code** in your repository on GitHub.  The **Codespace** is a completely separate **computer** from the one you are using that you are accessing through a web browser, and any changes you make on your Codespace will need to be synchronized with your GitHub repository using a push operation.  

   7. Open your GitHub repository tab again, and refresh the page.
   8. Once again, click the big green Code button and select Codespaces
   9. **Observe**: Note that the Codespace you just created is listed and marked as active (meaning that it is currently running). If you close your browser, you will be able to come back to this list and click on the Codespace to open it again.  You can click the `...` to perform several operations on that machine, including stopping it (it will automatically stop if you have not used it for some time) or deleting it.

      > **IMPORTANT**: changes made to files in a Codespace VM will persist after stopping and restarting the VM, but if a Codespace VM is deleted, **any changes that have not been committed and pushed back to the main GitHub repository will be lost**. Note also that a Codespace that has not been active for longer than about a month will be automatically **deleted**. Thus, it is a good idea to frequently commit and push changes from your Codespace back to your GitHub repository.

      > **IMPORTANT**: Your GitHub Student Developer Pack sets a limit of 180hrs/mo on Codespaces, after which your Codespace becomes unavailable. You can view your current usage by clicking your profile icon (top right) then Settings -> Billing and licensing -> Overview. Stopping your Codespace when you are done working on it can help reduce your usage as Codespaces only auto stop after half an hour of idleness.
      
7. Familiarize yourself with VS Code
   1. Open your lab 1 Codespace
   2. Use this documentation to familiarize yourself with the various parts of VS Code: https://code.visualstudio.com/docs/getstarted/userinterface
8. Explore your Codespace machine.
   1. Open the terminal panel of the VS Code interface. This terminal is a regular terminal that allows you to run commands on the Codespace machine.
   3. **OBSERVE**: the prompt message in the terminal window will look something like this: `@<your-github-username> -> /workspace/lab-1-24f-your-gihub-username (your-lab-branch-name) $ `. GitHub has created a user on this Codespace with your GitHub username. The `@<your-github-username>` part of the prompt is indicating the current user. The `(your-lab-branch-name)` part is indicating that you are working in that branch of a Git repository. You also see the current path that the terminal is working in.
   4. Enter the command `cd src` to 'change directory' to the `src` folder, and note that the path in the prompt changes to indicate that the terminal is now working from within the `src` folder.
   5. Enter the command `cd ..` to change 'up one directory' and note that you are now back in the main lab folder.
   6. Enter the command `lscpu` to get a listing of information about the CPU on your Codespace VM
   7. Enter the command `free -h` to show information about the amount of memory on your Codespace VM
   8. Enter the command `cat /etc/os-release` to get information about the operating system running on your Codespace VM
   9. **TIP**: As you enter commands, little dots appear at the left of the terminal window beside your commands. You can click these dots to perform operations like reruning a command or copying the output of the command.
   10. **TIP**: Any time you are in a terminal of this kind, you can often press the up or down arrows on your keyboard to cycle through previously run commands. This can save you a lot of typing when you are running the same command repeatedly.
       
9. Check your setup.

   In this and future labs, the `gh lab setup-check` command can be used to verify that you have created and initialized your lab repository correctly. If you have configured anything incorrectly it will notify you and give you advice on how to fix any problems.  Running the command should be the first the you do after initializing a new lab workspace in CSD110.

   1. Run `gh lab setup-check` now to verify that you have set things up correctly so far.

10. Run some Python in a REPL session
   1. In the terminal panel, run the command `python` to run a Python REPL
   2. **OBSERVE**: some information about the version of Python is displayed followed by a `>>>` prompt. This is the Python REPL, which is different than the terminal prompt. Here, you are working inside a running Python interpreter, and any commands you enter must be valid Python statements. To get back out to the terminal run the `exit()` statement, or type `Ctrl+d`
   3. In the Python REPL, enter the instruction `2 + 2`
   4.  **OBSERVE**: The result of the instruction is displayed.
   5.  Try running a few more math expressions. You can multiply, divide, and do exponents using the `*`, `/`, and `**` operators, respectively, as in `2 * 2`, `2 / 2`, and `2 ** 2`
   6.  Try some more complicated math expressions that involve multiple operations, such as `1 + 2 * 3 - 4 / 5`
   7.  **OBSERVE**: Python knows the standard order of operations!
   8.  Use parentheses to manipulate the order of operations, as in `(1+2)*(3-4)/5`.
   9.  Can you leave out the multiplication symbol as you can in mathematical notation?  Try `(1+2)(3-4)/5` to see that you get something called a `TypeError`.
       > Don’t concern yourself for now with the meaning of this error.  Just note the mention of something not being ‘callable’. In Python (and many other computer languages) parentheses are also used to indicate a ‘function call’.  We will discuss this more in the future, but for now let’s just try calling a function.
   10. Run the following three separate **statements**:
       ```python
       print(2) 
       print(2+2) 
       print("Hello, world!")
       ```
       
   11. **OBSERVE**: Python has a built-in function called `print` which simply prints to the console whatever value you give it.  You can give a function a value to use by putting the value inside parentheses immediately after the function name, as you did above.

       Notice that the **expression** 2+2 was **evaluated** to its mathematical result before printing.

   12. Some functions may accept multiple values, which you can specify by providing the values as a comma-separated list inside the parentheses.  The `print` function is one such function.

       At the prompt, run the single statement
        ```python
        print(2, 2+2, "Hello, world!")
        ```

   13. **OBSERVE**: In this case, the results of each expression in the comma-separated list are printed, with a space between each result.

       > **NOTE**: In a REPL, the `print` function is not very useful because the value of every instruction is automatically printed anyways.  But most programs are written as a collection of code files (sometimes called ‘scripts’) that are executed as a whole.  When a Python script gets run, the result of every statement is **not** printed automatically like it is in a Python REPL, so you need to be explicit if you do want your program to produce output by using the `print` function. Let’s now try a simple program in the text editor.

11. Write and run a Python script
   1. Open the `main.py` file from file explorer panel
   2. In the text editor, add the following lines of code:
      ```python
      2 
      2+2 
      "Hello, world!" 
      ```
   3.  Run the script by running the following command in the terminal panel: `python src/main.py`
   
       > **NOTE**: Be sure you are in the **terminal** and not in a running REPL session, and be sure that your terminal is working from the **main lab folder, NOT the src folder**.

   4.  **OBSERVE**: There is no output in the terminal! That is because, as mentioned above, Python scripts do not print plain values to the console unless explicitly instructed to do so.
   5.  Change the script to the following, and run it again: 
       ```python
       2 
       print(2+2) 
       print("Hello, world!")
       ```
   6.  **OBSERVE**: The two statements that you gave as values to the print function are now indeed printed in the console.  Note also that the unprinted statement is still not displayed. 
   7.  Feel free to experiment with further Python code to your heart's content.

11. Commit and push your changes to GitHub. 

      Remember, your Codespace is not your GitHub repository. The changes you have made to `main.py` in your Codespace still need to be pushed to your GitHub repo.  Let's do that now.

      The first thing to do is to make a commit, for which you must do two things: provide a short description of the commit, and choose which changes to include in the commit.

      1. Open the Source Control panel in the VS Code interface. (And note that the Source Control icon is showing a small badge indicating the number of files with uncommitted changes. Helpful!)
      2. In the Message field, enter a message like "Completed Lab 1"
      3. **OBSERVE**: In the "Changes" list, all files with changes are listed. Since you have only changed `main.py` this is the only file that appears here. In future labs you will change multiple files, and you can include multiple files in one commit, and/or make multiple commits as you work.
      4. **OBSERVE**: There is an `M` beside the file name. Hover over it and note that the `M` indicates that this is a Modified file. You may also encounter `D` (Deleted), and `U` (Untracked; new files will start as untracked until you add them in a commit).
      5. Click on the `main.py` file name in the "Changes" list and examine the view opened by VS Code.
      6. **OBSERVE**: VS Code displays a side-by-side view comparing the file as it was in the previous commit with the file as it is now, giving you a quick way to verify that you are committing the correct changes. This view is often called a 'diff' (short for 'difference').
      7. Close the diff
      8. Hover over `main.py` in the "Changes" list
      9. **OBSERVE**: Three icons appear: one to open the file, one to discard the changes in the file (that is revert the file back to the state it was in in the previous commit), and one to stage the changes.
      10. Click the Stage Changes icon
      11. **OBSERVE**: A new list labelled "Staged Changes" has appeared. This list contains the set of changes that will be committed when you commit. Again, since you only have one file with changes, things are simple for now. In future labs you will have multiple files with changes. Only the files you add to the "Staged Changes" list will be included in a commit. You may choose to include some or all current changes in a commit. If you choose to include only some changes, you will need to do further commits in order to include the uncommitted changes in the repository. This can be useful when, for example, you are working on two tasks at once. You could create one commit with an appropriate message for the one task, and separate commit for the other.
      12. Finally, click the Commit button. This commits the changes to the Git repository **on your Codespace**. But you still need to push this commit to your **GitHub repository**.
      13. **OBSERVE**: The Commit button has changed to a "Sync Changes" button with a number beside it. This number indicates how many commits need to be pushed to the GitHub repository in order for it to be synchronised.

          > **NOTE**: It is normal to make multiple commits to a repository before pushing back to GitHub. When a push occurs, all commits that are not already in the GitHub repo will be included in the synchronization.
      14. Click the Sync Changes button to push your commits from your Codespace repository to your GitHub repository.
      14. Open your GitHub repository and verify that your changes are indeed now present there by opening the `main.py` file in GitHub.
      15. Back in the main file listing of your GitHub repository, at the top right of the listing click the `Commits` label.
      16. **OBSERVE**: A list of all the commits that have been made in this repository is shown with the most recent commit at the top.
      17. Click the commit ID (the 7-digit code near the right of each commit) to view the details of the commit.
      18. **OBSERVE**: The commit details are a very similar view as the diff view you saw in VS Code: it shows the changes made in this commit compared with the previous commit.
  12.  Create a Pull Request

       As discussed above, pull requests are used to request that someone review changes in a branch of code before merging the changes back into another branch. Here, the pull request is what you will submit to your teacher for review. In a workplace, a colleague might review your code and make suggestions.
       1.   Click the "Pull Requests" tab near the top of the GitHub repository page
       2.   Click the green "New pull request" button
       3.   Select the 'main' branch as the 'base' and your lab 1 branch as the 'compare' branch.
       4.   Enter a reasonable title, such as "Lab 1". (In a work environment, you would set an appropriate title and description of all the changes the branch involves.)
       5.   Click the "Create pull request" button.
       6.   Click the "Files changed" tab.
       7.   **OBSERVE**: You now see a summary of the changes in the entire set of commits in the whole branch. If there were multiple files involved (and there will be in future labs) you would see all those changes here. This is the view your teacher will use to review your code and provide feedback.

            > **NOTE 1**: You only need to create ONE pull request per branch. Once you have created one, any new commits that are pushed to that branch will be automatically incorporated into the pull request.
          
            > **NOTE 2**: Come back to this view to see your teacher's feedback inline with the code you've written, once feedback has been entered.

       8.   Copy the URL for this "Files changed" view.
       9.   Paste this URL in the Lab 1 submission folder on the LMS.

### You did it!
Whew! Congratulations! You have successfully initialized a lab assignment, provisioned a Codespace, created and run a Python script, committed and pushed your code to GitHub, and created a pull request. Your code is now ready for your instructor to review. You are well on your way to becoming a professional coder, and you are now ready to start writing much more interesting Python programs!

## Rubric

See the rubric attached to this lab in the LMS
