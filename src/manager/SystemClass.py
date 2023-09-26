from abc import ABC
from src.util.Gettable import Gettable

# Just a class to anotate a system to anotate the systems  
# that can be managed for a FeedbackLoop
class SystemClass(Gettable,ABC):
    pass