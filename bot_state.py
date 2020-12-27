

class State():
   def __init__(self):
      self.lang = 'NOT_SET'
      self.now = 0
      
   def set_lang(self, lang):
      if lang in ('рус','укр', 'NOT_SET'):
         self.lang = lang
   
   _reset = 0

   _start = 100
   

   def change(self, bot_state):
      self.now = bot_state


   def is_now(self, bot_state):
      return self.now == bot_state

if __name__ == '__main__':
   pass