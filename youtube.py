# from pytube import YouTube
from pytubefix import YouTube
from pytubefix.cli import on_progress
def download_youtube_video(video_url, output_path="YouTube_Download"):
    """
    Downloads a YouTube video to the specified output path.

    Args:
        video_url (str): The URL of the YouTube video.
        output_path (str): The directory where the video will be saved. Default is 'downloads'.

    Returns:
        str: The file path of the downloaded video.
    """
    try:
        # Create a YouTube object
        yt = YouTube(video_url,on_progress_callback = on_progress)

        # Get the highest resolution stream available
        video_stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc().first()
        # video_stream=yt.streams.filter(res='144p').first().download()

        print(f"Downloading: {yt.title}")
        # print(f"Video resolution: {video_stream.resolution}")
        
        # Download the video
        file_path = video_stream.download(output_path)
        
        print(f"Download completed. Saved at: {file_path}")
        print(f"Thumbnail: {yt.thumbnail_url}")
        return file_path
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Example URL of a YouTube video
    video_url = input("Enter the YouTube video URL: ")
    
    # Download the video
    download_youtube_video(video_url)
