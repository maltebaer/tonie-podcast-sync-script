from toniepodcastsync import Podcast, EpisodeSorting

checker_tobi = Podcast(
    "https://feeds.br.de/checkpod-der-podcast-mit-checker-tobi/feed.xml",
    episode_sorting = EpisodeSorting.RANDOM,
    volume_adjustment = 10,
)

maus_gute_nacht = Podcast(
    "https://kinder.wdr.de/radio/diemaus/audio/gute-nacht-mit-der-maus/diemaus-gute-nacht-104.podcast",
    episode_sorting = EpisodeSorting.RANDOM,
    volume_adjustment = 6,
)

maus_mix = Podcast(
    "https://kinder.wdr.de/radio/diemaus/audio/diemaus-musik/diemaus-musik-106.podcast",
    episode_sorting = EpisodeSorting.RANDOM,
    volume_adjustment = 6,
)

maus_zum_hoeren = Podcast(
    "https://kinder.wdr.de/radio/diemaus/audio/diemaus-60/diemaus-60-106.podcast",
    episode_sorting = EpisodeSorting.RANDOM,
    volume_adjustment = 6,
)
