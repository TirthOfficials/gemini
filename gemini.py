import google.generativeai as genai

# Configure your API key (replace with your actual API key)
genai.configure(api_key="YOUR_API")

def generate_response(model_name, prompt, temperature):
  """Generates a response from Gemini."""
  model = genai.GenerativeModel(model_name)
  response = model.generate_content(prompt, generation_config=genai.GenerationConfig(temperature=temperature))
  return response.text

# Example usage (participants will modify this section)
model_name = "gemini-2.0-flash"  # Or "gemini-ultra" if you have access.
prompt = "Write a short poem about a cat."
temperature = 0.7

response_text = generate_response(model_name, prompt, temperature)
print(response_text)

# Participants can modify model_name, prompt, and temperature