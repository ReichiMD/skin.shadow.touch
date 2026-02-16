# -*- coding: utf-8 -*-
"""
Shadow Touch Helper - Router Module
Handles routing for skin helper actions
"""

import sys
import xbmc
import xbmcaddon
from urllib.parse import parse_qs

from .config import log_error, log_info, log_debug
from .shadow_actions import (
    clear_movie_info,
    get_movie_info,
    show_movie_info_dialog,
    add_to_watchlist,
    mark_as_watched
)


def routing():
    """
    Main routing function
    Parses URL parameters and calls appropriate action handlers
    """
    try:
        # Parse arguments from sys.argv
        # sys.argv[0] = plugin://skin.shadow.touch/
        # sys.argv[1] = handle (not used for skins)
        # sys.argv[2] = ?action=show_info&tmdb_id=12345

        if len(sys.argv) < 3:
            log_debug("No arguments provided to router")
            return

        # Parse query string
        params = parse_qs(sys.argv[2].lstrip('?'))
        log_debug(f"Router params: {params}")

        # Get action
        action = params.get('action', [None])[0]

        if not action:
            log_error("No action specified in router")
            return

        # Route to appropriate handler
        if action == 'show_movie_info':
            # Show movie info dialog
            tmdb_id = params.get('tmdb_id', [None])[0]
            title = params.get('title', [None])[0]
            year = params.get('year', [None])[0]

            log_info(f"Showing movie info: ID={tmdb_id}, Title={title}, Year={year}")
            show_movie_info_dialog(tmdb_id=tmdb_id, title=title, year=year)

        elif action == 'clear_movie_info':
            # Clear movie info properties
            log_info("Clearing movie info")
            clear_movie_info()

        elif action == 'add_to_watchlist':
            # Add to watchlist
            tmdb_id = params.get('tmdb_id', [None])[0]
            if tmdb_id:
                log_info(f"Adding to watchlist: {tmdb_id}")
                add_to_watchlist(tmdb_id)
            else:
                log_error("No TMDB ID provided for watchlist")

        elif action == 'mark_as_watched':
            # Mark as watched
            tmdb_id = params.get('tmdb_id', [None])[0]
            if tmdb_id:
                log_info(f"Marking as watched: {tmdb_id}")
                mark_as_watched(tmdb_id)
            else:
                log_error("No TMDB ID provided for mark as watched")

        else:
            log_error(f"Unknown action: {action}")

    except Exception as e:
        log_error(f"Error in router: {str(e)}")
        import traceback
        log_error(traceback.format_exc())


def run_action(action, **kwargs):
    """
    Run action directly from skin using RunScript()

    Args:
        action (str): Action to run
        **kwargs: Action parameters

    Example usage from skin XML:
        RunScript(skin.shadow.touch,action=show_movie_info,tmdb_id=12345)
    """
    try:
        log_info(f"Running action: {action} with params: {kwargs}")

        if action == 'show_movie_info':
            show_movie_info_dialog(**kwargs)
        elif action == 'clear_movie_info':
            clear_movie_info()
        elif action == 'add_to_watchlist':
            add_to_watchlist(kwargs.get('tmdb_id'))
        elif action == 'mark_as_watched':
            mark_as_watched(kwargs.get('tmdb_id'))
        else:
            log_error(f"Unknown action: {action}")

    except Exception as e:
        log_error(f"Error running action: {str(e)}")
        import traceback
        log_error(traceback.format_exc())
