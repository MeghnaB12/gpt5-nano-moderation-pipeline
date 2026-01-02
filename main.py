import sys
import logging
from src.utils.pdf_loader import extract_text_from_pdf
from src.moderation.service import ModerationService
from src.llm.service import GPT5NanoService

# Setup
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def run_pipeline(pdf_path: str):
    logger.info("--- Starting GPT-5-Nano Pipeline ---")
    
    # 1. Accept input text via PDF
    try:
        logger.info(f"Loading PDF: {pdf_path}")
        raw_text = extract_text_from_pdf(pdf_path)
        if not raw_text.strip():
            logger.error("PDF is empty or text could not be extracted.")
            return
    except Exception as e:
        logger.error(f"Input Error: {e}")
        return

    # 2. Pass through Moderation
    mod_service = ModerationService()
    logger.info("Sending to Moderation...")
    mod_result = mod_service.check_content(raw_text)

    # 3. Check Flags
    if not mod_result["allowed"]:
        logger.warning("Pipeline Halted: Content Flagged.")
        print({
            "allowed": False,
            "flag": mod_result["flag"]
        })
        return

    # 4. Pass to GPT-5-Nano
    logger.info("Moderation passed. Sending to GPT-5-Nano...")
    llm_service = GPT5NanoService()
    try:
        response = llm_service.generate_response(raw_text)
        print("\n--- Final Output ---")
        print(response)
    except Exception as e:
        logger.error(f"LLM Generation Failed: {e}")

if __name__ == "__main__":
    # Example usage: python main.py document.pdf
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_pdf>")
    else:
        run_pipeline(sys.argv[1])