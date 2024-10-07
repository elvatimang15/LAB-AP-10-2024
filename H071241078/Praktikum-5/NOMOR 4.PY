def generate_substrings(s):
  substrings = []
  for sub_len in range(1, len(s) + 1):
    for start_index in range(len(s) - sub_len + 1):
      substrings.append(s[start_index:start_index + sub_len]) 
  return substrings 

# Get input from the user
input_string = input("Input your string: ")

# Generate and print all substrings
substrings = generate_substrings(input_string)
for substring in substrings:
  print(substring)