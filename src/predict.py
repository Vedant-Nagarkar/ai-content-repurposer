from src.logger import get_logger
from src.data import validate_and_clean
from src.features import build_prompt
from src.model import generate
from src.evaluate import evaluate_output

logger = get_logger(__name__)


def run_pipeline(text: str, format: str) -> str:
    logger.debug(f"run_pipeline called with format={format}")
    try:
        # Step 1 - Validate and clean input
        cleaned_text = validate_and_clean(text)

        # Step 2 - Build prompt
        prompt = build_prompt(cleaned_text, format)

        # Step 3 - Generate output
        output = generate(prompt)

        # Step 4 - Evaluate output
        evaluate_output(output, format)

        logger.info(f"Pipeline completed successfully for format={format}")
        return output

    except Exception as e:
        logger.error(f"Pipeline failed: {e}", exc_info=True)
        raise