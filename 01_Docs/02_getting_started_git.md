## Download Git 

To use Git on the command line, you will need to download, install, and configure Git on your computer, according to your operation system (https://git-scm.com/downloads).

## Create an account on GitHub.com

To get started with GitHub, you'll need to create a free personal account on GitHub.com and verify your email address.

Every person who uses GitHub.com signs in to a personal account. Your personal account is your identity on GitHub.com and has a username and profile. For example, see @octocat's profile.

## Basic commands

### Creating a remote Repository

1. **Sign Up/Login:** If you haven't already, sign up for a GitHub account or log in to your existing one.
2. **Create Repository:** Click on the "+" sign on the top right corner of the GitHub homepage and select "New repository". Give your repository a name, description, and choose whether it's public or private.
3. **Initialize with README:** You can choose to initialize your repository with a README file, which is often a good idea to provide initial information about your project.
4. **Create Repository:** Click on the "Create repository" button to create your repository.

### Clone a remote Repository
To clone an already created repository and work from it locally perform: 
```bash
git clone <repository_url>
```

### Making changes
1. **Stage Changes**: Use git add to stage your changes for commit.
   ```bash
   git add .
   ```
2. **Commit Changes**: Commit your changes with a descriptive message.
   ```bash
   git commit -m "Description of changes"
   ```
3. **Push Changes**: Push your changes to the remote repository on GitHub.
   ```bash
   git push origin main
   ```
### Branching
Branches allow you to work on different features or versions of your project simultaneously.

**Create Branch**: 
```bash
git branch <branch_name>
```
**Switch Branch**:
```bash
git checkout <branch_name>
```
**Merge Branch**:
```bash
git merge <branch_name>
```
### Create a pull request
Pull requests are used to propose changes and request them to be merged into the main branch.

**Create Pull Request**: On GitHub, navigate to your repository, and click on the "Pull requests" tab. Then click on "New pull request" and select the branches you want to merge.

**Review and Merge**: Collaborators can review your changes and merge them into the main branch.
