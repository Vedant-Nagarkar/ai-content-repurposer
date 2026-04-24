from src.logger import get_logger

logger = get_logger(__name__)


def build_prompt(text: str, format: str) -> str:
    logger.debug(f"build_prompt called with format={format}")

    if format == "LinkedIn Post":
        prompt = _role_prompt(text)
    elif format == "Twitter Thread":
        prompt = _few_shot_prompt(text)
    elif format == "Executive Summary":
        prompt = _cot_prompt(text)
    else:
        raise ValueError(f"Unknown format: {format}")

    logger.info(f"Prompt built for format: {format}")
    return prompt


def _role_prompt(text: str) -> str:
    return f"""You are a senior LinkedIn thought leader with 20 years of industry experience.
You write posts that are insightful, professional, and drive engagement.
Your posts always start with a strong hook, use short paragraphs, and end with a question or call to action.

Repurpose the following content into a LinkedIn post:

{text}

LinkedIn Post:"""


def _few_shot_prompt(text: str) -> str:
    return f"""Convert content into a Twitter thread. Each tweet must be under 280 characters and numbered.

Example 1:
Content: AI is transforming healthcare by enabling faster diagnosis and personalized treatment plans.
Thread:
1/ AI is changing healthcare forever. Here's how 🧵
2/ Doctors now use AI to detect diseases earlier than ever before.
3/ Personalized treatment plans are being built using patient data + ML models.
4/ The result? Better outcomes, faster recovery, lower costs.

Example 2:
Content: Remote work has changed how teams collaborate, communicate, and maintain culture.
Thread:
1/ Remote work didn't kill company culture. It just changed it 🧵
2/ Teams now rely on async communication more than ever.
3/ Tools like Notion, Slack, and Loom replaced the office whiteboard.
4/ The best remote teams over-communicate and document everything.

Now convert this content into a Twitter thread:
{text}

Thread:"""


def _cot_prompt(text: str) -> str:
    return f"""You are creating an executive summary. Think step by step before writing.

Step 1: Identify the core topic of the content.
Step 2: Extract the 3 most important points.
Step 3: Identify any key data, results, or conclusions mentioned.
Step 4: Write a concise executive summary in 3-5 sentences for a senior business audience.

Content:
{text}

Now follow the steps and write the executive summary:"""