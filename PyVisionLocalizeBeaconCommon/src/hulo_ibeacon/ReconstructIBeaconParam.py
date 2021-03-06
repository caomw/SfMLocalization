################################################################################
# Copyright (c) 2015 IBM Corporation
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
################################################################################

# -*- coding: utf-8 -*-

import hulo_param.ReconstructParam as ReconstructParam

class ReconstructIBeaconParam:
    reconstructParam = ReconstructParam.ReconstructParam
    
    # environment variables
    
    # Workspace settings (Overwrite hulo_param.ReconstructParam)
    LOCALIZE_PROJECT = "OpenMVGLocalization_AKAZE_BeaconMatch"
    
    LOCALIZE_PROJECT_PATH = reconstructParam.WORKSPACE_DIR + "/" + LOCALIZE_PROJECT + "/" + reconstructParam.C_PROJECT_CONFIG + "/" + LOCALIZE_PROJECT
    ###############################################################################################
        
    # general variable
    
    # normalization approach for received rssi (0: by max value , 1: median of nonzero values)
    # exportBeaconReconst.py option -a
    # OpenMVGLocalization_AKAZE_BeaconMatch option -n
    normApproach = 1
    
    #################################################################################################
    # sfmMergeGraphIBeacon.mergeModel   
    
    # Threshold for ratio between Gen Jac Sim of two signals that they will be admit as being close
    # to each other. Must be in range [0,1].
    coocThres = 0.1
    
    ########################################################################################################
    # sfmMergeGraphIBeacon.mergeOneModel
    
    # localization params
    
    # Number of knn selected via iBeacon similarity for localization
    # OpenMVGLocalization_AKAZE_BeaconMatch option -k
    locKNNnum = 200
    
    # Since several frames from video may have exactly the same iBeacon RSSI,
    # this parameter selects every LOCSKIPSELKNN frames from sorted list of knn
    # instead of all nearest neighbors to avoid selecting too many frames
    # from the same segment to match with query image.
    # OpenMVGLocalization_AKAZE_BeaconMatch option -i
    locSkipSelKNN = 1
