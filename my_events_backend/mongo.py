import atexit
import certifi
from pymongo import MongoClient
from django.conf import settings

# Global singletons (cache the client and database)
_client = None
_db = None


def get_client() -> MongoClient:
    """
    Get (and cache) a MongoDB client instance.

    Notes
    -----
    - Uses a global variable to avoid creating a new connection
      on every function call.
    - Reads `MONGODB_URI` from Django settings (usually set in .env).
    - Uses `certifi` to provide CA certificates (required for MongoDB Atlas).
    - Sets a 5-second server selection timeout to fail fast
      if the database is unreachable.

    Returns
    -------
    MongoClient
        A connected MongoDB client instance.

    Raises
    ------
    RuntimeError
        If `MONGODB_URI` is missing from settings.
    """
    global _client
    if _client is None:
        uri = getattr(settings, "MONGODB_URI", None)
        if not uri:
            raise RuntimeError("MONGODB_URI is missing from settings/.env")

        # Create the client only once and reuse it
        _client = MongoClient(
            uri,
            tlsCAFile=certifi.where(),  # ensures secure TLS connection to Atlas
            serverSelectionTimeoutMS=5000  # fail fast if unreachable
        )
    return _client


def get_db():
    """
    Get (and cache) the target MongoDB database.

    Notes
    -----
    - Calls `get_client()` to ensure a MongoClient is available.
    - Reads `MONGODB_DB_NAME` from Django settings (default: "my_events_backend").
    - Stores the database object globally so it's reused across calls.

    Returns
    -------
    Database
        The MongoDB database object.
    """
    global _db
    if _db is None:
        client = get_client()
        db_name = getattr(settings, "MONGODB_DB_NAME", "my_events_backend")
        _db = client[db_name]
    return _db


def get_events_collection():
    """
    Get the `events` collection from the database.

    Notes
    -----
    - Reads collection name from `MONGODB_EVENTS_COLLECTION`
      in settings (default: "events").

    Returns
    -------
    Collection
        The MongoDB collection object for events.
    """
    name = getattr(settings, "MONGODB_EVENTS_COLLECTION", "events")
    return get_db()[name]


def get_users_collection():
    """
    Get the `users` collection from the database.

    Notes
    -----
    - Reads collection name from `MONGODB_USERS_COLLECTION`
      in settings (default: "users").

    Returns
    -------
    Collection
        The MongoDB collection object for users.
    """
    name = getattr(settings, "MONGODB_USERS_COLLECTION", "users")
    return get_db()[name]


@atexit.register
def _close_client():
    """
    Close the global MongoClient when the Django process exits.

    Notes
    -----
    - Ensures clean shutdown and avoids leaving open sockets.
    - This function is automatically registered via `atexit`
      and called at interpreter exit.
    """
    global _client
    if _client is not None:
        _client.close()
