import asyncio
import random

class AIModelService:
    @staticmethod
    async def analyze_image():
         # Simulate image loading + AI inference delay

        await asyncio.sleep(4)
        
        # Return dummy prediction
        return {
            "filename": f"image{random.randint(1, 50)}.png",
            "bee_count": random.randint(1, 50),
            "confidence": round(random.uniform(0.85, 0.99), 2)
        }        