from app.agents.planner_agent import PlannerAgent


def test_planner_returns_plan():
    planner = PlannerAgent()
    profile = {"Probability": {"strength": "weak"}}
    output = planner.plan(profile, "Probability question", explicit_topic="Probability")

    assert output.topic == "Probability"
    assert output.subject == "Mathematics"
    assert len(output.plan_steps) == 3

