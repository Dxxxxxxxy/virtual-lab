### Guide to Customizing Agents and Adding Scientific Critic

This guide explains how to fine-tune agent characteristics and integrate the Scientific Critic.

---

## Files You Need to Modify

### 1. **Agent Definitions** - `ion_transport/agents/detailed_agents.py`

**Purpose:** Define expert characteristics, knowledge scope, and restrictions

**What to customize:**

```python
ELECTROCHEMISTRY_EXPERT = Agent(
    title="Dr. Elena Martinez - Electrochemistry Expert",  # Personalize with a name

    expertise="""Long, detailed description of:
    - Specific subfields (batteries, fuel cells, etc.)
    - Key techniques (impedance spectroscopy, etc.)
    - Specialized knowledge areas""",

    goal="""What this expert aims to achieve in the discussion""",

    role="""Detailed instructions including:

    1. KNOWLEDGE SCOPE - What they SHOULD know:
       - List specific topics, equations, phenomena
       - Be very specific: "Nernst-Planck", "Butler-Volmer", etc.

    2. KNOWLEDGE RESTRICTIONS - What they SHOULD NOT claim expertise in:
       - Other fields' details
       - BUT can draw analogies and ask questions

    3. COMMUNICATION STYLE:
       - How to present (equations first? examples first?)
       - Tone (quantitative? qualitative?)
       - What to emphasize

    4. DISCUSSION APPROACH:
       - How to interact with other experts
       - What connections to look for
       - When to defer to others""",

    model=DEFAULT_MODEL,
)
```

**Key Principle:**
- **BE SPECIFIC** in both expertise AND restrictions
- This creates realistic, focused discussions
- Prevents agents from claiming universal knowledge

---

### 2. **Custom Prompts** - `ion_transport/prompts/detailed_prompts.py`

**Purpose:** Define discussion structure and critic integration

**What to customize:**

#### A. Agendas for each round:
```python
ROUND_1_AGENDA = """
Clear instructions for what each expert should present:
- Specific questions to answer
- Format/structure to follow
- Examples to provide
- Mention that critic will respond after each expert
"""
```

#### B. Discussion rules:
```python
RIGOROUS_DISCUSSION_RULES = (
    "State assumptions explicitly",
    "Provide quantitative examples",
    "Distinguish facts from speculation",
    # Add more rules as needed
)
```

#### C. Questions to answer:
```python
ROUND_1_QUESTIONS = (
    "Specific question 1 with clear scope",
    "Specific question 2 requiring quantitative answer",
    "Specific question 3 asking for comparison",
)
```

---

### 3. **Execution Script** - `ion_transport/run_detailed_test.py`

**Purpose:** Run the symposium with customized agents and critic

**Key section to modify:**

```python
# Define the team
team_lead = SYMPOSIUM_PI

# IMPORTANT: Include critic multiple times if you want feedback after each expert
team_members = (
    EXPERT_1,
    CUSTOM_SCIENTIFIC_CRITIC,  # Critic responds after Expert 1
    EXPERT_2,
    CUSTOM_SCIENTIFIC_CRITIC,  # Critic responds after Expert 2
    EXPERT_3,
    CUSTOM_SCIENTIFIC_CRITIC,  # Critic responds after Expert 3
    # etc.
)
```

**Why this works:**
- The framework rotates through team members in order
- By placing the critic after each expert, it provides feedback in sequence
- The critic receives the full context of what was just said

---

## How to Run Your Customized Version

### Test with 2 experts + critic:
```bashyes
source .venv/bin/activate
python -m ion_transport.run_detailed_test
```

### Full symposium with 4 experts + critic:
Create `run_full_detailed_symposium.py` with all 4 experts and critic interspersed.

---

## Customization Examples

### Example 1: Restrict an Expert's Knowledge More Tightly

