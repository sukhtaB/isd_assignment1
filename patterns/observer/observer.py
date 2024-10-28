"""
Description: This module defines the Observer abstract class that serves as an interface
for all concrete observers in the application.
Author: Sukhtab Singh Warya
Date: 25/10/2024
"""

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    The Observer interface defines the method for receiving updates from the Subject.
    """

    @abstractmethod
    def update(self, message: str) -> None:
        """
        Called when the Subject notifies its observers.

        Parameters:
        message (str): The update message from the Subject.
        """
        pass