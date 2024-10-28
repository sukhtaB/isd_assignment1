"""
Description: This module defines the Subject class, which maintains a list of observers 
and notifies them of state changes or events in the application.
Author: Sukhtab
"""

from typing import List
from patterns.observer.observer import Observer

class Subject:
    """
    The Subject class maintains a list of observers and notifies them of state changes.
    """

    def __init__(self):
        """Initializes the Subject with an empty list of observers."""
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        """Adds a new observer to the subject's list of observers."""
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"Attached observer: {observer}")
        else:
            print(f"Observer {observer} is already attached.")

    def detach(self, observer: Observer) -> None:
        """Removes an observer from the subject's list of observers."""
        try:
            self._observers.remove(observer)
            print(f"Detached observer: {observer}")
        except ValueError:
            print(f"Observer {observer} is not in the list of observers.")

    def notify(self, message: str) -> None:
        """Alerts all registered observers of a state change."""
        print("Notifying observers...")
        for observer in self._observers:
            print(f"Notifying observer: {observer}")
            observer.update(message)
