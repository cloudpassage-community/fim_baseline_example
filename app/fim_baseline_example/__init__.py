from git import Repo
import os
import sys
from config_helper import ConfigHelper # NOQA
from fim_baseline_example import FIM_BaselineExample # NOQA

# pull down the Halo helper wrapper if it does not exist
ERROR = 1

# pull down the Halo API wrapper and manage module path
halo_general_repo = "https://github.com/jgibbons-cp/halo_general.git"
cwd = os.getcwd()
repo_dir = "%s/halo_general" % cwd
sys.path.append(repo_dir)

# clone it if we don't have it
if os.path.exists(repo_dir) is False:
    Repo.clone_from(halo_general_repo, repo_dir)

try:
    from halo_general import HaloGeneral  # NOQA
except ImportError as e:
    print "Error: %s\n" % e
    sys.exit(ERROR)

__author__ = "CloudPassage"
__version__ = "1.0"
