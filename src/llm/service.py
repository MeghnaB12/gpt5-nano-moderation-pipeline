from src.utils.robustness import retry_with_backoff

class GPT5NanoService:
    @retry_with_backoff(retries=3, delay=1)
    def generate_response(self, prompt: str) -> str:
        """
        Mock GPT-5-Nano generation.
        """
        # Simulate processing limit (Truncation for safety)
        safe_prompt = prompt[:1000] 
        
        # Mock Response
        return (
            f"GPT-5-Nano Response:\n"
            f"Based on your input PDF, I have analyzed the content. "
            f"Here is a summary of the first 50 chars: '{safe_prompt[:50]}...'"
            f"\n[Analysis Complete]"
        )