# 第一次把本项目上传到 GitHub（图文式步骤）

你已经有 GitHub 账号即可，不需要先安装额外软件（用网页 + 终端即可）。若本机还没有安装 **Git**，请先安装：[https://git-scm.com/downloads](https://git-scm.com/downloads)

---

## 第一步：在 GitHub 网站上新建空仓库

1. 打开 [https://github.com/new](https://github.com/new) 并登录。  
2. **Repository name** 填一个英文名，例如：`research-automation-demo`（不要用中文名，避免部分工具兼容问题）。  
3. 选 **Public**。  
4. **不要**勾选 “Add a README / Add .gitignore / Choose a license”（本仓库里已经准备好了这些文件）。  
5. 点 **Create repository**。  
6. 创建完成后，页面会显示仓库地址，请复制 **HTTPS** 地址，形如：  
   `https://github.com/你的用户名/research-automation-demo.git`

---

## 第二步：在本机项目目录里绑定远程并推送

打开终端（Terminal），执行下面命令（把 URL 换成你刚复制的地址）：

```bash
cd "/Users/heyuanjing/Downloads/百度同步/数据分析自动化项目"

git remote add origin https://github.com/你的用户名/research-automation-demo.git
git branch -M main
git push -u origin main
```

第一次 `git push` 时，GitHub 会要求登录：

- **推荐**：用 **Personal Access Token (PAT)** 代替密码（GitHub 已不再支持用账号密码推送代码）。  
  创建令牌：[https://github.com/settings/tokens](https://github.com/settings/tokens) → **Generate new token**，勾选 **`repo`**，生成后复制一串字符；在终端提示输入密码时，**把这串令牌粘贴进去**（输入时屏幕可能不显示字符，属于正常现象）。

推送成功后，刷新 GitHub 仓库页面即可看到所有文件。

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
