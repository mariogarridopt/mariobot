import openai
import time

class aibot():
  def __init__(self, api_key):
      self.prompt = ""
      self.last_generated_time = None
      openai.api_key = api_key
      
  def init_ai_prompt(self):
    return "The following is a conversation with an AI assistant named MarioBot. The assistant is helpful, creative, clever, funny, and very friendly.\n\n"

  def ask_ai(self, question):
    if openai.api_key == '':
      return ''

    if self.last_generated_time is None or (time.time() - self.last_generated_time) > 900:
      self.clear_conversation()
    
    if self.prompt == "" :
        self.prompt = self.init_ai_prompt()
      
    self.prompt = self.prompt + "\nHuman: " + str(question) + "\nAI:"
    
    try:
      response = openai.Completion.create(
        model="text-davinci-003",
        prompt=self.prompt,
        temperature=0.9,
        max_tokens=550,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6
      )
      
      self.prompt = self.prompt + response.choices[0].text
      print(self.prompt)

      return response.choices[0].text
    except Exception as e:
      print(e)
      return "MarioBot is now sleeping, please try later... :zzz::zzz::zzz:"
    
  def clear_conversation(self):
    self.prompt = ""