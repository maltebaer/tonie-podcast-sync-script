from toniepodcastsync import ToniePodcastSync, Podcast
from credentials import username, password
from tonies import gudrun, rolfi, yeti
from podcasts import checkerTobi, pumuckl, mausGuteNacht

# Create instance of ToniePodcastSync
tps = ToniePodcastSync(username, password)

# For an overview of your creative tonies and their IDs
tps.print_tonies_overview()

# The tonie will be filled with as much episodes as fit (90 min max).
# Episode are ordered with newest first
# Use the optional parameter to limit total
tps.sync_podcast_to_tonie(checkerTobi, gudrun)
tps.sync_podcast_to_tonie(pumuckl, rolfi)
tps.sync_podcast_to_tonie(mausGuteNacht, yeti)
