import heapq
import itertools


class PriorityOrderQueue:
    def __init__(self):
        self._queue = []
        self._counter = itertools.count()

        self._priority_map = {
            "high": 1,
            "normal": 2,
            "low": 3
        }

    def add_order(self, order):
        priority = order["priority"]

        count = next(self._counter)

        heapq.heappush(
            self._queue,
            (self._priority_map[priority], count, order)
        )

    def get_next_order(self):
        if not self._queue:
            return None

        _, _, order = heapq.heappop(self._queue)

        return order

    def pending_order_count(self):
        return len(self._queue)

    def is_empty(self):
        return len(self._queue) == 0


if __name__ == "__main__":
    queue = PriorityOrderQueue()

    queue.add_order({
        "order_id": "0001",
        "priority": "high",
        "timestamp": "2026-05-03 09:00:00"
    })

    queue.add_order({
        "order_id": "0002",
        "priority": "normal",
        "timestamp": "2026-05-03 09:04:00"
    })

    queue.add_order({
        "order_id": "0003",
        "priority": "low",
        "timestamp": "2026-05-03 09:08:00"
    })

    print(queue.get_next_order())
    print(queue.get_next_order())
    print(queue.get_next_order())