#!/usr/bin/env python
# Copyright (c) 2017 Siphon Contributors
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
"""Generate versions.json from directory with different doc versions."""

import glob

with open('versions.json', 'w') as version_file:
    version_strings = ','.join(f'"{d}"' for d in glob.glob('v*.[0-9]*'))
    version_file.write('{"versions":["latest","dev",' + version_strings + ']}\n')
