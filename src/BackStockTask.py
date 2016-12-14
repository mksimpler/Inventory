from vocollect_core.task.task import TaskBase
from vocollect_core.dialog.functions import prompt_only, prompt_ready
from vocollect_core.utilities.localization import itext

from LutOdr import InventoryLut
from vocollect_lut_odr.receivers import StringField, NumericField

import errno

REQUEST_STOCK = 'requestBackStock'
QUANTITY_PROMPT = 'quantityPrompt'

class BackStockTask(TaskBase):
    def __init__(self, location, taskRunner = None, callingTask = None):
        super(BackStockTask, self).__init__(taskRunner, callingTask)
        
        self.name = 'taskQuery'
        self._location = location
        
        self._queryLut = InventoryLut('LUTBackStock',
                                      StringField('Location'),
                                      NumericField('Quantity'))
        
    def initializeStates(self):
        self.addState(REQUEST_STOCK, self.request_stock)
        self.addState(QUANTITY_PROMPT, self.quantity_prompt)
    
    def request_stock(self):
        err = self._queryLut.send(self._location)
        
        if err == 0:
            self._quantity = 0
            for data in self._queryLut.get_data():
                self._quantity += data['Quantity']
                
        elif err == errno.ECONNREFUSED:
            prompt_ready(itext('error.connection.refused'), True)
            self.next_state = REQUEST_STOCK
        
        elif err == errno.ETIMEDOUT:
            prompt_ready(itext('error.connection.timeout'), True)
            self.next_state = REQUEST_STOCK
            
    def quantity_prompt(self):
        prompt_only(itext('backstock.quantity', str(self._quantity)))