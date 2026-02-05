# Agent Pipeline – Basic Flow

## What is a Pipeline?
A pipeline defines how input flows through an agent, gets processed,
and produces output.

## Pipeline Flow
Input → Processing → Output

## Input
- A participant joins the LiveKit room
- The agent receives this as an event

## Processing
- The agent reacts to the event
- A simple response string is generated

## Output
- The agent outputs the response (logged output)

## Key Insight
LiveKit pipelines are event-driven rather than request-response.
The agent remains active and reacts to events dynamically.
