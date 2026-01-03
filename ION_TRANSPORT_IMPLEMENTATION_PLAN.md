# Ion Transport Symposium Implementation Plan

## Overview
Transform the Virtual Lab framework into a multi-agent AI symposium system for discussing unified theoretical frameworks of ion transport across multiple scientific disciplines.

## Research Domains & Expert Agents

### 1. Electrochemistry Expert
- **Focus**: Electrochemical energy storage (batteries, supercapacitors)
- **Key Topics**:
  - Ion diffusion in electrolytes
  - Charge transfer kinetics
  - Double layer formation
  - Nernst-Planck equations

### 2. Membrane Science Expert
- **Focus**: Water desalination, ion exchange membranes, selective ion membranes
- **Key Topics**:
  - Ion selectivity mechanisms
  - Donnan exclusion
  - Concentration polarization
  - Membrane potential

### 3. Biology/Neuroscience Expert
- **Focus**: Ion channels in cell membranes
- **Key Topics**:
  - Gating mechanisms
  - Selectivity filters
  - Goldman-Hodgkin-Katz equation
  - Action potentials

### 4. Iontronics Expert
- **Focus**: Ionic transistors, diodes, memristors
- **Key Topics**:
  - Ion-electron coupling
  - Ionic conductivity in solid-state
  - Synaptic plasticity
  - Neuromorphic computing

### 5. Principal Investigator (Symposium Organizer)
- **Role**: Orchestrate discussions, synthesize insights, identify unifying principles

---

## Implementation Steps

### **STEP 1: Create Ion Transport Project Structure**

```
virtual_lab/
├── src/virtual_lab/          # Keep unchanged (core framework)
├── ion_transport/            # NEW: Your application
│   ├── agents/               # Agent definitions
│   │   └── symposium_agents.py
│   ├── meetings/             # Meeting configurations
│   │   └── unified_framework_symposium.py
│   ├── prompts/              # Custom prompts
│   │   └── ion_transport_prompts.py
│   ├── results/              # Output directory
│   │   ├── symposium_round_1/
│   │   ├── symposium_round_2/
│   │   └── final_synthesis/
│   └── run_symposium.py      # Main execution script
└── nanobody_design/          # Keep as reference (can delete later)
```

### **STEP 2: Define Expert Agents**

Create `ion_transport/agents/symposium_agents.py`:

```python
from virtual_lab.agent import Agent
from virtual_lab.constants import DEFAULT_MODEL

# Electrochemistry Expert
ELECTROCHEMISTRY_EXPERT = Agent(
    title="Electrochemistry Expert",
    expertise="electrochemical energy storage, ion transport in electrolytes, charge transfer kinetics, and electrochemical interfaces",
    goal="elucidate ion transport mechanisms in electrochemical systems and contribute to a unified theoretical framework",
    role="provide insights on ion transport from electrochemistry perspective, including Nernst-Planck equations, migration-diffusion coupling, and double layer effects",
    model=DEFAULT_MODEL,
)

# Membrane Science Expert
MEMBRANE_SCIENCE_EXPERT = Agent(
    title="Membrane Science Expert",
    expertise="ion-selective membranes, water desalination, ion exchange processes, and membrane transport phenomena",
    goal="explain ion selectivity and transport in synthetic membranes and identify commonalities with other fields",
    role="discuss Donnan exclusion, concentration polarization, membrane potential, and selectivity mechanisms in synthetic systems",
    model=DEFAULT_MODEL,
)

# Biology/Neuroscience Expert
BIOLOGY_EXPERT = Agent(
    title="Biology and Neuroscience Expert",
    expertise="ion channels, membrane biology, neuronal signaling, and biological ion transport",
    goal="provide biological perspective on ion transport and identify principles that transcend synthetic-biological divide",
    role="explain gating mechanisms, selectivity filters, action potentials, and biological ion regulation",
    model=DEFAULT_MODEL,
)

# Iontronics Expert
IONTRONICS_EXPERT = Agent(
    title="Iontronics Expert",
    expertise="ionic devices, neuromorphic computing, ion-electron coupling, and emerging iontronic technologies",
    goal="bridge concepts from traditional ion transport to next-generation ionic devices",
    role="discuss ionic transistors, diodes, memristors, and how ion transport principles enable neuromorphic computation",
    model=DEFAULT_MODEL,
)

# Principal Investigator (Symposium Chair)
SYMPOSIUM_PI = Agent(
    title="Symposium Chair and Principal Investigator",
    expertise="interdisciplinary science, theoretical frameworks, and scientific synthesis across multiple fields",
    goal="synthesize insights from all experts to develop a unified theoretical framework for ion transport",
    role="facilitate discussion, ask probing questions, identify commonalities and differences across fields, and guide the team toward unified principles",
    model=DEFAULT_MODEL,
)
```

### **STEP 3: Design Symposium Structure**

The symposium will have **multiple rounds**:

