"""
Description: This module defines the Subject class, which maintains a list of observers 
and notifies them of state changes or events in the application.
Author: Sukhtab
"""

from typing import List
from patterns.observer.observer import Observer  # Ensure this is correct

class Subject:
    """
    The Subject class maintains a list of observers and notifies them of state changes.
    """

    def __init__(self):
        """
        Initializes the Subject with an empty list of observers.
        """
        self._observers: List[Observer] = []  # Correct type hinting

    def attach(self, observer: Observer) -> None:
        """
        Adds a new observer to the subject's list of observers.

        Parameters:
        observer (Observer): The observer to be added.
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """
        Removes an observer from the subject's list of observers.

        Parameters:
        observer (Observer): The observer to be removed.
        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str) -> None:
        """
        Alerts all registered observers of a state change.

        Parameters:
        message (str): The message to be sent to observers.
        """
        for observer in self._observers:
            observer.update(message)  # Assuming update is correctly defined in Observer
