
import sqlite3


DEFAULT_CONNECTION_STRING = "slowburn-cache.db"
CON = None


__all__ = [
    "set_database",
]


class CacheMissError(Exception): pass  # noqa


def ensure_db_connection(cxn_string=DEFAULT_CONNECTION_STRING):
    global CON
    if CON is None:
        set_database(cxn_string)


def set_database(cxn_string):
    global CON
    CON = sqlite3.connect(cxn_string)
    CON.execute(
        "CREATE TABLE IF NOT EXISTS cache (\
            id INTEGER PRIMARY KEY, \
            cache_name VARCHAR, \
            key VARCHAR, \
            value VARCHAR, \
            UNIQUE(cache_name, key) ON CONFLICT REPLACE \
        )"
    )


def _cache_get(cache_name, key):
    ensure_db_connection()
    results = CON.execute("SELECT value FROM cache WHERE cache_name = (?) AND key = (?)", (cache_name, key))
    try:
        return list(results)[0][0]
    except IndexError:
        raise CacheMissError


def _cache_set(cache_name, key, value):
    ensure_db_connection()
    CON.execute("INSERT OR REPLACE INTO cache(cache_name, key, value) VALUES (?, ?, ?)", (cache_name, key, value))
    CON.commit()
