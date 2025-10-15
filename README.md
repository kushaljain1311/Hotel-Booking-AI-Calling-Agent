# Hotel Booking AI Calling Agent

An AI-powered voice assistant named Sophie that automates hotel booking confirmations through natural, human-like conversations. Built using LiveKit for real-time voice interaction, LangChain for intelligent dialogue management, and Function Calling to verify booking details and request late checkout.

---

## Features

- Real-time voice interaction using LiveKit
- Intelligent conversation flow using LangChain
- Backend operations via Function Calling
- Tool integrations:
  - `get_weather`: Fetch current weather for a city
  - `search_web`: Search hotel or booking-related information online
- Polite, professional, and context-aware communication
- Simple conversation memory for tracking previous interactions

---

## Project Structure

Live_kit/
├── agent.py              # Main AI agent script
├── tools.py              # Tool functions (get_weather, search_web)
├── prompt.py             # Agent and session instructions
├── requirements.txt      # Python dependencies
├── .gitignore            # Ignored files (venv, .env, etc.)
├── LICENSE
├── gen_token.py          # Optional helper scripts
└── livekit-server.exe    # LiveKit server executable


## Setup Instructions

### 1. Clone the repository

git clone https://github.com/kushaljain1311/Hotel-Booking-AI-Calling-Agent.git
cd Hotel-Booking-AI-Calling-Agent

text

### 2. Create a virtual environment and install dependencies

python -m venv venv
venv\Scripts\activate # Windows
pip install -r requirements.txt

text

### 3. Set up environment variables

Create a `.env` file in the project root with the following:

LIVEKIT_URL=ws://localhost:7880
LIVEKIT_API_KEY=devkey
LIVEKIT_API_SECRET=supersecret
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY

text

Replace `YOUR_GOOGLE_API_KEY` with your valid Google API key.

---

## Running the Project

### 1. Start the LiveKit Server

In one terminal, run:

.\livekit-server.exe --dev --udp-port 7880 --keys "devkey: supersecret"

text

You can change the port (`--udp-port`) and keys (`--keys "key:secret"`) as needed.

### 2. Run the AI Agent

Open another terminal and run:

python agent.py console

text

This will launch Sophie, the hotel booking confirmation agent.  
The agent will connect to your LiveKit server and handle booking verification calls in real-time.

---

## Usage

Sophie will follow a step-by-step flow:

- Introduce herself and explain the call purpose.
- Verify booking under John Doe with check-in date 2025-10-01.
- Confirm room count, breakfast, charges, and parking.
- Request late checkout.
- Collect the staff member’s name.
- Thank the staff and end the call.
- Tools `get_weather` and `search_web` can be invoked contextually for weather updates or online information.

---

## Notes

- Ensure `.env` is properly set before running the server or agent.
- The `.exe` file is from the open-source LiveKit server.
- Avoid committing sensitive keys like `.env` to GitHub.

---

## Dependencies

- Python 3.10+
- [LiveKit](https://github.com/livekit/livekit-server)
- LangChain
- Requests
- Google Realtime API
- Other dependencies listed in `requirements.txt`

---

## License

This project is licensed under the [MIT License](https://chatgpt.com/c/LICENSE).
