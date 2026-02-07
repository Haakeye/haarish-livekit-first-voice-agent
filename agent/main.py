import asyncio
from livekit import rtc
from livekit.agents import JobContext, WorkerOptions, cli


async def entrypoint(ctx: JobContext):
    """
    Agent lifecycle entrypoint
    """

    print("Agent started")

    # STEP 1: Initialize and connect the agent session
    await ctx.connect()
    print("Agent session connected")

    # STEP 2: Receive user input (participant joins the room)
    @ctx.room.on("participant_connected")
    async def on_participant_connected(participant: rtc.RemoteParticipant):
        print(f"INPUT: Participant joined -> {participant.identity}")

        # STEP 3: Process input
        response = f"Hello {participant.identity}, LiveKit agent is running"

        # STEP 4: Output
        print(f"OUTPUT: {response}")

    # Keep agent alive
    await asyncio.Event().wait()


if __name__ == "__main__":
    cli.run_app(
        WorkerOptions(
            entrypoint_fnc=entrypoint
        )
    )
