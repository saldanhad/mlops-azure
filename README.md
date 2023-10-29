# mlops-azure

Collection of scripts to implement MLOps using Azure Machine Learning.

![01-01-architecture](https://github.com/saldanhad/mlops-azure/assets/115748404/22a70f4b-67c1-47a8-945f-61754c36363e)

---

### Trunk Based Development - linting and unit tests (source:https://learn.microsoft.com/en-us/training/modules/work-linting-unit-test-github-actions/)

![Image](https://learn.microsoft.com/en-us/training/wwl-data-ai/work-linting-unit-test-github-actions/media/03-02-pull-request.png)

* The production code is hosted in the main branch.
* A data scientist creates a feature branch for model development.
* The data scientist creates a pull request to propose to push changes to the main branch.
* When a pull request is created, a GitHub Actions workflow is triggered to verify the code.
* When the code passes linting and unit testing, the lead data scientist needs to approve the proposed changes.
* After the lead data scientist approves the changes, the pull request is merged, and the main branch is updated accordingly.
