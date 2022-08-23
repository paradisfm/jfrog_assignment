# importing necessary packages
import requests
from pyartifactory import Artifactory
from pyartifactory.models import NewUser, LocalRepository

# authentication
art = Artifactory(url="https://hadar2.jfrog.io/artifactory",
                  auth=('username',
                        'password_or_api_key'),
                  verify=False,
                  api_version=2)


# defining all functions in order to create cli

# pings server
def sys_ping(host):
    resp = requests.get(host)
    if not resp:
        print('unable to ping system.')
    else:
        print("yeehaw! you're in.")


# create a user
def create_user():
    username = input("Enter a username: ")
    pw = input("Enter a password: ")
    uemail = input("Enter an email: ")
    user = NewUser(name=username, password=pw, email=uemail)
    new_user = art.users.create(user)
    print(f'test user "{new_user.name}" created :~)')


# delete a user
def delete_user():
    user_exile = input('which user would you like to delete?')
    art.users.delete(user_exile)
    print('test user deleted :~)')


# creating a local repository
def create_repo():
    ukey = input('what is the repository key?')
    local_repo = LocalRepository(key=ukey)
    new_local_repo = art.repositories.create_repo(local_repo)
    print(f'local repository "{new_local_repo.key}" created :~)')


# list all repositories
def list_repos():
    repositories = art.repositories.list()
    print(repositories)


# creating CLI
cur_command = input("Enter a command: ")
while "exit" != cur_command:
    if cur_command == "ping":
        url = "https://hadar2.jfrog.io/"
        sys_ping(url)
    elif cur_command == "create user":
        create_user()
    elif cur_command == "delete user":
        delete_user()
    elif cur_command == 'create repo':
        key = "test-local-repo"
        create_repo()
    elif cur_command == 'list repos':
        list_repos()
    cur_command = input("Enter a command: ")
