from django.shortcuts import render,redirect
from pytubefix import YouTube
from pytubefix.cli import on_progress
from django.http import JsonResponse
import os
# def youtube(request,path='downloads'):
#     video_details = None
#     if request.method == 'POST':
#         url=request.POST['link']
#         yt=YouTube(url,on_progress_callback = on_progress)
#         video_details = {
#             'title': yt.title,
#             'channel_name': yt.author,
#             'thumbnail_url': yt.thumbnail_url,
#             'duration': yt.length,  # Duration in seconds
#         }
#         # Get the highest resolution stream available
#         stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc().first()
#         stream.download(output_path=path)
#         return JsonResponse({'video_details': video_details})
#         # return render(request,'index.html',{'video_details': video_details})
#     return render(request,'index.html',{'video_details': video_details})

from django.conf import settings

def youtube(request, path='downloads'):
    video_details = None
    download_url = None  # Variable to store the download URL
    if request.method == 'POST':
        url = request.POST['link']
        yt = YouTube(url, on_progress_callback=on_progress)
        video_details = {
            'title': yt.title,
            'channel_name': yt.author,
            'thumbnail_url': yt.thumbnail_url,
            'duration': yt.length,  # Duration in seconds
        }

        # Get the highest resolution stream available
        stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc().first()

        # Construct the download path (this will be relative to MEDIA_ROOT)
        download_path = os.path.join(settings.MEDIA_ROOT, path, yt.title + ".mp4")
        
        # Ensure the directory exists
        os.makedirs(os.path.dirname(download_path), exist_ok=True)

        # Download the video
        stream.download(output_path=os.path.dirname(download_path))

        # Construct the URL that can be used for downloading
        download_url = settings.MEDIA_URL + path + '/' + yt.title + ".mp4"

        return JsonResponse({'video_details': video_details, 'download_url': download_url})

    return render(request, 'index.html', {'video_details': video_details})
