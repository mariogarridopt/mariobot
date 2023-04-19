import openai
import time

class aibot():
  def __init__(self, api_key):
      self.prompt = ""
      openai.api_key = api_key
      
  def init_ai_prompt(self):
    return "The following is a conversation with an AI assistant named MarioBot. The assistant is helpful, creative, clever, funny, and very friendly.\n\n"

  def ask_ai(self, question):    
    self.prompt = self.init_ai_prompt() + "\nHuman: " + str(question) + "\nAI:"
    
    try:
      response = openai.Completion.create(
        model="text-davinci-003",
        prompt=self.prompt,
        temperature=0.9,
        max_tokens=10,
        top_p=1,
        n=1,
        stream=False,
        frequency_penalty=0.0,
        presence_penalty=0.6
      )
      
      return response.choices[0].text
    except Exception as e:
      print(e)
      return "MarioBot is now sleeping, please try later... :zzz: :zzz: :zzz:"
