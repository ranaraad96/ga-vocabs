# Configuration file for vocabs_load.py file. Edit this template and save as config.py
GITHUB_RAW_URI_BASE = "https://example.org"
GITHUB_USR = "github_username"  # or any valid GitHub account
GITHUB_PWD = "github_password"  # for the valid GitHub account

GRAPHDB_REPO_ID = "ga-vocs"
GRAPHDB_REPO_URI = "http://localhost:7200/repositories/{}".format(GRAPHDB_REPO_ID)
GRAPHDB_LOAD_DATA_URI = "http://localhost:7200/rest/data/import/upload/{}/url".format(GRAPHDB_REPO_ID)
GRAPHDB_USR = "graphdb_username"
GRAPHDB_PWD = "graphdb_password"
