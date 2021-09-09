import enum

class GENERAL(enum.Enum):
    MAX_IMAGE_PER_RUN = "max_image_per_run"
    MAX_IMAGES = "max_images"

class AUTHENTICATION(enum.Enum):
    REDDIT = "reddit_secret_location"

class LOCATION(enum.Enum):
    STORAGE_LOCATION = "storage_location"
    CONFIGURATION_LOCATION = "configuration_location"

class INTERVAL(enum.Enum):
    HOUR = "hour"
    DAY = "day"

class FILTER:
    class RESOLUTION:
        RESOLUTION_MIN = "resolution_min"
        RESOLUTION_MAX = "resolution_max"

    class REDDIT:
        SUBREDDITS = "subreddits"
