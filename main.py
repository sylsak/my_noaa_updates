# Navigate to the NOAA website and webscrape for surf observations
from noaa_scrape import NOAAScraper
from email_sender import EmailSender

surf_content = NOAAScraper("https://www.weather.gov/hfo/surfreports")
results = surf_content.call_webpage()

email = EmailSender()
email.send_email(results)