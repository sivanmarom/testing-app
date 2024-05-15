Certainly! I've updated the README to reflect the use of an IAM role for EC2 instances to access the S3 bucket without needing a specific bucket policy. Here's the revised version:

---

# Django Video Streaming Application

## Overview
This Django application demonstrates video streaming from an AWS S3 bucket. The application retrieves a video file stored in S3 and streams it to a web page using Django.

## Key Features
- **Video Streaming**: Streams video directly from an AWS S3 bucket to the web browser using Django.
- **Secure AWS Integration**: Utilizes AWS IAM roles and boto3 to securely access and stream video content from S3.

## Prerequisites
- Python 3.8 or higher
- pip and virtualenv
- AWS Account
- AWS CLI configured on your machine

## AWS S3 Bucket Setup
Follow these steps to create and configure an S3 bucket for storing your video files:

### Create the S3 Bucket
1. Log in to the AWS Management Console.
2. Navigate to the S3 service.
3. Click "Create bucket".
4. Provide a unique name for your bucket and select a Region.
5. Uncheck "Block all public access" to ensure the bucket is not publicly accessible.
6. Click "Create bucket".

## AWS EC2 Instance IAM Role
Assign an IAM role to your EC2 instance that grants it permissions to access your S3 bucket:
1. Navigate to the IAM service in the AWS Management Console.
2. Click on "Roles", then "Create role".
3. Select "AWS service" as the type of trusted entity, and choose "EC2" as the service that will use this role.
4. Attach policies that grant access to your S3 bucket. For testing purposes, you could use the `AmazonS3FullAccess` policy, but it is recommended to create a custom policy that grants only necessary permissions.
5. Complete the role creation and attach the role to your EC2 instance.

## Installation

### Clone the Repository
```bash
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
```

### Set Up Python Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Apply Migrations
```bash
python manage.py migrate
```

### Run the Server
```bash
python manage.py runserver 0.0.0.0:8000
```

## How It Works
- **Video Retrieval**: The application uses boto3 to interact with AWS S3. When the endpoint `/video` is hit, the server fetches the video file from S3 using the permissions provided by the IAM role attached to the EC2 instance.
- **Template Rendering**: The main page (`index.html`) includes a video tag whose source is set to the `/video` endpoint. This setup keeps the actual video URL hidden and secure, utilizing Django's capability to handle streaming data directly.

## Security Considerations
- **IAM Role for EC2**: Ensure that the EC2 instance has an IAM role with the appropriate permissions to access the S3 bucket. Avoid using overly permissive policies like `AmazonS3FullAccess` in production.
- **Bucket Access**: The S3 bucket should not be publicly accessible. Manage access strictly via IAM roles.
