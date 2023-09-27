"""Define the start up events and shut down events.

Please be aware that you can define multiple events and add them to the FastAPI
instance, and the adding order decides the executing order.
"""
import logging
from ..configs import get_settings
from ..db.init_db import flash_contents
from ..db import Base, engine

settings = get_settings()
logger = logging.getLogger(settings.PROJECT_SLUG)


async def startup_db_handler() -> None:
    """startup event, it will be executed before the app is ready to create
    tables in DB and flash contents to DB."""
    logger.info("Creating all tables in DB ...")
    Base.metadata.create_all(engine)  # type: ignore
    logger.info("Flashing contents to DB ...")
    flash_contents()


async def shutdown_db_handler() -> None:
    """shutdown event, it will be executed before the app is shutting
    down to clean the DB."""
    logger.info("Dropping all tables in DB ...")
    Base.metadata.drop_all(engine)  # type: ignore
