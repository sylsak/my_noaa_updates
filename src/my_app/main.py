# Navigate to the NOAA website and webscrape for surf observations
from src.my_app.modules.noaa_scrape import NOAAScraper
from src.my_app.modules.email_sender import EmailSender

surf_content = NOAAScraper("https://www.weather.gov/hfo/surfreports")
results = surf_content.call_webpage()

email = EmailSender()
email.send_email(results)