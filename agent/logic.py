"""
Agent Logic Module

This module contains the core behavior of the LiveKit agent.
It is responsible for handling user input and producing output.

This separation is intentional to distinguish:
- Agent lifecycle & framework glue (main.py)
- Agent behavior / decision logic (logic.py)
"""

from livekit import rtc


async def handle_participant_join(participant: rtc.RemoteParticipant):
    """
    Core agent logic.

    INPUT:
        A participant joining the LiveKit room

    PROCESSING:
        Simple greeting generation

    OUTPUT:
        Console output (for learning & debugging)
    """

    print(f"INPUT: Participant joined -> {participant.identity}")

    response = f"Hello {participant.identity}, LiveKit agent is running"

    print(f"OUTPUT: {response}")
