import gradio as gr
from src.predict import run_pipeline
from src.logger import get_logger

logger = get_logger(__name__)


def repurpose(text: str, format: str) -> str:
    logger.info(f"App received request for format={format}")
    try:
        result = run_pipeline(text, format)
        return result
    except ValueError as e:
        logger.error(f"Validation error: {e}", exc_info=True)
        return f"Error: {str(e)}"
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        return "Something went wrong. Check logs for details."


with gr.Blocks(title="AI Content Repurposer") as app:
    gr.Markdown("# AI Content Repurposer")
    gr.Markdown("Paste any long-form text and repurpose it into LinkedIn Post, Twitter Thread, or Executive Summary.")

    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(
                label="Paste your content here",
                placeholder="Paste your article, blog post, or notes...",
                lines=10
            )
            format_choice = gr.Radio(
                choices=["LinkedIn Post", "Twitter Thread", "Executive Summary"],
                label="Select output format",
                value="LinkedIn Post"
            )
            submit_btn = gr.Button("Repurpose", variant="primary")

        with gr.Column():
            output_text = gr.Textbox(
                label="Repurposed Output",
                lines=10
            )

    submit_btn.click(
        fn=repurpose,
        inputs=[input_text, format_choice],
        outputs=output_text
    )

if __name__ == "__main__":
    logger.info("Starting AI Content Repurposer app")
    app.launch()