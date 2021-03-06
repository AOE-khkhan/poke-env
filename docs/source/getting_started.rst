.. _getting_started:


Getting started
***************

This sections will guide you in installing ``poke-env`` and configuring a suited showdown server.

Installing ``poke-env``
=======================

``poke-env`` requires python >= 3.6 to be installed. It has a number of dependencies that are listed `here <https://github.com/hsahovic/poke-env/blob/master/requirements.txt>`__ and that will be installed automatically, including `numpy <https://numpy.org/>`__.

Installation can be performed via pip with:

.. code-block:: bash

    pip install poke-env

.. note:: Although the module does not support python 3.5, this can be worked around by replacing `aiologger` imports by `logger` imports. This will however affect performance. If this is an issue for your use case, please `open an issue <https://github.com/hsahovic/poke-env/issues>`__.

Configuring a showdown server
=============================

``poke-env`` communicates with a pokemon showdown server. A public implementation of showdown is hosted `here <https://play.pokemonshowdown.com/>`__, and can be used to test your agents against real human players.

However, this implementation:

- Requires an internet connection at all time
- Has numerous performance limitation (move rate, number of concurrent battles...)
- Is not meant to be used to train agents

Therefore, it is recommended to host you own server. Fortunately, Pokemon Showdown is `open-source <https://play.pokemonshowdown.com/>`__ and just requires `Node.js v10+ <https://nodejs.org/en/>`__. You can either use the official implementation - in this case, you will need to configure it to remove rate limiting and other performance bottlenecks - or our custom and `ready-to-use fork <https://github.com/hsahovic/Pokemon-Showdown>`__, which is the recommended option that will be covered in this guide.

First, you will need to `install node v10+ <https://nodejs.org/en/download/>`__. Then, you can clone the optimized showdown repo:

.. code-block:: bash

    git clone https://github.com/hsahovic/Pokemon-Showdown.git

Everything is now almost ready to create your first agent: you just have to start the showdown server:

.. code-block:: bash

    cd Pokemon-Showdown
    node pokemon-showdown

You should then get something like this:

.. code-block:: bash

    NEW GLOBAL: global
    NEW CHATROOM: lobby
    NEW CHATROOM: staff
    Worker 1 now listening on 0.0.0.0:8000
    Test your server at http://localhost:8000

If that is the case, congratulations! You just launched your server! You can now refer to :ref:`examples` to create your first agent.

Configuring showdown players
============================

``Player`` instances require a ``player_configuration`` argument, which must be of type ``PlayerConfiguration``.

``PlayerConfiguration`` are named tuples with two arguments: an username and a password.

Users without authentication
----------------------------

If your showdown configuration does not require authentication, you can use any username and set the password to ``None``.

.. code-block:: python

    from poke_env.player_configuration import PlayerConfiguration

    # This will work on servers that do not require authentication, which is the
    # case of the server launched in our 'Getting Started' section
    my_player_config = PlayerConfiguration("my_username", None)

Users with authentication
--------------------------

If your showdown configuration uses authentication, the values of each ``player_configuration`` that you create must be defined in the server's authentication database. On `pokemonshowdown.com <https://play.pokemonshowdown.com/>`__, you can achieve this by registering an username.

.. code-block:: python

    from poke_env.player_configuration import PlayerConfiguration

    # This object can be used with a player connecting to a server using authentication
    # The user 'my_username' must exist and have 'super-secret-password' as his password
    my_player_config = PlayerConfiguration("my_username", "super-secret-password")

Connecting your bots to showdown
================================

``Player`` instances require a ``server_configuration`` argument, which must be of type ``ServerConfiguration``.

``ServerConfiguration`` are named tuples with two arguments: a server url and an authentication endpoint url.

``poke-env`` includes two ready-to-use ``ServerConfiguration`` objects: ``LocalhostServerConfiguration`` and ``ShowdownServerConfiguration``.

The first one points to ``locahost:8000`` (the default endpoint for a local showdown server), whereas the second one points to ``https://play.pokemonshowdown.com/``. Both use the same authentication endpoint, https://play.pokemonshowdown.com/action.php?.

If you use our custom fork of showdown, as mentionned in Getting Started, players do not need to authenticate to battle. This effectively skips authentication calls to the authentication endpoint: your agents can access your server without an internet connection.

Custom server configuration
===========================

You can create your own server configuration if you want to connect your player to another server. You can do so like that:

.. code-block:: python

    from poke_env.server_configuration import ServerConfiguration

    # If your server is accessible at my.custom.host:5432, and your authentication
    # endpoint is authentication-endpoint.com/action.php?
    my_server_config= ServerConfiguration(
        "my.custom.host:5432",
        "authentication-endpoint.com/action.php?"
    )

    # You can now use my_server_config with a Player object

Creating agents
===============

In ``poke-env``, agents are represented by instances of python classes inheriting from ``Player``. This class incorporates everything that is needed to communicate with showdown servers, as well as many utilities designed to make creating agents easier.

To get started on creating agent, we recommended taking a look at explained examples.

- Running agent: :ref:`cross_evaluate_random_players`
- Creating a first non-trivial agent: :ref:`max_damage_player`
- Using Reinforcement Learning to train an agent: :ref:`rl_with_open_ai_gym_wrapper`
- Using teams and managing team preview in non-random formats: :ref:`ou_max_player`
- Building a custom teambuilder: :ref:`using_custom_teambuilder`
