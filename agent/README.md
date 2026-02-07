# Voice Agent

This folder contains the implementation of my first LiveKit voice agent using Python

## Agent Logic

In this initial version, the agent logic is implemented directly inside the
agent session lifecycle in `main.py`.

The agent reacts to participant join events, processes the input, and produces
a basic output. This design is intentional to focus on understanding the
LiveKit AgentSession lifecycle and pipeline flow before introducing tools
and advanced behaviors.
