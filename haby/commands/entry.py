import click

from .info import info
from .create import create
from .new import new
from .update import update
from .stats import stats
from .log import log
from .delete import delete


"""
How to use?
haby info:
show username, habits count
haby stats:
show statistics
haby create user
create user, habit json
haby new habit
create new habit
haby update habitname
be able to modify name, activities count, etc.
haby log habitname
add 1 activity
if all done - tell user
haby delete habitname
delete habitname
haby stat habitname 
show strick 
"""


@click.group()
def entry():
    "check if config file exist. if not - trigger creation command workflow"


entry.add_command(info)
entry.add_command(stats)
entry.add_command(create)
entry.add_command(new)
entry.add_command(update)
entry.add_command(log)
entry.add_command(delete)
