from .util import stringify, listify

def execute(conditions: str | list[str], cmds_to_run: str | list[str]):
    conditions = stringify(conditions)
    cmds_to_run = listify(cmds_to_run)
    # TODO generate file to execute in?
    for cmd in cmds_to_run:
        yield f'execute {conditions} run {cmd}'