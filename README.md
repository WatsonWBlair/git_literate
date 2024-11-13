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
Record your own score using the rubric below, remember that you will have to prove your final tally before receiving any prizes; so keep be prepared to provide links to the commits, comments and pull requests you get points for!

Please note that using ChatGPT or other generative AI tools to solve any coding challenges will result in disqualification from wining any prizes.

Point will be deducted for poor behavior: mean comments, frivolous use of `Request Changes`, ect... BE KIND TO EACH OTHER!

You get 1 point the first time you do each of the following:
- [ ] Create a local branch
  - [ ] ensure you have the latest version of main using `git checkout main && git pull`
  - [ ] create a new local branch using `git checkout -b <branch_name>`
- [ ] Push a local branch to remote
  - [ ] from your local working branch use `git push --set-upstream origin <branch_name>`
- [ ] Label a Pull Request appropriately
  - [ ] Open a pull request with a valid code change
  - [ ] Add a label using Github's UI
- [ ] Comment on a pull request
  - [ ] add a comment praising something about the pull request (eg: code formatting, variable naming, solution efficiency, ect...)
- [ ] Suggest a change to an open PR
  - [ ] use Github's UI to suggest a code change to an open PR (regardless of if it's accepted or not).
- [ ] Resolve a merge conflict
  - [ ] ensure you have the latest version of main using `git checkout main && git pull`
  - [ ] checkout your working branch.
  - [ ] Merge `main` into your current branch using `git merge main`
  - [ ] Review and resolve conflicts in the affected files, then commit, and push the changes.
    - [ ] ensure that your commit message contains information about the merge conflict.
- [ ] Resolve a requested change on one of your PRs
  - [ ] After another user has `requested changes` on your PR, resolve the issue.
- [ ] Open a `Draft Pull Request`
  - [ ] When opening a pull request, select the option `Open Draft PR` instead of `Open PR`.



You get 1 point each time you do one of the following:
- [ ] Merge a valid solution into `main` (1 point)
  - [ ] Note that a valid PR contains code changes relevant to only ONE challenge.
  - [ ] Open a pull request from your branch to main that introduces a new, valid, solution to a coding challenge.
  - [ ] Address feedback, implement the required changes, test the code, and push the updated branch.
  - [ ] The pull request will update automatically for further review and, once accepted, can be merged into main. [Note that reviews become `stale`/invalid if a commit is pushed to a branch after approval is given]
- [ ] Iterate on an existing solution (1 points)
  - [ ] Open a pull request from your branch to main that contains an improvement to an existing solution.
  - [ ] Address feedback, implement the required changes, test the code, and push the updated branch.
  - [ ] The pull request will update automatically for further review and, once accepted, can be merged into main.
- [ ] Leave a meaningful review on an open pull request (1 point)
  - [ ] Review the pull request by examining the changes in the "Files changed" tab.
  - [ ] Leave feedback, and either approve the PR or request changes.
  - [ ] Ensure that all relevant tests pass before finalizing the review.
- [ ] Collaborate with someone on the same Branch / Pull Request (1 point)
  - [ ] Coordinate with a peer to work the same branch.
  - Be careful about merge conflicts!
- [ ] Add a new item to `Lessons_Learned.md`
  - What do know now that you wish you had know before beginning the workshop?
  - What will you be sure to remember for the future?
- [ ] ECT...
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
  gh repo clone WatsonWBlair/git_literate
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

    pytest <challenge-name>_test.py # test a specific challenge
    pytest # test all challenges

    git commit -am 'feat: <challenge-name> Complete!' # Commit changes to your local branch
    git push # Update the remote branches git history to match the local branch
```



<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.
