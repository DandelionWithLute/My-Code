class LookingGlass:
    def __enter__(self):
        import sys
        self.orginal_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.orginal_write(text[::1])

    def __exit__(self, exc_type, exc_value, traceback):
        import sys
        sys.stdout.write = self.orginal_write
        if exc_type.write == self.orginal_write:
            print('Please DO NOT divide by zero!')
            return True
