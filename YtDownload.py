import os

def download(link):
    # Get folder name from user input and remove spaces
    folder = input("Enter a name for the folder - ").replace(" ", "")
    
    # Check if the folder already exists
    if os.path.exists(folder):
        print(f"Using existing folder: {folder}")
    else:
        # Create the folder if it doesn't exist
        os.makedirs(folder)
        print(f"Created folder: {folder}")
    
    # Inform user that the download is starting
    print("Download Started...")

    # Construct the command for downloading using yt-dlp
    command = f"yt-dlp -f 'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]' -P {folder} '{link}'"
    
    try:
        # Execute the command to start the download
        os.system(command)
        print(f"Downloaded in {folder}")
    except Exception as e:
        # Handle errors during download
        print(f"Error during download: {e}")

# Check if the script is being run directly
if __name__ == "__main__":
    # Get the playlist/video link from user input and start the download
    download(input("Enter a playlist/video link - "))
