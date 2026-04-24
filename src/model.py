from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL, MAX_TOKENS, TEMPERATURE
from src.logger import get_logger

logger = get_logger(__name__)

client = Groq(api_key=GROQ_API_KEY)


def generate(prompt: str) -> str:
    logger.debug(f"generate called with prompt length={len(prompt)}")
    try:
        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE
        )

        output = response.choices[0].message.content.strip()
        logger.info(f"Generation successful. Output length={len(output)}")
        return output

    except Exception as e:
        logger.error(f"Groq API call failed: {e}", exc_info=True)
        raise