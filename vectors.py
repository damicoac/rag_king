import numpy as np
import tiktoken
from sentence_transformers import SentenceTransformer
from numpy.linalg import norm
import hashlib

def num_tokens_from_string(string: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding("cl100k_base")
    num_tokens = len(encoding.encode(string))
    return num_tokens

def num_tokens_from_messages(messages):
    """Returns the number of tokens used by a list of messages."""
    encoding = tiktoken.get_encoding("cl100k_base")
    num_tokens = 0
    for message in messages:
        num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":  # if there's a name, the role is omitted
                num_tokens += -1  # role is always required and always 1 token
    num_tokens += 2  # every reply is primed with <im_start>assistant
    return num_tokens

def find_matches(query_vector, dataset_dict):
    matches_to_return = []
    for key in dataset_dict:
        value = dataset_dict[key]
        match_value = cosine_similarity(query_vector, value['vector'])
        if match_value > 0.5: #right now this only cares about matches greater than .5
            matches_to_return.append(key)

    return matches_to_return


def make_vector_from_text(text):
    model_path = "location of nomic-embed-text-v1.5 directory" # TODO update this to the directory of your nomic-embed-test directory
    embedder = SentenceTransformer(model_path, trust_remote_code=True)
    embedding = embedder.encode(text, convert_to_numpy=True).tolist()
    return embedding
    
def cosine_similarity(a, b):
    """
    Calculates the cosine similarity between two vectors.

    Parameters:
    a (numpy.ndarray): The first vector.
    b (numpy.ndarray): The second vector.

    Returns:
    float: The cosine similarity between the two vectors.
    """
    return np.dot(a, b)/(norm(a)*norm(b))

def chunkifier(item_in_dataset, dataset_dict, text):
    # this is where chunking happens. right now it is set to chunk every 2000 characters with a 1000 character overlap. in general, 4 characters is a token.
    front_index = 0
    back_index = 2000
    total_length = len(text)
    while back_index < total_length:
        new_item_dict = item_in_dataset
        guid = hashlib.sha256(text[front_index:back_index].encode(encoding="UTF-8")).hexdigest()
        new_item_dict['id'] = guid
        vector = make_vector_from_text(text[front_index:back_index])
        new_item_dict['vector'] = vector
        new_item_dict['chunk'] = text[front_index:back_index]
        front_index += 1000
        back_index += 1000
        dataset_dict[new_item_dict['id']] = new_item_dict

def main():
    print("TESTING")

    print("COMPELTE")

if __name__ == "__main__":
    main()
