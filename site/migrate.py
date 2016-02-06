import os
import sys
sys.path.insert(0, os.path.abspath('../../../scaffold/'))
from config import settings

from scaffold.core.data.database import db
db.config(settings.database)
from scaffold.core.data.migrations import export_schema, import_schema

export_schema()
#import_schema()



