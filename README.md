# YouTube Video Downloader

A simple web application built using Django that allows users to download YouTube videos by providing the video URL. The application fetches the video details and offers a download link for the highest-resolution MP4 stream available.

## Features

- Extracts video details such as title, channel name, thumbnail, and duration.
- Downloads the highest resolution MP4 video available.
- Provides a direct download link for the video.
- Saves downloaded videos in a configurable directory.

## Installation

### Prerequisites
- Python (>=3.8)
- Django (>=3.2)
- pytubefix (a patched version of pytube)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/youtube-video-downloader.git
   cd youtube-video-downloader
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure Django settings:
   - Open `settings.py` and configure the `MEDIA_ROOT` and `MEDIA_URL` variables to define where downloaded videos will be stored and how they will be served.

   ```python
   MEDIA_ROOT = BASE_DIR / 'media'
   MEDIA_URL = '/media/'
   ```

5. Run database migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Open your browser and visit `http://127.0.0.1:8000/`.

## Usage

1. Enter the YouTube video URL in the input field on the homepage.
2. Click the submit button.
3. The app will fetch the video details and provide a download link for the video.

## Project Structure

```
.
├── youtube_video_downloader
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── templates
│   │   └── index.html
├── media
│   └── downloads
├── manage.py
└── requirements.txt
```

- `views.py`: Contains the logic for handling requests and downloading videos.
- `index.html`: The homepage template for the application.
- `media/downloads`: The default directory where downloaded videos are saved.

## Dependencies

- Django
- pytubefix

Install dependencies with:
```bash
pip install django pytubefix
```

## Notes

- Ensure that the `MEDIA_ROOT` directory has appropriate write permissions.
- The application uses `pytubefix`, a patched version of `pytube`, to handle video downloads. If there are issues, ensure that `pytubefix` is up-to-date.



