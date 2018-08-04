from pathlib import Path
from sh.contrib import git
from xdg.BaseDirectory import xdg_data_home

BASE_DIR = xdg_data_home + '/lumi/'
DISTRO_REPO_URL = 'https://github.com/liveunix/lumi-grub.git'
GRUB_REPO_URL = 'https://github.com/liveunix/lumi-grub.git'

def sync_repo(uri, dir):
    """Synchronize a single repository"""
    repo_exists = Path(dir).exists()

    if repo_exists is False:
        return git.clone(uri, dir)
    git.pull('origin', 'master', rebase=True, _cwd=dir)

def sync(base_dir=BASE_DIR):
    """Synchronize the LUMI repositories.

    If the repositories are not on the system, clone them.
    Otherwise, it pulls the updates from the remote repositories.
    """
    GRUB_DIR = base_dir + 'grub'
    DISTRO_DIR = base_dir + 'distro'

    sync_repo(GRUB_REPO_URL, GRUB_DIR)
    sync_repo(DISTRO_REPO_URL, DISTRO_DIR)