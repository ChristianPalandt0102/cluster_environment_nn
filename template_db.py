class TemplateDB:

    def __init__(self):
        self.templates = []

    def integrate(self, tpl):

        self.templates.append(tpl)

        print("[EVOLUTION] new template integrated:",
              tpl["id"])