```python
BIOLOGY_EXPERT = Agent(
    ...
    role="""...
    2. KNOWLEDGE RESTRICTIONS - You have LIMITED expertise in:
       - Synthetic membrane polymer chemistry (you only know proteins)
       - Battery electrode kinetics (you understand charge transfer concepts but not SEI details)
       - Solid-state ionics device physics (your experience is aqueous biological systems)
       - Industrial process optimization

       IMPORTANT: When these topics arise:
       - Acknowledge your limitations explicitly
       - Ask clarifying questions instead of making claims
       - Offer biological analogies if relevant, but note they may not apply
       - Defer to the appropriate expert
    ..."""
)
```

### Example 2: Make the Critic More Aggressive

```python
AGGRESSIVE_CRITIC = Agent(
    title="Tough Scientific Reviewer",
    ...
    role="""You are a notoriously rigorous reviewer. Your standards:

    1. DEMAND EVIDENCE:
       - "Where is the data?" for any empirical claim
       - "Show me the calculation" for theoretical claims
       - "Which paper?" for literature claims

    2. CHALLENGE EVERYTHING:
       - Question all assumptions, even "obvious" ones
       - Ask "how do you know?" repeatedly
       - Demand error bars and uncertainties

    3. ZERO TOLERANCE FOR:
       - Handwaving or vague statements
       - Unsupported extrapolations
       - Analogies without limits stated
       - Mixing correlation with causation

    4. BUT BE CONSTRUCTIVE:
       - Suggest experiments to test claims
       - Propose alternative explanations
       - Acknowledge good arguments when made
    """,
)
```

### Example 3: Add Domain-Specific Examples to Prompts

```python
ROUND_1_AGENDA = """
Each expert provide ONE concrete, quantitative example:

- Electrochemistry: Fast-charging Li-ion batteries
  → State: current density, concentration polarization, limiting phenomenon

- Membrane Science: Reverse osmosis desalination
  → State: flux, selectivity, concentration polarization

- Biology: K+ channel selectivity
  → State: selectivity ratio, conductance, energy barrier

- Iontronics: Organic electrochemical transistor (OECT)
  → State: switching time, on/off ratio, ion accumulation

This allows direct comparison of numbers across fields.
"""
```

---

## Advanced: Modifying Discussion Flow

If you want even more control (e.g., critic only speaks after Round 1, not during), you would need to modify the core framework in `src/virtual_lab/run_meeting.py`.

### Current limitation:
The framework rotates through all team members equally. You can't easily make the critic speak "on demand" only after certain experts.

### Workaround (what we're using):
Include the critic multiple times in the team member list at strategic positions.

### Future enhancement (requires modifying core):
Add a `critic_agent` parameter to `run_meeting()` that automatically inserts critic feedback after each non-critic team member. This would require ~50 lines of code changes in `run_meeting.py`.

Would you like me to implement this enhancement?

---

## Summary Checklist

To fully customize your symposium:

- [ ] Edit `ion_transport/agents/detailed_agents.py`:
  - [ ] Customize each expert's expertise, goal, and role
  - [ ] Add specific knowledge restrictions
  - [ ] Define communication style
  - [ ] Customize the Scientific Critic behavior

- [ ] Edit `ion_transport/prompts/detailed_prompts.py`:
  - [ ] Write detailed agendas for each round
  - [ ] Add specific questions to answer
  - [ ] Define discussion rules
  - [ ] Include critic feedback instructions

- [ ] Edit `ion_transport/run_detailed_test.py`:
  - [ ] Choose which experts to include
  - [ ] Position the critic in team_members list
  - [ ] Set number of rounds
  - [ ] Enable/disable PubMed search

- [ ] Run and iterate:
  - [ ] Test with 2 experts first
  - [ ] Review critic feedback quality
  - [ ] Adjust agent prompts as needed
  - [ ] Scale up to full 4-expert symposium

---

## Quick Start: Run the Detailed Test Now

```bash
# Make sure API key is set
source ~/.zshrc

# Activate environment
cd "virtual_lab"
source .venv/bin/activate

# Run the detailed test with critic
python -m ion_transport.run_detailed_test
```

This will show you:
- How detailed agent customization works
- How the critic provides feedback
- What the discussion quality looks like

Then you can modify the agents and prompts to your liking!
