# Voice Agent

This folder contains the implementation of my first LiveKit voice agent using Python

## Agent Logic

In this initial version, the agent logic is implemented directly inside the
agent session lifecycle in `main.py`.

The agent reacts to participant join events, processes the input, and produces
a basic output. This design is intentional to focus on understanding the
LiveKit AgentSession lifecycle and pipeline flow before introducing tools
and advanced behaviors.

# Agent Module

This directory contains the implementation of the first LiveKit agent.

## File Responsibilities

### main.py
- Handles agent lifecycle and session initialization
- Connects the agent to LiveKit Cloud
- Registers event listeners
- Delegates behavior to the logic module

### logic.py
- Contains the core agent behavior
- Processes user input events
- Implements the agent’s decision-making logic

## Design Rationale

The agent logic is intentionally separated from lifecycle management to:
- Improve clarity
- Make agent behavior easier to extend
- Prepare for tool usage and multi-agent workflows in later phases
