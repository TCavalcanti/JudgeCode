import signal
import time
 
class Timeout:
    
    def handler(self, signum, frame):
        raise Exception("Timeout")

    def timeout(self, func, args=(), kwargs={}, timeout_duration=2):
        
        signal.signal(signal.SIGALRM, self.handler)
        signal.alarm(timeout_duration)

        try:
            valor = func(*args, **kwargs)
        except Exception, e:
            valor = e.message

        signal.alarm(0)
        return valor
