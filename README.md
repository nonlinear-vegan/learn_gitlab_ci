## Learning how to use GitLab CI

In order to learn how to use GitLab CI, I set of this simple test situation.
There is a simple python function, add\_numbers, and a unit test for it. The CI
job uses a docker images as a runner to execute the unit tests upon pushing 
commits to the GitLab master branch.

Here's a rough overview:

### Runners

Runners are virtual machines that actually run your tests. You can use shared ones, or 
create and register your own. For this example, I installed the GitLab CI runner on my
local machine, a mac. 
Full instructions here: [https://gitlab.com/gitlab-org/gitlab-ci-multi-runner](https://gitlab.com/gitlab-org/gitlab-ci-multi-runner).

I installed and registered the runner. Here are some details of the registration 
for this example:

```bash
$ gitlab-ci-multi-runner register
Please enter the gitlab-ci coordinator URL (e.g. https://gitlab.com/ci):
https://gitlab.com/ci
Please enter the gitlab-ci token for this runner:
<your token here>
Please enter the gitlab-ci description for this runner:
learning_gitlab_ci
Please enter the gitlab-ci tags for this runner (comma separated):
docker
INFO[0054] 67503196 Registering runner... succeeded
Please enter the executor: ssh, shell, parallels, docker, docker-ssh:
docker
Please enter the Docker image (eg. ruby:2.1):
python:2.7
```


### .gitlab-ci.yml Configuration file

The .gitlab-ci.yml file defines what is done for the build, and 
is placed in the top-level project directory. 

This configuration file specifies the docker runner is to use the python:2.7 
base image, and run the unitTest_add_numbers.py script:

```yml
image: python:2.7
job1:
  script: python unitTest_add_numbers.py
```

Documentation for configuration file:
[http://doc.gitlab.com/ci/yaml/README.html](http://doc.gitlab.com/ci/yaml/README.html)


Documentation for using docker to execute your runner:
[http://doc.gitlab.com/ci/docker/using_docker_images.html](http://doc.gitlab.com/ci/docker/using_docker_images.html)


### Trigger builds

You can trigger builds via the API, or simply committing to the GitLab repo for the project. Neat.
