from .atri import Atri
from fastapi import Request, Response
from atri_utils import *

def init_state(at: Atri):
    """
    This function is called everytime "Publish" button is hit in the editor.
    The argument "at" is a dictionary that has initial values set from visual editor.
    Changing values in this dictionary will modify the intial state of the app.
    """
    at.TextBox3.custom.text = ""
    pass

def handle_page_request(at: Atri, req: Request, res: Response, query: str):
    """
    This function is called whenever a user loads this route in the browser.
    """
    at.TextBox3.custom.text = ""
    pass

def handle_event(at: Atri, req: Request, res: Response):
    """
    This function is called whenever an event is received. An event occurs when user
    performs some action such as click button.
    """

    if at.Button1.onClick:
        num1 = int(at.Input1.custom.value)
        num2 = int(at.Input2.custom.value)
        at.TextBox3.custom.text = num1 + num2

    if at.Button2.onClick:
        num1 = int(at.Input1.custom.value)
        num2 = int(at.Input2.custom.value)
        at.TextBox3.custom.text = num1 - num2

    if at.Button3.onClick:
        num1 = int(at.Input1.custom.value)
        num2 = int(at.Input2.custom.value)
        at.TextBox3.custom.text = num1 * num2
    
    if at.Button4.onClick:
        num1 = int(at.Input1.custom.value)
        num2 = int(at.Input2.custom.value)
        at.TextBox3.custom.text = round(num1 / num2, 2)

    if at.Button5.onClick:
        at.TextBox3.custom.text = ""
        at.Input1.custom.value = ""
        at.Input2.custom.value = ""
        
    pass