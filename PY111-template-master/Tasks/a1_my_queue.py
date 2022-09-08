"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        self.queue = []  # todo для очереди можно использовать python list

    def enqueue(self, elem: Any) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        # if elem not in self.queue:
        #     self.queue.insert(0, elem)
        #     return True
        # return False

        self.queue.insert(0, elem)

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if no elements.

        :return: dequeued element
        """

        # if len(self.queue) > 0:
        #     return self.queue.pop()
        # return ("Очередь пустая")

        if not self.queue:
            return None
        return self.queue.pop()

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        try:
            self.queue[ind]
        except IndexError:
            return None
        reversed_index = -ind - 1
        return self.queue[reversed_index]

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.queue.clear()
        return None
