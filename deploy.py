import os
import subprocess
import datetime
import urllib.parse

# CONFIGURATION
# ---------------------------------------------------------
# Your GitHub username
USERNAME = "Rey-EL" 
# Your Repository name
REPO_NAME = "app-assets"
# The folder where you put your images
IMAGE_FOLDER = "images"
# ---------------------------------------------------------

def run_command(command):
    """
    Runs a shell command and handles errors.
    """
    try:
        # subprocess.run executes the command in the shell.
        # check=True raises an exception if the command fails.
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(e)
        exit(1)

def get_image_urls():
    """
    Generates the direct URLs for all images in the folder.
    """
    base_url = f"https://{USERNAME}.github.io/{REPO_NAME}/{IMAGE_FOLDER}/"
    
    print("\n--- 🔗 Your Image URLs ---")
    
    # os.walk traverses the directory tree
    for root, dirs, files in os.walk(IMAGE_FOLDER):
        for file in files:
            # We encode the filename to handle spaces or special characters safely
            # e.g., "my logo.png" becomes "my%20logo.png"
            clean_filename = urllib.parse.quote(file)
            full_url = base_url + clean_filename
            print(f"File: {file}\nURL:  {full_url}\n")

def git_push_workflow():
    """
    Executes the git commands to upload changes.
    """
    print("--- 🚀 Starting Deployment ---")
    
    # 1. Add changes
    # Adds all new files in the current directory to the staging area
    print("Step 1: Staging files...")
    run_command("git add .")
    
    # 2. Commit changes
    # Saves the snapshot with a timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_message = f"Auto-deploy: {timestamp}"
    print(f"Step 2: Committing with message '{commit_message}'...")
    # We use a try-except block here because if there are no changes, git commit will fail.
    try:
        subprocess.run(f'git commit -m "{commit_message}"', shell=True, check=True)
    except subprocess.CalledProcessError:
        print("No changes to commit. Everything is up to date.")
        return

    # 3. Push to GitHub
    # Uploads the commit to the remote repository
    print("Step 3: Pushing to GitHub...")
    run_command("git push origin main")
    print("✅ Upload complete!")

if __name__ == "__main__":
    git_push_workflow()
    get_image_urls()
