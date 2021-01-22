
import AutoGit

"""
"""

master = AutoGit.setBranchScope("master")
master.addFile(".")
master.commit("auto-git")
master.push("origin")