import os


class Settings:
    """
    Application configuration loaded from environment variables.
    """

    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "gemma3:1b"
    )

    TEMPERATURE = float(
        os.getenv("TEMPERATURE", 0.3)
    )


settings = Settings()