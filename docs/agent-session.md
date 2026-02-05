# AgentSession – Core Understanding

## What is an AgentSession?
An AgentSession represents the lifecycle of a LiveKit agent inside a room.
It manages the agent’s connection, context, and event-driven execution.

## Lifecycle of an AgentSession
1. Agent process starts
2. AgentSession is initialized
3. Agent connects to the LiveKit room
4. Agent waits for input events
5. Agent processes input
6. Agent produces output
7. Session remains active until stopped

## Session Context
The JobContext (`ctx`) provides:
- Access to the LiveKit room
- Participant events
- Session-level state
- Lifecycle control

## Key Learnings
- An agent cannot process input before session connection
- All interactions are event-driven
- Agent logic lives inside the session lifecycle

## Limitations (Current Stage)
- No state persistence across restarts
- Output limited to logs
