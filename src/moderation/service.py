from src.utils.robustness import retry_with_backoff

class ModerationService:
    @retry_with_backoff(retries=2, delay=0.5)
    def check_content(self, text: str) -> dict:
        """
        Mock moderation. Flags text containing specific trigger words.
        """
        # Mock logic: Flag if specific keywords are found
        forbidden_keywords = ["violence", "illegal_content", "hate_speech"]
        
        for keyword in forbidden_keywords:
            if keyword in text.lower():
                return {
                    "allowed": False,
                    "flag": f"Detected forbidden category: {keyword}"
                }
        
        # Simulate network latency
        # time.sleep(0.1) 
        
        return {"allowed": True, "flag": None}