**Round 1**: Understanding Current Paradigms
- Each expert presents their field's approach to ion transport
- PI identifies initial commonalities

**Round 2**: Identifying Unifying Principles
- Discuss shared equations (Nernst, Poisson-Nernst-Planck, etc.)
- Identify universal mechanisms (selectivity, gating, concentration gradients)

**Round 3**: Developing Unified Framework
- Synthesize a theoretical framework
- Map field-specific terms to universal concepts

**Round 4**: Applications and Future Directions
- Apply framework to solve cross-domain problems
- Identify research gaps

### **STEP 4: Create Custom Prompts**

Create `ion_transport/prompts/ion_transport_prompts.py`:

```python
"""Custom prompts for ion transport symposium."""

# Symposium agendas for each round
ROUND_1_AGENDA = """
Understand the current state of ion transport theory in each field.

Each expert should:
1. Describe the fundamental equations governing ion transport in your field
2. Explain the key physical mechanisms (e.g., diffusion, migration, convection)
3. Discuss what makes ion transport unique or challenging in your domain
4. Identify the most important unsolved problems

Goal: Create a comprehensive map of how different fields approach ion transport.
"""

ROUND_2_AGENDA = """
Identify unifying principles and common theoretical foundations across all fields.

Focus on:
1. Shared mathematical frameworks (Nernst-Planck, Poisson-Boltzmann, etc.)
2. Universal mechanisms (selectivity, concentration gradients, electric fields)
3. Common challenges (non-equilibrium dynamics, multi-scale coupling)
4. Conceptual bridges between fields (e.g., membrane potential in biology vs. membranes in desalination)

Goal: Find the theoretical common ground.
"""

ROUND_3_AGENDA = """
Develop a unified theoretical framework for ion transport.

Tasks:
1. Propose a general mathematical formulation that applies across domains
2. Define universal concepts and terminology
3. Map field-specific phenomena to general framework
4. Identify what is universal vs. what is domain-specific

Goal: Create a coherent theoretical framework.
"""

ROUND_4_AGENDA = """
Apply the unified framework and identify future research directions.

Questions:
1. How can insights from one field solve problems in another?
2. What new technologies or applications emerge from this unified view?
3. What are the biggest gaps in current understanding?
4. What experiments or simulations would test the unified framework?

Goal: Make the framework actionable and impactful.
"""

# Agenda questions for each round
ROUND_1_QUESTIONS = (
    "What are the 2-3 most fundamental equations in your field for describing ion transport?",
    "What physical mechanisms control ion selectivity in your systems?",
    "What is the biggest challenge or unsolved problem in understanding ion transport in your field?",
)

ROUND_2_QUESTIONS = (
    "Which equations or principles appear in ALL fields, perhaps under different names?",
    "What are the key dimensionless numbers that govern ion transport universally?",
    "Can we identify a 'master equation' that all fields use or derive from?",
)

ROUND_3_QUESTIONS = (
    "What should be the core components of a unified theoretical framework?",
    "How do we reconcile different length scales (atomic in channels vs. macroscopic in batteries)?",
    "What terminology should we adopt to facilitate cross-field communication?",
)

ROUND_4_QUESTIONS = (
    "What is one concrete problem in your field that could benefit from insights from other fields?",
    "What new technology could emerge from applying this unified framework?",
    "What is the highest priority experiment to validate this framework?",
)
```

### **STEP 5: Create Main Execution Script**

Create `ion_transport/run_symposium.py`:

