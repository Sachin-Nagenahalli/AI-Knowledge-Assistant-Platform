from app.rag.context_expander import ContextExpander


class Pipeline:

    def __init__(self):

        self.expander = ContextExpander()

    def process(
        self,
        retrieval,
    ):

        expanded = self.expander.expand(
            retrieval
        )

        return expanded