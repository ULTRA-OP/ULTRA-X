
import asyncio
import os
import sys

import git
import heroku3

from ULTRA.utils import admin_cmd

IS_SELECTED_DIFFERENT_BRANCH = (
    "It looks like a custom branch {branch_name} "
    "is being used:\n"
    "In this case, Updater is unable to identify the branch to be updated."
    "please check out to an official branch (master), and re-start the updater."
)
OFFICIAL_UPSTREAM_REPO = "https://github.com/ULTRA-OP/HEROKU"
REPO_REMOTE_NAME = "temponame"
IFFUCI_ACTIVE_BRANCH_NAME = "main"
NO_HEROKU_APP_CFGD = "No heroku app detected, but a key is given !?!?!?!"
HEROKU_GIT_REF_SPEC = "HEAD:refs/heads/master"
RESTARTING_APP = "Restarting App..."



@borg.on(admin_cmd("update ?(.*)", outgoing=True))
async def updater(message):
    folder = os.path.abspath("/app")
    try:
        repo = git.Repo(folder)
    except git.exc.InvalidGitRepositoryError as e:
        repo = git.Repo.init(folder)
        origin = repo.create_remote(REPO_REMOTE_NAME, OFFICIAL_UPSTREAM_REPO)
        origin.fetch()
        repo.create_head(IFFUCI_ACTIVE_BRANCH_NAME, origin.refs.master)
        repo.heads.master.checkout(True)

    active_branch_name = repo.active_branch.name
    if active_branch_name != IFFUCI_ACTIVE_BRANCH_NAME:
        await message.edit(
            IS_SELECTED_DIFFERENT_BRANCH.format(branch_name=active_branch_name)
        )
        return False

    try:
        repo.create_remote(REPO_REMOTE_NAME, OFFICIAL_UPSTREAM_REPO)
    except Exception as e:
        print(e)
    temp_upstream_remote = repo.remote(REPO_REMOTE_NAME)
    temp_upstream_remote.fetch(active_branch_name)
    repo.git.reset("--hard", "FETCH_HEAD")

    if Config.HEROKU_API_KEY is not None:

        heroku = heroku3.from_key(Config.HEROKU_API_KEY)
        heroku_applications = heroku.apps()
        if len(heroku_applications) >= 1:
            if Config.HEROKU_APP_NAME is not None:
                heroku_app = None
                for i in heroku_applications:
                    if i.name == Config.HEROKU_APP_NAME:
                        heroku_app = i
                if heroku_app is None:
                    await message.edit(
                        "Provided Heroku App Name doesn't exist or maybe incorrect. Please go to your app and recheck the app name."
                    )
                    return
                heroku_git_url = heroku_app.git_url.replace(
                    "https://", "https://api:" + Config.HEROKU_API_KEY + "@"
                )
                if "heroku" in repo.remotes:
                    remote = repo.remote("heroku")
                    remote.set_url(heroku_git_url)
                else:
                    remote = repo.create_remote("heroku", heroku_git_url)
                asyncio.get_event_loop().create_task(
                    deploy_start(bot, message, HEROKU_GIT_REF_SPEC, remote)
                )

            else:
                await message.edit(
                    "Config var `HEROKU_APP_NAME` not found. Please set it from Heroku Site..."
                )
                return
        else:
            await message.edit(NO_HEROKU_APP_CFGD)
    else:
        await message.edit("Var `HEROKU_API_KEY` is either empty or incorrect values are filled.")


async def deploy_start(tgbot, message, refspec, remote):
    await message.edit(RESTARTING_APP)
    await message.edit(
        "Updated your Bot successfully sur!!!\n\nNow type .ping after 5 mins to check if I'm on🚶😏\n"
    )
    await remote.push(refspec=refspec)
    await tgbot.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)


