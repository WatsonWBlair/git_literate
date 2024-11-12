# 📗 Table of Contents

- [📖 About the Project](#about-project)
  - [🛠 Tech Stack](#tech-stack)
- [💻 Getting Started](#getting-started)
  - [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Install](#install)
  - [Usage](#usage)
  - [Run tests](#run-tests)
- [📝 License](#license)

<!-- PROJECT DESCRIPTION -->

# 📖 Python Coding Challenges <a name="about-project"></a>

Welcome Sienberg Students! Today we'll be exploring basic github functionality while working on python code challenges!
Follow the steps below to set up the repository on your computer.

You get a point for each of the following:
- [ ] Merge a valid solution into `main` (2 points)
  - [ ] Once the pull request is reviewed and approved, merge it into `main` using "Merge commit"
  - [ ] Update local branch and push the changes to the repository. 
- [ ] Provide feedback on a pull request (1 point)
  - [ ] Review the pull request by examining the changes in the "Files changed" tab.
  - [ ] Leave feedback, and either approving or requesting revisions. Ensure all tests pass before finalizing the review.
- [ ] Iterate on an existing solution (1 points)
  - [ ] Pull the latest changes from main
  - [ ] Address feedback, implement the required changes, test the code, and push the updated branch.
  - [ ] The pull request will update automatically for further review and, once accepted, can be merged into main.
- [ ] Resolve a merge conflict (1 points)
  - [ ] Pull the latest changes from main.
  - [ ] Review and resolve conflicts in the affected files, then commit, and push the changes.
  - [ ] The pull request will update, and the conflict will be resolved for merging.
- [ ] ETC...


Winner gets a prize!


## 🛠 Tech Stack <a name="tech-stack"></a>
- [Python](https://www.python.org/)
- [Pytest](https://docs.pytest.org/en/7.2.x/)



<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>

> To get a local copy up and running, follow these steps.

### Prerequisites

In order to run this project you need:

- [ ] [python3](https://docs.python-guide.org/starting/install3/osx/)
- [ ] [github cli](https://github.com/cli/cli#installation)
- [ ] [github account](https://github.com/)
- [ ] [make for mac](https://formulae.brew.sh/formula/make) or [make for windows](https://gnuwin32.sourceforge.net/packages/make.htm)

```Shell
  python3 --version # Python is installed
  git --version # Github is installed
  gh auth login # Sign into github
  which make # make is installed
```

### Setup

Clone this repository to your desired folder:

```Shell
  git clone git@github.com:WatsonWBlair/git_literate.git
```


### Install

Install this project with:

```Shell
  sudo make init
```


### Usage

To run the project, execute the following command:


```bash
    git checkout <branch-name> #checkout a working branch

    pytest -p no:cacheprovider <challenge-name>_test.py # test a specific challenge
    pytest -p no:cacheprovider # test all challenges

    git commit -am 'feat: <challenge-name> Complete!' # Commit changes to your local branch
    git push # Update the remote branches git history to match the local branch
```



<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.
