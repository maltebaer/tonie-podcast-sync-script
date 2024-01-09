from toniepodcastsync import ToniePodcastSync
from credentials import username, password

# Create instance of ToniePodcastSync
tps = ToniePodcastSync(username, password)

# For an overview of your creative tonies and their IDs
tps.print_tonies_overview()
