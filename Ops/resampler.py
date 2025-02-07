'''===================================================================
Copyright 2019 Matthias Komm, Vilius Cepaitis, Robert Bainbridge, 
Alex Tapper, Oliver Buchmueller. All Rights Reserved. 
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0
    
Unless required by applicable law or agreed to in writing, 
software distributed under the License is distributed on an "AS IS" 
BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express 
or implied.See the License for the specific language governing 
permissions and limitations under the License.
==================================================================='''


import tensorflow as tf
import os

resampler_module = tf.load_op_library(os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'libResampler.so'
))

class resampler():       
    def __init__(self,
        rates,
        batch
    ):
        if type(batch)==type(dict()):
            self.inputBatch = []
            for name in sorted(batch.keys()):
                self.inputBatch.append(batch[name])
     
        elif type(batch)==type(list()):
            self.inputBatch = batch


        output = resampler_module.resampler(
            rates,
            self.inputBatch
        )
        
        
        if type(batch)==type(dict()):
            self.outputBatch = {}
            for i,name in enumerate(sorted(batch.keys())):
                self.outputBatch[name]=output[i]
        elif type(batch)==type(list()):
            self.outputBatch = output
            
    def resample(self):
        return self.outputBatch

            
