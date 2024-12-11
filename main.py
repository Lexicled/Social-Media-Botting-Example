from mistralai import Mistral
from openai import OpenAI
import json

CAMPAIGN = "Fair trade for American workers" # Description of the propaganda to spread
SIDE = "right" # Political alignment (left or right)

# Bet you thought you were getting free API keys lol, not on my watch
MISTRAL_API_KEY = "..."
OPENAI_API_KEY = "..."

# Models, adjust as needed
TXT_MODEL = "mistral-large-latest"
IMG_MODEL = "dall-e-3"

# Prompting - sets political alignment and goals, states task, defines specific output format (JSON)
prompt = f"You are an experienced AI advertiser working for the social media agency of the American government. You are currently working on the following campaign: '{CAMPAIGN}'. Create a prompt for a viral and odd AI generated image with a subtle {SIDE.lower()}-leaning political undertone and a title for the social media post. Output this as a JSON object with 2 properties: 'prompt' and 'title'."

txt_client = Mistral(api_key=MISTRAL_API_KEY)
img_client = OpenAI(api_key=OPENAI_API_KEY)

def post(img_url, title):
    pass # Post to socials e.g. Instagram, Facebook, etc.

# Get image prompt and title from Mistral
messages = [
    {
        "role": "user",
        "content": prompt,
    }
]
chat_response = txt_client.chat.complete(
      model = TXT_MODEL,
      messages = messages,
      response_format = {
          "type": "json_object",
      }
)

# Decode Mistral's output
decoder = json.decoder.JSONDecoder()
json_response = decoder.decode(chat_response.choices[0].message.content)
img_prompt = json_response["prompt"]
post_title = json_response["title"]

# Generate the image with OpenAI's DALL-E 3
response = img_client.images.generate(
    model=IMG_MODEL,
    prompt=img_prompt,
    size="1024x1024",
    quality="standard",
    n=1,
)
image_url = response.data[0].url

post(image_url, post_title) # Post the AI image to all socials with the previously generated title