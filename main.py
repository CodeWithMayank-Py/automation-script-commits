import os
import git
from datetime import datetime
import pytz
import time
import random

# Define your local time zone
local_tz = pytz.timezone('Asia/Kolkata')  # e.g., 'America/New_York'

# Set up repository path
repo_path = os.getcwd()

# Define the file to be updated
file_name = 'daily_commit.txt'

# Define the range for random commits
min_commits = 25
max_commits = 40

def make_commits():
    try:
        # Pick a random number of commits within the specified range
        num_commits = random.randint(min_commits, max_commits)

        repo = git.Repo(repo_path)
        origin = repo.remote(name='origin')
        
        for i in range(num_commits):
            # Update the content of the same file
            with open(file_name, 'a') as f:  # Append mode
                f.write(f"Updated content for commit {i+1} at {datetime.now(local_tz).strftime('%Y-%m-%d %H:%M:%S')}\n")
            
            # Add changes to the staging area
            repo.git.add(file_name)
            
            # Commit changes
            commit_message = f"Automated commit {i+1} at {datetime.now(local_tz).strftime('%Y-%m-%d %H:%M:%S')}"
            repo.index.commit(commit_message)
            
            # Push changes with retry logic
            for attempt in range(3):  # Retry up to 3 times
                try:
                    origin.push()
                    break  # If successful, break the loop
                except Exception as push_error:
                    print(f"Push failed, retrying... ({attempt+1}/3)")
                    time.sleep(5)

            print(f"Committed and pushed changes: {commit_message}")
            
            # Wait for a short period before the next commit
            time.sleep(10)  # sleep for 10 seconds

    except Exception as e:
        print(f"Error lines received while fetching: {e}")

if __name__ == "__main__":
    make_commits()
