

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

---

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
become established as by far the most widely used. We focus on use of Git via
its command line interface as we believe this is the best way to communicate the
important fundamental concepts.

Git is a very powerful tool. Unfortunately it is also quite difficult to start
using. Git often uses confusing and unintuitive terminology and the benefits of
its use are often only apparent in the longer term. Today we will make every
effort to demystify Git and make clear why its usage is an essential part of
any programming activity.
