import os
import subprocess
import shutil
from datetime import datetime
from dotenv import load_dotenv
from github import Github, Auth

load_dotenv()

token = os.getenv("GITHUB_TOKEN")
github = Github(auth=Auth.Token(token))
folder = "github-" + datetime.now().strftime("%Y-%m-%d")

print("create folder: " + folder)
os.chdir(os.path.expanduser("~/Downloads/"))
os.mkdir(folder)

for repo in github.get_user().get_repos(affiliation="owner"):
	print("git clone: " + repo.name)
	subprocess.run(
		[
			"git",
			"clone",
			f"git@github.com:{repo.full_name}.git",
			f"{folder}/{repo.name}",
		],
		capture_output=True,
	)

print("create zip")
shutil.make_archive(folder, "zip", folder)
shutil.rmtree(folder)

print("done")
github.close()
