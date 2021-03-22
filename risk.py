def info():  
    '''Prints a basic library description'''
    print("Software library for the Online Risk project.")

def detect_tag():
    print("No tag detected")
    return False

def read_tag():
    print("Error reading tag info")
    return False
    
def display_on():
    print("Display turned ON")
    
def display_off():
    print("Display turned OFF")
    
def clear_display():
    print("Display cleared")
    
def text_to_display(text):
    print(text)
    
def i2c_send_output(addr,out):
    print(out + " sent to " + addr)
    
def i2c_read_input(addr):
    print("reading from " + addr)
    
def buzz(dur):
    print("Buzzer buzzing for " + dur + seconds)
