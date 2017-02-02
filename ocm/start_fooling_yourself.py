#!/usr/bin/env python3
# Author: Thoxvi <A@Thoxvi.com>

import os
import sys
import time
import random

MIN = 60
HOUR = 60 * MIN
DAY = 24 * HOUR
MONTH = 31 * DAY
YEAR = 12 * MONTH

TMP_CHANGE_FILE = ".ocm"


def run_command(cmd: str):
    print(cmd)
    if os.system(cmd) != 0:
        return False
    else:
        return True


def set_envs(**kwargs):
    """
    GIT_AUTHOR_NAME
    GIT_AUTHOR_EMAIL
    GIT_AUTHOR_DATE
    GIT_COMMITTER_NAME
    GIT_COMMITTER_EMAIL
    GIT_COMMITTER_DATE

    :return: None
    """

    for k, v in kwargs.items():
        os.environ[k] = v


class DateGenerator(object):
    def __init__(self, start_timestamp, end_timestamp):
        self.__start_timestamp = int(start_timestamp)
        self.__end_timestamp = int(end_timestamp)

    def __iter__(self):
        now_timestamp = self.__start_timestamp
        end_timestamp = self.__end_timestamp
        while now_timestamp < end_timestamp:
            now_timestamp += random.randint(10 * MIN, 50 * MIN)
            yield now_timestamp
        raise StopIteration


class RandomReader(object):
    def __init__(self, file):
        self.__line_list = open(file).read().split("\n")

    def get_random_line(self):
        return random.choice(self.__line_list).replace("'", "")


class GitRepoController(object):
    def __commit_this_repo(self) -> bool:
        return (run_command("git add .") and
                run_command("git commit -m '%s'" % self.__msg_gen.get_random_line()))

    def __init__(self, repo):
        repo = os.path.realpath(os.path.expanduser(repo))

        if not os.path.exists(repo):
            os.makedirs(repo, exist_ok=True)

        os.chdir(repo)
        if not os.path.exists("%s/.git" % repo):
            run_command("git init")

        print("Repo path: %s" % repo)
        self.__git_repo_path = repo
        self.__tmp_file = "%s/%s" % (self.__git_repo_path, TMP_CHANGE_FILE)
        self.__msg_gen = RandomReader("%s/msg.data" % os.path.split(__file__)[0])

    def commit(self, commit_timestamp):
        commit_timestamp = "%s +0800" % str(commit_timestamp)
        os.environ["GIT_AUTHOR_DATE"] = commit_timestamp
        os.environ["GIT_COMMITTER_DATE"] = commit_timestamp
        os.chdir(self.__git_repo_path)
        with open(self.__tmp_file, "w") as file:
            file.write(commit_timestamp)
        return self.__commit_this_repo()

    def __del__(self):
        if os.path.exists(self.__tmp_file):
            os.remove(self.__tmp_file)
            os.unsetenv("GIT_AUTHOR_DATE")
            os.unsetenv("GIT_COMMITTER_DATE")
            self.__commit_this_repo()


def main():
    pass


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Example: ocm ~/git/one-click-man")
        exit(1)

    workspace = (sys.argv[1])
    grc = GitRepoController(workspace)
    timestamp = time.time()
    for timestamp in DateGenerator(timestamp - 1 * YEAR, timestamp):
        if not grc.commit(timestamp):
            print("Failure to commit")
            exit(1)
