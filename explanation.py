from openai import OpenAI

client = OpenAI()

def generate_explanation(change, drivers):

    prompt = f"""
KPI change: {change}

Drivers:
{drivers}

Explain the change in simple financial terms.
"""

    resp = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return resp.output_text