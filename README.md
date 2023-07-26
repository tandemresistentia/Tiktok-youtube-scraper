[![TikTok and YouTube Scraper](https://raw.githubusercontent.com/tandemresistentia/Tiktok-youtube-scraper/main/assets/tiktok_youtube_scraper.png)](https://github.com/tandemresistentia/Tiktok-youtube-scraper)

# TikTok and YouTube Scraper

A Python web scraping tool for extracting data from TikTok and YouTube. This script provides a simple and efficient way to collect video information, such as video title, views, likes, comments, and other relevant data from both platforms.

## Features

- Extract TikTok video data, including video title, views, likes, comments, and more.
- Collect YouTube video data, such as title, views, likes, dislikes, and comments.
- Save the extracted data to a CSV file for further analysis or use.

## Prerequisites

Before running the scraper, ensure you have the following requirements installed:

- Python 3.7+
- [pip](https://pip.pypa.io/en/stable/installing/) package manager

## Installation

1. Clone this repository to your local machine using:

   ```
   git clone https://github.com/tandemresistentia/Tiktok-youtube-scraper.git
   ```

2. Navigate to the project directory:

   ```
   cd Tiktok-youtube-scraper
   ```

3. Install the required Python packages using pip:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Modify the input file (`input.csv`) with the TikTok and YouTube video URLs you want to scrape. Ensure that each URL is in a new line and includes a column header.

2. Run the scraper script:

   ```
   python scraper.py
   ```

3. The script will start processing the URLs and extract the relevant video data from both platforms.

4. Once the process is complete, the data will be saved in the `output.csv` file, which will be created in the same directory.

## Contributing

Contributions to this project are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.

## Disclaimer

This scraper is intended for educational purposes and data analysis only. Please ensure you comply with the terms of service and use it responsibly.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to use this TikTok and YouTube scraper to extract data and perform your analysis. If you encounter any problems or have suggestions for improvements, please let us know through issues or pull requests. Happy scraping! 😄
