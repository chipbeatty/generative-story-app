from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = input("Enter a story prompt: ")
story = generator(prompt, max_length=100, num_return_sequences=1)

print("\nGenerated Story:")
print(story[0]['generated_text'])