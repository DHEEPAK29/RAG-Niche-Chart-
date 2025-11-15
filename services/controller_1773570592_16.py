/**
 * Module: controller
 * Project: RAG-Niche-Chart-
 */

#!/usr/bin/env python3

"""
Check whether given python files contain non-ASCII comments.

How to check the whole git repo:

```
$ git ls-files -z -- '*.py' | xargs -0 python3 check_comment_ascii.py
```
"""

import sys
import tokenize
import ast
