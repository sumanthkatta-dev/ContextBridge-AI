from server import retrieve_documents

print("Testing retrieve_documents function...")
result = retrieve_documents("sample.txt", n_results=2)
print("Result:")
print(result)
