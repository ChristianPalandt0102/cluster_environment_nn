def prefetch(self, predicted_items):
    for item in predicted_items:
        self.store(item)