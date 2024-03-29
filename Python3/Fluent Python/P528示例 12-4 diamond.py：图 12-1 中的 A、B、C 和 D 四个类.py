class A:
    def ping(self):
        print('ping:', self)

class B:
    def pong(self):
        print('pong:', self)

class C(A):
    def pong(self):
        print('Pong:', self)

class D(B, C):
    def ping(self):
        super().ping()
        print('post-ping:', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)