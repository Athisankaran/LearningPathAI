from dataclasses import dataclass

@dataclass
class ChatMessage:
    role: str
    content: str

    @property
    def token_estimate(self) -> int:
        return len(self.content) // 4

def format_conversation(messages: list[ChatMessage]) -> str:
    formatted_lines = []
    for msg in messages:
        formatted_lines.append(f"{msg.role}: {msg.content}")
    
    return "\n".join(formatted_lines)

conversation = [
    ChatMessage(role="system", content="You are a helpful AI assistant."),
    ChatMessage(role="user", content="Explain type hints to me."),
    ChatMessage(role="assistant", content="Type hints act as sticky notes for your variables.")
]

print(format_conversation(conversation))

for msg in conversation:
    print(f"[{msg.role}] token count: {msg.token_estimate}")