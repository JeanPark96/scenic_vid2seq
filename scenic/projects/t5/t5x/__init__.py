# Copyright 2023 The T5X Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Import API modules."""

import scenic.projects.t5.t5x.adafactor
import scenic.projects.t5.t5x.checkpoints
import scenic.projects.t5.t5x.decoding
import scenic.projects.t5.t5x.gin_utils
import scenic.projects.t5.t5x.infer
import scenic.projects.t5.t5x.losses
import scenic.projects.t5.t5x.models
import scenic.projects.t5.t5x.partitioning
import scenic.projects.t5.t5x.state_utils
import scenic.projects.t5.t5x.train_state
import scenic.projects.t5.t5x.trainer
import scenic.projects.t5.t5x.utils

from scenic.projects.t5 import t5x
# Version number.
from scenic.projects.t5.t5x.version import __version__

# TODO(adarob): Move clients to t5x.checkpointing and rename
# checkpoints.py to checkpointing.py
checkpointing = t5x.checkpoints
