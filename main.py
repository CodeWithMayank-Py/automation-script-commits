import os
import git
from datetime import datetime
import pytz
import time

# Define your local time zone
local_tz = pytz.timezone('Asia/Kolkata')  # e.g., 'Asia/Kolkata'

# Set up repository path
repo_path = os.getcwd()

# Define the file to be updated
file_name = 'daily_commit.txt'

def make_commits(n):
    try:
        repo = git.Repo(repo_path)
        origin = repo.remote(name='origin')
        
        for i in range(4):
            # Update the content of the same file
            with open(file_name, 'w') as f:
                f.write(f"Updated content for commit at {datetime.now(local_tz).strftime('%Y-%m-%d %H:%M:%S')}\n")
            
            # Add changes to the staging area
            repo.git.add(file_name)
            
            # Commit changes
            commit_message = f"Automated commit {i+1} at {datetime.now(local_tz).strftime('%Y-%m-%d %H:%M:%S')}"
            repo.index.commit(commit_message)
            
            # Push changes
            origin.push()
            
            print(f"Committed and pushed changes: {commit_message}")
            
            # Optionally, wait for a short period before the next commit
            time.sleep(5)  # sleep for 5 seconds (adjust as needed)

    except Exception as e:
        print(f"Error lines received while fetching: {e}")

if __name__ == "__main__":
    make_commits(15)
