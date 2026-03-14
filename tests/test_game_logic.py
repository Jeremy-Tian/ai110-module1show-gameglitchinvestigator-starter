from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_hint_messages():
    # AI collaboration: After fixing the backwards hint messages, we created this test
    # to ensure the bug doesn't reoccur. It specifically checks that hints give correct directional advice.
    # Test that hint messages are correct (this targets the bug where messages were backwards)
    # When guess is too high, should tell player to go lower
    outcome_high, message_high = check_guess(60, 50)
    assert outcome_high == "Too High"
    assert "LOWER" in message_high  # Should contain "Go LOWER!"

    # When guess is too low, should tell player to go higher
    outcome_low, message_low = check_guess(40, 50)
    assert outcome_low == "Too Low"
    assert "HIGHER" in message_low  # Should contain "Go HIGHER!"
