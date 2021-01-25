#!/usr/bin/env python
import os
import sys
from django.db import models

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restifsc.settings")

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
    on_delete = models.DO_NOTHING
