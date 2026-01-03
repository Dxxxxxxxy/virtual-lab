"""Test run with detailed agents and Scientific Critic integration.

This script demonstrates:
1. Highly customized expert agents with specific knowledge and restrictions
2. Scientific Critic providing feedback after experts speak
3. More rigorous discussion structure
"""

from pathlib import Path
from virtual_lab.run_meeting import run_meeting
from ion_transport.agents.detailed_agents import (
    SYMPOSIUM_PI,
    ELECTROCHEMISTRY_EXPERT,
    MEMBRANE_SCIENCE_EXPERT,
    CUSTOM_SCIENTIFIC_CRITIC,
)
from ion_transport.prompts.detailed_prompts import (
    TEST_AGENDA_WITH_CRITIC,
    ROUND_1_QUESTIONS,
    RIGOROUS_DISCUSSION_RULES,
)


def main():
    """Run a test with detailed agents and scientific critic."""

    print("\n" + "="*80)
    print("ION TRANSPORT SYMPOSIUM - DETAILED TEST WITH CRITIC")
    print("="*80)
    print("\nThis test demonstrates:")
    print("- Finely-tuned expert agents with specific expertise and restrictions")
    print("- Scientific Critic providing rigorous feedback")
    print("- More structured and critical discussion")
    print("\nParticipants:")
    print("  1. Symposium Chair (PI) - Facilitator")
    print("  2. Electrochemistry Expert - Dr. Elena Martinez")
    print("  3. Membrane Science Expert - Prof. James Chen")
    print("  4. Scientific Critic - Dr. Marcus Weber")
    print("\nEstimated cost: ~$0.50-0.70")
    print("="*80 + "\n")

    # Define team - NOTE: Critic is included as a team member
    # The critic will speak in rotation with other experts
    team_lead = SYMPOSIUM_PI
    team_members = (
        ELECTROCHEMISTRY_EXPERT,
        CUSTOM_SCIENTIFIC_CRITIC,  # Critic speaks after electrochemistry expert
        MEMBRANE_SCIENCE_EXPERT,
        CUSTOM_SCIENTIFIC_CRITIC,  # Critic speaks again after membrane expert
    )

    # Results directory
    results_dir = Path("ion_transport/results/detailed_test_with_critic")
    results_dir.mkdir(parents=True, exist_ok=True)

    # Run the meeting
    print("Starting discussion with critic feedback...\n")

    summary = run_meeting(
        meeting_type="team",
        agenda=TEST_AGENDA_WITH_CRITIC,
        agenda_questions=ROUND_1_QUESTIONS,
        agenda_rules=RIGOROUS_DISCUSSION_RULES,
        save_dir=results_dir,
        save_name="detailed_discussion",
        team_lead=team_lead,
        team_members=team_members,
        num_rounds=2,  # 2 rounds for testing
        pubmed_search=False,  # Disable for faster testing
        return_summary=True,
    )

    print("\n" + "="*80)
    print("DETAILED TEST COMPLETE")
    print("="*80)
    print(f"\nResults saved in: {results_dir}")
    print("\n✅ Key Features Demonstrated:")
    print("   - Expert agents with specific knowledge boundaries")
    print("   - Scientific Critic challenges assumptions and demands rigor")
    print("   - More structured discussion with clear rules")
    print("\nNext Steps:")
    print("   1. Review the discussion to see critic feedback")
    print("   2. Adjust agent characteristics in detailed_agents.py as needed")
    print("   3. Run full 4-expert symposium with all rounds")


if __name__ == "__main__":
    main()
