
import AutoGit

master = AutoGit.Branch("master")
master_add = master.addFile(".")
master_commit = master.commit("auto-git")
master_push = master.push("origin")

launcher = AutoGit.Launcher()
launcher.setDate("2021/1/24/21")
launcher.setCycle(5)
launcher.run(master)