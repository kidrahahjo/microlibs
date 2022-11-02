import logging
from typing import Any, Callable, Coroutine

logger = logging.getLogger(__name__)

AsyncFunction = Callable[..., Coroutine[Any, Any, Any]]


def retryable(max_tries: int = 2) -> Callable[[AsyncFunction], AsyncFunction]:
    def decorate(func: AsyncFunction) -> AsyncFunction:
        async def _func(*args: Any, **kwargs: Any) -> Any:
            for i in range(max_tries):
                try:
                    logger.debug("[MICROLIBS]: Trying to execute the function!")
                    return await func(*args, **kwargs)
                except Exception as err:
                    logger.debug(
                        "[MICROLIBS]: Failed to execute, retrying!",
                        extra={"err_message": err.__cause__, "retry_attempt": i},
                    )
                    if i == max_tries - 1:
                        logger.debug("[MICROLIBS]: Cannot execute the function!")
                        raise

        return _func

    return decorate
