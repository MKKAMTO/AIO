from urllib.parse import urlparse

def get_service(url):
    domain = urlparse(url).netloc
    if 'deezer.com' in domain:
        from .deezer import DeezerService
        return DeezerService
    elif 'spotify.com' in domain:
        from .spotify import SpotifyService
        return SpotifyService
    elif 'tidal.com' in domain:
        from .tidal import TidalService
        return TidalService
    elif 'qobuz.com' in domain:
        from .qobuz import QobuzService
        return QobuzService
    elif 'kkbox.com' in domain:
        from .kkbox import KKBOXService
        return KKBOXService
    else:
        return None