```python
"""Run the Ion Transport Symposium."""

from pathlib import Path
from virtual_lab.run_meeting import run_meeting
from ion_transport.agents.symposium_agents import (
    SYMPOSIUM_PI,
    ELECTROCHEMISTRY_EXPERT,
    MEMBRANE_SCIENCE_EXPERT,
    BIOLOGY_EXPERT,
    IONTRONICS_EXPERT,
)
from ion_transport.prompts.ion_transport_prompts import (
    ROUND_1_AGENDA,
    ROUND_1_QUESTIONS,
    ROUND_2_AGENDA,
    ROUND_2_QUESTIONS,
    ROUND_3_AGENDA,
    ROUND_3_QUESTIONS,
    ROUND_4_AGENDA,
    ROUND_4_QUESTIONS,
)

def main():
    """Run multi-round symposium."""

    # Define team
    team_lead = SYMPOSIUM_PI
    team_members = (
        ELECTROCHEMISTRY_EXPERT,
        MEMBRANE_SCIENCE_EXPERT,
        BIOLOGY_EXPERT,
        IONTRONICS_EXPERT,
    )

    # Results directory
    results_dir = Path("ion_transport/results")
    results_dir.mkdir(parents=True, exist_ok=True)

    # Round 1: Understanding Current Paradigms
    print("\n" + "="*80)
    print("ROUND 1: Understanding Current Paradigms")
    print("="*80 + "\n")

    round1_summary = run_meeting(
        meeting_type="team",
        agenda=ROUND_1_AGENDA,
        agenda_questions=ROUND_1_QUESTIONS,
        save_dir=results_dir / "symposium_round_1",
        save_name="round_1_discussion",
        team_lead=team_lead,
        team_members=team_members,
        num_rounds=2,  # 2 rounds of discussion
        pubmed_search=True,  # Enable literature search
        return_summary=True,
    )

    # Round 2: Identifying Unifying Principles
    print("\n" + "="*80)
    print("ROUND 2: Identifying Unifying Principles")
    print("="*80 + "\n")

    round2_summary = run_meeting(
        meeting_type="team",
        agenda=ROUND_2_AGENDA,
        agenda_questions=ROUND_2_QUESTIONS,
        save_dir=results_dir / "symposium_round_2",
        save_name="round_2_discussion",
        team_lead=team_lead,
        team_members=team_members,
        summaries=(round1_summary,),  # Include Round 1 summary as context
        num_rounds=3,  # More rounds for deeper discussion
        pubmed_search=True,
        return_summary=True,
    )

    # Round 3: Developing Unified Framework
    print("\n" + "="*80)
    print("ROUND 3: Developing Unified Framework")
    print("="*80 + "\n")

    round3_summary = run_meeting(
        meeting_type="team",
        agenda=ROUND_3_AGENDA,
        agenda_questions=ROUND_3_QUESTIONS,
        save_dir=results_dir / "symposium_round_3",
        save_name="round_3_discussion",
        team_lead=team_lead,
        team_members=team_members,
        summaries=(round1_summary, round2_summary),
        num_rounds=4,  # Most important round
        pubmed_search=True,
        return_summary=True,
    )

    # Round 4: Applications and Future Directions
    print("\n" + "="*80)
    print("ROUND 4: Applications and Future Directions")
    print("="*80 + "\n")

    final_summary = run_meeting(
        meeting_type="team",
        agenda=ROUND_4_AGENDA,
        agenda_questions=ROUND_4_QUESTIONS,
        save_dir=results_dir / "symposium_round_4",
        save_name="round_4_discussion",
        team_lead=team_lead,
        team_members=team_members,
        summaries=(round1_summary, round2_summary, round3_summary),
        num_rounds=3,
        pubmed_search=True,
        return_summary=True,
    )

    print("\n" + "="*80)
    print("SYMPOSIUM COMPLETE")
    print("="*80)
    print(f"\nResults saved in: {results_dir}")
    print("\nFinal Summary:")
    print(final_summary)

if __name__ == "__main__":
    main()
```

### **STEP 6: Modify Constants for Your Domain**

Update `src/virtual_lab/constants.py`:
- The PubMed tool description is already updated (line 57: "ion transport and separation")
- No other changes needed!

### **STEP 7: Set Up OpenAI API**

1. Get OpenAI API key from https://platform.openai.com/
2. Set environment variable:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```
3. Or create `.env` file (add to .gitignore!)

### **STEP 8: Run the Symposium**

```bash
# Activate environment
source .venv/bin/activate

# Run symposium
python -m ion_transport.run_symposium
```

---

## Advanced Customizations

### Option 1: Individual Expert Deep Dives
Before the team meeting, run individual meetings where each expert explores their field more deeply:

```python
# Individual meeting with critic
run_meeting(
    meeting_type="individual",
    agenda="Provide a comprehensive review of ion transport theory in electrochemistry",
    team_member=ELECTROCHEMISTRY_EXPERT,
    save_dir=results_dir / "individual_electrochemistry",
    num_rounds=2,
    pubmed_search=True,
)
```

### Option 2: Add More Expert Agents
- Computational Chemistry Expert (molecular dynamics simulations)
- Materials Science Expert (solid-state ion conductors)
- Chemical Engineering Expert (process optimization)

### Option 3: Different Meeting Structures
- **Debate Format**: Set agenda rules for opposing viewpoints
- **Problem-Solving**: Focus on specific unsolved problems
- **Literature Review**: Synthesize recent papers

### Option 4: Custom Tools Beyond PubMed
Add tools for:
- Web of Science search
- Patent database
- Equation solver
- Simulation data

---

## Expected Costs

Based on GPT-5.2 pricing:
- Input: $1.75 per 1M tokens
- Output: $14 per 1M tokens

Estimated cost per symposium round:
- 4 experts × 3 discussion rounds × ~5000 tokens = ~60,000 tokens input
- ~20,000 tokens output
- **Cost per round: ~$0.40**
- **Total symposium (4 rounds): ~$1.60**

Very affordable! You can run many iterations.

---

## Next Steps

1. ✅ Create directory structure
2. ✅ Define agents
3. ✅ Write prompts
4. ✅ Create execution script
5. ⚙️ Test with small example
6. 🚀 Run full symposium
7. 📊 Analyze results
8. 🔄 Iterate and refine

Would you like me to implement any of these steps now?
