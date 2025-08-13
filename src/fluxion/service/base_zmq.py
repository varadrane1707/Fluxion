from abc import ABC, abstractmethod
from fluxion.utils._log import FluxionLogger
import zmq

class BaseWorker(ABC):
    def __init__(self, backend_addr):
        self.logger = FluxionLogger(self.__class__.__name__)
        self.context = self.create_zmq_context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.connect(backend_addr)

    @abstractmethod
    def process(self, data: dict) -> dict:
        """Implement worker-specific processing logic."""
        pass

    def run(self):
        self.logger.info("Worker started")
        while True:
            data = self.socket.recv_json()
            self.logger.debug(f"Received data: {data}")
            try:
                result = self.process(data)
                self.socket.send_json({"status": "ok", "data": result})
            except Exception as e:
                self.logger.exception("Error in worker")
                self.socket.send_json({"status": "error", "message": str(e)})
