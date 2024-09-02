import os
from datetime import datetime
from git import Repo
import time

# Define the repository path and file to update
repo_path = os.path.abspath('.')
file_path = os.path.join(repo_path, 'daily_commit.txt')

def update_file():
    # Write the current timestamp to the file
    with open(file_path, 'w') as file:
        file.write(f"Commit made on {datetime.now()}\n")

def make_commit():
    # Initialize the repository
    repo = Repo(repo_path)
    
    # Make 20 commits
    for _ in range(14):
        # Update the file with a new commit
        update_file()
        
        # Stage the changes
        repo.git.add(file_path)
        
        # Commit the changes
        repo.index.commit("Automated commit at " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        
        # Wait a short time to simulate different commit times
        time.sleep(10)
    
    # Push the changes
    origin = repo.remote(name='origin')
    origin.push()

if __name__ == "__main__":
    make_commit()
