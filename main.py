
import AutoGit

master = AutoGit.setBranchScope("master")
master_add = master.addFile(".")
master_commit = master.commit("auto-git")
master_push = master.push("origin")

print(master_push)

launcher = AutoGit.getLauncher()
launcher.run(master)