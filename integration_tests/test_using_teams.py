# -*- coding: utf-8 -*-
import asyncio
import pytest

from poke_env.player.random_player import RandomPlayer
from poke_env.player.utils import cross_evaluate
from poke_env.player_configuration import PlayerConfiguration
from poke_env.server_configuration import LocalhostServerConfiguration


async def gen7ou_cross_evaluation(n_battles, format_, teams):
    players = [
        RandomPlayer(
            player_configuration=PlayerConfiguration("Player %d" % i, None),
            battle_format=format_,
            server_configuration=LocalhostServerConfiguration,
            max_concurrent_battles=n_battles,
            team=team,
        )
        for i, team in enumerate(teams)
    ]
    await cross_evaluate(players, n_challenges=n_battles)

    for player in players:
        await player.stop_listening()


@pytest.mark.asyncio
async def test_gen7ou_cross_evaluation(showdown_format_teams):
    for format_, teams in showdown_format_teams.items():
        await asyncio.wait_for(
            gen7ou_cross_evaluation(n_battles=5, format_=format_, teams=teams),
            timeout=3 * len(teams) + 3,
        )
