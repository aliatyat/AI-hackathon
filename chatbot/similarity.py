from sentence_transformers import SentenceTransformer, util
import json
import re

def normalize_question(text):
    # Add space between digits and letters
    text = re.sub(r'(\d)([A-Za-z])', r'\1 \2', text)
    text = re.sub(r'([A-Za-z])(\d)', r'\1 \2', text)
    return text

# Load the transformer model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def is_similar_question(user_question, json_path, threshold=0.8):
    # Load prompts from the JSON file
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Extract "prompt" fields
    prompts = [normalize_question(item['prompt']) for item in data]
    user_question = normalize_question(user_question)
    # Encode user question and stored prompts
    user_embedding = model.encode(user_question, convert_to_tensor=True)
    prompt_embeddings = model.encode(prompts, convert_to_tensor=True)

    # Compute cosine similarities
    cosine_scores = util.cos_sim(user_embedding, prompt_embeddings)[0]

    # Check if any similarity score is above the threshold
    return any(score >= threshold for score in cosine_scores)

# result = is_similar_question("Tell me about 42Amman", "data.json", threshold=0.75)
# print(result)
# result = is_similar_question("Tell me about 42 Amman", "data.json", threshold=0.75)
# print(result)
# result = is_similar_question("What's 42Amman", "data.json", threshold=0.75) 
# print(result)
# result = is_similar_question("What's 42 Amman", "data.json", threshold=0.75) 
# print(result)