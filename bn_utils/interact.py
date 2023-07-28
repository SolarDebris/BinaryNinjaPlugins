from binaryninja import *
from binaryninjaui import *


def get_current_context() -> Optional[Any]:
    ctx = UIContext.activeContext()
    if not ctx:
        ctx = UIContext.allContexts()[0]
    if not ctx:
        binaryninja.log_warn(f'No UI Context available')
        return None
    handler = ctx.contentActionHandler()
    if not handler:
        binaryninja.log_warn(f'No Action Context available')
        return None

    return handler.actionContext()
