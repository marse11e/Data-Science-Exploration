import os
import subprocess
from datetime import datetime


class GitRepositoryManager:
    def __init__(self, commit_message: str, branch_name: str) -> None:
        self.commit_message = commit_message
        self.branch_name = branch_name
        self.remote_repo_url = 'git@github.com:marse11e/Data-Science-Exploration.git'
        self.is_initialized = False

    def execute_command(self, command: str) -> None:
        try:
            subprocess.run(command, check=True, shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Ошибка выполнения команды '{command}': {e}")

    def initialize_repository(self) -> None:
        if not self.is_initialized and not os.path.exists('.git'):
            self.execute_command("git init")
            self.execute_command(f'git remote add origin {self.remote_repo_url}')
            self.is_initialized = True

    def push_changes(self) -> None:
        timestamp = datetime.now().strftime("%d%m%y %H-%M")
        self.execute_command('git add .')
        self.execute_command(f'git commit -m "{self.commit_message} {timestamp}"')
        self.execute_command(f'git checkout -b {self.branch_name}')
        self.execute_command(f'git push -u origin {self.branch_name}')


if __name__ == '__main__':
    commit_message = input('Введите то, что вы изменили:\n>>> ')
    
    git_manager = GitRepositoryManager(commit_message=commit_message, branch_name='master')
    git_manager.initialize_repository()
    git_manager.push_changes()
