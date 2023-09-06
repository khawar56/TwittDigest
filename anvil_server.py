from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.http

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def text_area_1_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
    pass

  def text_area_2_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
    pass

  def button_1_click(self, **event_args):
    prompts = anvil.server.call('send_prompts')
    self.text_area_1.text = prompts['world'] 
    self.text_area_2.text = prompts['sports'] 
    self.text_area_3.text = prompts['buisness'] 
    self.text_area_4.text = prompts['science'] 

  def button_2_click(self, **event_args):
    rejects = anvil.server.call('send_filtered_out_tweets')
    self.text_area_5.text = rejects
    # tweet1 = rejects[0]
    # tweet2 = rejects[1]
    # self.text_area_5.text = tweet1 + '\n' +tweet2
      

    



