from couchpotato.core.helpers.encoding import tryUrlencode
from couchpotato.core.logger import CPLog
from couchpotato.core.event import fireEvent
from couchpotato.core.media._base.providers.torrent.bitsoup import Base
from couchpotato.core.media.movie.providers.base import MovieProvider

log = CPLog(__name__)

autoload = 'Bitsoup'


class Bitsoup(MovieProvider, Base):
    cat_ids = [
        ([41], ['720p', '1080p']),
        ([17], ['3d']),
        ([20], ['dvdr']),
        ([19], ['brrip', 'dvdrip']),
    ]
    cat_backup_id = 0

    def buildUrl(self, media, quality):
        query = tryUrlencode({
            'search': '"%s" %s' % (
                fireEvent('library.query', media, include_year = False, single = True),
                media['info']['year']
            ),
            'cat': self.getCatId(quality['identifier'])[0],
        })
        return query