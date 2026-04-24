from src.logger import get_logger

logger = get_logger(__name__)

MIN_WORDS = 30

def validate_and_clean(text: str) -> str:
    logger.debug(f"validate_and_clean called with text length={len(text)}")
    try:
        if not text or not text.strip():
            raise ValueError("Input text is empty.")
        
        cleaned = text.strip()
        word_count = len(cleaned.split())
        
        if word_count < MIN_WORDS:
            raise ValueError(f"Input too short. Minimum {MIN_WORDS} words required, got {word_count}.")
        
        logger.info(f"Text validated successfully. Word count: {word_count}")
        return cleaned
    
    except ValueError as e:
        logger.error(f"Validation failed: {e}", exc_info=True)
        raise