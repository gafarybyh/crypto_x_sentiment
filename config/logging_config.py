
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_PATH = "./logs/app.log"

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": LOG_FORMAT
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": "DEBUG"
        },
        "file": {
            "class": "logging.FileHandler",
            "formatter": "standard",
            "level": "INFO",
            "filename": LOG_PATH
        }
    },
    "loggers": {
        "": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": False
        },
        
        # 🔧 Limit log from external library
        # Level (DEBUG 10, INFO 20, WARNING 30, ERROR 40, CRITICAL 50)	
        # "telegram": {"level": "INFO", "propagate": False}, # Only INFO until CRITICAL level on telegram library
        "asyncio": {"level": "INFO", "propagate": False},
        "tzlocal": {"level": "INFO", "propagate": False},
        "httpx": {"level": "INFO", "propagate": False},
        "httpcore": {"level": "INFO", "propagate": False},
        "twikit": {"level": "INFO", "propagate": False},
        "google-generativeai": {"level": "INFO", "propagate": False}, 
        "matplotlib": {"level": "INFO", "propagate": False}, 
        "PIL.PngImagePlugin": {"level": "INFO", "propagate": False}, 
    }
}

