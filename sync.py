import os
from dotenv import load_dotenv
from toniepodcastsync import ToniePodcastSync
from podcasts import checker_tobi, maus_gute_nacht

# Load environment variables from the .env file
load_dotenv()

# Create instance of ToniePodcastSync
tps = ToniePodcastSync(os.getenv("USERNAME"), os.getenv("PASSWORD"))

# For an overview of your creative tonies and their IDs
tps.print_tonies_overview()

gudrun = os.getenv("GUDRUN")
rolfi = os.getenv("ROLFI")
yeti = os.getenv("YETI")

tps.sync_podcast_to_tonie(checker_tobi, gudrun)
tps.sync_podcast_to_tonie(maus_gute_nacht, rolfi)
