import tiktoken # type: ignore

encoder = tiktoken.encoding_for_model("gpt-4")

# print("vocabulary size:", encoder.n_vocab)


text = "t"
tokens = encoder.encode(text)
print("Tokens:", tokens)


decoded = encoder.decode(text)
print("Decoded:", decoded)

  