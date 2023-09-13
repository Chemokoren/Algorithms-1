"""
Facade design pattern
- Exposing several components through a single interface

Motivation
----------
- Balancing complexity and presentation/usability
- In a typical home there are:
    - many subsytems(electrical, sanitation)
    - Complex internal structure e.g. floor layers
    - end user is not exposed to internals
- Same happens with software
    - Many systems working to provide flexibility
    - API consumers want it to 'just work'
    
Facade provides a simple, easy to understand/user interface over a large and 
sophisticated body of code.

Summary:
- Build a Facade to provide a simplified API over a set of classes
- May wish to (optionally) expose internals through the facade
- May allow users to 'escalate' to use more complex APIs if they need to

"""
class Buffer:
  def __init__(self, width=30, height=20):
    self.width = width
    self.height = height
    self.buffer = [' '] * (width*height)

  def __getitem__(self, item):
    return self.buffer.__getitem__(item)

  def write(self, text):
    self.buffer += text

class Viewport:
  def __init__(self, buffer=Buffer()):
    self.buffer = buffer
    self.offset = 0

  def get_char_at(self, index):
    return self.buffer[self.offset+index]

  def append(self, text):
    self.buffer += text

class Console:
  def __init__(self):
    b = Buffer()
    self.current_viewport = Viewport(b)
    self.buffers = [b]
    self.viewports = [self.current_viewport]

  # high-level
  def write(self, text):
    self.current_viewport.buffer.write(text)

  # low-level
  def get_char_at(self, index):
    return self.current_viewport.get_char_at(index)


if __name__ == '__main__':
  c = Console()
  c.write('hello')
  ch = c.get_char_at(3)
  print(ch)