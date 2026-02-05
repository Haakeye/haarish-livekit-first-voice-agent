"""
First LiveKit Task-Driven Agent
Author: Haarish Kumar

Goal:
- Initialize a LiveKit agent
- Start an agent session
- Observe pipeline flow (input -> processing -> output)
"""

import asyncio
from livekit import rtc
from livekit.agents import JobContext, WorkerOptions, cli


async def entrypoint(ctx: JobContext):
    """
    This function represents the agent lifecycle.
    It is called when the agent session starts.
    """

    print("Agent started")

    # STEP 1: Initialize and connect the agent session
    await ctx.connect()
    print("Agent session connected")

    # STEP 2: Receive user input (participant joins the room)
    @ctx.room.on("participant_connected")
    async def on_participant_connected(participant: rtc.RemoteParticipant):
        print(f"INPUT: Participant joined -> {participant.identity}")

        # STEP 3: Process input (simple processing logic)
        response = f"Hello {participant.identity}, LiveKit agent is running"

        # STEP 4: Output result
        print(f"OUTPUT: {response}")

    # Keep the agent alive
    await asyncio.Event().wait()


if __name__ == "__main__":
    cli.run_app(
        WorkerOptions(
            entrypoint_fnc=entrypoint
        )
    )
