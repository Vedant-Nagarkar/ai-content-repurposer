from src.logger import get_logger

logger = get_logger(__name__)

MIN_OUTPUT_WORDS = 20


def evaluate_output(output: str, format: str) -> dict:
    logger.debug(f"evaluate_output called for format={format}")
    try:
        if not output or not output.strip():
            raise ValueError("Model returned empty output.")

        word_count = len(output.strip().split())

        if word_count < MIN_OUTPUT_WORDS:
            raise ValueError(f"Output too short: {word_count} words for format={format}")

        result = {
            "format": format,
            "word_count": word_count,
            "char_count": len(output),
            "passed": True
        }

        logger.info(f"Output evaluation passed for format={format}. Words={word_count}")
        return result

    except ValueError as e:
        logger.error(f"Evaluation failed: {e}", exc_info=True)
        raise