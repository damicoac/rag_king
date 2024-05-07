import json



# in the root dir of this project there will be a json file. 
# it will be an array of chunks

# example chunks
# # Assuming you have several chunk_dict objects like this:
# chunk_dict1 = {
#     "id": 12345,
#     "file_name": "example.txt",
#     "chunk": b"This is chunk data 1",
#     "vector": np.array([0.1, 0.5, -0.2])
# }

# chunk_dict2 = {
#     "id": 67890,
#     "file_name": "another_file.pdf",
#     "chunk": b"Different chunk data",
#     "vector": np.array([0.8, -0.3, 0.6])
# }
# # ... and so on

# # Create the master dictionary
# chunks_by_id = {
#     chunk_dict1["id"]: chunk_dict1,
#     chunk_dict2["id"]: chunk_dict2
#     # ... add more chunk dictionaries here
# }

# # Accessing a chunk
# print(chunks_by_id[12345])  # This would print chunk_dict1


def write_to_file(datasets):
    # if you want to change the name of the knoweldge base file, programatically or other wise. these funtions are where you do it.
    with open('knoweldge_base.json', 'w') as f:
        json.dump(datasets, f)

def load_json_file():
    with open('knoweldge_base.json') as f:
        data = json.load(f)
    return data

def main():
    print("TESTING")

    print("COMPELTE")

if __name__ == "__main__":
    main()
