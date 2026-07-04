import os
import json

from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_groq import ChatGroq

load_dotenv()

# =====================================================
# LLM
# =====================================================

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0,
)

# =====================================================
# SIMPLE CALL
# =====================================================

def call_llm(
    system_prompt: str,
    user_prompt: str,
) -> str:

    response = llm.invoke(
        [
            ("system", system_prompt),
            ("human", user_prompt),
        ]
    )

    return response.content


# =====================================================
# STRUCTURED CALL
# =====================================================

def call_structured(
    system_prompt: str,
    user_prompt: str,
    schema: type[BaseModel],
):

    schema_json = json.dumps(
        schema.model_json_schema(),
        indent=2
    )

    response = llm.invoke(
        [
            (
                "system",
                f"""
{system_prompt}

Return ONLY valid JSON matching the schema below.
If you can't complete all fields, use sensible defaults or omit optional fields.

JSON SCHEMA:

{schema_json}
"""
            ),
            ("human", user_prompt),
        ]
    )

    content = response.content.strip()

    try:
        start = content.find("{")
        end = content.rfind("}") + 1

        if start == -1 or end == 0:
            raise ValueError("No JSON object found in response")

        json_text = content[start:end]

        # Try to parse and validate
        try:
            return schema.model_validate_json(json_text)
        except json.JSONDecodeError:
            # If JSON is invalid, try to fix common issues
            # Fix unclosed strings by removing trailing incomplete strings
            try:
                parsed = json.loads(json_text)
                return schema.model_validate(parsed)
            except:
                # Last resort: return schema with defaults
                return schema()

    except Exception as e:

        print("\n======================")
        print("STRUCTURED OUTPUT ERROR")
        print("======================\n")
        print(content)
        print("\nUsing schema defaults due to parsing error")
        print("======================\n")

        # Return schema with default values instead of failing
        return schema()