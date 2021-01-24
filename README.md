<h1>Auto Git</h1>

<br/>

- git을 실행시켜주는 모듈.

<br/>

```python
import AutoGit

master = AutoGit.Branch("master") # set main branch
master_add = master.addFile(".") # same with "git add ."
master_commit = master.commit("auto-git") # same with "git commit -m auto-git"
master_push = master.push("origin") # same with "git push origin [branch]"

launcher = AutoGit.Launcher() # set git launcher
launcher.run(master) # run
```

<br/>
<br/>

- 주기를 설정해 반복적으로 실행가능.
- setCycle 함수 인자로는 초 단위가 들어감.

<br/>

```python
import AutoGit

master = AutoGit.Branch("master")
master_add = master.addFile(".")
master_commit = master.commit("auto-git")
master_push = master.push("origin")

launcher = AutoGit.Launcher()
launcher.setCycle(5) # set cycle. (second)
launcher.run(master)
```

<br/>
<br/>

- 특정 시각에 실행가능.
- setDate 인자로는 hour(시간) 까지만 들어감.
- setCycle 함수를 꼭 넣어야함. 이때 주기는 시간을 확인할 텀(sleep time) 이 됨.

```python
import AutoGit

master = AutoGit.Branch("master")
master_add = master.addFile(".")
master_commit = master.commit("auto-git")
master_push = master.push("origin")

launcher = AutoGit.Launcher()
launcher.setDate("2021/1/24/21") # set date. (year/month/day/hour)
launcher.setCycle(5) # set cycle. (sleep time for checking date)
launcher.run(master)
```
