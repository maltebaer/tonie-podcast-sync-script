from toniepodcastsync import ToniePodcastSync
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Create instance of ToniePodcastSync
tps = ToniePodcastSync(os.getenv("USERNAME"), os.getenv("PASSWORD"))

# For an overview of your creative tonies and their IDs
tps.print_tonies_overview()
