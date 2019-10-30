import logging

try:
    from config import KAFKA_USER, KAFKA_SERVER, KAFKA_PASSWORD  # noqa F401
except ModuleNotFoundError:
    raise Exception(
        'Please provide the login credentials in a config.py (Template available in config.py.dist)') from None

console = logging.StreamHandler()
console.setFormatter(logging.Formatter('%(asctime)s %(levelname)s [%(name)s]: %(message)s', "%Y-%m-%d %H:%M:%S"))
root = logging.getLogger()
root.handlers.clear()
root.addHandler(console)

# Configure logglevels
logging.getLogger().setLevel(logging.WARNING)
logging.getLogger("ftfbroker").setLevel(logging.DEBUG)
