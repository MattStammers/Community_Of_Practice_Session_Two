

## The Essence of Version Control

- A system for managing your work (not necessarily just code) which **records
  snapshots** of the current state of a set of files
- Provides a historical record for your project
- Reports "diffs" that describe the file changes between snapshots
- Implements **branching**:
  - Allows working on several different features at the same time and switching
    between them whilst also maintaining a working copy of the code
  - Different people can work on the same code/project without interfering with
    each other
  - You can experiment with an idea and discard it if it turns out to be bad
- Implements **merging**:
  - The opposite of branching
  - Combines different branches together

THIS IS A MISTAKE

## What Can Go Wrong Without Version Control

- Lots of manual work to manage files
- Names are uninformative
- Not clear which versions are compatible
- Difficult to find changes between versions

### Mistakes Happen

Without recorded snapshots you cannot:

- Undo mistakes and go back to a working version of your code
- Find out when a mistake was made and which results it may affect
- You might not even be able to tell what your mistake was (*"It was working
  yesterday..."*)

### Working on different things

- For example new features and bug fixes, but you also want to use the current
  code for ongoing analysis
- Usually leads to multiple different copies of the code
- Copies need to be combined back together - but this often doesn't happen

### Collaboration

- *"I will just finish my work and then you can start with your changes."*
- *"Can you please send me the latest version?"*
- *"Where is the latest version?"*
- *"Which version are you using?"*
- *"Which version have the authors used in the paper I am trying to reproduce?"*

### Reproducibility

- How do you indicate which version of your code you have used in your paper?
- When you find a bug, how do you know when precisely this bug was introduced?
  (Are published results affected? do you need to inform collaborators or users
  of your code?)

## What about Dropbox or Google Drive?

Using a system like this solves some but not all of the issues above:

- Document/code is in one place, no need to email snapshots.
- How can you use an old version? Possible to get old versions but in a much
  less useful way - snapshots of files, not directories.
- What if you want to work on multiple versions at the same time? Do you make a
  copy? How do you merge copies?
- What if you don't have internet?

## Git - A Version Control System (VCS)

Whilst there are many different implementations of VCS, Git has
become established as by far the most widely used.

## GitHub - A cloud based version control platform
GitHub is a cloud-based platform where you can store, share, and work together with others to write code.

Storing your code in a "repository" on GitHub allows you to:

- Showcase or share your work.
- Track and manage changes to your code over time.
- Let others review your code, and make suggestions to improve it.
- Collaborate on a shared project, without worrying that your changes will impact the work of your collaborators before you're ready to integrate them.
- Collaborative working, one of GitHub’s fundamental features, is made possible by the open-source software, Git, upon which GitHub is built.

  ## How do Git and GitHub work together?

When you upload files to GitHub, you'll store them in a "Git repository." This means that when you make changes (or "commits") to your files in GitHub, Git will automatically start to track and manage your changes.

There are plenty of Git-related actions that you can complete on GitHub directly in your browser, such as creating a Git repository, creating branches, and uploading and editing files.

However, most people work on their files locally (on their own computer), then continually sync these local changes—and all the related Git data—with the central "remote" repository on GitHub. There are plenty of tools that you can use to do this, such as GitHub Desktop.

Once you start to collaborate with others and all need to work on the same repository at the same time, you’ll continually:

- Pull all the latest changes made by your collaborators from the remote repository on GitHub.
- Push back your own changes to the same remote repository on GitHub.
Git figures out how to intelligently merge this flow of changes, and GitHub helps you manage the flow through features such as "pull requests."
