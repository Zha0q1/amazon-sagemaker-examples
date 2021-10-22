# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file
# except in compliance with the License. A copy of the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "LICENSE.txt" file accompanying this file. This file is distributed on an "AS IS"
# BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, express or implied. See the License for
# the specific language governing permissions and limitations under the License.

import subprocess
import sys
import os

os.environ[
    'PYTHONPATH'] += ':/shared/DeepLearningExamples/PyTorch/Segmentation/MaskRCNN/pytorch'

os.environ['FI_EFA_USE_DEVICE_RDMA'] = '1'
#os.environ['FI_PROVIDER'] = 'efa'

# true entry point path is consistent with model specific Dockerfile
exe = 'python'

if 'dataparallel' in os.environ['SM_FRAMEWORK_PARAMS']:
    path = '/shared/DeepLearningExamples/PyTorch/Segmentation/MaskRCNN/pytorch/tools/train_net.py'
else:
    path = '/shared/DeepLearningExamples/PyTorch/Segmentation/MaskRCNN/pytorch/tools/train_net_sm.py'

cmd_list = [exe] + [path] + sys.argv[1:]
cmd = ' '.join(cmd_list)

print('entry point cmd is', cmd)

subprocess.run(cmd, shell=True)