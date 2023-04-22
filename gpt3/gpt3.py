import openai
openai.api_key = "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"

# # list models
# models = openai.Model.list()
#
# # print the first model's id
#
#
# # create a completion
# completion = openai.Completion.create(model="gpt-3.5-turbo", prompt="give me some financial words, and translate with english")
#
# # print the completion
# print(completion.choices[0].text)
#
# import openai
# openai.api_key = "sk-..."  # supply your API key however you choose

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "帮我写首诗吧，杜甫风格的七言律诗"}])
print(completion.choices[0].message.content)