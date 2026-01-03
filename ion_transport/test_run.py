"""Test run for ion transport symposium - simplified version.

This is a minimal test to verify the system works before running the full symposium.
"""

from pathlib import Path
from virtual_lab.run_meeting import run_meeting
from ion_transport.agents.test_agents import (
    SYMPOSIUM_PI,
    ELECTROCHEMISTRY_EXPERT,
    MEMBRANE_SCIENCE_EXPERT,
)
from ion_transport.prompts.test_prompts import (
    TEST_AGENDA,
    TEST_QUESTIONS,
    TEST_RULES,
)


def main():
    """Run a simple test symposium with 2 experts."""

    print("\n" + "="*80)
    print("ION TRANSPORT SYMPOSIUM - TEST RUN")
    print("="*80)
    print("\nThis is a simplified test with:")
    print("- 2 experts (Electrochemistry + Membrane Science)")
    print("- 1 discussion topic")
    print("- 2 rounds of discussion")
    print("- Estimated cost: ~$0.30-0.50")
    print("\n" + "="*80 + "\n")

    # Define team
    team_lead = SYMPOSIUM_PI
    team_members = (
        ELECTROCHEMISTRY_EXPERT,
        MEMBRANE_SCIENCE_EXPERT,
    )

    # Results directory
    results_dir = Path("ion_transport/results/test_run")
    results_dir.mkdir(parents=True, exist_ok=True)

    # Run the test meeting
    print("Starting discussion...\n")

    summary = run_meeting(
        meeting_type="team",
        agenda=TEST_AGENDA,
        agenda_questions=TEST_QUESTIONS,
        agenda_rules=TEST_RULES,
        save_dir=results_dir,
        save_name="test_discussion",
        team_lead=team_lead,
        team_members=team_members,
        num_rounds=2,  # Just 2 rounds for testing
        pubmed_search=False,  # Disable for faster testing (enable later)
        return_summary=True,
    )

    print("\n" + "="*80)
    print("TEST SYMPOSIUM COMPLETE")
    print("="*80)
    print(f"\nResults saved in: {results_dir}")
    print("\nFinal Summary:")
    print("-" * 80)
    print(summary)
    print("-" * 80)

    print("\n✅ Test successful! You can now:")
    print("1. Review the discussion in: ion_transport/results/test_run/")
    print("2. Check the cost in the output above")
    print("3. Run the full symposium with all 4 experts if satisfied")


if __name__ == "__main__":
    main()
