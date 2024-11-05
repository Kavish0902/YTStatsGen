from flask import Flask, request, jsonify
from googleapiclient.discovery import build
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Replace with your API key
API_KEY = 'REPLACE'

# Function to get video details
def get_video_details(video_id):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    request = youtube.videos().list(
        part='snippet,contentDetails,statistics',
        id=video_id
    )
    response = request.execute()
    return response

# Function to get channel details
def get_channel_details(channel_id):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    request = youtube.channels().list(
        part='statistics',
        id=channel_id
    )
    response = request.execute()
    return response

@app.route('/stats', methods=['GET'])
def video_stats():
    video_id = request.args.get('videoId')
    if not video_id:
        return jsonify({'error': 'Missing video ID'}), 400

    try:
        details = get_video_details(video_id)
        if 'items' in details and len(details['items']) > 0:
            video = details['items'][0]
            channel_id = video['snippet']['channelId']
            channel_title = video['snippet'].get('channelTitle', 'N/A')
            view_count = video['statistics'].get('viewCount', 'N/A')
            like_count = video['statistics'].get('likeCount', 'N/A')

            # Get channel details for subscriber count
            channel_details = get_channel_details(channel_id)
            sub_count = channel_details['items'][0]['statistics'].get('subscriberCount', 'N/A')

            response_data = {
                'channelTitle': channel_title,
                'viewCount': view_count,
                'likeCount': like_count,
                'subCount': sub_count
            }
            return jsonify(response_data)
        else:
            return jsonify({'error': 'Video not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
