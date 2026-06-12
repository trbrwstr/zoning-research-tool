from openai import AsyncOpenAI
from typing import Dict, Optional
import logging
import json
from app.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AIInterpretationService:
    """
    Uses GPT-4 to interpret zoning codes and provide human-readable summaries.
    """
    
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
    
    async def interpret_zoning_data(self, raw_data: Dict) -> Dict:
        """
        Interpret raw zoning data and provide a comprehensive summary.
        
        Args:
            raw_data: Raw zoning data from scraping
            
        Returns:
            Dictionary with interpreted zoning information
        """
        try:
            prompt = self._build_interpretation_prompt(raw_data)
            
            response = await self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert in municipal zoning codes and land use regulations. Your task is to interpret zoning data and provide clear, actionable summaries for real estate developers, architects, and contractors."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,
                response_format={"type": "json_object"}
            )
            
            result = json.loads(response.choices[0].message.content)
            logger.info("Successfully interpreted zoning data with GPT-4")
            return result
            
        except Exception as e:
            logger.error(f"Error interpreting zoning data: {e}")
            return self._get_fallback_interpretation(raw_data)
    
    def _build_interpretation_prompt(self, raw_data: Dict) -> str:
        """Build the prompt for GPT-4 interpretation."""
        prompt = f"""
Analyze the following zoning data and provide a comprehensive interpretation:

Raw Zoning Data:
{json.dumps(raw_data, indent=2)}

Please provide a JSON response with the following structure:
{{
    "summary": "A brief 2-3 sentence summary of the zoning classification",
    "zoning_code": "The zoning code designation",
    "permitted_uses": ["List of primary permitted uses"],
    "conditional_uses": ["List of conditional uses with conditions"],
    "prohibited_uses": ["List of prohibited uses"],
    "setback_requirements": {{
        "front": "Front setback requirement",
        "rear": "Rear setback requirement",
        "side": "Side setback requirement",
        "notes": "Any additional setback notes"
    }},
    "height_restrictions": {{
        "maximum_height": "Maximum building height",
        "stories": "Maximum number of stories",
        "notes": "Any additional height restrictions"
    }},
    "lot_coverage": {{
        "maximum_coverage": "Maximum lot coverage percentage",
        "impervious_surface": "Impervious surface limits",
        "open_space": "Open space requirements"
    }},
    "parking_requirements": {{
        "residential": "Parking spaces per residential unit",
        "commercial": "Parking spaces per square foot",
        "notes": "Additional parking requirements"
    }},
    "development_standards": ["List of key development standards"],
    "potential_issues": ["List of potential issues or restrictions to be aware of"],
    "recommendations": ["List of recommendations for development"]
}}
"""
        return prompt
    
    def _get_fallback_interpretation(self, raw_data: Dict) -> Dict:
        """Provide a fallback interpretation if AI fails."""
        return {
            "summary": "Unable to interpret zoning data automatically. Please review raw data.",
            "zoning_code": raw_data.get("zoning_code", "Unknown"),
            "permitted_uses": [],
            "conditional_uses": [],
            "prohibited_uses": [],
            "setback_requirements": {
                "front": raw_data.get("setbacks", "Not specified"),
                "rear": "Not specified",
                "side": "Not specified",
                "notes": ""
            },
            "height_restrictions": {
                "maximum_height": raw_data.get("height_limits", "Not specified"),
                "stories": "Not specified",
                "notes": ""
            },
            "lot_coverage": {
                "maximum_coverage": raw_data.get("coverage", "Not specified"),
                "impervious_surface": "Not specified",
                "open_space": "Not specified"
            },
            "parking_requirements": {
                "residential": "Not specified",
                "commercial": "Not specified",
                "notes": ""
            },
            "development_standards": [],
            "potential_issues": ["AI interpretation unavailable"],
            "recommendations": ["Review raw zoning data manually"]
        }
    
    async def answer_zoning_question(self, context: Dict, question: str) -> str:
        """
        Answer specific questions about zoning based on context.
        
        Args:
            context: Existing zoning data and interpretations
            question: User's specific question
            
        Returns:
            Answer to the question
        """
        try:
            prompt = f"""
Based on the following zoning information, answer the user's question:

Zoning Context:
{json.dumps(context, indent=2)}

User Question: {question}

Provide a clear, concise answer with specific references to the zoning code where applicable.
"""
            
            response = await self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a zoning code expert. Provide accurate, helpful answers to zoning questions."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            logger.error(f"Error answering zoning question: {e}")
            return "I'm unable to answer that question at this time. Please consult the raw zoning data or contact local zoning officials."
