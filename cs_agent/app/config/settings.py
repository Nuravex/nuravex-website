import os


class Settings:
    """
    Application configuration loaded from environment variables.
    """

    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "claude-sonnet-4-5-20250929"
    )

    TEMPERATURE = float(
        os.getenv("TEMPERATURE", 0.3)
    )


settings = Settings()