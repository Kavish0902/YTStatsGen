# YTStatsGen

YTStatsWebsite is a simple web application that allows users to view YouTube video statistics like view count, like count, and subscriber count for a video’s channel. The application consists of a front-end webpage (`youtube_stats.html`) and a back-end server (`youtube_api_server.py`) built using Flask.

## Features
- Fetch YouTube video statistics such as views, likes, and subscriber count.
- Interactive front-end interface for entering YouTube video URLs.
- Back-end server using the YouTube API to retrieve video statistics.

## Prerequisites
Before setting up the project, make sure you have the following:
- **Python 3.7+**
- **pip** (Python package manager)
- **Flask** and **google-api-python-client** libraries

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/YTStatsWebsite.git
   cd YTStatsWebsite

2. Install required Python packages: Run the following command to install Flask and google-api-python-client:
   
   pip install Flask google-api-python-client flask-cors

3. Set up your YouTube Data API key:
Go to the Google Cloud Console.

Create a project (if you don't already have one).

Go to APIs & Services > Credentials and click Create Credentials > API Key.

Enable the YouTube Data API v3 for your project.

Open youtube_api_server.py and replace API_KEY = 'REPLACE' with your actual API key.

USAGE

1. Run the backend server: In your terminal, navigate to the project folder and start the Flask server:
  python youtube_api_server.py

1.5 The server will start at http://localhost:5000.

2. Open the front-end HTML file: Open youtube_stats.html in your browser.

3. Retrieve video statistics:

3.5 Enter a YouTube video URL in the input box.
      3.5.1 Click Get Video Stats to fetch and display the statistics for the video.

