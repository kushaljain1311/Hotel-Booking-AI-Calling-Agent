
from dotenv import load_dotenv
import os
from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import noise_cancellation
from prompt import AGENT_INSTRUCTIONS, SESSION_INSTRUCTIONS
from livekit.plugins import google
from tools import get_weather, search_web

load_dotenv(".env.local")
load_dotenv()

# -------------------------
# Simple conversation memory
# -------------------------
class ConversationMemory:
    def __init__(self):
        self.history = []

    def add_message(self, role, content):
        """Add a message to memory"""
        self.history.append({"role": role, "content": content})

    def get_history(self):
        """Return conversation history"""
        return self.history

# -------------------------
# Agent with memory
# -------------------------
class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=AGENT_INSTRUCTIONS,
            llm=google.beta.realtime.RealtimeModel(
                voice="Aoede",
                temperature=0.8,
            ),
            tools=[get_weather, search_web],  # you can add get_weather, search_web if needed  
        )
        self.memory = ConversationMemory()

    def update_memory(self, role, content):
        self.memory.add_message(role, content)

    def get_conversation_history(self):
        return self.memory.get_history()

# -------------------------
# Entry point
# -------------------------
async def entrypoint(ctx: agents.JobContext):
    agent_instance = Assistant()
    session = AgentSession()  # memory is now managed inside the agent

    await session.start(
        room=ctx.room,
        agent=agent_instance,
        room_input_options=RoomInputOptions(
        video_enabled=True,
        audio_enabled=True,
        noise_cancellation=noise_cancellation.BVC(),
    )

    )

    await session.generate_reply(
        instructions=SESSION_INSTRUCTIONS
    )

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
