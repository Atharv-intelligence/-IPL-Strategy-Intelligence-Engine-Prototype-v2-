"""Reusable recommendation filters for matchup analytics."""


def get_dangerous_matchups(matchups):
    """Return matchups where the batter has a low strike rate and at least one dismissal."""
    return matchups[
        (matchups["matchup_type"] == "Dangerous")
    ].copy()


def get_favorable_matchups(matchups):
    """Return matchups where the batter has a high strike rate without a dismissal."""
    return matchups[
        (matchups["matchup_type"] == "Favorable")
    ].copy()


def get_top_recommendations(matchups, limit=20):
    """Rank dangerous matchups by dismissals, then by lower strike rate."""
    dangerous = get_dangerous_matchups(matchups)
    return dangerous.sort_values(
        ["dismissals", "strike_rate"],
        ascending=[False, True],
    ).head(limit)
