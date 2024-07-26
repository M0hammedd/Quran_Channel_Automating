import os
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Define paths and constants
CLIENT_SECRETS_FILE = 'C:\\Users\\Mohamed\\Downloads\\client_secret_137588845720-hdf81d4h7dmefs1t235ap8g1glhk9lt4.apps.googleusercontent.com (1).json'
TOKEN_FILE = 'token.json'
VIDEO_FOLDER = 'B:\\personal folders\\automatic_quran_vids\\output_vids\\'

# OAuth 2.0 scopes for YouTube Data API
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

def get_authenticated_service():
    credentials = None

    # Load credentials from token file if it exists
    if os.path.exists(TOKEN_FILE):
        credentials = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    # If there are no valid credentials, prompt the user to log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
            credentials = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open(TOKEN_FILE, 'w') as token:
            token.write(credentials.to_json())

    return build('youtube', 'v3', credentials=credentials)

def upload_video(youtube, video_file, title, description):
    tags = ['قرآن', 'تلاوة', 'الشيخ المنشاوي', 'محمد المنشاوي', 'الشيخ محمد المنشاوي', 'الشيخ صديق المنشاوي', 'صديق المنشاوي', 'الشيخ محمد', 'المنشاوي']

    category_id = '22'  # Category ID for People & Blogs

    # Construct video metadata
    request_body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': tags,
            'categoryId': category_id
        },
        'status': {
            'privacyStatus': 'unlisted'
        }
    }

    # Initialize media upload
    media = MediaFileUpload(video_file, chunksize=-1, resumable=True)

    # Attempt to upload the video
    try:
        # Execute resumable upload
        response = youtube.videos().insert(
            part='snippet,status',
            body=request_body,
            media_body=media
        ).execute()

        print(f'Video uploaded successfully: https://www.youtube.com/watch?v={response["id"]}')

    except Exception as e:
        print(f'Error uploading video: {str(e)}')
