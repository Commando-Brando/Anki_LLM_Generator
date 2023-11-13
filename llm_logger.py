import logging


def has_stream_handler(logger):
    """Check if the given logger has a StreamHandler.

    Arguments:
        logger: The logger to check.

    Returns:
        True if the logger has a StreamHandler, False otherwise.
    """
    return any(
        isinstance(handler, logging.StreamHandler) for handler in logger.handlers
    )


LOGGER_NAME = "LLM"
