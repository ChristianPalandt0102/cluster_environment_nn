# sandbox_guard.py

class SandboxGuard:

    def __init__(self):
        self.max_runtime = 2  # seconds

    def safe_execute(self, func, *args):

        try:
            result = func(*args)
            return result
        except Exception as e:
            return {"error": str(e)}