if __name__ == '__main__':
    # Authenticate and create YouTube service
    youtube = get_authenticated_service()

    # Updated Video data: filenames, titles, and descriptions for the new Surahs
    video_data = [
    ("a (1).mp4", "الشيخ المنشاوي | سورة يونس | surah Yunus", 
     "استمع إلى تلاوة نادرة ومؤثرة لسورة يونس بصوت القارئ المميز محمد صديق المنشاوي. في هذه التلاوة، ستجد الخشوع والتدبر في كلمات الله تعالى. يعتبر الشيخ المنشاوي أحد أبرز قراء القرآن الكريم، وتتميز قراءته بالعذوبة والروحانية العميقة. نأمل أن تجدوا في هذه التلاوة ما يعينكم على التفكر والتدبر في كتاب الله العزيز. لا تنسوا الاشتراك في القناة وتفعيل جرس الإشعارات والإعجاب بالفيديو إذا نال إعجابكم ومشاركته مع أصدقائكم وأحبتكم ليعم الثواب. بارك الله فيكم. Listen to a rare and moving recitation of Surah Yunus by the distinguished reciter Sheikh Muhammad Siddiq Al-Minshawi. In this recitation, you will find humility and reflection in the words of Allah. Sheikh Al-Minshawi is one of the most prominent Quran reciters, known for his melodious and deeply spiritual recitations. We hope you find in this recitation what helps you contemplate and reflect on the noble Quran. Don't forget to subscribe to the channel, activate the notification bell, like the video if you enjoyed it, and share it with your friends and loved ones to spread the reward. May Allah bless you all."),
    ("a (2).mp4", "الشيخ المنشاوي | سورة هود | surah Hud", 
     "استمع إلى تلاوة نادرة ومؤثرة لسورة هود بصوت القارئ المميز محمد صديق المنشاوي. في هذه التلاوة، ستجد الخشوع والتدبر في كلمات الله تعالى. يعتبر الشيخ المنشاوي أحد أبرز قراء القرآن الكريم، وتتميز قراءته بالعذوبة والروحانية العميقة. نأمل أن تجدوا في هذه التلاوة ما يعينكم على التفكر والتدبر في كتاب الله العزيز. لا تنسوا الاشتراك في القناة وتفعيل جرس الإشعارات والإعجاب بالفيديو إذا نال إعجابكم ومشاركته مع أصدقائكم وأحبتكم ليعم الثواب. بارك الله فيكم. Listen to a rare and moving recitation of Surah Hud by the distinguished reciter Sheikh Muhammad Siddiq Al-Minshawi. In this recitation, you will find humility and reflection in the words of Allah. Sheikh Al-Minshawi is one of the most prominent Quran reciters, known for his melodious and deeply spiritual recitations. We hope you find in this recitation what helps you contemplate and reflect on the noble Quran. Don't forget to subscribe to the channel, activate the notification bell, like the video if you enjoyed it, and share it with your friends and loved ones to spread the reward. May Allah bless you all."),
    ("a (3).mp4", "الشيخ المنشاوي | سورة يوسف | surah Yusuf", 
     "استمع إلى تلاوة نادرة ومؤثرة لسورة يوسف بصوت القارئ المميز محمد صديق المنشاوي. في هذه التلاوة، ستجد الخشوع والتدبر في كلمات الله تعالى. يعتبر الشيخ المنشاوي أحد أبرز قراء القرآن الكريم، وتتميز قراءته بالعذوبة والروحانية العميقة. نأمل أن تجدوا في هذه التلاوة ما يعينكم على التفكر والتدبر في كتاب الله العزيز. لا تنسوا الاشتراك في القناة وتفعيل جرس الإشعارات والإعجاب بالفيديو إذا نال إعجابكم ومشاركته مع أصدقائكم وأحبتكم ليعم الثواب. بارك الله فيكم. Listen to a rare and moving recitation of Surah Yusuf by the distinguished reciter Sheikh Muhammad Siddiq Al-Minshawi. In this recitation, you will find humility and reflection in the words of Allah. Sheikh Al-Minshawi is one of the most prominent Quran reciters, known for his melodious and deeply spiritual recitations. We hope you find in this recitation what helps you contemplate and reflect on the noble Quran. Don't forget to subscribe to the channel, activate the notification bell, like the video if you enjoyed it, and share it with your friends and loved ones to spread the reward. May Allah bless you all."),
    ("a (4).mp4", "الشيخ المنشاوي | سورة الرعد | surah Ar-Ra'd", 
     "استمع إلى تلاوة نادرة ومؤثرة لسورة الرعد بصوت القارئ المميز محمد صديق المنشاوي. في هذه التلاوة، ستجد الخشوع والتدبر في كلمات الله تعالى. يعتبر الشيخ المنشاوي أحد أبرز قراء القرآن الكريم، وتتميز قراءته بالعذوبة والروحانية العميقة. نأمل أن تجدوا في هذه التلاوة ما يعينكم على التفكر والتدبر في كتاب الله العزيز. لا تنسوا الاشتراك في القناة وتفعيل جرس الإشعارات والإعجاب بالفيديو إذا نال إعجابكم ومشاركته مع أصدقائكم وأحبتكم ليعم الثواب. بارك الله فيكم. Listen to a rare and moving recitation of Surah Ar-Ra'd by the distinguished reciter Sheikh Muhammad Siddiq Al-Minshawi. In this recitation, you will find humility and reflection in the words of Allah. Sheikh Al-Minshawi is one of the most prominent Quran reciters, known for his melodious and deeply spiritual recitations. We hope you find in this recitation what helps you contemplate and reflect on the noble Quran. Don't forget to subscribe to the channel, activate the notification bell, like the video if you enjoyed it, and share it with your friends and loved ones to spread the reward. May Allah bless you all."),
    ("a (5).mp4", "الشيخ المنشاوي | سورة إبراهيم | surah Ibrahim", 
     "استمع إلى تلاوة نادرة ومؤثرة لسورة إبراهيم بصوت القارئ المميز محمد صديق المنشاوي. في هذه التلاوة، ستجد الخشوع والتدبر في كلمات الله تعالى. يعتبر الشيخ المنشاوي أحد أبرز قراء القرآن الكريم، وتتميز قراءته بالعذوبة والروحانية العميقة. نأمل أن تجدوا في هذه التلاوة ما يعينكم على التفكر والتدبر في كتاب الله العزيز. لا تنسوا الاشتراك في القناة وتفعيل جرس الإشعارات والإعجاب بالفيديو إذا نال إعجابكم ومشاركته مع أصدقائكم وأحبتكم ليعم الثواب. بارك الله فيكم. Listen to a rare and moving recitation of Surah Ibrahim by the distinguished reciter Sheikh Muhammad Siddiq Al-Minshawi. In this recitation, you will find humility and reflection in the words of Allah. Sheikh Al-Minshawi is one of the most prominent Quran reciters, known for his melodious and deeply spiritual recitations. We hope you find in this recitation what helps you contemplate and reflect on the noble Quran. Don't forget to subscribe to the channel, activate the notification bell, like the video if you enjoyed it, and share it with your friends and loved ones to spread the reward. May Allah bless you all."),
    ("a (6).mp4", "الشيخ المنشاوي | سورة الحجر | surah Al-Hijr", 
     "استمع إلى تلاوة نادرة ومؤثرة لسورة الحجر بصوت القارئ المميز محمد صديق المنشاوي. في هذه التلاوة، ستجد الخشوع والتدبر في كلمات الله تعالى. يعتبر الشيخ المنشاوي أحد أبرز قراء القرآن الكريم، وتتميز قراءته بالعذوبة والروحانية العميقة. نأمل أن تجدوا في هذه التلاوة ما يعينكم على التفكر والتدبر في كتاب الله العزيز. لا تنسوا الاشتراك في القناة وتفعيل جرس الإشعارات والإعجاب بالفيديو إذا نال إعجابكم ومشاركته مع أصدقائكم وأحبتكم ليعم الثواب. بارك الله فيكم. Listen to a rare and moving recitation of Surah Al-Hijr by the distinguished reciter Sheikh Muhammad Siddiq Al-Minshawi. In this recitation, you will find humility and reflection in the words of Allah. Sheikh Al-Minshawi is one of the most prominent Quran reciters, known for his melodious and deeply spiritual recitations. We hope you find in this recitation what helps you contemplate and reflect on the noble Quran. Don't forget to subscribe to the channel, activate the notification bell, like the video if you enjoyed it, and share it with your friends and loved ones to spread the reward. May Allah bless you all."),
    ("a (7).mp4", "الشيخ المنشاوي | سورة النحل | surah An-Nahl", 
     "استمع إلى تلاوة نادرة ومؤثرة لسورة النحل بصوت القارئ المميز محمد صديق المنشاوي. في هذه التلاوة، ستجد الخشوع والتدبر في كلمات الله تعالى. يعتبر الشيخ المنشاوي أحد أبرز قراء القرآن الكريم، وتتميز قراءته بالعذوبة والروحانية العميقة. نأمل أن تجدوا في هذه التلاوة ما يعينكم على التفكر والتدبر في كتاب الله العزيز. لا تنسوا الاشتراك في القناة وتفعيل جرس الإشعارات والإعجاب بالفيديو إذا نال إعجابكم ومشاركته مع أصدقائكم وأحبتكم ليعم الثواب. بارك الله فيكم. Listen to a rare and moving recitation of Surah An-Nahl by the distinguished reciter Sheikh Muhammad Siddiq Al-Minshawi. In this recitation, you will find humility and reflection in the words of Allah. Sheikh Al-Minshawi is one of the most prominent Quran reciters, known for his melodious and deeply spiritual recitations. We hope you find in this recitation what helps you contemplate and reflect on the noble Quran. Don't forget to subscribe to the channel, activate the notification bell, like the video if you enjoyed it, and share it with your friends and loved ones to spread the reward. May Allah bless you all."),
    ("a (8).mp4", "الشيخ المنشاوي | سورة الإسراء | surah Al-Isra'", 
     "استمع إلى تلاوة نادرة ومؤثرة لسورة الإسراء بصوت القارئ المميز محمد صديق المنشاوي. في هذه التلاوة، ستجد الخشوع والتدبر في كلمات الله تعالى. يعتبر الشيخ المنشاوي أحد أبرز قراء القرآن الكريم، وتتميز قراءته بالعذوبة والروحانية العميقة. نأمل أن تجدوا في هذه التلاوة ما يعينكم على التفكر والتدبر في كتاب الله العزيز. لا تنسوا الاشتراك في القناة وتفعيل جرس الإشعارات والإعجاب بالفيديو إذا نال إعجابكم ومشاركته مع أصدقائكم وأحبتكم ليعم الثواب. بارك الله فيكم. Listen to a rare and moving recitation of Surah Al-Isra' by the distinguished reciter Sheikh Muhammad Siddiq Al-Minshawi. In this recitation, you will find humility and reflection in the words of Allah. Sheikh Al-Minshawi is one of the most prominent Quran reciters, known for his melodious and deeply spiritual recitations. We hope you find in this recitation what helps you contemplate and reflect on the noble Quran. Don't forget to subscribe to the channel, activate the notification bell, like the video if you enjoyed it, and share it with your friends and loved ones to spread the reward. May Allah bless you all.")
]




    # Upload each video
    for video_info in video_data:
        video_filename, video_title, video_description = video_info
        video_path = os.path.join(VIDEO_FOLDER, video_filename)

        if os.path.exists(video_path):
            upload_video(youtube, video_path, video_title, video_description)
        else:
            print(f'Video file not found: {video_path}')
