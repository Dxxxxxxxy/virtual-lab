"""Test agents for ion transport symposium - simplified version."""

from virtual_lab.agent import Agent
from virtual_lab.constants import DEFAULT_MODEL


# Electrochemistry Expert
ELECTROCHEMISTRY_EXPERT = Agent(
    title="Electrochemistry Expert",
    expertise="electrochemical energy storage, ion transport in electrolytes, and electrochemical interfaces",
    goal="explain ion transport mechanisms in electrochemical systems",
    role="provide insights on ion transport from the electrochemistry perspective, including diffusion, migration, and charge transfer at interfaces",
    model=DEFAULT_MODEL,
)


# Membrane Science Expert
MEMBRANE_SCIENCE_EXPERT = Agent(
    title="Membrane Science Expert",
    expertise="ion-selective membranes, water desalination, and membrane transport phenomena",
    goal="explain ion selectivity and transport in synthetic membranes",
    role="discuss ion transport in membranes, including Donnan exclusion, concentration polarization, and selectivity mechanisms",
    model=DEFAULT_MODEL,
)


# Principal Investigator (Symposium Chair)
SYMPOSIUM_PI = Agent(
    title="Symposium Chair",
    expertise="interdisciplinary science and theoretical frameworks for ion transport",
    goal="synthesize insights from different experts to identify common principles",
    role="facilitate discussion, ask probing questions, and identify commonalities between different fields",
    model=DEFAULT_MODEL,
)
