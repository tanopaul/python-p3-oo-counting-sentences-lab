#!/usr/bin/env python3

class MyString:
  
  def __init__(self, value=''):
    self.value = value

  def get_value(self):
    return self._value
  
  def set_value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print('The value must be a string.')
  
  value = property(get_value, set_value)

  def is_sentence(self):
    if self.value[-1] == '.':
      return True
    else:
      return False
    
  def is_question(self):
    if self.value[-1] == '?':
      return True
    else:
      return False
    
  def is_exclamation(self):
    if self.value[-1] == '!':
      return True
    else:
      return False
    
  def count_sentences(self):
    count = 0
    prev_char = None
    for char in self.value:
      if prev_char is not char:
        if char == '!' or char == '.' or char == '?':
          count += 1
      prev_char = char

    return count
