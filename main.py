
import AutoGit

master = AutoGit.setBranchScope("master")
master_add = master.addFile(".")
master_commit = master.commit("auto-git")
master_push = master.push("origin")

launcher = AutoGit.getLauncher()
launcher.run(master)