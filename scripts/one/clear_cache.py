#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Clear all .cache
"""

from __future__ import annotations

import os.path

from one import data_dir
from one import delete_files

if __name__ == "__main__":
	delete_files(
		dirs= [os.path.join(data_dir, "*")],
		extension = ".cache",
		recursive = True
	)
