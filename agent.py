import os
import tempfile

from google.adk import Agent
from google.adk.tools.computer_use.computer_use_toolset import ComputerUseToolset

from .playwright import PlaywrightComputer

# Define user_data_dir path
profile_name = 'browser_profile_for_adk'
profile_path = os.path.join(tempfile.gettempdir(), profile_name)
os.makedirs(profile_path, exist_ok=True)

computer_with_profile = PlaywrightComputer(
    screen_size=(1280, 936),
    user_data_dir=profile_path,
)

# Create agent with the toolset using the new computer instance
root_agent = Agent(
    model='gemini-2.5-computer-use-preview-10-2025',
    name='hello_world_agent',
    description=(
        'computer use agent that can operate a browser on a computer to finish'
        ' user tasks'
    ),
    instruction=""" you are a computer use agent """,
    tools=[ComputerUseToolset(computer=computer_with_profile)],
)