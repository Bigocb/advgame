import sys
sys.path.insert(0, './*')
from data.src.metrics.db import mets as metmain
from data.src.tagging.tagging import check_tags
from data.src.controller.app import main, app
import data.src.generator

app.run()
# metmain()
# check_tags()
