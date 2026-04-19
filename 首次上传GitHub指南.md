# 第一次把 DataLoom 上传到 GitHub（图文式步骤）

你已经有 GitHub 账号即可，不需要先安装额外软件（用网页 + 终端即可）。若本机还没有安装 **Git**，请先安装：[https://git-scm.com/downloads](https://git-scm.com/downloads)

---

## 第一步：在 GitHub 网站上新建空仓库

1. 打开 [https://github.com/new](https://github.com/new) 并登录。  
2. **Repository name** 建议填 **`DataLoom`**（与 [Roleica/DataLoom](https://github.com/Roleica/DataLoom) 一致即可；不要用中文仓库名，避免部分工具兼容问题）。  
3. 选 **Public**。  
4. **不要**勾选 “Add a README / Add .gitignore / Choose a license”（本仓库里已经准备好了这些文件）。  
5. 点 **Create repository**。  
6. 创建完成后，页面会显示仓库地址，请复制 **HTTPS** 地址，形如：  
   `https://github.com/你的用户名/DataLoom.git`

---

## 第二步：在本机项目目录里绑定远程并推送

本仓库**已经初始化过 Git，并完成首次提交**（`main` 分支上已有代码）。你只需绑定 GitHub 上的空仓库并推送。

**若你的仓库是 [https://github.com/Roleica/DataLoom](https://github.com/Roleica/DataLoom)**：本机可能已配置好 `origin`（与 `https://github.com/Roleica/DataLoom.git` 一致）。在终端检查：

```bash
cd "/Users/heyuanjing/Downloads/百度同步/数据分析自动化项目"   # 本机若已改名，请改路径
git remote -v
```

若已显示 `origin ... github.com/Roleica/DataLoom.git`，**只需推送**（必须在「能弹出登录/输入密码」的终端里执行，Cursor 里无人值守的 push 会卡住）：

```bash
git branch -M main
git push -u origin main
```

若还没有 `origin`，或地址不对，执行：

```bash
git remote add origin https://github.com/Roleica/DataLoom.git
# 若提示 origin 已存在但 URL 错误：
# git remote set-url origin https://github.com/Roleica/DataLoom.git
git branch -M main
git push -u origin main
```

**仅有 `.git` 地址不够完成上传**：还必须由**你的账号**通过 HTTPS（Personal Access Token）或 SSH 完成身份验证；把链接发给我可以帮你写好命令，但**无法代替你输入令牌**。

第一次 `git push` 时，GitHub 会要求登录：

- **推荐**：用 **Personal Access Token (PAT)** 代替密码（GitHub 已不再支持用账号密码推送代码）。  
  创建令牌：[https://github.com/settings/tokens](https://github.com/settings/tokens) → **Generate new token**，勾选 **`repo`**，生成后复制一串字符；在终端提示输入密码时，**把这串令牌粘贴进去**（输入时屏幕可能不显示字符，属于正常现象）。

推送成功后，刷新 [GitHub 上的 DataLoom 仓库](https://github.com/Roleica/DataLoom) 即可看到所有文件。

---

## 日常：在本地改代码，再更新 GitHub

可以。习惯流程是：

```bash
cd "/Users/heyuanjing/Downloads/百度同步/数据分析自动化项目"
git status                    # 看改了哪些文件
git add -A                    # 或只 add 指定文件
git commit -m "简要说明改了什么"
git push                      # 推到 GitHub（首次已用过 -u 之后可直接 push）
```

若你在**另一台电脑**上改过仓库，或曾在 GitHub 网页上编辑过文件，推送前建议先拉取再推：

```bash
git pull --rebase origin main
git push
```

---

## 第三步：让别人（或你自己）能跑 demo

仓库页面的 **README** 里写了运行方式。本机在项目根目录执行：

```bash
python3 run_demo.py --topic "你的研究主题"
```

会在本机生成 `runs/<一次运行的ID>/` 下的占位产物（该目录已被 `.gitignore` 忽略，不会误传到 GitHub）。

---

## 常见问题

| 现象 | 处理 |
|------|------|
| `fatal: not a git repository` | 先 `cd` 到本项目根目录（含 `run_demo.py` 的那一层）。 |
| `remote origin already exists` | 执行 `git remote remove origin` 后重新 `git remote add origin ...`。 |
| 推送被拒绝 | 确认 GitHub 上建的是**空仓库**；若你在网页上点了创建 README，需按 GitHub 提示先 `git pull` 再推送，或新建另一个空仓库更简单。 |

---

## 可选：安装 GitHub CLI（以后建库更方便）

若你希望一条命令在终端里建远程仓库，可安装 [GitHub CLI](https://cli.github.com/)，登录后使用 `gh repo create`。这不是必须步骤。
