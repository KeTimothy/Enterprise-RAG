from app.services.embeddings import embedding_service

text = "Employees are entitled to 14 days of annual leave."

embedding = embedding_service.embed_text(text)

print(type(embedding))  # Should print: <class 'list'>
print(len(embedding))  # Should print the length of the embedding vector
print(embedding[:10])  # Should print the first 10 elements of the embedding vector