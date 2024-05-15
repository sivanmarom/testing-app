from django.shortcuts import render
from django.http import HttpResponse
import boto3

def index(request):
    return render(request, 'index.html', {'video_url': '/video'})

def video(request):
    s3 = boto3.client('s3')
    bucket_name = "testing-bucket-sivan"
    video_file = "test.mp4"
    video_object = s3.get_object(Bucket=bucket_name, Key=video_file)
    return HttpResponse(
        video_object['Body'].read(),
        content_type='video/mp4',
        headers={'Content-Disposition': f'inline; filename={video_file}'}
    )
